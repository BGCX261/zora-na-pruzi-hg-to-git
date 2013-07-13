#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>
    
from ..__ELEMENT import __ELEMENT
from ..__DAVAJ_ELEMENT import __DAVAJ_ELEMENT as E

import lxml.etree

#from zora_na_pruzi.strojmir.css.CSS_TABULKA import CSS_TABULKA

#from ..PATH import ATRIBUT



from . import __nastavení
__nastavení.balíček = __name__
E = E(__nastavení)

class __ELEMENT_HTML5(__ELEMENT):
    
    def __str__(self):
        return lxml.etree.tounicode(self,  pretty_print=True,  method="html",  doctype='<!doctype html>')
        
    def css_link(self,  CSS):
        soubor = CSS.soubor
        print(soubor)
        if soubor is None:
            raise ValueError('CSS není uloženo do souboru.')
        self.getroottree().getroot().hlavička.append(E.LINK(rel = 'stylesheet',  href = soubor))
