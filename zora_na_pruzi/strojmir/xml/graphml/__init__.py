#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>
    
from ..__ELEMENT import __ELEMENT
from ..__DAVAJ_ELEMENT import __DAVAJ_ELEMENT as E

#from zora_na_pruzi.strojmir.css.CSS_TABULKA import CSS_TABULKA

#from ..PATH import ATRIBUT

from . import __nastavení
__nastavení.balíček = __name__
E = E(__nastavení)

class __ELEMENT_GRAFU(__ELEMENT):
    pass
