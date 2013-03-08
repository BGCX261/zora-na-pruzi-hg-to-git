#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

from zora_na_pruzi.vidimir.__SOUBOR import __SOUBOR

class GRAPHML(__SOUBOR):
       
    def __call__(self):
        print(self.obsah.xml_deklarace)
        print(self)
