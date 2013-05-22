#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je třída, která reprezentuje sloupec
'''

from ..prvky_databáze.tabulka_databáze import tabulka_databáze
from .formát import formát_názvu, formát_hodnoty

from .výraz import výraz

from copy import copy

class sloupec_tabulky(object):
    
    def __init__(self,  jméno,  tabulka = None,  alias = None):
        
        if not isinstance(jméno,  str):
            raise TypeError('Jméno sloupce musí být řetězec ale je typu {}'.format(type(jméno)))
            
        if tabulka is not None and not isinstance(tabulka,  tabulka_databáze):
            raise TypeError('Databázová tabulka musí být typu tabulka_databáze, ale je typu {}'.format(type(tabulka)))
            
        if alias is not None:
            if not isinstance(alias,  str):
                raise TypeError('Alias pro název sloupce musí být řetězec, ale je typu {}'.format(type(alias)))
            
        self._jméno = jméno
        self._tabulka = tabulka
        self._alias = alias
        self._směr_řazení = None
        
        
    def AS(self,  alias):
#        nový_sloupec = type(self)(self,  alias = alias)
        nový_sloupec = copy(self)
        nový_sloupec._alias = alias
        
        return nový_sloupec

    def ASC(self):
        nový_sloupec = copy(self)
        nový_sloupec._směr_řazení = 'ASC'
        return nový_sloupec
        
    def DESC(self):
        nový_sloupec = copy(self)
        nový_sloupec._směr_řazení = 'DESC'
        return nový_sloupec

    def jméno(self):
        
        return formát_názvu(self._jméno)


    def __str__(self):
        
        název = self.jméno()
        
        if self._tabulka is not None:
            název = '{}.{}'.format(self._tabulka,  název)
        
        if self._alias is not None:
            název = '{} AS {}'.format(název,  formát_názvu(self._alias))
            
        if self._směr_řazení is not None:
            název = '{} {}'.format(název,  self._směr_řazení)
            
        return název
     
    def __eq__(self,  other):
        return výraz(self,  '=',  other)
        
    def __lt__(self,  other):
        return výraz(self,  '<',  other)
        
    def __le__(self,  other):
        return výraz(self,  '<=',  other)
       
    def __ne__(self,  other):
        return výraz(self,  '!=',  other)     
     
    def __ge__(self,  other):
        return výraz(self,  '>=',  other)
        
    def __gt__(self,  other):
        return výraz(self,  '>',  other)
        
    def __getitem__(self,  klíč):
        '''
        Toto je podpora hstore
        '''
        return hstore_sloupec(jméno = self._jméno,  tabulka = self._tabulka,  alias = self._alias,  hstore_klíč = klíč)
        
    def LIKE(self,  other):
        return výraz(self,  ' LIKE ',  other)
        

class hstore_sloupec(sloupec_tabulky):
    
    def __init__(self,  jméno,  tabulka = None,  alias = None,  hstore_klíč = None):
        super().__init__(jméno = jméno,  tabulka = tabulka,  alias = alias)
        self._hstore_klíč = hstore_klíč
        
    def jméno(self):
       
        klíč = self._hstore_klíč
        if isinstance(klíč,  str):
            klíč = formát_hodnoty(klíč)
        elif isinstance(klíč,  (list,  tuple)):
            klíč = 'ARRAY[{}]'.format(','.join(map(formát_hodnoty,  klíč)))
        else:
            raise TypeError('Neznámý typ klíče pro hstore')
            
            
        return '{sloupec}->{klíč}'.format(sloupec = super().jméno(),  klíč = klíč)
       
        
    def __eq__(self,  other):
#         'b=>1'
        vlevo = super().jméno()
        vpravo = '{}=>{}'.format(formát_názvu(self._hstore_klíč),  formát_názvu(other))
#        vpravo = formát_hodnoty(vpravo)
        return výraz(vlevo,  '@>',  vpravo)
        
class funkce_databáze(sloupec_tabulky):
    
    def __init__(self,  jméno,  schéma = None):
        super().__init__(jméno = jméno)
        self._schéma = schéma
    
    def __call__(self,  *args):
        self.__parametry = args
    
    def jméno(self):
        
        jméno = super().jméno()
        
        if self._schéma is not None:
            jméno = '{}.{}'.format(formát_názvu(self._schéma),  jméno)
        
        return '{jméno}({parametry})'.format(jméno = jméno,  parametry = ','.join(map(str,  self.__parametry)))

