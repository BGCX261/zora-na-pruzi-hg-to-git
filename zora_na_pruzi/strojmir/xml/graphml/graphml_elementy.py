#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import lxml.etree
from .__ELEMENT import __ELEMENT
from . import NS_GRAPHML

class graphml(__ELEMENT):
        
    __klíče = None
        
    @property
    def uzly(self):
        for uzel in self.getroottree().findall('//{}'.format(NS_GRAPHML.node)):
            yield uzel
            
    @property
    def vazby(self):
        for vazba in self.getroottree().findall('//{}'.format(NS_GRAPHML.edge)):
            yield vazba
            
    @property
    def klíče(self):
        if self.__klíče is None:
            from .seznam_klíčů import Seznam_klíčů
            self.__klíče = Seznam_klíčů(xml = self.getroottree())
            
        return self.__klíče
    
class key(__ELEMENT):
    
    __default = None
    
    @property
    def jméno(self):
        return self.attrib['attr.name']
        
    @property
    def datový_typ(self):
        return self.attrib['attr.type']
    
    @property
    def default(self):
        if self.__default is None:
            default = self.find(NS_GRAPHML.default)
            if default is not None:
                self.__default = default.text
        return self.__default
 
 
class __PRVEK_GRAFU(__ELEMENT):
    @property
    def jméno(self):
        return self.attrib['id']

    @property
    def data(self):
        return self.findall(NS_GRAPHML.data)

class graph(__PRVEK_GRAFU):
    pass
    
class node(__PRVEK_GRAFU):
    pass
    
class edge(__PRVEK_GRAFU):
    pass
    
class default(__ELEMENT):
    pass


class data(__ELEMENT):
    
#    __klíč = KLÍČE()
    __klíč = None
    
    @property
    def jméno(self):
        return self.klíč.jméno
        
    @property
    def datový_typ(self):
        return self.klíč.datový_typ
    
    @property
    def default(self):
        return self.klíč.default
        
    @property
    def klíč(self):
        if self.__klíč is None:
            klíče = self.getroottree().getroot().klíče
            id_klíče = self.attrib['key']
            self.__klíč = klíče[id_klíče]
            
        return self.__klíč
