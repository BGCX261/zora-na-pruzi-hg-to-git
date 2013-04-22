#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import os
import datetime,  pytz

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
            print(klíč,  hodnota)

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


def správné_datetime(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, tz = pytz.UTC)


class SVÍCA(CSV_DATA):

    _převody = {
                 'BAR': (int, ),
                 'OPEN TIME': (int,  správné_datetime),
                 'OPEN': ( float, ),
                'HIGHT': ( float, ),
                'LOW': ( float, ),
                'CLOSE': ( float, ),
                'da li seju': (na_číslo,  bool, ),
                'znamení sklizně': (na_číslo,  bool, ),
                'medvědí ohrada': ( float, ),
                'býčí ohrada': ( float, ),
                'hranice medvěda': ( float, ),
                'hranice býka': ( float, ),
                'velikost býků': ( float, ),
                'velikost medvědů': ( float, ),
                'cena býků': ( float, ),
                'cena medvědů': ( float, ),
                'býčí čekaná': ( float, ),
                'medvědí čekaná': ( float, ),
                'profit při otevření':( float, ),
                'profit hore':( float, ),
                'profit dole':( float, ),
                'profit při zavření':( float, ),
                'celkový swap':( float, ),
                'celkové uložené zisky':( float, ),

                 }
                 
    @property
    def čas(self):
        index = self._klíče.index('OPEN TIME')
        return self._hodnoty[index]


class INFO(CSV_DATA):

    _převody = {
                 'DIGITS': (int, ),
                 'POINT':( float, ),
                 'TICKVALUE':( float, ),
                 'SPRED': (int, ),
                 'odstup': (int, ),
                 'rozestup': (int, ),
                 'sázím loty':( float, ),
                 'býčí swap':( float, ),
                 'medvědí swap':( float, ),
                 'sklízím při zisku':( float, ),
                 }


def info_z_csv(csv_soubor):
        with open(csv_soubor,  mode = "r",  encoding = "windows-1250") as čtu_soubor:
            hlavička = čtu_soubor.readline()
            info = čtu_soubor.readline()
            return INFO(hlavička,  info)

def data_z_csv(csv_soubor):

#        print('IMPORTUJI {}'.format(self._csv_soubor))

    with open(csv_soubor,  mode = "r",  encoding = "windows-1250") as čtu_soubor:

        čtu_soubor.readline()
        čtu_soubor.readline()

        hlavička = čtu_soubor.readline()

        for řádek in čtu_soubor:
            yield SVÍCA(hlavička,  řádek)
                
#
#def zjistím_cestu_k_info_csv(cesta_k_csv_datům):
#    adresář,  soubor = os.path.split(cesta_k_csv_datům)
#    z_názvu = soubor.split('_')
#    symbol = z_názvu[0]
#    soubor = '{}_info.csv'.format(symbol)
#
#    return os.path.join(os.path.dirname(adresář),  'info',  soubor)
#
#def najdu_info_csv(soubor):
#    soubor = zjistím_cestu_k_info_csv(soubor)
#    return info_z_csv(soubor)
#
#def info_z_csv(soubor):
#    info = INFO()
#    with open(soubor,  mode = "r",  encoding = "windows-1250") as čtu_soubor:
#        for řádek in čtu_soubor:
#            data = řádek.strip().split(';')
#            info.pridavam(data[0],  data[1])
#
#
#    return info
#

