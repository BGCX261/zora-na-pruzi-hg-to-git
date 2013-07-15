#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

def main():
    '''
    spouštím funkci main()
    '''
    
    db = připojím_postgrersql()
    for účet in sql_účetní_osnova(db):
        print(účet)

def připojím_postgrersql():
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
#    
#    parser.add_argument('soubor')
#    
#    #    a včíl to možu rozparsovat
#    args = parser.parse_args()
#    
#    print('soubor',  args.soubor)

    main()
