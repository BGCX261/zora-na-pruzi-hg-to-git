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

csv_adresář = os.path.join(os.path.dirname(__file__), 'experts/files/talasnica/python')


def uložím_data_do_csv(cílové_csv,  zdrojové_csv,  zpracuji_řádek,  hlavička = None):
    '''
    spouštím funkci main()
    '''
    
    csv_cesta_k_souboru = os.path.join(csv_adresář,  csv_soubor)
    
 
    talasnica = Talasnica()
    
    with open(csv_cesta_k_souboru,  mode = "w",  encoding = "windows-1250") as do_souboru:
        i = 0
        
        if hlavička is not None:
            do_souboru.write(hlavička + '\n')
            
        for data in talasnica(zdrojové_csv):
#            print(data)
            řádek = ';'.join(map(str,  zpracuji_řádek(data)))
            print(řádek)
            do_souboru.write(řádek + '\n')
            i = i + 1
            if i > 10:
                    break
    

if __name__ == '__main__':

    from talasnica.testuji_talasnicu import csv_soubor as zdrojové_csv 

    def cena_obchodů(talasnica):
        return (talasnica.data.čas, 
                    talasnica.obchody[HORE].cena, 
                    talasnica.obchody[DOLE].cena
                       )
     
    class Exportuji_vše(object):
        
        def __init__(self,  *args):
            self.hlavička = ';'.join(map(str,  args))
            print(self.hlavička)
        
        def __call__(self,  talasnica):
            
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


    symbol = 'EURJPY.'
    perioda = 60
    
    csv_soubor = 'graf_{}_{}.csv'.format(symbol,  perioda)
#    uložím_data_do_csv(csv_soubor, zdrojové_csv,  zpracuji_řádek = cena_obchodů,  hlavička = None)
    
    exportuji_vše = Exportuji_vše('timestamp',  'čas', 
                    'BAR'
                    'hranice býka',  'hranice medvěda', 
                    'býčí ohrada',  'medvědí ohrada', 
                    'býčí čekaná',  'medvědí čekaná', 
                    'velikost býků', 'velikost medvědů', 
                    'cena býků',  'cena medvědů', 
                    'da li seju', 
                    'znamení sklizně', 

                   PROFIT_OPEN,  PROFIT_HORE,  PROFIT_DOLE,  PROFIT_CLOSE,
                   ULOŽENÝ_ZISK,  SWAP)
                   
    csv_soubor = 'export_{}_{}.csv'.format(symbol,  perioda)
    uložím_data_do_csv(csv_soubor,  zdrojové_csv,  zpracuji_řádek = exportuji_vše,  hlavička = exportuji_vše.hlavička)
