#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

from . import NS_GRAPHML

class Seznam_klíčů(dict):
    
    def __init__(self,  xml):
#        if not for_element in ('graph',  'node',  'edge'):
#            raise TypeError('Seznam klíčů může být pouze pro graph, edge, nebo node.')
#        
#        self.__for_element = for_element
        self.__xml = xml
#        self.__klíče = None
       
#    def __getitem__(self,  klíč):
    def __missing__(self,  klíč):

#        def najdi_definici(klíč):
        if klíč not in self:
            element_klíče = self.__xml.find(NS_GRAPHML(NS_GRAPHML.key,  klíč = 'id',  hodnota = klíč))
            
            if element_klíče is None:
                raise KeyError('Klíč <key id = "{}" ... > nejestvuje.'.format(klíč))
#            for_element = element_klíče.attrib.get('for')
#            if for_element != self.__for_element:
#                raise TypeError('Klíč pro <key id = "{id}" for = "{for_element}" ... > není určen elementu "{má_být}" ale elementu "{for_element}"'.format(id = klíč,  má_být = self.__for_element,  for_element = for_element))
        
            self[klíč] = element_klíče 
            
        return self[klíč]
      

        
    def get(self,  klíč,  default  = None):
        try:
            return self.__getitem__(klíč)
        except KeyError:
            return default
        
    def items(self):
        for klíč in self.keys():
            yield (klíč,  self[klíč])
        
    def __iter__(self):
        if self.__klíče is None:
            klíče = []
            print('AAA ',  NS_GRAPHML(NS_GRAPHML.key,  klíč = 'for',  hodnota = self.__for_element))
            print(self.__for_element)
            for definice in self.__xml.findall(NS_GRAPHML(NS_GRAPHML.key,  klíč = 'for',  hodnota = self.__for_element)):
                print('KEZ ',  definice.attrib['id'],  definice.attrib['for'])
                klíče.append(definice.attrib['id'])
            self.__klíče = klíče
        return iter(self.__klíče)
       
#    funkce keys() dělá totéž co __iter__
    keys = __iter__

