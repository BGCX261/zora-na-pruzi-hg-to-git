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

NEO4J_DIR = 'neo4j_servery'
NEO4J_BIN = 'bin/neo4j'

ZAPNUTO = 'server je zapnut'
VYPNUTO = 'server je vypnut'

class Neo4j(object):
    
    def __init__(self,  adresář_databáze):
         
        hen = os.path.dirname(__file__)
        gdb_adresář = os.path.realpath(os.path.join(hen,  NEO4J_DIR,  adresář_databáze))
        self.neo4j_bin = os.path.realpath(os.path.join(gdb_adresář,  NEO4J_BIN))
    
        print('Vytvářím neo4j server z adresáře {}.'.format(gdb_adresář))
    
    def status(self):
        status = subprocess.check_output((self.neo4j_bin,  'status')).decode('utf-8')
        
        print(status)
        
        if 'Neo4j Server is not running' in status:
            return VYPNUTO,  status
             
        if 'Neo4j Server is running' in status:
            return ZAPNUTO,  status
             
        raise ValueError('Neznámý stav neo4j serveru: {}'.format(status))
    
    def start(self):
        '''
        spouštím funkci main()
        '''
        
        print('zapnu server {}'.format(self.neo4j_bin))
        
        stav,  status = self.status()
        if stav == VYPNUTO:
            subprocess.Popen((self.neo4j_bin,  'start'))
        else:
            raise ValueError('Neo4j server nebyl spuštěn. Status: {}'.format(status))
            
    def stop(self):
        '''
        spouštím funkci main()
        '''
        
        print('vypnu server {}'.format(self.neo4j_bin))
        
        stav,  status = self.status()
        if stav == ZAPNUTO:
            subprocess.Popen((self.neo4j_bin,  'stop'))
        else:
            raise ValueError('Neo4j server nebyl vypnut. Status: {}'.format(status))
    

    

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
    
    spusť = getattr(neo4j,  args.úkol)
    spusť()

   
