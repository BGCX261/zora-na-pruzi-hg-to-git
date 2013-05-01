#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

import os
import time

from talasnica.Talasnica import Talasnica
from talasnica.konstanty import *

class Exportuji_svíčku(object):

    hlavička = ('timestamp',  'čas',
                    'BAR',
                    'býčí ohrada',  'medvědí ohrada',
                    'býčí čekaná',  'medvědí čekaná',
                    'velikost býků', 'velikost medvědů',
                    'cena býků',  'cena medvědů',
                    'velikost postavení',  'cena postavení',
                    'da li seju',
                    'znamení sklizně',

                   PROFIT_OPEN,  PROFIT_HORE,  PROFIT_DOLE,  PROFIT_CLOSE,
                   ULOŽENÝ_ZISK,  SWAP)

    def __call__(self,  talasnica):

        def ima(to,  ono):
            if to is not None:
                return getattr(to,  ono)

            return 0

        return (
                talasnica.data.čas, talasnica.data['OPEN TIME'],
                 talasnica.data['BAR'],
                 ima(talasnica.býčiště,  'start'),  ima(talasnica.medvědiště,  'start'),
                 ima(talasnica.býčiště,  'čekaná'),  ima(talasnica.medvědiště,  'čekaná'),
                talasnica.obchody.býci.velikost,  talasnica.obchody.medvědi.velikost,
                talasnica.obchody.býci.cena, talasnica.obchody.medvědi.cena,
                talasnica.obchody.velikost,  talasnica.obchody.cena,
                int(talasnica.znamení_setby),
                int(talasnica.znamení_sklizně),
                talasnica.profit_při_otevření,
                talasnica.obchody.profit(talasnica.data[HIGHT]),
                talasnica.obchody.profit(talasnica.data[LOW]),
                talasnica.obchody.profit(talasnica.data[CLOSE]),
                talasnica.obchody.uložený_zisk,
                talasnica.obchody.swap
                       )

class Exportuji_obchody(object):
    hlavička = (
                    'tiket',
                    'směr',
                    'čas otevření',  'cena otevření',
                    'velikost',
                    'zavři na stopce', 'zavři na profitu',
                    'čas zavření', 'cena zavření',
                    'profit',  'swap'
                    )

#    def __init__(self,  talasnica):
#        self.talasnica = talasnica

    def __call__(self,  obchod):
        return (
                    obchod.tiket,
                    int(obchod.směr == DOLE),
                    obchod.čas_otevření.timestamp,  obchod.cena_otevření,
                    obchod.velikost,
                    0, 0,
                    obchod.čas_zavření.timestamp,  obchod.cena_zavření or 0,
                    0,  obchod.swap
                       )


class Exportuji_ohradu(object):

    hlavička = (
                    'čas',
                    'start',
                    'čekaná'
                    )

    def __call__(self,  talasnica,  generátor):

        return (talasnica.data[OPEN_TIME].timestamp,
                                    generátor.start,
                                    generátor.čekaná
                        )




#######################

def davaj_třídu_souboru(symbol,  časový_rámec,  parametry,  encoding):



    class Soubor(object):
        '''
        zapíše do souboru
        '''

        csv_adresář = os.path.join(os.path.dirname(__file__), 'experts/files/talasnica/python')

        def __init__(self,  jméno):

            self.encoding = encoding

            csv_adresář = self.csv_adresář

    #        vytvořím podadresáře ak nejestvují
            for adresář in symbol.replace('.',  '_'),  JMÉNO_GRAFU[časový_rámec]:
                csv_adresář = os.path.join(csv_adresář,  adresář)
                if not os.path.isdir(csv_adresář):
                    print('vytvářím adresář {}'.format(csv_adresář))
                    os.mkdir(csv_adresář)

            csv_adresář = csv_adresář

            self.cesta = os.path.join(csv_adresář,  '{}.csv'.format(jméno))

            print('uložím do souboru {}'.format(self.cesta))


        def __enter__(self):
            print('enter {}'.format(self.cesta))
            self.soubor = open(self.cesta,  mode = "w",  encoding = self.encoding)
            časová_značka = time.time()
            self.řádek(int(časová_značka))
            self.řádek('SYMBOL',  'časový rámec')
            self.řádek(symbol,  časový_rámec)
            self.řádek(len(parametry))
            self.řádek(*parametry.keys())
            self.řádek(*parametry.values())

            return self

        def řádek(self,  *sloupce):
            csv_řádek = ';'.join(map(str,  sloupce))
            print(csv_řádek, file = self.soubor)

        def __exit__(self, *args):
            print('exit {}'.format(self.cesta))
            self.soubor.close()

    return Soubor

def exportuji_talasnicu(zdrojové_csv,  parametry):
    print('exportuji Talasnicu')
    print('zdrojový soubor {}'.format(zdrojové_csv))
    print('parametry {}'.format(parametry))

    talasnica = Talasnica(zdrojové_csv = zdrojové_csv,  parametry = parametry)

#    print(talasnica.info)

    Soubor = davaj_třídu_souboru(symbol = talasnica.info['SYMBOL'],  časový_rámec = talasnica.info['časový rámec'],  parametry = parametry,  encoding = "windows-1250")

    ohrada = {HORE: None,  DOLE: None}
    hranice = {HORE: None,  DOLE: None}

    with Soubor(jméno = 'svíčky') as soubor,  Soubor(jméno = 'býčí_ohrada') as soubor_býčí_ohrady,  Soubor(jméno = 'medvědí_ohrada') as soubor_medvědí_ohrady:
        exportér = Exportuji_svíčku()
        soubor.řádek(*exportér.hlavička)

        exportér_generátoru = Exportuji_ohradu()
        soubor_býčí_ohrady.řádek(*exportér_generátoru.hlavička)
        soubor_medvědí_ohrady.řádek(*exportér_generátoru.hlavička)

        for talasnica_na_svíčce in talasnica:
#            svíčky
            řádek = exportér(talasnica_na_svíčce)
            soubor.řádek(*řádek)

#            generátor

            for směrem,  generátor in (HORE,  talasnica_na_svíčce.býčiště),  (DOLE,  talasnica_na_svíčce.medvědiště):
                if generátor is not None:
                    if not hranice[směrem] == generátor.čekaná or not ohrada[směrem] == generátor.start:
                        ohrada[směrem] = generátor.start
                        hranice[směrem] = generátor.čekaná

                        if směrem == HORE:
                            soubor_býčí_ohrady.řádek(*exportér_generátoru(talasnica = talasnica_na_svíčce,  generátor = generátor))
                        elif směrem == DOLE:
                            soubor_medvědí_ohrady.řádek(*exportér_generátoru(talasnica = talasnica_na_svíčce,  generátor = generátor))

    with Soubor(jméno = 'obchody') as soubor:
        exportér = Exportuji_obchody()
        soubor.řádek(*exportér.hlavička)
        for obchody in talasnica.obchody.býci.obchody.values(),  talasnica.obchody.medvědi.obchody.values(),  talasnica.obchody.uzavřené:
            for obchod in obchody:
                řádek = exportér(obchod)
                soubor.řádek(*řádek)


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

    parametry = {'sklízím při zisku': 1000,
                        'odstup':200,
                        'rozestup': 200,
                        'sázím loty': 0.1
                 }

    talasnica = exportuji_talasnicu(zdrojové_csv,  parametry)
    print(talasnica)

#    if args.tabulka is True:
#        csv_soubor = 'tabulka_{}_{}.csv'.format(symbol,  perioda)
#        print('Exportuji tabulku do {}'.format(csv_soubor))
#        exporter = Exportuji_vše(csv_soubor,  zdrojové_csv,  parametry)
#        exporter()
#
#    if args.graf is True:
#        csv_soubor = 'graf_{}_{}.csv'.format(symbol,  perioda)
#        print('Exportuji graf do *{}'.format(csv_soubor))
#        exporter = Exportuji_graf(csv_soubor,  zdrojové_csv,  parametry)
#        talasnica = exporter()
#        print(talasnica)
