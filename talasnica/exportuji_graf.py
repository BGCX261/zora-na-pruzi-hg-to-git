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
                 
                 talasnica.obchody[DOLE].velikost,  talasnica.obchody[HORE].velikost, 
                talasnica.obchody[HORE].cena, talasnica.obchody[DOLE].cena, 
                talasnica.znamení_setby, 
                talasnica.znamení_sklizně, 
                talasnica.profit(talasnica.data[OPEN]), 
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
        
#        csv_soubor_profitu = 'profit_' + self.cílové_csv
#        csv_soubor_ohrada = 'profit_' + self.cílové_csv
#        csv_soubor_býčí_čekaná = 'profit_' + self.cílové_csv
#        csv_soubor_medvědí_čekaná = 'profit_' + self.cílové_csv
        csv_soubor_obchodů = 'obchody_' + self.cílové_csv
        csv_soubor_obchodů = open(self.cesta_k_souboru(csv_soubor_obchodů),  mode = "w",  encoding = self.encoding)
        
#        with open(csv_soubor_profitu,  mode = "w",  encoding = self.encoding) as soubor_ohrada:
#            pass

        for talas in talasnica(self.zdrojové_csv):
            continue
            
#        print(talasnica.uzavřené_obchody)
            
        for obchod in talasnica.uzavřené_obchody:
#            print(obchod)
            

            print(obchod[ČAS_OTEVŘENÍ].timestamp, 
                    obchod[OTEVÍRACÍ_CENA], 
                    obchod[ČAS_ZAVŘENÍ].timestamp, 
                    obchod[ZAVÍRACÍ_CENA],
                   int(obchod[SMÉR] == DOLE) , 
                    sep = ';', 
                    file = csv_soubor_obchodů
                  )
                  
        csv_soubor_obchodů.close()
                

if __name__ == '__main__':

    from talasnica.testuji_talasnicu import csv_soubor as zdrojové_csv 

    symbol = 'EURJPY.'
    perioda = 60
    
    csv_soubor = 'graf_{}_{}.csv'.format(symbol,  perioda)
#  exporter = Cena_obchodů(csv_soubor, zdrojové_csv)
    
    csv_soubor = 'export_{}_{}.csv'.format(symbol,  perioda)
#    exporter = Exportuji_vše(csv_soubor,  zdrojové_csv)
    exporter = Exportuji_graf(csv_soubor,  zdrojové_csv)
    
    exporter()
