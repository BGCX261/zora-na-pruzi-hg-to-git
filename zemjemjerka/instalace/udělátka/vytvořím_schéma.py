#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

"""
tento skript vytváří nové schéma v databázi
"""

import postgresql

def vytvořím_schéma(jméno_schémy,  db):
    
    příkaz = 'CREATE SCHEMA "{}"'.format(jméno_schémy)
    print("spouštím SQL příkaz:\n\t{}".format(příkaz))
    
    try:
        db.execute(příkaz)
    except postgresql.exceptions.DuplicateSchemaError:
        print("\tSchému {} není možné vytvořit, již takové jestvuje.".format(jméno_schémy))
    else:
        print("\tSchéma {} bylo úspěšně vytvořeno.".format(jméno_schémy))
