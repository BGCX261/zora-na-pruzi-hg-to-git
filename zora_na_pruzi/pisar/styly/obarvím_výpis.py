#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je nástroj, který obarví výpis
'''

from zora_na_pruzi.pisar.konzole.obarvi import OBARVI
from zora_na_pruzi.pisar.konzole.barvy import *


#from zora_na_pruzi.pohunci.obarvím_výpis import davaj_obarvovací_funkci
#
#obarvi_nadpis_print = davaj_obarvovací_funkci(barva = 'dark_blue', pozadí = 'on_green',  styl = ['bold'])
#obarvi_soubor_print = davaj_obarvovací_funkci(barva = 'white',  styl = ['bold'],  end = ' ')
#
#obarvi_spuštění_příkazu  = davaj_obarvovací_funkci(barva = 'white',  pozadí='on_dark_red',  end = ' ')
#obarvi_validaci  = davaj_obarvovací_funkci(barva = 'dark_blue',  pozadí = 'on_dark_white',  end = ' ')
#
#obarvi_zprávu_print = davaj_obarvovací_funkci(barva = 'red',  end = ' ')
#obarvi_poznámku_print = davaj_obarvovací_funkci(barva = 'green',  end = ' ')
#obarvi_upozornění_print = davaj_obarvovací_funkci(barva='dark_red',  pozadí='on_white',  end = ' ')

NADPIS = OBARVI(ČERNÁ,  NA_SIVÉ,  formát = '{0}\n\t{{}}\n{0}'.format('*'*64))

INFO  = OBARVI(BÍLÁ,  NA_TMAVĚ_ČERVENÉ)
CHYBA  = OBARVI(ŽLUTÁ,  NA_TMAVĚ_ČERVENÉ)

PŘÍKAZ = OBARVI(BÍLÁ,  NA_TMAVĚ_ČERVENÉ,  PROHOĎ_BARVU_A_POZADÍ)
SOUBOR = OBARVI(BÍLÁ,  TUČNĚ,  NA_TMAVĚ_SIVÉ)
