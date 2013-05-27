#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který spustí neo4j server
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

import os
import py2neo
#from py2neo import neo4j

NEO4J_URL = 'http://localhost:7474/db/data/'
NEO4J_ADRESÁŘ = '/opt/neo4j/databáze/testovací'
NEO4J_BIN = 'bin/neo4j'
NEO4J_SERVER_PROPERTIES = 'conf/neo4j-server.properties'

def připojím_se_k_databázi(NEO4J_URL,  NEO4J_ADRESÁŘ):
    '''
    spouštím funkci připojím_se_k_databázi()
    '''
    try:
        graph_db = py2neo.neo4j.GraphDatabaseService(NEO4J_URL)
        print('připojil jsem se k neo4j databázi na {}'.format(NEO4J_URL))
    except py2neo.rest.SocketError as e:
        if NEO4J_ADRESÁŘ is not None:
            příkaz = '{} start'.format(os.path.join(NEO4J_ADRESÁŘ,  NEO4J_BIN))
            from zora_na_pruzi.system.spustím_příkaz import spustím_příkaz_a_vypíšu
            spustím_příkaz_a_vypíšu(příkaz)
            NEO4J_URL = zjistím_neo4j_url_z_konfigurace(NEO4J_ADRESÁŘ)
            připojím_se_k_databázi(NEO4J_URL,  None)
        else:
            raise e
            
def zjistím_neo4j_url_z_konfigurace(NEO4J_ADRESÁŘ):
        soubor_nastavení = os.path.join(NEO4J_ADRESÁŘ,  NEO4J_SERVER_PROPERTIES)
        import pyproperties
        nastavení = pyproperties.Properties(soubor_nastavení)
#        for klíč,  hodnota in nastavení.properties.items():
#            print(klíč,  hodnota)

        nastavení.properties.setdefault('org.neo4j.server.webserver.address',  'localhost')
        neo4j_url_webserveru = 'http://{0[org.neo4j.server.webserver.address]}:{0[org.neo4j.server.webserver.port]}{0[org.neo4j.server.webadmin.data.uri]}'.format(nastavení.properties)
        
        return neo4j_url_webserveru

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

    připojím_se_k_databázi(NEO4J_URL,  NEO4J_ADRESÁŘ)
