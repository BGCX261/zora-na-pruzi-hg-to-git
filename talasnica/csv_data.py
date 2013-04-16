#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import os
import datetime

import locale
locale.setlocale(locale.LC_ALL, '')


def na_číslo(hodnota):
    if hodnota is None:
        return None
    
    return int(hodnota)

class CSV_DATA(dict):
    def __init__(self,  hlavička = '',  řádek_dat = ''):
        self._klíče = hlavička.strip().split(';')
        self._hodnoty = řádek_dat.strip().split(';')
        
    def __missing__(self,  klíč):
        index = self._klíče.index(klíč)
        try:
            hodnota = self._hodnoty[index]
        except IndexError:
            print('Nema klíča {}'.format(klíč))
            hodnota = None
            
        for funkce in self._převody.get(klíč,  []):
            hodnota = funkce(hodnota)
            
        self[klíč] = hodnota
        return self[klíč]
        
    def __str__(self):
        for klíč in self._klíče:
            self[klíč]
            
        return super().__str__()
        
    def pridavam(self,  klíč,  hodnota):
        if klíč in self._klíče:
            raise KeyError('Už jestvuje klíč {}'.format(klíč))
            
        self._klíče.append(klíč)
        self._hodnoty.append(hodnota)
        
class Svíca(CSV_DATA):
    
    _převody = {
                 'BAR': (int, ), 
                 'OPEN TIME': (int,  datetime.datetime.fromtimestamp), 
                 'OPEN': ( float, ), 
                'HIGHT': ( float, ), 
                'LOW': ( float, ), 
                'CLOSE': ( float, ), 
                'spred': (int, ), 
                'odstup': (int, ), 
                'rozestup': (int, ), 
                'point': ( float, ), 
                'da li seju': (na_číslo,  bool, ), 

                'medvedi ohrada': ( float, ), 
                'byci ohrada': ( float, ), 
                'medvedi min': ( float, ), 
                'byci max': ( float, ), 
                'velikost byku': ( float, ), 
                'velikost medvedu': ( float, ), 
                'cena byku': ( float, ), 
                'cena medvedu': ( float, ),
                'cena oc. byka': ( float, ), 
                'cena oc. medveda': ( float, ), 
                 }
    
class INFO(CSV_DATA):
    
    _převody = {
                 'MODE_DIGITS': (int, ), 
                 'MODE_POINT':( float, ),
                 }

    def cena(self,  hodnota):
        přesnost = self['MODE_DIGITS']
#        point = self['MODE_POINT']
#        hodnota = hodnota + point/100
#        print('CENU {} => {}'.format(hodnota,  round(hodnota,  přesnost)))
        return round(hodnota ,  přesnost)
        
    def velikost(self,  hodnota):

        return round(hodnota,  2)


def data_z_csv(soubor):
    
    print('IMPORTUJI {}'.format(soubor))
    
    with open(soubor,  mode = "r",  encoding = "windows-1250") as čtu_soubor:
        
        hlavička = čtu_soubor.readline()
#        print(hlavička.strip().replace(';',  '\t|\t'))
        
        for řádek in čtu_soubor:
            yield Svíca(hlavička,  řádek)


def zjistím_cestu_k_info_csv(cesta_k_csv_datům):
    adresář,  soubor = os.path.split(cesta_k_csv_datům)
    z_názvu = soubor.split('_')
    symbol = z_názvu[0]
    soubor = '{}_info.csv'.format(symbol)
    
    return os.path.join(os.path.dirname(adresář),  'market_info',  soubor)
    
def najdu_info_csv(soubor):
    soubor = zjistím_cestu_k_info_csv(soubor)
    return info_z_csv(soubor)

def info_z_csv(soubor):
    info = INFO()
    with open(soubor,  mode = "r",  encoding = "windows-1250") as čtu_soubor:
        for řádek in čtu_soubor:
            data = řádek.strip().split(';')
            info.pridavam(data[0],  data[1])
            
            
    return info
            

if __name__ == '__main__':

    soubor = './experts/files/profitmetr/ladenka/EURJPY.60_2013-04-15-21-43-25.csv'

    for data in data_z_csv(soubor):
        da_li_seju = data['da li seju']
        print(data)
