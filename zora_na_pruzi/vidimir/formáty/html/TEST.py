#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

from zora_na_pruzi.vidimir.stroj.Formát import Formát

class TEST(object):
    
    TAB = 4
    
    @property
    def START(self):
        return Formát(formát = '<div class="TEST START">{}</div>')
 
    @property
    def OK(self):
        return Formát(formát = '<div class="TEST OK">{}</div>')

    @property
    def CHYBA(self):
        return Formát(formát = '<div class="TEST CHYBA">{}</div>')
        

        
TEST = TEST()
