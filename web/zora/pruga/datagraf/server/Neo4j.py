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

class Neo4j(object):
    
    def __init__(self,  jméno_databáze):
        self.__jméno_databáze = jméno_databáze
        self.__adresář_databáze = os.path.join(os.path.dirname(__file__),  self.__jméno_databáze)
        
#        hen = os.path.dirname(__file__)
#        self.gdb_adresář = gdb_adresář = os.path.realpath(os.path.join(hen,  NEO4J_DIR,  adresář_databáze))
#        self.neo4j_bin = os.path.realpath(os.path.join(gdb_adresář,  NEO4J_BIN))
    
        debug('Vytvářím neo4j ovladač neo4j serveru, koji je v adresáři {}.'.format(self.__adresář_databáze))
        
        self.__url = None
    
    @property
    def __neo4j_bin(self):
#        mám použít os.path.realpath ????
        return os.path.join(self.__adresář_databáze,  'bin/neo4j')
 
    @property
    def __server_properties(self):
    
        soubor_nastavení = os.path.join(self.__adresář_databáze,  'conf/neo4j-server.properties')
        from . import pyproperties
        return pyproperties.Properties(soubor_nastavení)

    @property
    def server_properties(self):
        for klíč,  hodnota in self.__server_properties.properties.items():
            yield klíč,  hodnota

    def status(self):
        status = subprocess.check_output((self.__neo4j_bin,  'status')).decode('utf-8')
        
        debug('status: {}'.format(status))
        
        jméno_databáze = self.__jméno_databáze
        
        class Status(object):
            
            def __init__(self,  zpráva):
                self.__zpráva = zpráva
                if 'Neo4j Server is not running' in zpráva:
                    self.__spuštěno = False
                elif 'Neo4j Server is running' in zpráva:
                    self.__spuštěno = True
                else:
                    raise ValueError('Neznámý stav neo4j serveru: {}'.format(status))
    
            def __bool__(self):
                return self.__spuštěno
                
            def __eq__(self,  other):
                if isinstance(other,  bool):
                    return self.__spuštěno == other
                else:
                    raise TypeError('Neporovnatelno')
                
            def __str__(self):
                return 'stav neo4j databáze "{}": {}'.format(jméno_databáze,  self.__zpráva)
        
        return Status(zpráva = status)
             
    def start(self):
        '''
        spouštím funkci main()
        '''
        
        debug('zapnu server {}'.format(self.__neo4j_bin))
        
        status = self.status()
        
        if not status:
#            subprocess.Popen((self.neo4j_bin,  'start'))
            return subprocess.check_output((self.__neo4j_bin,  'start')).decode('utf-8')
        else:
            raise ValueError('Neo4j server nebyl spuštěn.\n\t{}'.format(status))
            
    def stop(self):
        '''
        spouštím funkci main()
        '''
        
        debug('vypnu server {}'.format(self.__neo4j_bin))
        
        status = self.status()
        if status:
#            subprocess.Popen((self.neo4j_bin,  'stop'))
            return subprocess.check_output((self.__neo4j_bin,  'stop')).decode('utf-8')
        else:
            raise ValueError('Neo4j server nebyl vypnut.\n\t{}'.format(status))
    
    
    
    @property
    def url(self):
        if self.__url is None:
    #        for klíč,  hodnota in nastavení.properties.items():
    #            print(klíč,  hodnota)
            nastavení = self.__server_properties
            nastavení.properties.setdefault('org.neo4j.server.webserver.address',  'localhost')
            neo4j_url_webserveru = 'http://{0[org.neo4j.server.webserver.address]}:{0[org.neo4j.server.webserver.port]}{0[org.neo4j.server.webadmin.data.uri]}'.format(nastavení.properties)
        
            self.__url =  neo4j_url_webserveru
        
        return self.__url
