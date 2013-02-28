#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

from zora_na_pruzi.vidimir.stroj.konzole.obarvi import OBARVI
from zora_na_pruzi.vidimir.stroj.konzole.barvy import *

from zora_na_pruzi.vidimir import pohled as p

#NADPIS = OBARVI(ČERNÁ,  NA_SIVÉ,  nadtržítko = '=',  podtržítko = '=',  formát = '*** {} ***',  odsazení = 10)
#H1 = NADPIS
#H2 = OBARVI(ČERNÁ,  NA_SIVÉ,  formát = '| {} |',  nadtržítko = '_',  podtržítko = '-',  odsazení = 10)
#H3 = OBARVI(ČERNÁ,  NA_SIVÉ,   nadtržítko = '-.',  podtržítko = '-.',  odsazení = 10)
#
#INFO  = OBARVI(BÍLÁ,  NA_TMAVĚ_ČERVENÉ)
#CHYBA  = OBARVI(ŽLUTÁ,  NA_TMAVĚ_ČERVENÉ)
#
#PŘÍKAZ = OBARVI(BÍLÁ,  NA_TMAVĚ_ČERVENÉ,  PROHOĎ_BARVU_A_POZADÍ)
#SOUBOR = OBARVI(BÍLÁ,  TUČNĚ,  NA_TMAVĚ_SIVÉ)
#OBJEKT = OBARVI(SIVÁ,  TUČNĚ,  NA_ČERNÉ)

class TEST(object):
    
    TAB = 4
    
    @property
    def START(self):
        return OBARVI(ZELENÁ,  NA_TMAVĚ_AZUROVÉ,  formát = '{} {{}}'.format('startuji' | p.INFO))
 
    @property
    def OK(self):
        return OBARVI(ZELENÁ,  NA_TMAVĚ_AZUROVÉ,  formát = '{} {{}}'.format('... OK' | p.INFO),  odsazení = self.TAB)

    @property
    def CHYBA(self):
        return OBARVI(ŽLUTÁ,  NA_TMAVĚ_ČERVENÉ,  formát = '{} {{}}'.format('... CHYBA' | p.CHYBA),  odsazení = self.TAB)
        

        
TEST = TEST()
