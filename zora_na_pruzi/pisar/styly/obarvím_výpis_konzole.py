#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je nástroj, který obarví výpis
'''

from zora_na_pruzi.pisar.konzole.obarvi import OBARVI
from zora_na_pruzi.pisar.konzole.barvy import *

NADPIS = OBARVI(ČERNÁ,  NA_SIVÉ,  formát = '{0}\n\t{{}}\n{0}'.format('*'*64))

INFO  = OBARVI(BÍLÁ,  NA_TMAVĚ_ČERVENÉ)
CHYBA  = OBARVI(ŽLUTÁ,  NA_TMAVĚ_ČERVENÉ)

PŘÍKAZ = OBARVI(BÍLÁ,  NA_TMAVĚ_ČERVENÉ,  PROHOĎ_BARVU_A_POZADÍ)
SOUBOR = OBARVI(BÍLÁ,  TUČNĚ,  NA_TMAVĚ_SIVÉ)
