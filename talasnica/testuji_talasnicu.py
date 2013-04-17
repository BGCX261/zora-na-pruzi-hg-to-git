#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import os

from talasnica.spustím_talasnicu import Talasnica,  BUY,  SELL

#jen pro testy
from .csv_data import zjistím_cestu_k_info_csv



#medvedi_ohrada = 0
#byci_ohrada = 0
#cena_ocekavaneho_medveda = 0
#cena_ocekavaneho_byka = 0
#cena_medvedu = 0
#velikost_medvedu = 0
#velikost_byku = 0
#cena_byku = 0

csv_soubor = os.path.join(os.path.dirname(__file__), 'experts/files/profitmetr/ladenka/EURJPY._60_2013-04-16-10-59-16.csv')
    
def test_zjistím_cestu_k_info_csv():
    cesta = zjistím_cestu_k_info_csv(csv_soubor)
    print(cesta)
    assert cesta == os.path.join(os.path.dirname(__file__), 'experts/files/profitmetr/market_info/EURJPY._info.csv')
    assert os.path.isfile(cesta)

def test_talasnica():
        
    talasnica = Talasnica(csv_soubor)
    
    for data in talasnica.start():
       
#        ExtMapBuffer_medvedi_ohrada[pos] = medvedi_ohrada;
        assert talasnica.ohrada[SELL] == data['medvedi ohrada']
#        ExtMapBuffer_byci_ohrada[pos] = byci_ohrada;
        assert talasnica.ohrada[BUY] == data['byci ohrada']
#        ExtMapBuffer_velikost_medvedu[pos] = velikost_medvedu;
        assert talasnica.velikost[SELL] == data['velikost medvedu']
#        ExtMapBuffer_velikost_byku[pos] = velikost_byku;
        assert talasnica.velikost[BUY] == data['velikost byku']
#        ExtMapBuffer_cena_medvedu[pos] = cena_medvedu;
#        assert talasnica.cena[SELL] == data['cena medvedu']
        assert talasnica.porovnám_cenu(talasnica.cena[SELL],  data['cena medvedu']) is True
#        ExtMapBuffer_cena_byku[pos] = cena_byku;
        assert talasnica.cena[BUY] == data['cena byku']
#        ExtMapBuffer_cekajici_medved[pos] = cena_ocekavaneho_medveda;
        assert talasnica.čekaná[SELL] == data['cena oc. medveda']
#        ExtMapBuffer_cekajici_byk[pos] = cena_ocekavaneho_byka;
        assert talasnica.čekaná[BUY] == data['cena oc. byka']
        

if __name__ == '__main__':
    test_zjistím_cestu_k_info_csv()
    test_talasnica()
    
