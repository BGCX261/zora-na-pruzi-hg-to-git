#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

"""
tento skript instaluje strukturu, schéma, atové typy a funkce zemjemjerky
"""

import os
from pruga.zemjemjerka.nastavení.adresáře import ADRESÁŘ_SQL_SKRIPTOV_ZEMJEMJERKY
from pruga.zemjemjerka.nastavení.databáze import davaj_připojení, SCHÉMA_POSTGIS,  SCHÉMA_PUBLIC,  SCHÉMA_OSM,  SCHÉMA_ZEMJEMJERKY
from pruga.zemjemjerka.instalace.udělátka.vytvořím_schéma import vytvořím_schéma
from pruga.zemjemjerka.instalace.udělátka.nastavím_schéma import nastavím_schéma
from pruga.zemjemjerka.instalace.udělátka.spustím_sql_skript import spustím_sql_skript

#import postgresql

def nainstaluji_zemjemjerku():
    
    db = davaj_připojení()
    
    vytvořím_schéma(SCHÉMA_ZEMJEMJERKY,  db = db)
    
    nastavím_schéma(SCHÉMA_ZEMJEMJERKY,  SCHÉMA_OSM, SCHÉMA_POSTGIS,  SCHÉMA_PUBLIC,   db = db)
    
    jména_sql_skriptů =  ['funkce/datové_typy/bod.sql', 
                                        'funkce/davaj_bod.sql',  
                                        'funkce/davaj_body_cesty.sql', 
                                        'funkce/davaj_body_relace.sql', 
                                    'pohledy/přehled_klíčů_v_bodech_cestách_a_relacích.sql', 
#                                    'funkce_wgs84-to-utm.sql'
                                    ]
    
    for jméno_sql_skriptu in jména_sql_skriptů:
        cesta_k_sql_skriptu = os.path.join(ADRESÁŘ_SQL_SKRIPTOV_ZEMJEMJERKY,  jméno_sql_skriptu)
#        print(cesta_k_sql_skriptu)
        spustím_sql_skript(cesta_k_sql_skriptu,  db)

    db.close()


if __name__ == "__main__":
    
    print(__doc__)
    
    nainstaluji_zemjemjerku()
    
