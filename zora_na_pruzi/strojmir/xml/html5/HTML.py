#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je třída, která ...
'''
#import lxml.etree
from . import __ELEMENT_HTML5,  E

class HTML(__ELEMENT_HTML5):
    
    @property
    def titulek(self):
        return self._davaj_obsah_jedinečného(E.TITLE)
        
    @titulek.setter
    def titulek(self,  titulek):
        self._nastav_obsah_jedinečného(E.TITLE, titulek)
        
    @property
    def popisek(self):
        tag = E.META
        tag['name'] = 'description'
        meta = self._davaj_jedinečného(tag)
        return meta.get('content',  None)
        
    @popisek.setter
    def popisek(self,  popisek):
        tag = E.META
        tag['name'] = 'description'
        meta = self._davaj_či_vytvoř_jedinečného(tag)
        meta.set('content',  popisek)
