#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import postgresql
import types

def postgresql_připojím_se_k_databázi(nastavení_připojení = None):

#    if hasattr(připojím_se_k_databázi,  'db'):
#        return připojím_se_k_databázi.db

    if isinstance(nastavení_připojení,  types.ModuleType):
        převod_názvů = {'host': 'SERVER', 
                                            'port': 'PORT',
                                            'user': 'UŽIVATEL', 
                                            'password': 'HESLO_UŽIVATELE', 
                                            'database': 'JMÉNO_DATABÁZE'
                                            }
        parametry = {}
        for název_db,  název_uživatelský in  převod_názvů.items():
            if hasattr(nastavení_připojení,  název_uživatelský):
                parametry[název_db] = getattr(nastavení_připojení,  název_uživatelský)
        db = postgresql.open(**parametry)
    #        elif isinstance(nastavení_připojení,  postgresql.driver.pq3.Connection):
    #            db = nastavení_připojení
    else:
        raise ValueError('Z "{}" neumím přečíst nastavení k dastabázi.'.format(nastavení_připojení))

    return db
