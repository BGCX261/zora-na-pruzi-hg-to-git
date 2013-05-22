#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je třída, která vytvoří příkaz INSERT
'''

from ..prvky_databáze.formát import formát_hodnoty

from ..prvky_databáze.sloupec_tabulky import sloupec_tabulky
from ..prvky_databáze.tabulka_databáze import tabulka_databáze

from ._příkaz import _příkaz

class INSERT(_příkaz):
    
    def __init__(self,  tabulka):
        if not isinstance(tabulka,  tabulka_databáze):
            raise TypeError('Databázová tabulka musí být typu tabulka_databáze, ale je typu {}'.format(type(tabulka)))
            
        self.__tabulka = tabulka
        self.__sloupce = None
        self.__hodnoty_musí_být_zadány_jako_slovník = False
        self.__hodnoty = []
        
    def INTO(self,  *args):
#        print('nastavuji sloupce v INSERT',  args)
        sloupce = []
        for sloupec in args:  
            if isinstance(sloupec,  sloupec_tabulky):
#                sloupce.append(getattr(self.__tabulka,  sloupec.jméno()))
                sloupce.append(sloupec)
            elif isinstance(sloupec,  str):
                sloupce.append(getattr(self.__tabulka,  sloupec))
            else:
                raise TypeError('Sloupec tabulky musí být typu sloupec_tabulky, ale je typu {}'.format(type(sloupec)))
            
        self.__sloupce = tuple(sloupce)
        
        return self
        
    def VALUES(self,  *args,  **kwargs):
#        print('nastavuji hodnoty v INSERT')
#        print('\tbez klíčů: ',  args)
#        print('\ta s klíči ',  kwargs)
        
#        když nejsou zadané sloupce
        if self.__sloupce is None:
#            očekávám seznam název_sloupce: hodnota
            if not kwargs:
                raise ValueError('Nejdřív zadej sloupce, potom přidávej hodnoty')
            else:
#                a ty názvy si z toho vytáhnu
                sloupce = tuple(kwargs.keys())
                self.INTO(*sloupce)
#                a zamezím přijímat VALUES bez klíčů,  jako seznam, nebo n-tice  protože není jisté pořadí klíčů
                self.__hodnoty_musí_být_zadány_jako_slovník = True

        if len(self.__sloupce) != len(args) + len(kwargs):
            raise ValueError('Hodnot mosí být tolik, kolik je sloupců, máš {} sloupců a {} hodnot'.format(len(self.__sloupce),   len(args) + len(kwargs)))            
 

        hodnoty = []
        hodnoty_předané_bez_klíče = list(args)
        
        for sloupec in self.__sloupce:
            klíč = sloupec._jméno
            if self.__hodnoty_musí_být_zadány_jako_slovník:
                try:
#                    print('\t{0} = kwargs["{0}"]'.format(klíč))
                    hodnoty.append(kwargs[klíč])
                except KeyError as e:
                    raise ValueError('V tomto případě očekávám, že hodnotu zadáš jako {} = {}'.format(klíč,  '?hodnota?')) from e
            else:
                if klíč in kwargs:
#                    print('\t{0} = kwargs["{0}"]'.format(klíč))
                    hodnota = kwargs[klíč]
                else:
                    try:
#                        print('\t{} = args[{}]'.format(klíč,  len(args) - len(hodnoty_předané_bez_klíče)))
                        hodnota = hodnoty_předané_bez_klíče.pop(0)
                    except IndexError as e:
                        raise ValueError('Nenašel jsem hodnotu pro sloupec {}'.format(klíč)) from e
#                hodnoty_předané_bez_klíče.pop()
                hodnoty.append(hodnota)
                       
        self.__hodnoty.append(hodnoty)
        
        return self

#    def vyčisti_hodnoty(self):
#        self._hodnoty = []
  
    def __str__(self):
        
        if self.__tabulka is None:
#        if not isinstance(self._tabulka,  tabulka):
            raise ValueError("Neznám jméno tabulky")
#            raise ValueError("Tabulka mosí být typu danimir.tabulka.tabulka")
            
        if not self.__sloupce:
            raise ValueError("Neznám sloupce tabulky")
            
        if not self.__hodnoty:
            raise ValueError("Nemám hodnoty, které bych vložil do tabulky")
            
        příkaz = ['INSERT INTO']
        
        příkaz.append(str(self.__tabulka))
        
#        sloupce = ','.join(map(str,  self.__sloupce))
        sloupce = (sloupec.jméno() for sloupec in self.__sloupce)
        příkaz.append("({sloupce})".format(sloupce = ','.join(sloupce)))
        
        příkaz.append('VALUES')
        
        výpis = []
        for hodnoty in self.__hodnoty:
                
            řádek = map(formát_hodnoty,  hodnoty)
                    
            výpis.append('({})'.format(','.join(řádek)))
#            příkaz.append(hodnoty)
            
        příkaz.append('\t{}'.format(',\n\t'.join(výpis)))
        
        return '\n'.join(příkaz)
        
#    def vykonej(self,  enom_vypiš = False):
#        sql = self.__str__()
#        if enom_vypiš:
#            print(sql)
#        else:
#            self._db.execute(sql)


if __name__ == '__main__':

    print(__doc__)

#    main()



