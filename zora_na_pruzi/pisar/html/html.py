#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je objekt, který upraví výpis pomocí html
Nejdříve vytvoříš instanci a tu pak použiješ pomocí operátoru |
from lxml.html import builder as E
html = HTML(E.P('{}', E.CLASS('třída'), styl='styl')
kód = 'nějaký text' | html
print(kód)

barvy jsou uvedeny v souboru barvy
'''

import lxml.html

from lxml.html import builder as E

class HTML(object):
    
    def __init__(self,  element):
#    def __init__(self,  barva, pozadí = None,  styl = None,  formát = None):
        
        self.__html = lxml.html.tostring(element,   pretty_print=True).decode(encoding = 'UTF-8')
            
    def __ror__(self,  text):
        return self.__html.format(text)
