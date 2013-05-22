#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který importuje faktury z psql databáze a, či nebo, z xml zálohy
'''

import logging
logging.basicConfig(level=logging.DEBUG)
from logging import debug


import datetime

#from pruga1.danimir import databáze
#from pruga1.danimir.příkazy import SELECT
#
#from pruga1.danimir.připojení import účetnictví

#db = databáze(účetnictví)
#tabulka = db.rozpis_přijatých_faktur

#from pruga1.grafomir.databáze.připojení.hlavní_databáze import g


class jako_objekt():
    
    def __init__(self,  slovník):
        if not isinstance(slovník,  dict):
            raise TypeError('davaj slovník')
        self.data = slovník
        
    def __getattr__(self,  klíč):
        return self.data[klíč]
        
    def __str__(self):
        return str(self.data)
        
    def __getitem__(self,  klíč):
        return self.data[klíč]
        
    def __iter__(self):
        for klíč,  hodnota in self.data.items():
            yield klíč,  hodnota

def na_datum(str):
    return datetime.datetime.strptime(str.split('+')[0],  '%Y-%m-%d')

def načtu_z_databáze(funkce_zpracující_záznam = print):
    '''
    zahájí běh programu
    '''

    print('='*45)
    print('IMPORTUJI Z POSTGRESQL {}'.format(tabulka))
    print('='*45)

    sql = SELECT(
                tabulka.adresář_IČ.AS('ičo'), 
                tabulka.adresář_DIČ.AS('dič'), 
                tabulka.adresář_název.AS('jméno_firmy'), 
                
                tabulka.číslo_došlé_faktury, 
                tabulka.datum_splatnosti_faktury, 
                tabulka.datum_vystavení_faktury, 
                tabulka.datum_zdanitelného_plnění_faktury, 
                
                tabulka.číslo_přijaté_faktury, 
                tabulka. název_položky, 
                tabulka. popis_faktury.AS('popis_položky'), 
                tabulka. množství, 
                tabulka. jednotková_cena, 
                tabulka. cena_bez_dph, 
                tabulka. sazba_dph, 
                tabulka. DPH, 
                tabulka. celková_částka_faktury.AS('celková_částka_položky'), 
                
                tabulka.pořadí_položky, 
                
                tabulka.adresář_město.AS('město'), 
                tabulka.adresář_PSČ.AS('psč'), 
                tabulka.adresář_ulice.AS('ulice')
             ).FROM(tabulka)
    
    odpověď = db(sql)
#    print(odpověď)
    
    for záznam in odpověď:
        funkce_zpracující_záznam(záznam)


def načtu_z_xml_zálohy(soubor,  funkce_zpracující_záznam = print):
    
    print('='*45)
    print('IMPORTUJI Z XML {}'.format(soubor))
    print('='*45)
    
    from lxml import etree
    
    tree = etree.parse(soubor)
    root = tree.getroot()
    
#    print(root.tag,  len(root))
    
    hlavička = ('jméno_firmy', 'ičo', 'město', 'ulice', 'číslo_došlé_faktury', 'datum_vystavení_faktury',  
                     'datum_splatnosti_faktury', 
                     'datum_zdanitelného_plnění_faktury', 
                     'číslo_přijaté_faktury', 
                     'název_položky', 
                     'popis_položky', 
                     'množství' , 
                    'jednotková_cena' , 
                    'cena_bez_dph', 
                    'sazba_dph' , 
                    'DPH' , 
                    'celková_částka_položky', 
                    'pořadí_položky'
                     )
    
    print(';'.join(hlavička))
    
    for element in root.findall('faktura-prijata'):
#        print(element.tag)
        data = {}
        data['ičo'] = element.find('ic').text
#        print(data['ičo'])
        if data['ičo'] is None:
            raise ValueError('nenašel sem ičo')
            continue
        

        data['dič'] = element.find('dic').text
        data['jméno_firmy'] = element.find('nazFirmy').text
        data['ulice'] = element.find('ulice').text
        data['psč'] = element.find('psc').text
        data['město'] = element.find('mesto').text
                
        data['číslo_došlé_faktury'] = element.find('cisDosle').text
        data['datum_splatnosti_faktury'] = na_datum(element.find('datSplat').text)
        data['datum_vystavení_faktury'] = na_datum(element.find('datVyst').text)
        data['datum_zdanitelného_plnění_faktury'] = na_datum(element.find('duzpPuv').text)
        
        data['číslo_přijaté_faktury'] = element.find('kod').text
        
        data['pořadí_položky'] = '1'
        
        element_položek = element.find('polozkyFaktury')
        if element_položek is not None:
            for element_položky in element_položek.findall('faktura-prijata-polozka'):
                data['název_položky'] = element_položky.find('nazev').text
                data['popis_položky'] = element.find('popis').text
                data['množství'] = element_položky.find('mnozMj').text
                data['jednotková_cena'] = element_položky.find('cenaMj').text
                data['cena_bez_dph'] = element_položky.find('sumZkl').text
                data['sazba_dph'] = element_položky.find('szbDph').text
                data['DPH'] = element_položky.find('sumDph').text
                data['celková_částka_položky'] = element_položky.find('sumCelkem').text
                data['pořadí_položky'] = element_položky.find('cisRad').text
        else:
#            print('nemá položky')
            data['název_položky'] = element.find('popis').text
            data['popis_položky'] = ''
            data['množství'] = '1'
            data['jednotková_cena'] = element.find('sumZklCelkem').text
            data['cena_bez_dph'] = element.find('sumZklCelkem').text
             
            if element.find('sumDphSniz').text == '0.0':
                if not element.find('sumDphZakl').text == '0.0':
                    data['sazba_dph'] = element.find('szbDphZakl').text
                else:
                    data['sazba_dph'] = '0'
            else:
                data['sazba_dph'] = element.find('szbDphSniz').text
            
            data['DPH'] = element.find('sumDphCelkem').text
            data['celková_částka_položky'] = element.find('sumCelkem').text
        
                
               
                
            data =  jako_objekt(data)
#            print(data)
#            funkce_zpracující_záznam(data)
            řádek = (data['jméno_firmy'],  data['ičo'],  data['město'],  data['ulice'],  data['číslo_došlé_faktury'],  data['datum_vystavení_faktury'],  
                     data['datum_splatnosti_faktury'], 
                     data['datum_zdanitelného_plnění_faktury'], 
                     data['číslo_přijaté_faktury'], 
                     data['název_položky'], 
                     data['popis_položky'], 
                     data['množství'] , 
                    data['jednotková_cena'] , 
                    data['cena_bez_dph'], 
                    data['sazba_dph'] , 
                    data['DPH'] , 
                    data['celková_částka_položky'], 
                    data['pořadí_položky']
                     )
             
            řádek2 = []
            for x in řádek:
                řádek2.append(str(x))
            print(';'.join(řádek2))
    

def vložím_fakturu_do_grafu(data):
    

#    print(data)
    
    ičo = data['ičo']
    print('*'*40)
    print('IČO {}'.format(ičo))
    
    data_firmy = {}
    data_firmy = {'ičo': ičo,  'dič': data.dič,  'jméno': data.jméno_firmy}
    data_firmy['adresa'] = '{z.ulice}, {z.psč} {z.město}'.format(z = data)
    
#    firma = g.firma.index.get_unique(ičo = ičo)
    firma = g.firma.get_or_create('ičo',  ičo,  data_firmy)
   
    data_faktury = {
                    'číslo_faktury': data['číslo_došlé_faktury'], 
                    'datum_vystavení': data['datum_vystavení_faktury'], 
                    'datum_splatnosti': data['datum_splatnosti_faktury'], 
                    'datum_zdanitelného_plnění': data['datum_zdanitelného_plnění_faktury']
                 }

#    print(data_faktury)
    def uprav_čas(hodnota):
        if isinstance(hodnota,  datetime.date):
            hodnota = datetime.datetime.combine(hodnota,  datetime.time(hour = 12))
        return hodnota
        
    data_faktury = {klíč: uprav_čas(hodnota) for klíč,  hodnota in data_faktury.items()}
#    print(data_faktury)
    
    cypher_skript = '''START  firma = node({id_firmy})
                                MATCH firma-[:`firma_vystavila_fakturu`]->faktura
                                WHERE faktura.`číslo_faktury` = {cislo_faktury}
                                RETURN faktura'''
    params = {'id_firmy': firma.eid,  'cislo_faktury': data['číslo_došlé_faktury']}
    faktura = g.cypher.single(cypher_skript,  params)

    if faktura is None:
        print("přidávám fakturu")
        faktura = g.faktura.create(data_faktury)
        firma_vystavuje_fakturu = g.firma_vystavila_fakturu.create(firma,  faktura)
     
    data_položky = {
                            'název': data['název_položky'] if data['název_položky'] is not None else '', 
                            'popis': data['popis_položky'], 
                            'množství': data['množství'], 
                            'jednotka': 'nevím, prostě kusy', 
                            'jednotková_cena': data['jednotková_cena'], 
                            'sazba_dph': data['sazba_dph'], 
                            'celková_cena': data['celková_částka_položky'], 
                            'základ_dph': data['cena_bez_dph'], 
                            'dph': data['DPH']
                            }

    cypher_skript = '''START  faktura = node({id_faktury})
                                MATCH faktura<-[hrana:`položka_přidána_do_faktury`]-polozka
                                WHERE hrana.`pořadí` = {`pořadí_položky`}
                                RETURN polozka'''
    params = {'id_faktury': faktura.eid,  'pořadí_položky': data['pořadí_položky']}
    položka = g.cypher.single(cypher_skript,  params)
    
    if položka is None:
        print("přidávám položku")
        položka = g.položka_faktury.create(data_položky)
        položka_přidána_do_faktury = g.položka_přidána_do_faktury.create(položka,  faktura,  pořadí = data['pořadí_položky'])
    
#    print(firma.data())
#    print(data_firmy)
#    print(data_faktury)
#    print(data_položky)
    
#    print(g.firma.index.count(element_type = "firma"))
#    záznam = g.firma.get_or_create('ičo',  firma['ičo'],  **firma)
#    print('uzel eid = {}, celkem {} uzlů'.format(záznam.eid,  len(list(g.firma.get_all()))))
    
    

if __name__ == '__main__':

    print(__doc__)
    
#    načtu_z_databáze(funkce_zpracující_záznam = vložím_fakturu_do_grafu)
    
#    načtu_z_xml_zálohy(soubor = 'zaloha_prijatych_faktur.xml',  funkce_zpracující_záznam = vložím_fakturu_do_grafu)
    načtu_z_xml_zálohy(soubor = 'zaloha_prijatych_faktur.xml',  funkce_zpracující_záznam = print)

#    from pruga1.grafomir.databáze.export.graphviz import dot
#    dot.draw(uzly = g.V,  hrany = g.E)
    



