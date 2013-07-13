#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

import os
import subprocess

import logging
logger = logging.getLogger(__name__)
debug = logger.debug

NEO4J_DIR = 'neo4j_servery'
NEO4J_BIN = 'bin/neo4j'
NEO4J_SERVER_PROPERTIES = 'conf/neo4j-server.properties'

ZAPNUTO = 'server je zapnut'
VYPNUTO = 'server je vypnut'

class Neo4j(object):
    
    def __init__(self,  adresář_databáze):
         
        hen = os.path.dirname(__file__)
        self.gdb_adresář = gdb_adresář = os.path.realpath(os.path.join(hen,  NEO4J_DIR,  adresář_databáze))
        self.neo4j_bin = os.path.realpath(os.path.join(gdb_adresář,  NEO4J_BIN))
    
        debug('Vytvářím neo4j ovladač neo4j serveru, koji je v adresáři {}.'.format(gdb_adresář))
        
        self.__url = None
    
    def status(self):
        status = subprocess.check_output((self.neo4j_bin,  'status')).decode('utf-8')
        
        debug('status: {}'.format(status))
        
        if 'Neo4j Server is not running' in status:
            return VYPNUTO,  status
             
        if 'Neo4j Server is running' in status:
            return ZAPNUTO,  status
             
        raise ValueError('Neznámý stav neo4j serveru: {}'.format(status))
    
    def start(self):
        '''
        spouštím funkci main()
        '''
        
        debug('zapnu server {}'.format(self.neo4j_bin))
        
        stav,  status = self.status()
        if stav == VYPNUTO:
#            subprocess.Popen((self.neo4j_bin,  'start'))
            return subprocess.check_output((self.neo4j_bin,  'start')).decode('utf-8')
        else:
            raise ValueError('Neo4j server nebyl spuštěn. Status: {}'.format(status))
            
    def stop(self):
        '''
        spouštím funkci main()
        '''
        
        debug('vypnu server {}'.format(self.neo4j_bin))
        
        stav,  status = self.status()
        if stav == ZAPNUTO:
#            subprocess.Popen((self.neo4j_bin,  'stop'))
            return subprocess.check_output((self.neo4j_bin,  'stop')).decode('utf-8')
        else:
            raise ValueError('Neo4j server nebyl vypnut. Status: {}'.format(status))
    

    @property
    def url(self):
        if self.__url is None:
         
            soubor_nastavení = os.path.join(self.gdb_adresář,  NEO4J_SERVER_PROPERTIES)
            from pruga.databáze import pyproperties
            nastavení = pyproperties.Properties(soubor_nastavení)
    #        for klíč,  hodnota in nastavení.properties.items():
    #            print(klíč,  hodnota)

            nastavení.properties.setdefault('org.neo4j.server.webserver.address',  'localhost')
            neo4j_url_webserveru = 'http://{0[org.neo4j.server.webserver.address]}:{0[org.neo4j.server.webserver.port]}{0[org.neo4j.server.webadmin.data.uri]}'.format(nastavení.properties)
        
            self.__url =  neo4j_url_webserveru
        
        return self.__url

if __name__ == '__main__':

    print(__doc__)

    import argparse
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser()

#   a pak mu nastavím jaké příkazy a parametry má přijímat
    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, {}'.format(__version__))
    
    parser.add_argument('--graf_db',  default = 'testovací')
    parser.add_argument('úkol',  default = 'status')
    
    #    a včíl to možu rozparsovat
    args = parser.parse_args()

    neo4j = Neo4j(args.graf_db)
    
    if args.úkol == 'url':
        print('url neo4j serveru',  neo4j.url)
    else:
        spusť = getattr(neo4j,  args.úkol)
        print(spusť())

   
