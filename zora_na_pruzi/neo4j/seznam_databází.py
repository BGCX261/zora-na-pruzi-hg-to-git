#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

import os
from zora_na_pruzi.neo4j import *

def davaj_seznam_databází():
    '''
    spouštím funkci main()
    '''
    for adresář in os.listdir(NEO4J_ADRESÁŘ_DATABÁZÍ):
        yield adresář
    

def davaj_properties(adresář):
    properties = načtu_properties_serveru(adresář)
    port = properties['org.neo4j.server.webserver.port']
    adresa = properties['org.neo4j.server.webserver.address']
    
    properties = načtu_properties_wrapperu(adresář)
    port = properties['wrapper.name']

if __name__ == '__main__':

#    print(__doc__)
#
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

    seznam_databází = davaj_seznam_databází()
    for databáze in seznam_databází:
        print(databáze)
