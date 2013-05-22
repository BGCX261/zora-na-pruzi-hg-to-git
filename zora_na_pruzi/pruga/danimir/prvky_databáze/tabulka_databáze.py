#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je třída, která reprezentuje tabulku
'''

#from  danimir.sloupec_tabulky import sloupec_tabulky

from .formát import formát_názvu

class tabulka_databáze(object):
    
    def __init__(self,  jméno,  schéma = None):
        self.__dict__['_tabulka_databáze__jméno'] = jméno
        self.__dict__['_tabulka_databáze__schéma'] = schéma
#        self.__dict__['sloupce'] = []

    def __call__(self,  *args):
        from  ..prvky_databáze.sloupec_tabulky import funkce_databáze
        funkce = funkce_databáze(jméno = self.__jméno,  schéma = self.__schéma)
        funkce(*args)
        return funkce
        
    def __getattr__(self,  jméno):

        if jméno == '_spojení__jméno':
            return self.__jméno
        
        from  ..prvky_databáze.sloupec_tabulky import sloupec_tabulky
        
#        print('volám tabulka __getattr__(self,  jméno)',  jméno)
        return sloupec_tabulky(jméno,  tabulka = self)

    def __str__(self):
        
        if self.__schéma is not None:
            return '{}.{}'.format(*map(formát_názvu,  (self.__schéma,  self.__jméno)))
        else:
            return formát_názvu(self.__jméno)
     
#    def __repr__(self):
#        db = 'db'
#        if self.__schéma is not None:
#            return "{}['{}'].{}".format(db,  self.__schéma,  self.__jméno)
#        else:
#            return '{}.{}'.format(db,  self.__jméno)
        
        
#    def __setattr__(self,  jméno,  hodnota):
#        print('volám databáze __setattr__(self,  jméno, hodnota)',  jméno,  hodnota)
#        self.__dict__[jméno] = hodnota
        

