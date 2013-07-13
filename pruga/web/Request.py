#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

#from urllib.parse import urlencode, quote,  unquote
from urllib.parse import unquote

class Request(object):
    
    def __init__(self,  environ = None):
        self.__environ = environ or {}
        self.__cesta = None
        self.__query = None
        
    @property
    def cesta(self):
        if self.__cesta is None:
            cesta = self.__environ['PATH_INFO']
            try:
                cesta = cesta.encode('latin1').decode('utf8')
            except (UnicodeEncodeError,  UnicodeDecodeError) as e:
                print(e)
                
            self.__cesta = cesta.strip('/').split('/')
            
        return self.__cesta
        
    @property
    def parametry(self):
        metoda = self.metoda
        
        if metoda == 'GET':
            return self.GET
            
        raise AttributeError('Nemám atributy pro požadavek metodou {}'.format(metoda))
        
    @property
    def GET(self):
        if self.__query is None:
            self.__query = {}
            query_string = self.__environ.get('QUERY_STRING', '')
            
            for str_páru in query_string.replace(';','&').split('&'):
                if not str_páru:
                    continue
                pár = str_páru.split('=', 1)
                if len(pár) != 2:
                    pár.append('')
                klíč = unquote(pár[0].replace('+', ' '))
                hodnota = unquote(pár[1].replace('+', ' '))
                self.__query[klíč] = hodnota
        
        return self.__query
        
    @property
    def metoda(self):
        return self.__environ.get('REQUEST_METHOD', 'GET').upper()
