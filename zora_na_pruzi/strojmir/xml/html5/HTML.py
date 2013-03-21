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
    def hlavička(self):
        return self._davaj_či_vytvoř_jedinečného(E.HEAD)
        
    @property
    def tělo(self):
        return self._davaj_či_vytvoř_jedinečného(E.BODY)
