#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

#@TODO: Tohle je rozpracovaná předělávka na nový způsob, nemá původní funkčnost, dodělat, nebo odstranit

from zora_na_pruzi.vidimir.stroj.konzole.dekorátory import obarvi
from zora_na_pruzi.vidimir.stroj.konzole.barvy import *

from zora_na_pruzi.vidimir.Formátuji import TEXT

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

    
TAB = 4

#START = Obarvi(ZELENÁ,  NA_TMAVĚ_AZUROVÉ,  formát = '{} {{}}'.format('startuji' | TEXT.INFO))
def START(text):
    return text

#OK = Obarvi(ZELENÁ,  NA_TMAVĚ_AZUROVÉ,  formát = '{} {{}}'.format('... OK' | TEXT.INFO),  odsazení = TAB)
def OK(text):
    return text

#CHYBA = Obarvi(ŽLUTÁ,  NA_TMAVĚ_ČERVENÉ,  formát = '{} {{}}'.format('... CHYBA' | TEXT.CHYBA),  odsazení = TAB)
def CHYBA(text):
    return text

