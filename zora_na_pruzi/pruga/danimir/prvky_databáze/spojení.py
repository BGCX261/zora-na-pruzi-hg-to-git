#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který ...
'''

from ..prvky_databáze.tabulka_databáze import tabulka_databáze
from ..prvky_databáze.sloupec_tabulky import sloupec_tabulky

class spojení(object):
    
    def __init__(self,  první_tabulka,  druhá_tabulka):
        
        if isinstance(první_tabulka,  tabulka_databáze):
            jméno_sloupce = 'id_{}'.format(druhá_tabulka.__jméno)
            první_sloupec = getattr(první_tabulka,  jméno_sloupce)
        elif isinstance(první_tabulka,  sloupec_tabulky):
            první_sloupec = první_tabulka
        else:
            raise TypeError('Spojovat sa možu enem sloupce tabulky, zadej tabulku, nebo sloupec tabulky, zadal si {}'.format(type(první_tabulka)))

        if isinstance(druhá_tabulka,  tabulka_databáze):
            druhý_sloupec = druhá_tabulka.id
        elif isinstance(druhá_tabulka,  sloupec_tabulky):
            druhý_sloupec = druhá_tabulka
        else:
            raise TypeError('Spojovat sa možu enem sloupce tabulky, zadej tabulku, nebo sloupec tabulky, zadal si {}'.format(type(první_tabulka)))


        self.__první_sloupec = první_sloupec
        self.__druhý_sloupec = druhý_sloupec
        
    def __str__(self):
        return 'JOIN {druhý_sloupec._tabulka}\n\tON {první_sloupec} = {druhý_sloupec}'.format(první_sloupec = self.__první_sloupec,  druhý_sloupec = self.__druhý_sloupec)
