#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který ...
'''

from postgresql.driver.pq3 import Statement
from postgresql.types import Row

class objektový_přístup_k_výsledku(object):
    
    def __init__(self,  statement):
        if not isinstance(statement,  Statement):
            raise TypeError('objektový_přístup_k_výsledku podporuje pouze postgresql.driver.pq3.Statement')
            
        self.__statement = statement
        
#        převod_typů = zip(statement.column_names,  statement.sql_column_types)
#        self.__převod_typů = dict(převod_typů)
        
        
#    def __getitem__(self,  klíč):
#        for řádek in self.__statement:
#            print(řádek,  type(řádek))
#            yield(řádek_výsledku(řádek))
            
    def __iter__(self):
        def řádek(řádek):
            return řádek_výsledku(řádek)
        return map(řádek,  self.__statement)
        
        
#    def sloupce(self):
#        return self.__statement.column_names
        
            
class řádek_výsledku(object):
    
    def __init__(self,  řádek):
        if not isinstance(řádek,  Row):
            raise TypeError('řádek_výsledku podporuje pouze postgresql.driver.pq3.Statement')
        self.__řádek = řádek
        
    def __getattr__(self,  klíč):
        return self.__řádek[klíč]
        
    def __str__(self):
        return str(self.__řádek)
        
    def __getitem__(self,  klíč):
        return self.__řádek[klíč]
        
    def __iter__(self):
        for klíč,  hodnota in self.__řádek.items():
            yield klíč,  hodnota
