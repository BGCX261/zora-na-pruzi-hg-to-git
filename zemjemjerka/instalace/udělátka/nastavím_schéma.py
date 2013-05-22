#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

"""
nastavím schéma
"""

import postgresql

def nastavím_schéma(*schémata,  db = None):
    
    jméno_schémy = ",".join(schémata)
    
    příkaz = 'SET search_path TO {}'.format(jméno_schémy)
    print("spouštím SQL příkaz:\n\t{}".format(příkaz))
    
    try:
        db.execute(příkaz)
    except postgresql.exceptions.ParameterValueError as e:
        print("\tSchéma {} nelze nastavit: {}.".format(jméno_schémy,  e))
        db.close()
        return
    else:
        print("\tZměněno schéma {}.".format(jméno_schémy))
