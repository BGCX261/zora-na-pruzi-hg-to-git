#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který spustí neo4j server
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

from py2neo import neo4j


def main():
    '''
    spouštím funkci main()
    '''
    graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")
    print(graph_db)
    print(vars(graph_db))

if __name__ == '__main__':

    print(__doc__)

#    import argparse
#    #  nejdříve si parser vytvořím
#    parser = argparse.ArgumentParser()
#
##   a pak mu nastavím jaké příkazy a parametry má přijímat
#    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, {}'.format(__version__))
#    
#    parser.add_argument('soubor')
#    
#    #    a včíl to možu rozparsovat
#    args = parser.parse_args()
#    
#    print('soubor',  args.soubor)

    main()
