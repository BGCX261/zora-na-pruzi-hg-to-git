#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který importuje firmy z psql databáze
'''

from zora_na_pruzi import *

from danimir import databáze
from danimir.příkazy import SELECT

from danimir.připojení import účetnictví



db = databáze(účetnictví)
tabulka = db.rozpis_přijatých_faktur

def načtu_z_databáze(funkce_zpracující_záznam = print):
    '''
    zahájí běh programu
    '''

#
#"přijaté_faktury_položky"."jednotková_cena", "přijaté_faktury_položky"."pořadí_položky", 
#"přijaté_faktury_položky"."množství", "přijaté_faktury_položky"."název_položky", 
#"přijaté_faktury_položky"."DPH", "přijaté_faktury_položky".cena_bez_dph, "přijaté_faktury_položky".sazba_dph, 
#"přijaté_faktury_položky".typ_ceny_dph, 
#"přijaté_faktury_položky"."typ_položky", 
#"přijaté_faktury_položky".typ_sazby_dph, 
#"přijaté_faktury_položky".id_faktury, 
#"přijaté_faktury_položky"."zaúčtován_nákup", 
#"přijaté_faktury_položky"."zaúčtováno_dph", 
#"přijaté_faktury_položky"."zaúčtována_platba", "přijaté_faktury"."poslední_změna" AS "poslední_změna_faktury", 
#"přijaté_faktury"."číslo_bankovního_účtu" AS "číslo_bankovního_účtu_faktury",
#"přijaté_faktury"."číslo_došlé_faktury", "přijaté_faktury".datum_splatnosti AS datum_splatnosti_faktury, 
#"přijaté_faktury"."datum_vystavení" AS "datum_vystavení_faktury", 
#"přijaté_faktury"."datum_zdanitelného_plnění" AS "datum_zdanitelného_plnění_faktury",
#"přijaté_faktury".iban, "přijaté_faktury"."číslo_přijaté_faktury", 
#"přijaté_faktury".popis AS popis_faktury, 
#"přijaté_faktury"."celková_částka" AS "celková_částka_faktury", 
#"přijaté_faktury"."celková_dph_snížená", "přijaté_faktury"."celková_dph_základní", 
#"přijaté_faktury"."celková_osvobozená_od_dph", "přijaté_faktury"."celková_bez_dph", 
#"přijaté_faktury"."variabilní_symbol", "přijaté_faktury"."forma_úhrady",
#"přijaté_faktury"."stav_úhrady", "přijaté_faktury".id_dodavatele,
#"adresář".id AS "adresář_id",
#"adresář"."poslední_změna" AS "adresář_poslední_změna", 
#"adresář"."kód" AS "adresář_kód", 
#"adresář"."název" AS "adresář_název", 
#"adresář"."platí_od" AS "adresář_platí_od", 
#"adresář"."platí_do" AS "adresář_platí_do", 
#"adresář".email AS "adresář_email", 
#"adresář".fax AS "adresář_fax", 
#"adresář"."město" AS "adresář_město", 
#"adresář".mobil AS "adresář_mobil", 
#"adresář"."PSČ" AS "adresář_PSČ", 
#"adresář".telefon AS "adresář_telefon",
#"adresář".ulice AS "adresář_ulice", 
#"adresář".www AS "adresář_www", 
#"adresář"."DIČ" AS "adresář_DIČ", 
#"adresář"."IČ" AS "adresář_IČ", 
#"adresář"."plátce_DPH" AS "adresář_plátce_DPH", 
#"adresář"."obvyklá_splatnost" AS "adresář_obvyklá_splatnost", 
#"adresář".typ_vztahu AS "adresář_typ_vztahu"
#   FROM "přijaté_faktury"
#   JOIN "přijaté_faktury_položky" ON "přijaté_faktury".id = "přijaté_faktury_položky".id_faktury
#   JOIN "adresář" ON "přijaté_faktury".id_dodavatele = "adresář".id;
#
#ALTER TABLE "rozpis_přijatých_faktur"
#  OWNER TO postgres;


    sql = SELECT(tabulka.adresář_IČ.AS('ičo'), 
                    tabulka.adresář_DIČ.AS('dič'),
                    tabulka.adresář_název.AS('jméno'), 
                        tabulka.adresář_PSČ.AS('psč'), 
                        tabulka.adresář_město.AS('město'), 
                        tabulka.adresář_ulice.AS('ulice'), 
                        tabulka.adresář_plátce_DPH.AS('plátce_DPH'), 
                        tabulka.adresář_typ_vztahu.AS('typ_vztahu')
             ).FROM(tabulka)
#             group nefunguje,  bo požaduje kokotiny
#             .GROUP_BY(tabulka.adresář_IČ)
    
    debug(sql)
    odpověď = db(sql)
#    print(odpověď)
    
    jedinečné = set()
    for záznam in odpověď:
        ičo = záznam.ičo
        if ičo not in jedinečné:
            jedinečné.add(ičo)
            data = {'ičo': ičo,  'dič': záznam.dič,  'jméno': záznam.jméno}
            data['adresa'] = '{z.ulice}, {z.psč} {z.město}'.format(z = záznam)
            funkce_zpracující_záznam(data)


def načtu_z_xml_zálohy(soubor,  funkce_zpracující_záznam = print):
    
    from lxml import etree
    
    tree = etree.parse(soubor)
    root = tree.getroot()
    
    print(root.tag,  len(root))
    
    for element in root.findall('faktura-prijata'):
#        print(element.tag)
        data = {}
        data['ičo'] = element.find('ic').text
#        print(ičo)
#        if ičo is None:
#            print('nenašel sem ičo')
#            continue
            
#        ičo = ičo.text
#        print(ičo)
        

        data['dič'] = element.find('dic').text
        data['jméno'] = element.find('nazFirmy').text
        ulice = element.find('ulice').text
        psč = element.find('psc').text
        město = element.find('mesto').text
        data['adresa'] = '{ulice}, {psč} {město}'.format(ulice = ulice,  psč = psč,  město = město)
        
        
        funkce_zpracující_záznam(data)
    

def vložím_firmu_do_grafu(data):

    firma = zora.Třídy_uzlů['firma'](**data)
    try:
        firma.vytvořím_nový_uzel()
        print('Vytvořil jsem firmu {}'.format(firma))
    except IndexError:
        print('Firma již jestvuje {}'.format(firma))
    print(mithrades)
    
    
    

if __name__ == '__main__':

    print(__doc__)

#    graf.vymažu_vše_z_grafu()
    
    mithrades = {}
    mithrades['ičo']  = '29191360'
    mithrades['dič']  = 'CZ29191360'
    mithrades['jméno']  = 'MITHRADES'
    mithrades['adresa']  = 'Kudlovice 35, 695 01 Babice'
    
    vložím_firmu_do_grafu(mithrades)
    
#    načtu_z_databáze(funkce_zpracující_záznam = vložím_firmu_do_grafu)
    
#    načtu_z_xml_zálohy(soubor = 'zaloha_prijatych_faktur.xml',  funkce_zpracující_záznam = vložím_firmu_do_grafu)
    



