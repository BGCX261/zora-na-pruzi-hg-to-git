#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

#import lxml.etree
from .__ELEMENT import __ELEMENT

NS_GRAPHML = '{http://graphml.graphdrawing.org/xmlns}'

class ATRIBUT(object):
    '''
    Tato třída umožní vytvořit vyhledávací parametr pomocí operátoru +
    '''
    
    def __init__(self,  klíč,  hodnota = None):
        if hodnota is None:
            self.__zápis = '[@{}]'.format(klíč)
        else:
            self.__zápis = '[@{}="{}"]'.format(klíč,  hodnota)
            
    def __radd__(self,  tag):
        return '{}{}'.format(tag,  self.__zápis)

    def __str__(self):
        return self.__zápis

class GRAPHML(__ELEMENT):
        
    TAG = '{}graphml'.format(NS_GRAPHML)
    __klíče = None
        
    @property
    def grafy(self):
        for graf in self.getroottree().findall('//{}'.format(GRAPH.TAG)):
            yield graf
            
    @property
    def graf(self):
        return self.find(GRAPH.TAG)
        
    @property
    def uzly(self):
        for uzel in self.getroottree().findall('//{}'.format(NODE.TAG)):
            yield uzel
            
    @property
    def vazby(self):
        for vazba in self.getroottree().findall('//{}'.format(EDGE.TAG)):
            yield vazba
            
    @property
    def klíče(self):
        if self.__klíče is None:
            from .seznam_klíčů import Seznam_klíčů
            self.__klíče = Seznam_klíčů(xml = self.getroottree())
            
        return self.__klíče
    
class KEY(__ELEMENT):
    
    TAG = '{}key'.format(NS_GRAPHML)
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
            default = self.find(DEFAULT.TAG)
            if default is not None:
                self.__default = default.text
        return self.__default
 
 
class __PRVEK_GRAFU(__ELEMENT):
    @property
    def jméno(self):
        return self.attrib['id']

    @property
    def data(self):
        return self.findall(DATA.TAG)

class GRAPH(__PRVEK_GRAFU):
    
    TAG = '{}graph'.format(NS_GRAPHML)
    
    @property
    def uzly(self):
        for uzel in self.findall(NODE.TAG):
            yield uzel
            
    @property
    def vazby(self):
        for vazba in self.findall(EDGE.TAG):
            yield vazba
    
class NODE(__PRVEK_GRAFU):
    
    TAG = '{}node'.format(NS_GRAPHML)
    
    @property
    def graf(self):
        '''
        vrátí vložený graf, jestvuje-li
        '''
        return self.find(GRAPH.TAG)
    
class EDGE(__PRVEK_GRAFU):
    
    TAG = '{}edge'.format(NS_GRAPHML)
    
    pass
    
class DEFAULT(__ELEMENT):
    
    TAG = '{}default'.format(NS_GRAPHML)
    
    pass


class DATA(__ELEMENT):
    
    TAG = '{}data'.format(NS_GRAPHML)

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
            klíč = klíče[id_klíče]
            if not self.getparent().tag.endswith(klíč.attrib['for']):
                raise TypeError('Klíč <key id={0} for={1}..>je určen pro {1} a nikolivěk pro {2}.'.format(id_klíče,  klíč.attrib['for'],  self.tag))
            self.__klíč = klíč
            
        return self.__klíč
