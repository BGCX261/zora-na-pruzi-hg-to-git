#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

from zora_na_pruzi.vidimir.stroj.konzole.Obarvi import Obarvi
from zora_na_pruzi.vidimir.stroj.konzole.barvy import *

from zora_na_pruzi.vidimir import F

#NADPIS = Obarvi(ČERNÁ,  NA_SIVÉ,  nadtržítko = '=',  podtržítko = '=',  formát = '*** {} ***',  odsazení = 10)
#H1 = NADPIS
#H2 = Obarvi(ČERNÁ,  NA_SIVÉ,  formát = '| {} |',  nadtržítko = '_',  podtržítko = '-',  odsazení = 10)
#H3 = Obarvi(ČERNÁ,  NA_SIVÉ,   nadtržítko = '-.',  podtržítko = '-.',  odsazení = 10)
#
#INFO  = Obarvi(BÍLÁ,  NA_TMAVĚ_ČERVENÉ)
#CHYBA  = Obarvi(ŽLUTÁ,  NA_TMAVĚ_ČERVENÉ)
#
#PŘÍKAZ = Obarvi(BÍLÁ,  NA_TMAVĚ_ČERVENÉ,  PROHOĎ_BARVU_A_POZADÍ)
#SOUBOR = Obarvi(BÍLÁ,  TUČNĚ,  NA_TMAVĚ_SIVÉ)
#OBJEKT = Obarvi(SIVÁ,  TUČNĚ,  NA_ČERNÉ)

class TEST(object):
    
    TAB = 4
    
    @property
    def START(self):
        return Obarvi(ZELENÁ,  NA_TMAVĚ_AZUROVÉ,  formát = '{} {{}}'.format('startuji' | F.INFO))
 
    @property
    def OK(self):
        return Obarvi(ZELENÁ,  NA_TMAVĚ_AZUROVÉ,  formát = '{} {{}}'.format('... OK' | F.INFO),  odsazení = self.TAB)

    @property
    def CHYBA(self):
        return Obarvi(ŽLUTÁ,  NA_TMAVĚ_ČERVENÉ,  formát = '{} {{}}'.format('... CHYBA' | F.CHYBA),  odsazení = self.TAB)
        

        
TEST = TEST()
