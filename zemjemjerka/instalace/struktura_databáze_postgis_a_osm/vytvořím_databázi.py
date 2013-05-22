#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

"""
vytvořím databázi pro geografická data načtená z osm (open street map)
"""

from pruga.zemjemjerka.nastavení.databáze import davaj_připojení,  JMÉNO_DATABÁZE,  SCHÉMA_POSTGIS,  SCHÉMA_OSM
from pruga.zemjemjerka.instalace.udělátka.vytvořím_schéma import vytvořím_schéma
import postgresql
    
def vytvořím_databázi():
#    databáze zemjemjerka ještě nejestvuje,  musíme se připojit k takové,  která by už měla v systému být
    db = davaj_připojení('postgres')
    
#    print(db)
    
    print("su připojený k databázi {}".format(db.version))
#    print("připojeno verze info databáze {}".format(db.version_info))
        
    příkaz = 'CREATE DATABASE "{}"'.format(JMÉNO_DATABÁZE)
    print("spouštím SQL příkaz:\n\t{}".format(příkaz))
    
    try:
        db.execute(příkaz)
    except postgresql.exceptions.DuplicateDatabaseError:
        print("\tDatabázi {} není možné vytvořit, již taková jestvuje.".format(JMÉNO_DATABÁZE))
    else:
        print("\tDatabáze {} byla úspěšně vytvořena.".format(JMÉNO_DATABÁZE))
    
    db.close()
    db = davaj_připojení(JMÉNO_DATABÁZE)
    vytvořím_schéma(jméno_schémy = SCHÉMA_POSTGIS,  db = db)
    vytvořím_schéma(jméno_schémy = SCHÉMA_OSM,  db = db)

    db.close()
    

if __name__ == "__main__":
    
    print(__doc__)
    
    vytvořím_databázi()

