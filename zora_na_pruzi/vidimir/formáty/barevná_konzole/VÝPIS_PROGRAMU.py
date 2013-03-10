#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

#@TODO: Tohle je starý a zavržený způsob,  třeba přepracovat do nového,  nebo zrušit zcela

from zora_na_pruzi.vidimir.stroj.konzole.dekorátory import obarvi
from zora_na_pruzi.vidimir.stroj.konzole.barvy import *
#
##from zora_na_pruzi.vidimir import F
#      
#VÝPIS_PROGRAMU = Obarvi(BÍLÁ,  NA_TMAVĚ_SIVÉ)
@obarvi(BÍLÁ,  NA_TMAVĚ_SIVÉ)
def VÝPIS_PROGRAMU(text):
    return text        

