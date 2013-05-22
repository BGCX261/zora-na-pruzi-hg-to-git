#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který importuje databázi flexibee do databáze knjigovoda
'''
import postgresql
from pruga.knjigovod.nastavení.databáze import davaj_připojení,  JMÉNO_DATABÁZE_FLEXIBEE,  JMÉNO_DATABÁZE
#from pruga.web.prohlížeče.prohlížeč import spustím_prohlížeč
from pruga.danimir.insert import INSERT
from pruga.danimir.select import vypíšu_jména_sloupců


def sql_ze_souboru(cesta_k_souboru):
    with open(cesta_k_souboru,  mode = "r",  encoding="utf8") as soubor:
        sql = soubor.read()
        
    return sql


def načtu_tabulku(sql_skript,  cílová_tabulka):
    '''
    provede import dle skriptu do určité tabulky
    '''
    db_flexibee = davaj_připojení(JMÉNO_DATABÁZE_FLEXIBEE)
    
    dotaz = sql_ze_souboru(sql_skript)
    print("spouštím SQL příkaz:\n\t{}".format(dotaz))
    
    pitanje = db_flexibee.prepare(dotaz)

    db = davaj_připojení(JMÉNO_DATABÁZE)
    insert = INSERT(db = db,  tabulka = cílová_tabulka)
    insert.sloupce(*pitanje.column_names)
    
    for hodnoty in pitanje:
#        print(hodnoty)
        insert.hodnoty(*hodnoty)
    
    insert.vykonej(enom_vypiš = True)
    
    db_flexibee.close()
    db.close()


if __name__ == '__main__':

    print(__doc__)
    

#    načtu_tabulku()

#    vypíšu_jména_sloupců(databáze = davaj_připojení(JMÉNO_DATABÁZE),  tabulka = 'adresář',  formát = ' AS "{}",')
#    vypíšu_jména_sloupců(databáze = davaj_připojení(JMÉNO_DATABÁZE_FLEXIBEE),  tabulka = 'aadresar')

#    načtu_tabulku(sql_skript = '/home/pruga/sql/účetnictví/flexibee/import_adresář.sql', cílová_tabulka = 'adresář')

#    vypíšu_jména_sloupců(databáze = davaj_připojení(JMÉNO_DATABÁZE),  tabulka = 'přijaté_faktury',  formát = ' AS "{}",')
#    vypíšu_jména_sloupců(databáze = davaj_připojení(JMÉNO_DATABÁZE_FLEXIBEE),  tabulka = 'ddoklfak')
    
#    načtu_tabulku(sql_skript = '/home/pruga/sql/účetnictví/flexibee/import_faktury.sql',  cílová_tabulka = 'přijaté_faktury')

#    vypíšu_jména_sloupců(databáze = davaj_připojení(JMÉNO_DATABÁZE),  tabulka = 'přijaté_faktury_položky',  formát = ' AS "{}",')
#    vypíšu_jména_sloupců(databáze = davaj_připojení(JMÉNO_DATABÁZE_FLEXIBEE),  tabulka = 'dpolfak')
    
#    načtu_tabulku(sql_skript = '/home/pruga/sql/účetnictví/flexibee/import_položky_faktur.sql',  cílová_tabulka = 'přijaté_faktury_položky')
 
    vypíšu_jména_sloupců(databáze = davaj_připojení(JMÉNO_DATABÁZE),  tabulka = 'adresář',  formát = '"adresář"."{0}" AS "adresář_{0}",') 


