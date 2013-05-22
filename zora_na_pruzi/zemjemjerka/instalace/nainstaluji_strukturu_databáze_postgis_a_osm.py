#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

"""
provedu instalaci, postupně spustím jednotlivé instalační skripty ve správném pořadí a se správnými parametry
"""

if __name__ == "__main__":
#    import sys

    from struktura_databáze_postgis_a_osm.vytvořím_databázi import vytvořím_databázi
    from struktura_databáze_postgis_a_osm.nainstaluji_postgis import nainstaluji_postgis
    from struktura_databáze_postgis_a_osm.nainstaluji_osm_databázi import nainstaluji_osm_databázi
    
#    from pruga.pohunci.spouštění_programu import spúšťám_program
    
    print(__doc__)
    
    vytvořím_databázi()
    nainstaluji_postgis()
    nainstaluji_osm_databázi()

    

