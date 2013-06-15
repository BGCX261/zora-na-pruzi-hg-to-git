#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

from py2neo import neo4j, cypher,  node,  rel

DOTAZY_JSOU_HEN = 'dotazy'

class Graf(dict):
    
    def __init__(self,  jméno):
        
        from pruga.databáze.Seznam_připojení import Seznam_připojení
        self.__neo4j =  Seznam_připojení[jméno]
        
        balíček = '.'.join(self.__class__.__module__.split('.')[:-1])
        self.__balíček = '{}.{}'.format(balíček,  DOTAZY_JSOU_HEN)
       
    @property
    def neo4j(self):
        return self.__neo4j
       
    def cypher(self,  dotaz,  parametry = None):
        return cypher.execute(self.__neo4j, dotaz,  parametry)[0]
      
#    def __ 
     
    def __missing__(self,  klíč):
        
        hledám_modul = klíč.split('.')
        jméno_funkce = hledám_modul.pop()
        hledám_modul.insert(0,  self.__balíček)
        cesta = '.'.join(hledám_modul)
        print(cesta)
        modul = __import__(cesta, globals(), locals(), [jméno_funkce], 0)
        print(modul.__name__)
        funkce = getattr(modul,  jméno_funkce)
        
#        self[klíč] = funkce
        return funkce(self)
