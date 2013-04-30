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
    
    def __init__(self,  cílové_csv,  zdrojové_csv,  parametry):
        self.cílové_csv = cílové_csv
        self.zdrojové_csv = zdrojové_csv
        self.parametry = parametry
        
    def cesta_k_souboru(self,  soubor):
        return os.path.join(self.csv_adresář,  soubor)

    def __call__(self):
     
        talasnica = Talasnica()
        
        with open(self.cesta_k_souboru(self.cílové_csv),  mode = "w",  encoding = self.encoding) as do_souboru:
    #        i = 0
            
            if self.hlavička is not None:
                do_souboru.write(self.csv_řádek(self.hlavička))
                
            for data in talasnica(self.zdrojové_csv, self.parametry):
    #            print(data)
                řádek = self.zpracuji_řádek(data)
                
                do_souboru.write(self.csv_řádek(řádek))
    #            i = i + 1
    #            if i > 10:
    #                    break
    
        return talasnica

                       
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
                 
                talasnica.obchody.býci.velikost,  talasnica.obchody.medvědi.velikost, 
                talasnica.obchody.býci.cena, talasnica.obchody.medvědi.cena, 
                int(talasnica.znamení_setby), 
                int(talasnica.znamení_sklizně), 
                talasnica.profit_při_otevření, 
                talasnica.obchody.profit(talasnica.data[HIGHT]), 
                talasnica.obchody.profit(talasnica.data[LOW]), 
                talasnica.obchody.profit(talasnica.data[CLOSE]), 
                talasnica.obchody.uložený_zisk, 
                talasnica.obchody.swap
                       )

class Cena_obchodů(Exportuji_talasnicu):
    encoding = "windows-1250"
    
    def zpracuji_řádek(self,  talasnica):
        return (talasnica.data.čas, 
                    talasnica.obchody.býci.cena, 
                    talasnica.obchody.medvědi.cena
                       )


class Exportuji_graf(Exportuji_talasnicu):
    encoding = "windows-1250"
    
    def __call__(self):
     
        talasnica = Talasnica()
        
#        jména souborů
        csv_soubory = {}
        
        for prefix in 'postavení', 'uzavřené_obchody',  'býčí_ohrada',  'medvědí_ohrada',  'otevřené_obchody',  'zisky':
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
        
        for talasnica_svíce in talasnica(self.zdrojové_csv, self.parametry):
#            nějaké změny v ohradě,  či hranicích
            for směrem,  generátor in (HORE,  talasnica_svíce.býčiště),  (DOLE,  talasnica_svíce.medvědiště):
                if generátor is not None:
                    if not hranice[směrem] == generátor.čekaná or not ohrada[směrem] == generátor.start:
                        ohrada[směrem] = generátor.start
                        hranice[směrem] = generátor.čekaná
                        
                        print(talasnica_svíce.data[OPEN_TIME].timestamp, 
                                    generátor.start, 
                                    generátor.čekaná, 
                                    sep = ';', 
                                    file = csv_soubory_ohrady[směrem]
                        )
#                    zapíšu obchodní pozice
            print(talasnica_svíce.data[OPEN_TIME].timestamp, 
                        talasnica_svíce.data['BAR'], 
                        talasnica_svíce.data[OPEN].prodej,
                        talasnica_svíce.obchody.býci.cena, 
                        talasnica_svíce.obchody.býci.velikost, 
                        talasnica_svíce.obchody.medvědi.cena, 
                        talasnica_svíce.obchody.medvědi.velikost, 
                        int(talasnica_svíce.znamení_setby), 
                        int(talasnica_svíce.znamení_sklizně), 
                        sep = ';', 
                        file = csv_soubory['postavení']
                        )
                        
#                    zapíšu zisky
            print(talasnica_svíce.data[OPEN_TIME].timestamp, 
                  talasnica_svíce.data['BAR'], 
                       talasnica_svíce.profit_při_otevření, 
                        talasnica_svíce.obchody.profit(talasnica_svíce.data[HIGHT]), 
                        talasnica_svíce.obchody.profit(talasnica_svíce.data[LOW]), 
                        talasnica_svíce.obchody.profit(talasnica_svíce.data[CLOSE]), 
                        talasnica_svíce.obchody.uložený_zisk, 
                        talasnica_svíce.obchody.swap,
                        talasnica_svíce.obchody.býci.cena, 
                        talasnica_svíce.obchody.býci.velikost, 
                        talasnica_svíce.obchody.medvědi.cena, 
                        talasnica_svíce.obchody.medvědi.velikost, 
                        sep = ';', 
                        file = csv_soubory['zisky']
                        )
            
#        print(talasnica.uzavřené_obchody)
            
        
        for obchod in talasnica.obchody.uzavřené:
            print(
                  int(obchod.směr == DOLE) ,
                  obchod.čas_otevření.timestamp, 
                  obchod.cena_otevření, 
                    obchod.čas_zavření.timestamp, 
                    obchod.cena_zavření,
                    
                    sep = ';', 
                    file = csv_soubory['uzavřené_obchody']
                  )
           
        for  seznam_otevřených_obchodů in talasnica.obchody.býci, talasnica.obchody.medvědi:
            for obchod in seznam_otevřených_obchodů.obchody.values():
                print(
                      int(obchod.směr == DOLE) ,
                      obchod.čas_otevření.timestamp, 
                        obchod.cena_otevření, 
#                        nemá čas zavření
#                        obchod[ČAS_ZAVŘENÍ].timestamp, 
#                        obchod[ZAVÍRACÍ_CENA],
                        
                        sep = ';', 
                        file = csv_soubory['otevřené_obchody']
                      )
             
        for soubor in csv_soubory.values():
            soubor.close()
            
        return talasnica
                

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
#        from talasnica.testuji_talasnicu import csv_soubor as zdrojové_csv 
        zdrojové_csv  = 'experts/files/talasnica/export/data/EURJPY._60_2013-04-26-21-59-59.csv'
        print('\t načtu {}'.format(zdrojové_csv))
    else:
        print('Načtu {}'.format(zdrojové_csv))
        
    symbol = 'EURJPY.'
    perioda = 60
    
    parametry = {'sklízím při zisku': 5000, 
                        'odstup':200, 
                        'rozestup': 200, 
                        'sázím loty': 0.1
                 }
    
    if args.tabulka is True:
        csv_soubor = 'tabulka_{}_{}.csv'.format(symbol,  perioda)
        print('Exportuji tabulku do {}'.format(csv_soubor))
        exporter = Exportuji_vše(csv_soubor,  zdrojové_csv,  parametry)
        exporter()
    
    if args.graf is True:
        csv_soubor = 'graf_{}_{}.csv'.format(symbol,  perioda)
        print('Exportuji graf do *{}'.format(csv_soubor))
        exporter = Exportuji_graf(csv_soubor,  zdrojové_csv,  parametry)
        talasnica = exporter()
        print(talasnica)
