#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je třída, která ...
'''

from ..konstanty import *

class Statistika(object):
    
    def __init__(self,  talasnica):
        
        self.__talasnica = talasnica
        
        #         při otevření svíce potřebuji profit pouze z obchodů, které byly otevřeny nejpopzději na předchozí svíci
#          při exportu s evšak k takové hodnotě nemohu dostat, neboť získávám až data s nově otevřenými obchody
#       proto si ten profit spočtu a uložím při započetí průchoud
        self.profit_při_otevření = None
        
#        statistické informace
        self.počáteční_čas = None
        self.konečný_čas = None
        self.samoj_bolšoj_otevřený_zisk = {OPEN: None,  HIGHT: None,  LOW: None,  CLOSE: None}
        self.samaja_bolšaja_otevřená_ztráta = {OPEN: None,  HIGHT: None,  LOW: None,  CLOSE: None}
        self.samoj_bolšoj_celkový_zisk = {OPEN: None,  HIGHT: None,  LOW: None,  CLOSE: None}
        self.samaja_bolšaja_celková_ztráta = {OPEN: None,  HIGHT: None,  LOW: None,  CLOSE: None}
        self.samaja_bolšaja_velikost = {HORE: None,  DOLE: None}
        self.samoj_bolšoj_býk = None
        self.samoj_bolšoj_medvěd = None
        self.počet_svíček = None
        
        self.počítadlo_znamení_vstupů = 0
        
        
    def na_první_svíčce(self):
        self.počáteční_čas = self.__talasnica.data[OPEN_TIME]
        self.počet_svíček = self.__talasnica.data[BAR]
        
    def pří_otevření_svíčky(self):
        
        self.poslední_svíce = self.__talasnica.data
        
        self.konečný_čas = self.__talasnica.data[OPEN_TIME]
            
        self.zisk_při_otevření = self.__talasnica.obchody.zisk(self.__talasnica.data[OPEN])
        
        self.samoj_bolšoj_otevřený_zisk[OPEN] = max(self.samoj_bolšoj_otevřený_zisk[OPEN] or 0,  self.zisk_při_otevření)
        self.samaja_bolšaja_otevřená_ztráta[OPEN] = min(self.samaja_bolšaja_otevřená_ztráta[OPEN] or 0,  self.zisk_při_otevření)
        celkový_zisk = self.zisk_při_otevření + self.__talasnica.obchody.uložený_zisk + self.__talasnica.obchody.swap
        self.samoj_bolšoj_celkový_zisk[OPEN] = max(self.samoj_bolšoj_celkový_zisk[OPEN] or 0,  celkový_zisk)
        self.samaja_bolšaja_celková_ztráta[OPEN] = min(self.samaja_bolšaja_celková_ztráta[OPEN] or 0,  celkový_zisk)
        
    def pří_zavření_svíčky(self):
        self.samoj_bolšoj_býk = max(self.samoj_bolšoj_býk or 0, self.__talasnica.obchody.býci.velikost )
        self.samoj_bolšoj_medvěd = max(self.samoj_bolšoj_medvěd or 0,  self.__talasnica.obchody.medvědi.velikost)
        
        velikost_postavení = self.__talasnica.obchody.velikost
        self.samaja_bolšaja_velikost[HORE] = max(self.samaja_bolšaja_velikost[HORE] or 0,  velikost_postavení)
        self.samaja_bolšaja_velikost[DOLE] = min(self.samaja_bolšaja_velikost[DOLE] or 0,  velikost_postavení)
        
        for KLÍČ_NA_CENĚ in HIGHT,  LOW,  CLOSE:
            zisk = self.__talasnica.obchody.zisk(self.__talasnica.data[KLÍČ_NA_CENĚ])
            self.samoj_bolšoj_otevřený_zisk[KLÍČ_NA_CENĚ] = max(self.samoj_bolšoj_otevřený_zisk[KLÍČ_NA_CENĚ] or 0,  zisk)
            self.samaja_bolšaja_otevřená_ztráta[KLÍČ_NA_CENĚ] = min(self.samaja_bolšaja_otevřená_ztráta[KLÍČ_NA_CENĚ] or 0, zisk)
            celkový_zisk = zisk + self.__talasnica.obchody.uložený_zisk + self.__talasnica.obchody.swap
            self.samoj_bolšoj_celkový_zisk[KLÍČ_NA_CENĚ] = max(self.samoj_bolšoj_celkový_zisk[KLÍČ_NA_CENĚ] or 0,  celkový_zisk)
            self.samaja_bolšaja_celková_ztráta[KLÍČ_NA_CENĚ] = min(self.samaja_bolšaja_celková_ztráta[KLÍČ_NA_CENĚ] or 0,  celkový_zisk)
        
    def pří_znamení_ke_vstupu(self):
        self.počítadlo_znamení_vstupů = self.počítadlo_znamení_vstupů + 1
        
    def __str__(self):
        import io
        import sys
        
        stdout = sys.stdout
        output_buffer = io.StringIO("")
        # přesměrování
        sys.stdout = output_buffer
        
        ODDELOVAC = '='*40
        
        print("*********")
        print("TALASNICA")
        print("*********")
        print('závěrečná zpráva')
        print()
        print('symbol {}'.format(self.__talasnica.info['SYMBOL']))
        print('svíčky od {} do {}'.format(self.počet_svíček,  self.poslední_svíce[BAR]))
        print('graf {}'.format(JMÉNO_GRAFU[self.__talasnica.info['časový rámec']]))
        
        print('započato {}'.format(self.počáteční_čas))
        print('ukončeno {}'.format(self.konečný_čas))
        doba = self.konečný_čas.datum - self.počáteční_čas.datum
        print('doba {}'.format(doba))
        print()
        print('počet znamení vstupů ',  self.počítadlo_znamení_vstupů)
        print('v průměru každých ',  doba/self.počítadlo_znamení_vstupů)
        print(ODDELOVAC)
        print()
        print('největší býk {:,.2f}'.format(self.samoj_bolšoj_býk).replace(",", " ").replace(".", ","))
        print('největší medvěd {:,.2f}'.format(self.samoj_bolšoj_medvěd).replace(",", " ").replace(".", ","))
        
        print('největší pozice {:,.2f} a {:,.2f}'.format(self.samaja_bolšaja_velikost[HORE],  self.samaja_bolšaja_velikost[DOLE]).replace(",", " ").replace(".", ","))
        print()
        print(ODDELOVAC)
        print()
        for klíč,  popis in ((OPEN,  PROFIT_OPEN),  (HIGHT,  PROFIT_HORE),  (LOW,  PROFIT_DOLE),  (CLOSE,  PROFIT_CLOSE)):
            print(popis)
            print('-'*40)
            print('{1:,.2f}{0:4} | {2:,.2f}{0:4}'.format(self.__talasnica.info['měna účtu'],  self.samoj_bolšoj_otevřený_zisk[klíč],  self.samaja_bolšaja_otevřená_ztráta[klíč]).replace(",", " ").replace(".", ","))
            print('{1:,.2f}{0:4} | {2:,.2f}{0:4}'.format(self.__talasnica.info['měna účtu'],  self.samoj_bolšoj_celkový_zisk[klíč],  self.samaja_bolšaja_celková_ztráta[klíč]).replace(",", " ").replace(".", ","))
            print('-'*40)
            print()

        print()
        print(ODDELOVAC)
        print()
        
        print("na poslední svíci")
        print("cena open",  self.poslední_svíce[OPEN])
        print()
        print('velikost hore {:,.2f} dole {:,.2f} celkem {:,.2f}'.format(self.__talasnica.obchody.býci.velikost,  self.__talasnica.obchody.medvědi.velikost,  self.__talasnica.obchody.velikost).replace(",", " ").replace(".", ","))
        print()
        uložený_zisk = self.__talasnica.obchody.uložený_zisk
        swap = self.__talasnica.obchody.swap
        zisk_při_otevření = self.zisk_při_otevření
        print('{:<25}{:>18,.2f}'.format('uložený zisk ',  uložený_zisk).replace(",", " ").replace(".", ","))
        print('{:<25}{:>18,.2f}'.format('+ swap',  swap).replace(",", " ").replace(".", ","))
        print('-'*40)
        print('{:>25}{:>18,.2f}'.format('= ',  uložený_zisk + swap).replace(",", " ").replace(".", ","))
        print('{:<25}{:>18,.2f}'.format('+ otevřené pozice ', zisk_při_otevření).replace(",", " ").replace(".", ","))
        print('-'*40)
        print('{:>25}{:>18,.2f}'.format('= ',  uložený_zisk + swap + zisk_při_otevření).replace(",", " ").replace(".", ","))
        
        # obnovíme standartní výstup
        sys.stdout = stdout
        return(output_buffer.getvalue())
