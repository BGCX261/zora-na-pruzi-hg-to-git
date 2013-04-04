#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je třída, která ...
'''
import os

def cesta_k_souboru(jméno):
    return os.path.join(os.path.dirname(__file__),  'sql',  jméno)

if __name__ == '__main__':
    from zora_na_pruzi.danimir.připojení.postgresql import pruga_test
    from zora_na_pruzi.danimir.připojení.připojím_postgresql import postgresql_připojím_se_k_databázi
    
    db = postgresql_připojím_se_k_databázi(pruga_test)
    
    for sql_skript in ('funkce_najdu_či_vytvořím_klíč.sql', 
                                'funkce_vytvořím_nový_uzel.sql'
                                ):
    
        print('SQL {}'.format(sql_skript))
    
        with open(cesta_k_souboru(sql_skript),  mode='r',  encoding='UTF-8') as sql_soubor:
            sql = sql_soubor.read()
    #        print(sql)
    #        try:
            db.execute(sql)
    #        except postgresql.exceptions.FunctionDefinitionError as e:
    #            print(e)
