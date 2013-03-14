#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

from . import __ELEMENT_GRAFU
    
class DATA(__ELEMENT_GRAFU):

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

