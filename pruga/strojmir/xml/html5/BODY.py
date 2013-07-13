#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

from . import __ELEMENT_HTML5,  E

class BODY(__ELEMENT_HTML5):
    
    @property
    def záhlaví(self):
        return self._davaj_či_vytvoř_jedinečného(E.HEADER)
        
    @property
    def zápatí(self):
        return self._davaj_či_vytvoř_jedinečného(E.FOOTER)
