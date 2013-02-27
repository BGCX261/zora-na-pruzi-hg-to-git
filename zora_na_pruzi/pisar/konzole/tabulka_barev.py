#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je skript, který vypíše tab ulku všech barev

    0 – vypne všechny atributy
    1 – tučný text
    4 – jednoduché podtržení
    5 – blikající text
    7 – prohodí barvy popředí a pozadí
    39 – nastaví výchozí barvu popředí
    49 – nastaví výchozí barvu pozadí
    30 až 37, 90 až 99 – nastavuje barvu popředí (jako proměnná „a“)
    40 až 47, 100 až 109 – nastavuje barvu pozadí (jako proměnná „a“)
    
    číslo		0		      1		     2		      3		 4		          5		        6		        7
    barva   černá   červená     zelená  žlutá   modrá   purpurová   tyrkysová   bílá 

'''

from zora_na_pruzi.pisar.konzole import barvy as modul_barev
from zora_na_pruzi.pisar.konzole.obarvi import OBARVI

barvy = ['BÍLÁ', 'TMAVĚ_MODRÁ', 'MODRÁ', 'ŽLUTÁ', 'SIVÁ', 'TMAVĚ_SIVÁ', 'AZUROVÁ', 'ČERNÁ', 'ČERVENÁ', 'TMAVĚ_ČERVENÁ', 'TMAVĚ_PURPUROVÁ', 'PURPUROVÁ', 'TMAVĚ_ZELENÁ', 'TMAVĚ_AZUROVÁ', 'TMAVĚ_ŽLUTÁ', 'ZELENÁ']
styly = ['PROHOĎ_BARVU_A_POZADÍ', 'BLIKACÍ', 'UKRYTÝ', 'TUČNĚ', 'PODTRŽENÝ']
pozadí = ['NA_TMAVĚ_AZUROVÉ', 'NA_TMAVĚ_ŽLUTÉ', 'NA_BÍLÉ', 'NA_AZUROVÉ', 'NA_TMAVĚ_ČERVENÉ', 'NA_ŽLUTÉ', 'NA_PURPUROVÉ', 'NA_TMAVĚ_ZELENÉ', 'NA_SIVÉ', 'NA_ČERVENÉ', 'NA_ČERNÉ', 'NA_TMAVĚ_MODRÉ', 'NA_MODRÉ', 'NA_TMAVĚ_PURPUROVÉ', 'NA_TMAVĚ_SIVÉ', 'NA_ZELENÉ']
for jméno_barvy in barvy:
    barva = getattr(modul_barev,  jméno_barvy)
    obarvím = OBARVI(barva)
    print('barva: ',  jméno_barvy | obarvím)
    for jméno_pozadí in pozadí:
        barva_pozadí = getattr(modul_barev,  jméno_pozadí)
        obarvím = OBARVI(barva,  barva_pozadí)
        print(jméno_pozadí | obarvím,  end = ' ')
        for jméno_stylu in styly:
            styl =  getattr(modul_barev,  jméno_stylu)
            obarvím = OBARVI(barva,  barva_pozadí,  styl)
            print(jméno_stylu | obarvím,  end = ' ')
        print()
    print('-'*44)
