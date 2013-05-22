#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

"""
nainstaluji postgis do schématu postgis
"""

import os
from pruga.zemjemjerka.nastavení.adresáře import ADRESÁŘ_POSTGISU
from pruga.zemjemjerka.nastavení.databáze import davaj_připojení, SCHÉMA_POSTGIS,  SCHÉMA_PUBLIC
from pruga.zemjemjerka.instalace.udělátka.nastavím_schéma import nastavím_schéma
from pruga.zemjemjerka.instalace.udělátka.spustím_sql_skript import spustím_sql_skript

import postgresql

def nainstaluji_postgis():
    
    db = davaj_připojení()
    
    nastavím_schéma(SCHÉMA_POSTGIS,  db = db)
    
    for jméno_sql_souboru in ['postgis.sql',  'spatial_ref_sys.sql']:
        cesta_k_sql_souboru = os.path.join(ADRESÁŘ_POSTGISU,  jméno_sql_souboru)
        spustím_sql_skript(cesta_k_sql_souboru,  db)
     
   
    nastavím_schéma(SCHÉMA_PUBLIC, SCHÉMA_POSTGIS,  db = db)  
    příkaz = 'CREATE EXTENSION hstore'
    print("spouštím SQL příkaz:\n\t{}".format(příkaz))
    try:
        db.execute(příkaz)
    except postgresql.exceptions.Error as e:
        print("\tHstore nelze vytvořit: {}.".format(e.message))
    else:
        print("\tHstore vytvořeno.")
        
    db.close()


if __name__ == "__main__":
    
    print(__doc__)
    
    nainstaluji_postgis()
    
