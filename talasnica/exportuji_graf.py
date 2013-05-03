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
                    'otevírací cena', 
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
                talasnica.data['OPEN'].prodej,
                ima(talasnica.býčiště,  'start'),  ima(talasnica.medvědiště,  'start'),
                ima(talasnica.býčiště,  'čekaná'),  ima(talasnica.medvědiště,  'čekaná'),
                talasnica.obchody.býci.velikost,  talasnica.obchody.medvědi.velikost,
                talasnica.obchody.býci.cena, talasnica.obchody.medvědi.cena,
                talasnica.obchody.velikost,  talasnica.obchody.cena,
                int(talasnica.znamení_setby),
                int(talasnica.znamení_sklizně),
                talasnica.profit_při_otevření,
                talasnica.obchody.zisk(talasnica.data[HIGHT]),
                talasnica.obchody.zisk(talasnica.data[LOW]),
                talasnica.obchody.zisk(talasnica.data[CLOSE]),
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
                    'uložený zisk',  'otevřený zisk', 'swap'
                    )

    def __init__(self,  závěrečná_cena):
        self.závěrečná_cena = závěrečná_cena

    def __call__(self,  obchod):
        return (
                    obchod.tiket,
                    int(obchod.směr == DOLE),
                    obchod.čas_otevření.timestamp,  obchod.cena_otevření,
                    obchod.velikost,
                    0, 0,
                    obchod.čas_zavření.timestamp,  obchod.cena_zavření or 0,
                    obchod.uložený_profit,  obchod.otevřený_profit(self.závěrečná_cena),  obchod.swap
                       )


#class Exportuji_ohradu(object):
#
#    hlavička = (
#                    'čas',
#                    'start',
#                    'čekaná'
#                    )
#
#    def __call__(self,  talasnica,  generátor):
#
#        return (talasnica.data[OPEN_TIME].timestamp,
#                                    generátor.start,
#                                    generátor.čekaná
#                        )
#

class Exportuji_parametry(object):

                    
    def __init__(self,  parametry):
        self.hlavička = parametry.keys()
        self.data = parametry.values()

#    def __call__(self):
#
#        return self.data


#######################

def davaj_třídu_souboru(symbol,  časový_rámec,  encoding):



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
            print('otevírám pro zápis soubor {}'.format(self.cesta))
            self.soubor = open(self.cesta,  mode = "w",  encoding = self.encoding)
#            časová_značka = time.time()
#            self.řádek(int(časová_značka))
#            self.řádek('SYMBOL',  'časový rámec')
#            self.řádek(symbol,  časový_rámec)
#            self.řádek(len(parametry))
#            self.řádek(*parametry.keys())
#            self.řádek(*parametry.values())

            return self

        def řádek(self,  *sloupce):
            csv_řádek = ';'.join(map(str,  sloupce))
            print(csv_řádek, file = self.soubor)

        def __exit__(self, *args):
            print('zapsáno do souboru {}'.format(self.cesta))
            self.soubor.close()

    return Soubor

def exportuji_talasnicu(zdrojové_csv,  parametry):
    print('exportuji Talasnicu')
    print('zdrojový soubor {}'.format(zdrojové_csv))
    print('parametry {}'.format(parametry))

    talasnica = Talasnica(zdrojové_csv = zdrojové_csv,  parametry = parametry)

#    print(talasnica.info)

    Soubor = davaj_třídu_souboru(symbol = talasnica.info['SYMBOL'],  časový_rámec = talasnica.info['časový rámec'],  encoding = "windows-1250")

#soubor,  který uzamkne načítání,  ak nejestvuje,  tak metatrader nebude načítat,  proto jej nejdříve smažu
    zamykací_soubor = Soubor("zámek")
    if os.path.isfile(zamykací_soubor.cesta):
        os.remove(zamykací_soubor.cesta)


    with Soubor(jméno = 'parametry') as soubor:
        exportér = Exportuji_parametry(parametry)
        soubor.řádek(*exportér.hlavička)
        soubor.řádek(*exportér.data)


#    ohrada = {HORE: None,  DOLE: None}
#    hranice = {HORE: None,  DOLE: None}


#    with Soubor(jméno = 'svíčky') as soubor,  Soubor(jméno = 'býčí_ohrada') as soubor_býčí_ohrady,  Soubor(jméno = 'medvědí_ohrada') as soubor_medvědí_ohrady:
    with Soubor(jméno = 'svíčky') as soubor:
        exportér = Exportuji_svíčku()
        soubor.řádek(*exportér.hlavička)

#        exportér_generátoru = Exportuji_ohradu()
#        soubor_býčí_ohrady.řádek(*exportér_generátoru.hlavička)
#        soubor_medvědí_ohrady.řádek(*exportér_generátoru.hlavička)

        for talasnica_na_svíčce in talasnica:
#            svíčky
            řádek = exportér(talasnica_na_svíčce)
            soubor.řádek(*řádek)

#            generátor

#            for směrem,  generátor in (HORE,  talasnica_na_svíčce.býčiště),  (DOLE,  talasnica_na_svíčce.medvědiště):
#                if generátor is not None:
#                    if not hranice[směrem] == generátor.čekaná or not ohrada[směrem] == generátor.start:
#                        ohrada[směrem] = generátor.start
#                        hranice[směrem] = generátor.čekaná
#
#                        if směrem == HORE:
#                            soubor_býčí_ohrady.řádek(*exportér_generátoru(talasnica = talasnica_na_svíčce,  generátor = generátor))
#                        elif směrem == DOLE:
#                            soubor_medvědí_ohrady.řádek(*exportér_generátoru(talasnica = talasnica_na_svíčce,  generátor = generátor))

    with Soubor(jméno = 'obchody') as soubor:
        exportér = Exportuji_obchody(závěrečná_cena = talasnica.data[OPEN])
        soubor.řádek(*exportér.hlavička)
        for obchody in talasnica.obchody.býci.obchody.values(),  talasnica.obchody.medvědi.obchody.values(),  talasnica.obchody.uzavřené:
            for obchod in obchody:
                řádek = exportér(obchod)
                soubor.řádek(*řádek)


    with Soubor(jméno = 'poslední_svíčka') as soubor:
        soubor.řádek("čas otevření",  talasnica.data[OPEN_TIME].timestamp,  talasnica.data[OPEN_TIME])
        soubor.řádek("cena",  "prodej",  "nákup",  "spred")
        soubor.řádek("otevřeno na",  talasnica.data[OPEN].prodej,  talasnica.data[OPEN].nákup,  talasnica.data[OPEN].spred)
        soubor.řádek("cena hore",  talasnica.data[HIGHT].prodej,  talasnica.data[HIGHT].nákup,  talasnica.data[HIGHT].spred)
        soubor.řádek("cena dole",  talasnica.data[LOW].prodej,  talasnica.data[LOW].nákup,  talasnica.data[LOW].spred)
        soubor.řádek("zavřeno na",  talasnica.data[CLOSE].prodej,  talasnica.data[CLOSE].nákup,  talasnica.data[CLOSE].spred)

#    obnovím ten zamykací soubor 
    with zamykací_soubor as soubor:
        časová_značka = time.time()
        soubor.řádek(int(časová_značka))

    return talasnica

if __name__ == '__main__':

    import argparse
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser()

#   a pak mu nastavím jaké příkazy a parametry má přijímat
    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, {}'.format(__version__))

    parser.add_argument('zdrojový_adresář')
#    parser.add_argument('--graf',  '-g',  action='store_true')
#    parser.add_argument('--tabulka',  '-t',  action='store_true')

    #    a včíl to možu rozparsovat
    args = parser.parse_args()

#    print(args)

    
    zdrojový_adresář = args.zdrojový_adresář
#    zdrojové_csv = args.zdrojový_soubor
#    csv_soubor = args.soubor

    if zdrojový_adresář is None:
        print('Není zadán zdrojový adresář')
    else:
        print('Načtu data z adresáře {}'.format(zdrojový_adresář))

        symbol = 'EURJPY.'
        perioda = 60

        parametry = {'sklízím při zisku': 1000,
                            'odstup':200,
                            'rozestup': 200,
                            'sázím loty': 0.1
                     }

        talasnica = exportuji_talasnicu(zdrojový_adresář,  parametry)
        print(talasnica)
