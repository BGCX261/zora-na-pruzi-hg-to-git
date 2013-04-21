#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import os

from talasnica.Talasnica import Talasnica,  BUY,  SELL,  PROFIT_OPEN, PROFIT_HORE, PROFIT_DOLE, PROFIT_CLOSE,  SWAP,  ULOŽENÝ_ZISK

#medvedi_ohrada = 0
#byci_ohrada = 0
#cena_ocekavaneho_medveda = 0
#cena_ocekavaneho_byka = 0
#cena_medvedu = 0
#velikost_medvedu = 0
#velikost_býků = 0
#cena_býků = 0

csv_soubor = 'EURJPY._60_2013-04-19-21-59-59.csv'
csv_soubor = os.path.join(os.path.dirname(__file__), 'experts/files/talasnica/profitmetr',  csv_soubor)


def test_talasnica_ceny():

    talasnica = Talasnica(csv_soubor)

    for data in talasnica.start():
#        if  data['BAR'] < 18685:
#            print(data)
#        if not talasnica.hranice[BUY] == data['býčí maximum']:
#            print(data)

        assert talasnica.da_li_seju == data['da li seju']
        assert talasnica.znamení_sklizně == data['znamení sklizně']

        assert talasnica.velikost[BUY] == data['velikost býků']
        assert talasnica.velikost[SELL] == data['velikost medvědů']

        assert talasnica.hranice[BUY] == data['hranice býka']
        assert talasnica.hranice[SELL] == data['hranice medvěda']

        assert talasnica.ohrada[SELL] == data['medvědí ohrada']
        assert talasnica.ohrada[BUY] == data['býčí ohrada']

        assert talasnica.čekaná[SELL] == data['medvědí čekaná']
        assert talasnica.čekaná[BUY] == data['býčí čekaná']

        assert talasnica.cena[SELL] == data['cena medvědů']
        assert talasnica.cena[BUY] == data['cena býků']

def test_talasnica_profity():

    talasnica = Talasnica(csv_soubor)

    for data in talasnica.start():

        assert talasnica.profit[PROFIT_OPEN] == data[PROFIT_OPEN]
        assert talasnica.profit[PROFIT_HORE] == data[PROFIT_HORE]
        assert talasnica.profit[PROFIT_DOLE] == data[PROFIT_DOLE]
        assert talasnica.profit[PROFIT_CLOSE] == data[PROFIT_CLOSE]

        assert talasnica.zisk[SWAP] == data[SWAP]

        assert talasnica.zisk[ULOŽENÝ_ZISK] == data[ULOŽENÝ_ZISK]

def export_talasnice():

    talasnica = Talasnica(csv_soubor)

    print(';'.join(('BAR', 
                    'hranice býka',  'hranice medvěda', 
                    'býčí ohrada',  'medvědí ohrada', 
                    'býčí čekaná',  'medvědí čekaná', 
                    'velikost býků', 'velikost medvědů', 
                    'cena býků',  'cena medvědů', 
                    'da li seju', 
                    'znamení sklizně', 

                   PROFIT_OPEN,  PROFIT_HORE,  PROFIT_DOLE,  PROFIT_CLOSE,
                   ULOŽENÝ_ZISK,  SWAP)))

    for data in talasnica.start():
        print(';'.join(map(str,  (data['BAR'],
                    talasnica.hranice[BUY],  talasnica.hranice[SELL],
                    talasnica.ohrada[BUY],  talasnica.ohrada[SELL],
                    talasnica.čekaná[BUY],  talasnica.čekaná[SELL],
                    talasnica.velikost[BUY],  talasnica.velikost[SELL],
                    talasnica.cena[BUY],  talasnica.cena[SELL],
                    talasnica.da_li_seju,
                    talasnica.znamení_sklizně ,
                       talasnica.profit[PROFIT_OPEN],  talasnica.profit[PROFIT_HORE],  talasnica.profit[PROFIT_DOLE],  talasnica.profit[PROFIT_CLOSE],
                       talasnica.zisk[ULOŽENÝ_ZISK],
                       talasnica.zisk[SWAP]
                       ))))


def analyzuji():
    talasnica = Talasnica(csv_soubor)
    for data in talasnica.start():
        continue

#    print('Talasnica souboru {} dokončena'.format(csv_soubor))
    talasnica.report()

if __name__ == '__main__':
#    export_talasnice()

    
    analyzuji()
    
