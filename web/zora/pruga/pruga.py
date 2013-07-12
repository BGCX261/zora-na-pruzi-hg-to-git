#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

def vypíšu_dostupné_databáze():
    '''
    spouštím funkci main()
    '''
    from datagraf.server import davaj_seznam_databází
    
    print('dostupné databáze')
    
    for databáze in davaj_seznam_databází():
        print(databáze)
    else:
        print('není žádná databáze')

def vytvořím_databází(jméno_databáze,  instalační_soubor):
    
    from datagraf.instalace import instaluji_neo4j
    
    print('želím da vytvořím databázi "{}"'.format(jméno_databáze))
    
    try:
        instaluji_neo4j(jméno_databáze,  instalační_soubor)
    except AttributeError as e:
        print(e)

if __name__ == '__main__':

    print(__doc__)

    import argparse
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser(description = 'Správce balíčku pruga.',  epilog = 'Tož gazduj!!!')

#   a pak mu nastavím jaké příkazy a parametry má přijímat
    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, {}'.format(__version__))
    
    subparsers = parser.add_subparsers(help = 'modul příkazů')
    parser_neo4j = subparsers.add_parser('neo4j', help='správce neo4j databáze')
#    parser_neo4j.set_defaults(modul = 'datagraf.příkazy')
    
    neo4j_příkazy = {
                     'list': 44, 
                     'create': 12
                     }
    
#    parser_neo4j.add_argument('příkaz', choices = neo4j_příkazy.keys(), help='co učiniti s databází')
    
    parser_neo4j_subparsers = parser_neo4j.add_subparsers(help = 'příkaz')
    parser_neo4j_list = parser_neo4j_subparsers.add_parser('list', help='vypíše dostupné neo4j databáze')
    parser_neo4j_list.set_defaults(příkaz = vypíšu_dostupné_databáze)
    
    
    parser_neo4j_create = parser_neo4j_subparsers.add_parser('create', help='vytvoří neo4j databázi')
    parser_neo4j_create.add_argument('jméno_databáze')
    parser_neo4j_create.add_argument('instalační_soubor')
    parser_neo4j_create.set_defaults(příkaz = vytvořím_databází)

    
    #    a včíl to možu rozparsovat
    args = vars(parser.parse_args())
#    modul = args.pop('modul')
    příkaz = args.pop('příkaz')
    
#    modul = __import__(modul, globals(), locals(), [příkaz], 0)
#    příkaz = getattr(modul,  příkaz)
#    print(modul)
    
    print(args)
    příkaz(**args)

    
