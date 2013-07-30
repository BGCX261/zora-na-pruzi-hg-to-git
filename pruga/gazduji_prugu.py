#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

import logging
logger = logging.getLogger(__name__)
debug = logger.debug
    
    
def vypíšu_dostupné_databáze(podrobně = None):
    '''
    spouštím funkci main()
    '''
    from datagraf.server import davaj_jména_databází
    
    print('dostupné databáze')
    
    i = 0
    for i,  jméno_databáze in enumerate(davaj_jména_databází(),  start = 1):
        if podrobně:
            neo4j_server = __davaj_neo4j_server(jméno_databáze)
            print('{0}: {1} {2.url} {3}'.format(i,  jméno_databáze,  neo4j_server,  neo4j_server.status()))
        else:
            print('{}: {}'.format(i,  jméno_databáze))
    else:
        if i == 0:
            print('není žádná databáze')

def vytvořím_databází(jméno_databáze,  instalační_soubor):
    
    from datagraf.instalace import instaluji_neo4j
    
    print('želím da vytvořím databázi "{}"'.format(jméno_databáze))
    
    try:
        instaluji_neo4j(jméno_databáze,  instalační_soubor)
    except AttributeError as e:
        print(e)

def __davaj_neo4j_server(jméno_databáze):
    from servery import davaj_server
    
    return davaj_server(jméno_databáze)

def davaj_server_properties(jméno_databáze):
    
    neo4j_server = __davaj_neo4j_server(jméno_databáze)
    for klíč,  hodnota in neo4j_server.properties():
        print(klíč,  hodnota)

def davaj_url_serveru(jméno_databáze):
    neo4j_server = __davaj_neo4j_server(jméno_databáze)
    
    print('url serveru {} je {}'.format(jméno_databáze,  neo4j_server.url))
 
def startuji_neo4j_server(jméno_databáze):
    neo4j_server = __davaj_neo4j_server(jméno_databáze)
    try:
        výpis = neo4j_server.start()
        print(výpis)
    except ValueError as e:
        print(e)
    
def zastavím_neo4j_server(jméno_databáze):
    neo4j_server = __davaj_neo4j_server(jméno_databáze)
    try:
        výpis = neo4j_server.stop()
        print(výpis)
    except ValueError as e:
        print(e)
    
def davaj_stav_neo4j_serveru(jméno_databáze):
    neo4j_server = __davaj_neo4j_server(jméno_databáze)
    výpis = neo4j_server.status()
    print(výpis)

if __name__ == '__main__':

    print('Пруга ради')

    import argparse
    
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser(description = 'Správce balíčku pruga.',  epilog = 'Tož gazduj!!!')

#   a pak mu nastavím jaké příkazy a parametry má přijímat
    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, {}'.format(__version__))
    
    parser.add_argument('--debug', '-d',  action='store_const', const=logging.DEBUG, default=logging.ERROR)
    
    
    subparsers = parser.add_subparsers(help = 'modul příkazů')
    parser_neo4j = subparsers.add_parser('neo4j', help='správce neo4j databáze')
#    parser_neo4j.set_defaults(modul = 'datagraf.příkazy')
    
#    parser_neo4j.add_argument('příkaz', choices = neo4j_příkazy.keys(), help='co učiniti s databází')
    
    parser_neo4j_subparsers = parser_neo4j.add_subparsers(help = 'příkaz')
    parser_neo4j_list = parser_neo4j_subparsers.add_parser('list', help='vypíše dostupné neo4j databáze')
    parser_neo4j_list.add_argument('--podrobně',  action='store_true')
    parser_neo4j_list.set_defaults(příkaz = vypíšu_dostupné_databáze)
    
    
    parser_neo4j_create = parser_neo4j_subparsers.add_parser('create', help='vytvoří neo4j databázi')
    parser_neo4j_create.add_argument('jméno_databáze')
    parser_neo4j_create.add_argument('instalační_soubor')
    parser_neo4j_create.set_defaults(příkaz = vytvořím_databází)
    
    parser_neo4j_create = parser_neo4j_subparsers.add_parser('properties', help='vypíšu nastavení neo4j databáze')
    parser_neo4j_create.add_argument('jméno_databáze')
    parser_neo4j_create.set_defaults(příkaz = davaj_server_properties)

    parser_neo4j_create = parser_neo4j_subparsers.add_parser('url', help='vypíšu url adresu neo4j databáze')
    parser_neo4j_create.add_argument('jméno_databáze')
    parser_neo4j_create.set_defaults(příkaz = davaj_url_serveru)

    parser_neo4j_create = parser_neo4j_subparsers.add_parser('start', help='spustím neo4j databázový server')
    parser_neo4j_create.add_argument('jméno_databáze')
    parser_neo4j_create.set_defaults(příkaz = startuji_neo4j_server)

    parser_neo4j_create = parser_neo4j_subparsers.add_parser('stop', help='vypnu neo4j databázový server')
    parser_neo4j_create.add_argument('jméno_databáze')
    parser_neo4j_create.set_defaults(příkaz = zastavím_neo4j_server)

    parser_neo4j_create = parser_neo4j_subparsers.add_parser('status', help='vypíšu stav neo4j databázového serveru')
    parser_neo4j_create.add_argument('jméno_databáze')
    parser_neo4j_create.set_defaults(příkaz = davaj_stav_neo4j_serveru)


    #    a včíl to možu rozparsovat
    args = vars(parser.parse_args())
#    modul = args.pop('modul')
    příkaz = args.pop('příkaz')
    
    logging.basicConfig(level = args.pop('debug'))
    debug('volám {} s parametry {}'.format(příkaz.__name__,  args) )
    příkaz(**args)

    
