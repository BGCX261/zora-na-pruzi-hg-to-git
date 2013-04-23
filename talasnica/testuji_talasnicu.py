#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import os

#from talasnica.Talasnica_ladenka_metatraderu import Talasnica
from talasnica.Talasnica import Talasnica
from talasnica.konstanty import HORE,  DOLE,  PROFIT_OPEN, PROFIT_HORE, PROFIT_DOLE, PROFIT_CLOSE,  SWAP,  ULOŽENÝ_ZISK

csv_soubor = 'EURJPY._60_2013-04-22-16-18-37.csv'
csv_soubor = os.path.join(os.path.dirname(__file__), 'experts/files/talasnica/profitmetr',  csv_soubor)

talasnica = Talasnica()

def test_talasnica_ceny():


    for svíca in talasnica(csv_soubor):
#        if  data['BAR'] < 18685:
#            print(data)
#        if not talasnica.hranice[BUY] == data['býčí maximum']:
#            print(data)

        assert svíca.znamení_setby == svíca.data['da li seju']
#        assert talasnica.znamení_sklizně == data['znamení sklizně']
#
#        assert talasnica.obchody[HORE].velikost == svíca.data['velikost býků']
#        assert talasnica.obchody[DOLE].velikost == svíca.data['velikost medvědů']
#
#        assert talasnica.hranice[BUY] == data['hranice býka']
#        assert talasnica.hranice[SELL] == data['hranice medvěda']
#
#        assert talasnica.ohrada[SELL] == data['medvědí ohrada']
#        assert talasnica.ohrada[BUY] == data['býčí ohrada']
#
#        assert talasnica.čekaná[SELL] == data['medvědí čekaná']
#        assert talasnica.čekaná[BUY] == data['býčí čekaná']
#
#        assert talasnica.cena[SELL] == data['cena medvědů']
#        assert talasnica.cena[BUY] == data['cena býků']

#def test_talasnica_profity():
#
#    for data in talasnica(csv_soubor):
#
#        assert talasnica.profit[PROFIT_OPEN] == data[PROFIT_OPEN]
#        assert talasnica.profit[PROFIT_HORE] == data[PROFIT_HORE]
#        assert talasnica.profit[PROFIT_DOLE] == data[PROFIT_DOLE]
#        assert talasnica.profit[PROFIT_CLOSE] == data[PROFIT_CLOSE]
#
#        assert talasnica.zisk[SWAP] == data[SWAP]
#
#        assert talasnica.zisk[ULOŽENÝ_ZISK] == data[ULOŽENÝ_ZISK]
#
#def test_výstupy():
#
#    for data in talasnica(csv_soubor):
#        assert talasnica.imam_znameni_ke_sklizni() == data['znamení sklizně']


if __name__ == '__main__':
    export_talasnice()

    
#    analyzuji()
    
