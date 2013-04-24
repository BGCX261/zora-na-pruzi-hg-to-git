#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'


import os

from talasnica.Talasnica import Talasnica
from talasnica.konstanty import *


class Exportuji_talasnicu(object):
    
    csv_adresář = os.path.join(os.path.dirname(__file__), 'experts/files/talasnica/python')
    encoding = 'utf-8'
    
    def __init__(self,  cílové_csv,  zdrojové_csv):
        self.cílové_csv = cílové_csv
        self.zdrojové_csv = zdrojové_csv
        
    def cesta_k_souboru(self,  soubor):
        return os.path.join(self.csv_adresář,  soubor)

    def __call__(self):
     
        talasnica = Talasnica()
        
        with open(self.cesta_k_souboru(self.cílové_csv),  mode = "w",  encoding = self.encoding) as do_souboru:
    #        i = 0
            
            if self.hlavička is not None:
                do_souboru.write(self.csv_řádek(self.hlavička))
                
            for data in talasnica(self.zdrojové_csv):
    #            print(data)
                řádek = self.zpracuji_řádek(data)
                
                do_souboru.write(self.csv_řádek(řádek))
    #            i = i + 1
    #            if i > 10:
    #                    break

                       
    def csv_řádek(self,  data,  oddělovač=';'):
        return oddělovač.join(map(str,  data)) + '\n'

class Exportuji_vše(Exportuji_talasnicu):
        
    hlavička = ('timestamp',  'čas', 
                    'BAR', 
                    'hranice býka',  'hranice medvěda', 
                    'býčí ohrada',  'medvědí ohrada', 
                    'býčí čekaná',  'medvědí čekaná', 
                    'velikost býků', 'velikost medvědů', 
                    'cena býků',  'cena medvědů', 
                    'da li seju', 
                    'znamení sklizně', 

                   PROFIT_OPEN,  PROFIT_HORE,  PROFIT_DOLE,  PROFIT_CLOSE,
                   ULOŽENÝ_ZISK,  SWAP)
    
    def zpracuji_řádek(self,  talasnica):
        
        def ima(to,  ono):
            if to is not None:
                return getattr(to,  ono)
                
            return 0

        return (
                talasnica.data.čas, talasnica.data['OPEN TIME'],  
                 talasnica.data['BAR'], 
                 0,  0, 
                 ima(talasnica.býčiště,  'start'),  ima(talasnica.medvědiště,  'start'), 
                 ima(talasnica.býčiště,  'čekaná'),  ima(talasnica.medvědiště,  'čekaná'), 
                 
                 talasnica.obchody[HORE].velikost,  talasnica.obchody[DOLE].velikost, 
                talasnica.obchody[HORE].cena, talasnica.obchody[DOLE].cena, 
                int(talasnica.znamení_setby), 
                int(talasnica.znamení_sklizně), 
                talasnica.profit_při_otevření, 
                talasnica.profit(talasnica.data[HIGHT]), 
                talasnica.profit(talasnica.data[LOW]), 
                talasnica.profit(talasnica.data[CLOSE]), 
                talasnica.uložený_zisk, 
                talasnica.swap
                       )

class Cena_obchodů(Exportuji_talasnicu):
    encoding = "windows-1250"
    
    def zpracuji_řádek(self,  talasnica):
        return (talasnica.data.čas, 
                    talasnica.obchody[HORE].cena, 
                    talasnica.obchody[DOLE].cena
                       )


class Exportuji_graf(Exportuji_talasnicu):
    encoding = "windows-1250"
    
    def __call__(self):
     
        talasnica = Talasnica()
        
#        jména souborů
        csv_soubory = {}
        
        for prefix in 'obchody',  'býčí_ohrada',  'medvědí_ohrada',  'otevřené_obchody',  'zisky':
            jméno = '{}_{}'.format(prefix,  self.cílové_csv)
            cesta = self.cesta_k_souboru(jméno)
            csv_soubory[prefix] = open(cesta,  mode = "w",  encoding = self.encoding)
            
        
        
        
        csv_soubory_ohrady = {
                    HORE: csv_soubory['býčí_ohrada'], 
                    DOLE: csv_soubory['medvědí_ohrada']
                }
        
#        with open(csv_soubor_profitu,  mode = "w",  encoding = self.encoding) as soubor_ohrada:
#            pass

        ohrada = {HORE: None,  DOLE: None}
        hranice = {HORE: None,  DOLE: None}
        
        for talas in talasnica(self.zdrojové_csv):
#            nějaké změny v ohradě,  či hranicích
            for směrem,  generátor in (HORE,  talas.býčiště),  (DOLE,  talas.medvědiště):
                if generátor is not None:
                    if not hranice[směrem] == generátor.čekaná or not ohrada[směrem] == generátor.start:
                        ohrada[směrem] = generátor.start
                        hranice[směrem] = generátor.čekaná
                        
                        print(talas.data[OPEN_TIME].timestamp, 
                                    generátor.start, 
                                    generátor.čekaná, 
                                    sep = ';', 
                                    file = csv_soubory_ohrady[směrem]
                        )
                      
#                    zapíšu zisky
            print(talas.data[OPEN_TIME].timestamp, 
                  talas.data['BAR'], 
                       talas.profit_při_otevření, 
                        talas.profit(talas.data[HIGHT]), 
                        talas.profit(talas.data[LOW]), 
                        talas.profit(talas.data[CLOSE]), 
                        talas.uložený_zisk, 
                        talas.swap,
                        talas.obchody[HORE].cena, 
                        talas.obchody[HORE].velikost, 
                        talas.obchody[DOLE].cena, 
                        talas.obchody[DOLE].velikost, 
                        sep = ';', 
                        file = csv_soubory['zisky']
                        )
            
#        print(talasnica.uzavřené_obchody)
            
        
        for obchod in talasnica.uzavřené_obchody:
            print(
                  int(obchod[SMÉR] == DOLE) ,
                  obchod[ČAS_OTEVŘENÍ].timestamp, 
                    obchod[OTEVÍRACÍ_CENA], 
                    obchod[ČAS_ZAVŘENÍ].timestamp, 
                    obchod[ZAVÍRACÍ_CENA],
                    
                    sep = ';', 
                    file = csv_soubory['obchody']
                  )
           
        for směr,  seznam_otevřených_obchodů in talasnica.obchody.items():
            for obchod in seznam_otevřených_obchodů.obchody.values():
                print(
                      int(obchod[SMÉR] == DOLE) ,
                      obchod[ČAS_OTEVŘENÍ].timestamp, 
                        obchod[OTEVÍRACÍ_CENA], 
#                        nemá čas zavření
#                        obchod[ČAS_ZAVŘENÍ].timestamp, 
#                        obchod[ZAVÍRACÍ_CENA],
                        
                        sep = ';', 
                        file = csv_soubory['otevřené_obchody']
                      )
             
        for soubor in csv_soubory.values():
            soubor.close()
                

if __name__ == '__main__':
    
    import argparse
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser()

#   a pak mu nastavím jaké příkazy a parametry má přijímat
    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, {}'.format(__version__))
    
    parser.add_argument('--zdrojový_soubor',  '-z')
    parser.add_argument('--graf',  '-g',  action='store_true')
    parser.add_argument('--tabulka',  '-t',  action='store_true')
    
    #    a včíl to možu rozparsovat
    args = parser.parse_args()

    print(args)

    zdrojové_csv = args.zdrojový_soubor
#    csv_soubor = args.soubor

    if zdrojové_csv is None:
        print('Není zadán zdrojový soubor')
        from talasnica.testuji_talasnicu import csv_soubor as zdrojové_csv 
        print('\t načtu {}'.format(zdrojové_csv))
    else:
        print('Načtu {}'.format(zdrojové_csv))
        
    symbol = 'EURJPY.'
    perioda = 60
    
    if args.tabulka is True:
        csv_soubor = 'tabulka_{}_{}.csv'.format(symbol,  perioda)
        print('Exportuji tabulku do {}'.format(csv_soubor))
        exporter = Exportuji_vše(csv_soubor,  zdrojové_csv)
        exporter()
    
    if args.graf is True:
        csv_soubor = 'graf_{}_{}.csv'.format(symbol,  perioda)
        print('Exportuji graf do *{}'.format(csv_soubor))
        exporter = Exportuji_graf(csv_soubor,  zdrojové_csv)
        exporter()
