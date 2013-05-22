#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

"""
tento skript nastaví výchozí schémata pro uživatele
"""

#import os
import postgresql
from pruga.zemjemjerka.nastavení.databáze import davaj_připojení, SCHÉMA_POSTGIS,  SCHÉMA_PUBLIC,  SCHÉMA_OSM,  SCHÉMA_ZEMJEMJERKY

#import postgresql

def nastavím_výchozí_schémy(uživatel):
    
    db = davaj_připojení()
    
    schémy = ','.join((SCHÉMA_ZEMJEMJERKY,  SCHÉMA_OSM, SCHÉMA_POSTGIS,  SCHÉMA_PUBLIC))
    příkaz = 'ALTER USER {} SET search_path TO {}'.format(uživatel,  schémy)
    print('spouštím SQL příkaz:\n\t{}'.format(příkaz))
    
    try:
        db.execute(příkaz)
    except postgresql.exceptions.Error as e:
        print('\tSchémy "{}" pro uživatele "{}" nelze nastavit: "{}".'.format(schémy, uživatel, e))
        db.close()
        return
    else:
        print('\tUživatel "{}" má včíl nastavené výchozí schémy "{}".'.format(uživatel,  schémy))

    db.close()

if __name__ == "__main__":
    
    print(__doc__)
    
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('uživatel', metavar='uživatel', type=str,  help='uživatel, kterému nastavíme schémata pro zemjemjekru jako výchozí')
    args = parser.parse_args()
    
    nastavím_výchozí_schémy(args.uživatel)
    
