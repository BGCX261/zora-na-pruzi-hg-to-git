#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

import logging
logging.basicConfig(level = logging.DEBUG)

from py2neo import neo4j, cypher,  node,  rel

def připojím_gdb(jméno):
    '''
    spouštím funkci main()
    '''
    
    from pruga.databáze.Seznam_připojení import Seznam_připojení
    gdb =  Seznam_připojení[jméno]
    return gdb

def seznam_indexů(gdb):
    indexy = gdb.get_indexes(neo4j.Node)
    print('seznam indexů')
    for index in indexy:
        print(index)

def připojím_postgresql():
    import postgresql
    db = postgresql.open(user = 'golf', database = 'účetnictví', port = 5432,  password='marihuana')
    return db

def sql_účetní_osnova(db):
    sql = 'SELECT * FROM "účetní_osnova" ORDER BY "číslo_účtu"'
    ps = db.prepare(sql)
    
    for řádek in ps:
        yield řádek
        
if __name__ == '__main__':

    print(__doc__)

    import argparse
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser()

#   a pak mu nastavím jaké příkazy a parametry má přijímat
#    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, {}'.format(__version__))
    
    parser.add_argument('--graf_db',  default = 'testovací')
    
    #    a včíl to možu rozparsovat
    args = parser.parse_args()
    
    print('připojím se k databázi ',  args.graf_db)

    gdb = připojím_gdb(args.graf_db)
    seznam_indexů(gdb)
