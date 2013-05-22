#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je třída, který vytvoří příkaz UPDATE
'''

from ..prvky_databáze.formát import formát_hodnoty

from ..prvky_databáze.sloupec_tabulky import sloupec_tabulky
from ..prvky_databáze.tabulka_databáze import tabulka_databáze

from ._příkaz import _příkaz

class UPDATE(_příkaz):
    
    def __init__(self,  tabulka):
        if not isinstance(tabulka,  tabulka_databáze):
            raise TypeError('Databázová tabulka musí být typu tabulka_databáze, ale je typu {}'.format(type(tabulka)))
            
        self.__tabulka = tabulka
        self.__hodnoty = None
        self.__where = None
        
    def SET(self,  **hodnoty):

        self.__hodnoty = dict(hodnoty)
        
        return self

    def WHERE(self,  where):
#        print('UPDATE WHERE',  where,  type(where))
        self.__where = where
        return self
  
    def __str__(self):
        
        if self.__tabulka is None:
            raise ValueError("Neznám jméno tabulky")
            
        if not self.__hodnoty:
            raise ValueError("Nemám hodnoty, které bych změnil v tabulce")
            
        příkaz = ['UPDATE']
        příkaz.append(str(self.__tabulka))
        
        příkaz.append('SET')
        
        výpis = []
        for klíč,  hodnota in self.__hodnoty.items():
            
            sloupec = getattr(self.__tabulka,  klíč)
            hodnota = formát_hodnoty(hodnota)
            
            výpis.append('{}={}'.format(sloupec.jméno(),  hodnota))
            
        příkaz.append(','.join(výpis))
        
        if self.__where is not None:
            příkaz.append('WHERE')
            příkaz.append(str(self.__where))
            
        return '\n'.join(příkaz)
        


#if __name__ == '__main__':
#
#    print(__doc__)

#    main()



