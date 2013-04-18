#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import os

from talasnica.Talasnica import Talasnica,  BUY,  SELL

#medvedi_ohrada = 0
#byci_ohrada = 0
#cena_ocekavaneho_medveda = 0
#cena_ocekavaneho_byka = 0
#cena_medvedu = 0
#velikost_medvedu = 0
#velikost_býků = 0
#cena_býků = 0

csv_soubor = os.path.join(os.path.dirname(__file__), 'experts/files/talasnica/profitmetr/EURJPY._60_2013-04-18-20-27-49.csv')
    

def test_talasnica():
        
    talasnica = Talasnica(csv_soubor)
    
    def porovnám_cenu(prvni,  druha):
        if prvni == druha:
            return True
            
#        zaokrouhleny rozdil
        rozdil = talasnica._info.cena(abs(prvni-druha))
        if rozdil == talasnica._info['POINT']:
            return True
            
        print('porovnávám ceny',  prvni,  druha,  'povolený rozdíl',  rozdil)
        return False
    
#    přesnost_ceny = talasnica._info['POINT']
    
    for data in talasnica.start():
        
        assert talasnica.hranice[BUY] == data['býčí maximum']
        assert talasnica.hranice[SELL] == data['medvědí minimum']
        
        assert talasnica.ohrada[SELL] == data['medvědí ohrada']
        assert talasnica.ohrada[BUY] == data['býčí ohrada']
        
        assert talasnica.čekaná[SELL] == data['medvědí čekaná']
        assert talasnica.čekaná[BUY] == data['býčí čekaná']

        assert talasnica.velikost[SELL] == data['velikost medvědů']
#        assert talasnica.cena[SELL] == data['cena medvědů']
#        if not porovnam_cenu(talasnica.cena[SELL],  data['cena medvědů']):
#            print(data)
        assert porovnám_cenu(talasnica.cena[SELL],  data['cena medvědů'])
        
        assert talasnica.velikost[BUY] == data['velikost býků']
        assert talasnica.cena[BUY] == data['cena býků']
        
        assert talasnica.da_li_seju == data['da li seju']
        print(';'.join(map(str,  (data['BAR'],  talasnica.velikost[SELL],  talasnica.cena[SELL],  talasnica.velikost[BUY],  talasnica.cena[BUY], 
                       talasnica.profit[0],  talasnica.profit[1],  talasnica.profit[2],  talasnica.profit[3],  
                       talasnica.uložený_zisk, 
                       talasnica.swap
                       ))))
#        'profit hore',  'profit dole',  'profit při zavření'
#        for číslo,  profit_v in enumerate(('profit při otevření',  )):
#            rozdíl = abs(talasnica.profit[číslo] - data[profit_v])
#            if rozdíl > přesnost_ceny:
#                print('Bar {} rozdíl v {} {} - {} = {}'.format(data['BAR'],  profit_v,  talasnica.profit[číslo],  data[profit_v],  rozdíl))
##            assert rozdíl < přesnost_ceny

def export_talasnice():
    
    talasnica = Talasnica(csv_soubor)
     
    print(';'.join(('BAR',  'velikost medvědů',  'cena medvědů',  'velikost býků',  'cena býků', 
                   'profit při otevření',  'profit hore',  'profit dole',  'profit při zavření',
                   'celkové uložené zisky',  'celkový swap')))
                   
    for data in talasnica.start():
        print(';'.join(map(str,  (data['BAR'],  talasnica.velikost[SELL],  talasnica.cena[SELL],  talasnica.velikost[BUY],  talasnica.cena[BUY], 
                       talasnica.profit[0],  talasnica.profit[1],  talasnica.profit[2],  talasnica.profit[3],  
                       talasnica.uložený_zisk, 
                       talasnica.swap
                       ))))
        
                   
    

if __name__ == '__main__':
#    test_talasnica()
    export_talasnice()
