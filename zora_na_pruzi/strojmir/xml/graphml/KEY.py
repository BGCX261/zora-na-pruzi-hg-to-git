#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

from . import __ELEMENT_GRAFU,  E

class KEY(__ELEMENT_GRAFU):
    
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
            default = self.find(E.DEFAULT.TAG)
            if default is not None:
                self.__default = default.text
        return self.__default
 
