#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je třída, která ...
'''
#import lxml.etree
from . import __ELEMENT_GRAFU,  E


class GRAPHML(__ELEMENT_GRAFU):
    
    __klíče = None
    
    @property
    def grafy(self):
        for graf in self.getroottree().findall('//{}'.format(E.GRAPH.TAG_NAME)):
            yield graf
            
    @property
    def graf(self):
        return self.find(E.GRAPH.TAG_NAME)
        
    @property
    def uzly(self):
        for uzel in self.getroottree().findall('//{}'.format(E.NODE.TAG_NAME)):
            yield uzel
            
    @property
    def vazby(self):
        for vazba in self.getroottree().findall('//{}'.format(E.EDGE.TAG_NAME)):
            yield vazba
            
    @property
    def klíče(self):
        if self.__klíče is None:
            from .seznam_klíčů import Seznam_klíčů
            self.__klíče = Seznam_klíčů(xml = self.getroottree())
            
        return self.__klíče
 
