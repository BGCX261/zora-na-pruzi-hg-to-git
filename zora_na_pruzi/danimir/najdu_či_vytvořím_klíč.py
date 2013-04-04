#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

def najdu_či_vytvořím_klíč(jméno_klíče,  tabulka_hodnot = None):
    '''
    vytvořím nový uzel
    '''
    from zora_na_pruzi.danimir.db import db
    db = db()
    
    vytvořím_nový_klíč = db.proc('najdu_či_vytvořím_klíč(character varying, character varying)')
    id_klíče = vytvořím_nový_klíč(jméno_klíče,  tabulka_hodnot)
    return id_klíče
    
#    sql = 'INSERT INTO "pruga"."uzly"("jméno") VALUES($1)' 
#    nový_uzel = db.prepare(sql)
#    nový_uzel(jméno_uzlu)

if __name__ == '__main__':

    print(__doc__)

    import argparse
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser()

#   a pak mu nastavím jaké příkazy a parametry má přijímat
    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, {}'.format(__version__))
    
    parser.add_argument('klíč')
    parser.add_argument('tabulka')
    
    #    a včíl to možu rozparsovat
    args = parser.parse_args()
    
    print('klíč',  args.klíč)

    id_klíče = najdu_či_vytvořím_klíč(args.klíč)
    print(id_klíče)
