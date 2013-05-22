#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

"""
nainstaluji osm databazove tabulky do schématu osm
"""

from pruga.zemjemjerka.nastavení.databáze import davaj_připojení, SCHÉMA_OSM,  SCHÉMA_POSTGIS,  SCHÉMA_PUBLIC
from pruga.zemjemjerka.nastavení.adresáře import ADRESÁŘ_OSMOSIS_SQL_DB_SCHEMA
from pruga.zemjemjerka.instalace.udělátka.nastavím_schéma import nastavím_schéma
from pruga.zemjemjerka.instalace.udělátka.spustím_sql_skript import spustím_sql_skript

def nainstaluji_osm_databázi():
    
    db = davaj_připojení()
        
    nastavím_schéma(SCHÉMA_OSM,  SCHÉMA_POSTGIS, SCHÉMA_PUBLIC,  db = db)
    
    spustím_sql_skript(ADRESÁŘ_OSMOSIS_SQL_DB_SCHEMA,  db)

if __name__ == "__main__":
    
    print(__doc__)
    
    nainstaluji_osm_databázi()
    
#    import sys
#    
#    from zora_na_pruzi.danimir.databaze import připojím_se_k_databázi,  zavřu_databázové_připojení
#    from zora_na_pruzi.danimir.databazove_dotazy import spustím_příkazy_ze_souboru
#    
#    from zora_na_pruzi.zemjemjerka.nastaveni import JMÉNO_DATABÁZE
#    
#    from zora_na_pruzi.zora_na_pruzi import Zora_na_pruzi
#    
#    app = Zora_na_pruzi(sys.argv)
#    
#    print(__doc__)
#    
#    db = připojím_se_k_databázi(JMÉNO_DATABÁZE)
#    
#    spustím_příkazy_ze_souboru(jména_souborů = ['pgsnapshot_schema_0.6.sql'], 
#                               cesta = '/opt/osmosis-0.40.1/script/', 
#                               db = db, 
#                               databázové_schéma='osm, postgis')
#    
#    zavřu_databázové_připojení()
