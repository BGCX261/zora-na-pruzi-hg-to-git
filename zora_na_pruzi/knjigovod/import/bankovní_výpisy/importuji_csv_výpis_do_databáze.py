#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, importuje bankovní výpisy
'''

import locale
locale.setlocale(locale.LC_ALL, '')

from datetime import date

from pruga.knjigovod.nastavení.databáze import davaj_připojení,   JMÉNO_DATABÁZE
from pruga.danimir.insert import INSERT

#@TODO: naučit měnit adresář s výpisy

TABULKA_BANKOVNÍ_VÝPISY = "bankovní_výpisy"

#@TODO: naučit zadávat číslo účtu, nebo jej získat z výpisu
ČÍSLO_ÚČTU = 1

# abych něco nenačítal dvakrát, zistím datum psoeldního zápisu a konverzní funkce _datum si to pak překontroluje

def datum_posledního_zápisu():
    db = davaj_připojení(JMÉNO_DATABÁZE)
    dotaz = 'SELECT max("{}") FROM "{}" WHERE "{}" = {}'.format("datum",  TABULKA_BANKOVNÍ_VÝPISY,  'číslo_účtu',  ČÍSLO_ÚČTU)
    pitanje = db.prepare(dotaz)
    datum = pitanje.first()
    return datum
    
už_mám_zapsané_výpisy_do = datum_posledního_zápisu()

def  projdu_soubory_výpisů(adresář):
    '''
    zahájí import výpisů
    '''
    
    import os
    import glob
    
    adresář = os.path.join(adresář,  '*.csv')
    
    for soubor in glob.glob(adresář):
        print(soubor)
        tabulka = přečtu_soubor_výpisu(soubor)
#        print(tabulka)
        zapíšu_výpis_do_databáze(tabulka)
        
def přečtu_soubor_výpisu(cesta_k_souboru):
    
    tabulka = []
    
    with open(cesta_k_souboru,  mode = 'r',  encoding='cp1250') as soubor:
        for řádka in soubor:
            řádka = řádka.strip()
#            řádka = řádka.strip(';')
            položky = řádka.split(';')
            položky = položky[0:-1]
            if len(položky) == 0:
                continue
            tabulka.append(položky)
        else:
#            toto je psolední řádek výpisu - suma - toho se musím zbavit
            suma = tabulka[-1]
#            třetí položka je částka,  která se mění,  nad ostatními provedem kontřrolu,  esli ide o řádek sumy
            if suma[0:2] == ['0', 'Suma'] and suma[3:] == ['', '', '', '', '', '', '', '', '', '']:
                tabulka.pop()
            else:
                raise ValueError('Tento formát výpisu nemá poslední řádek jako suma, tož radši nebudu pokračovat')
     
    if tabulka[0] != ['Převod', 'Datum', 'Objem', 'Protiúčet', 'Kód banky', 'KS', 'VS', 'SS', 'Uživatelská identifikace', 'Typ', 'Provedl', 'Název protiúčtu', 'Název banky']:
        raise ValueError('Tento formát výpisu neznám')

    return tabulka
    
def zapíšu_výpis_do_databáze(tabulka):
    global TABULKA_BANKOVNÍ_VÝPISY
    global ČÍSLO_ÚČTU
    
    záhlaví = tabulka.pop(0)

#    záhlaví výpisu má jiné názvy,  než sloupce v tabulce
    záhlaví_na_sloupce = {
                            "Datum" : "datum",
                            "Objem" : "částka",
                            "Převod" : "číslo_převodu",
                            "Protiúčet" : "protiúčet_číslo_účtu",
                            "Kód banky" : "protiúčet_kód_banky",
                            "KS" : "konstantní_symbol",
                            "VS" : "variabilní_symbol",
                            "SS" : "specifický_symbol",
                            "Uživatelská identifikace" : "poznámka",
                            "Typ" : "druh_platby",
                            "Provedl" : "platbu_provedl",
                            "Název protiúčtu" : "protiúčet_název_účtu",
                            "Název banky" : "protiúčet_název_banky"
                          }
                          
#    a ve výpisu je vše text,  to sa mosí upravit
    upravím_hodnoty_sloupců = {
                            "Datum" : _str_to_datum,
                            "Objem" : _str_to_decimal                             
                             }
    
#    takže správná jména sloupců budou hen
    jména_sloupců = [záhlaví_na_sloupce[jméno] for jméno in záhlaví]
#    včetně názvu účtu, který tam není
    jména_sloupců.append('číslo_účtu')
#    a tímto budeme upravovat hodnoty dále
    funkce_hodnot = [upravím_hodnoty_sloupců.get(jméno,  None) for jméno in záhlaví]
    
    db = davaj_připojení(JMÉNO_DATABÁZE)
    insert = INSERT(db = db,  tabulka = TABULKA_BANKOVNÍ_VÝPISY)
    insert.sloupce(*jména_sloupců)
    
#    upravíme hodnoty
    for řádek in tabulka:
        upravený_řádek = []
        
        for i,  položka in enumerate(řádek):
            if not položka:
               položka = None
            else:
                funkce = funkce_hodnot[i]
                if funkce:
                    položka = funkce(položka)
                
            upravený_řádek.append(položka)
            
        upravený_řádek.append(ČÍSLO_ÚČTU)
        
        insert.hodnoty(*upravený_řádek)
        

#    insert.vykonej(enom_vypiš = True)
    

def _str_to_datum(datum):
    global už_mám_zapsané_výpisy_do
    
    den,  měsíc,  rok = datum.split('.')
    
    datum = date(int(rok),  int(měsíc),  int(den))
    
    if datum <= už_mám_zapsané_výpisy_do:
        raise ValueError('Jestvuje zápis k tomuto účtu ze dne {}, tož myslím, že tento výpis je už zapsaný, raději skončím'.format(už_mám_zapsané_výpisy_do.strftime('%x')))
    
    return datum


def _str_to_decimal(převod):
    převod = převod.replace(',',  '.')
    převod = převod.replace(' ',  '')
    return float(převod)
    


def upravím_id_podle_data():
    db = davaj_připojení(JMÉNO_DATABÁZE)

#    nejdříve zistíme nejvyšší id
    dotaz = 'SELECT max("id") FROM "{tabulka}"'.format(tabulka = TABULKA_BANKOVNÍ_VÝPISY)
    pitanje = db.prepare(dotaz)
    max_id = pitanje.first()
    print("Dosavadní nejvyšší id {} o které dočasně zvětším všechna id".format(max_id))
    
#    pak všechna zvětší o nejvyšší id,  abych mohl volně měnit
    dotaz = 'UPDATE "{tabulka}" SET "id" = "id"+{max_id}'.format(tabulka = TABULKA_BANKOVNÍ_VÝPISY,   max_id = max_id)
    pitanje = db.prepare(dotaz)
    print("Počet změněných id {}".format(pitanje.first()))
    
#    resetuji sequenci - není třeba, chyba byla jinde
#    dotaz = "SELECT setval('bankovní_výpisy_id_seq', 1)"
#    pitanje = db.prepare(dotaz)
#    seq = pitanje.first()
#    print("resetován sequence na {} o které dočasně zvětším všechna id".format(seq))

    
    
#    včíl si všechny záznamy načtu
    dotaz = 'SELECT id FROM "{tabulka}" ORDER BY "datum", "id"'.format(tabulka = TABULKA_BANKOVNÍ_VÝPISY)
    pitanje = db.prepare(dotaz)
    
    for i, řádek in enumerate(pitanje()):
        id = řádek[0]
        dotaz = 'UPDATE "{tabulka}" SET "id" = {nove_id} WHERE "id" = {docasne_id}'.format(tabulka = TABULKA_BANKOVNÍ_VÝPISY,   max_id = max_id,  docasne_id = id,  nove_id = i+1)
        pitanje = db.prepare(dotaz)
        print("měním id {} > {}".format(id,  i+1))
        pitanje()
#        print(dotaz)
        
    print("Počet změněných id {}".format(i+1))
    

if __name__ == '__main__':

    print(__doc__)

    adresář = '/media/sf_V_DRIVE/účetnictví/MITHRADES/FIO banka - výpisy'
    projdu_soubory_výpisů(adresář)
    upravím_id_podle_data()
    

