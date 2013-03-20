#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

from . import E

class Seznam_klíčů(dict):
    
    def __init__(self,  xml):

        self.__xml = xml
        self.__klíče = None

       
    def __missing__(self,  klíč):

        tag = E.KEY
        tag['id'] = klíč
        element_klíče = self.__xml.find(str(tag))
        
        if element_klíče is None:
            raise KeyError('Klíč <key id = "{}" ... > nejestvuje.'.format(klíč))
  
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
          
            for definice in self.__xml.findall(str(E.KEY)):
                klíče.append(definice.attrib['id'])
            self.__klíče = klíče
        return iter(self.__klíče)
       
#    funkce keys() dělá totéž co __iter__
    keys = __iter__

