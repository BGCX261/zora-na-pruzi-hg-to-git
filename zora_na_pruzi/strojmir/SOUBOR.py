#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

from zora_na_pruzi.vidimir.__SOUBOR import __SOUBOR as VIDIMIR_SOUBOR

class SOUBOR(object):
        
    def __get__(self,  instance,  owner = None):
 
        modul = instance.__module__
        if not modul.startswith('zora_na_pruzi.strojmir'):
            raise TypeError('Zobrazit umím jenom objekty z balíčku zora_na_pruzi.strojmir')
            
        modul = modul.replace('zora_na_pruzi.strojmir',  'zora_na_pruzi.vidimir',  1)
        
        from zora_na_pruzi.strojmir import importuji
        najdu_třídu = importuji.davaj_importéra(jméno_balíčku = modul)
        TŘÍDA = najdu_třídu(jméno_třídy = instance.__class__.__name__)
        
        
        
        if not issubclass(TŘÍDA,  VIDIMIR_SOUBOR):
            raise TypeError('Třída {} v balíčku {} není potomkem třídy vidimir.__SOUBOR'.format(instance.__class__.__name__,  modul))
       
        return TŘÍDA(instance)
