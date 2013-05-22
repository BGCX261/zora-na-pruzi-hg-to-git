#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
export nezaúčtovaných položek z peněžního deníku (majíce v "má_dáti" či "dal"  null)
do csv formátu pro další zpracování v tabulkovém procesoru
'''
#import postgresql
import datetime
from pruga.knjigovod.nastavení.databáze import davaj_připojení,   JMÉNO_DATABÁZE
#from pruga.web.prohlížeče.prohlížeč import spustím_prohlížeč
from pruga.danimir.insert import INSERT
from pruga.danimir.databázové_typy.účetnictví_číslo_účtu import ROW

def vypíšu_položky_faktur_z_deníku():
 
    '''
    provede výpis z účetního deníku položek, které nemají zaučtovanou část má_dáti
    '''
    db = davaj_připojení(JMÉNO_DATABÁZE)
    
    dotaz = '''
    
    SELECT "rozpis_přijatých_faktur"."adresář_název",
 "rozpis_přijatých_faktur"."položky_název_položky",
  "rozpis_přijatých_faktur"."forma_úhrady",
  "účetní_deník".id,
   "účetní_deník".datum,
 "účetní_deník"."částka",
 "účetní_deník".popis,
 "účetní_deník"."má_dáti",
  "účetní_deník".dal,
  "účetní_deník".druh_dokladu,
   "účetní_deník"."číslo_dokladu",
    "účetní_deník"."pořadí_položky",
     "účetní_deník".krok
   FROM "účetní_deník"
   JOIN "rozpis_přijatých_faktur" ON "účetní_deník"."číslo_dokladu"::text = "rozpis_přijatých_faktur"."číslo_přijaté_faktury"::text
			AND "účetní_deník"."pořadí_položky"::text = "rozpis_přijatých_faktur"."položky_pořadí_položky"::text
  WHERE "účetní_deník".druh_dokladu::text = 'PŘIJATÁ FAKTURA'::text AND ("má_dáti" is null OR "dal" is null)
  ORDER BY "účetní_deník".datum, "účetní_deník"."číslo_dokladu", "účetní_deník"."pořadí_položky", "účetní_deník".krok
    
    '''
    
    pitanje = db.prepare(dotaz)
    
    for hodnoty in pitanje:
        print(';'.join(map(str,  hodnoty)))
    
    db.close()


if __name__ == '__main__':

    vypíšu_položky_faktur_z_deníku()
