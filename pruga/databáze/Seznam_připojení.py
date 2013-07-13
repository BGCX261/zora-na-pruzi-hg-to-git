#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

class Seznam_připojení(dict):
    
    def __missing__(self,  jméno):
        from pruga.databáze.Neo4j import Neo4j,  VYPNUTO
        neo4j_server = Neo4j(jméno)
        
        stav,  status = neo4j_server.status()
    
        if stav == VYPNUTO:
            neo4j_server.start()
        
        from py2neo.neo4j import GraphDatabaseService
        self[jméno] = GraphDatabaseService(neo4j_server.url)
        return self[jméno]
    
Seznam_připojení = Seznam_připojení()


    

    
