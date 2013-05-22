#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

"""
spustím SQL ze skriptu
"""

import postgresql

def spustím_sql_skript(cesta_k_sql_skriptu,  db):
        print("spouštím SQL ze souboru:\n\t{}".format(cesta_k_sql_skriptu))
        
        with open(cesta_k_sql_skriptu) as sql_skript:
            příkaz = sql_skript.read()
#            print(příkaz )
            try:
                db.execute(příkaz)
            except postgresql.exceptions.Error as e:
                #                print(dir(e))
                print("\tSpuštění SQL skriptu {} selhalo: {}.".format(cesta_k_sql_skriptu,  e.message))
#                raise e
#                return
            else:
                print("\tSkript {} byl úspěšně vykonán.".format(cesta_k_sql_skriptu))
