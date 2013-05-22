# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

"""
hen je nastavení připojení k databázi
"""

import postgresql

JMÉNO_DATABÁZE =   "zemjemjerka"
SCHÉMA_PUBLIC = "public"
SCHÉMA_POSTGIS = 'postgis'
SCHÉMA_OSM  =  'osm'
SCHÉMA_ZEMJEMJERKY  =  'zemjemjerka'


SERVER =  'localhost'
UŽIVATEL =  'golf'
HESLO_UŽIVATELE = 'marihuana'

def davaj_připojení(databáze = JMÉNO_DATABÁZE):
    
    return postgresql.open(user = UŽIVATEL, host = SERVER, password = HESLO_UŽIVATELE,  database = databáze)


