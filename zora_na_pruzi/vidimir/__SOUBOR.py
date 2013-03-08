#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

from .VÝSTUP import VÝSTUP

class __SOUBOR():
    
    def __init__(self,  obsah):
        self.__obsah = obsah
       
    @property
    def obsah(self):
        return self.__obsah
        
    def __call__(self):
        print(self.obsah)
        
    def __rshift__(self,  soubor):
        '''
        operátor SOUBOR >> soubor:řetězec umožní uložit obsah do souboru
        '''
        if not isinstance(soubor,  (str, )):
            raise TypeError('Operátor >> očekává jméno souboru.'.format(self.tag))
        
        print('uložím objekt {0} do souboru {1}'.format(self.__class__.__name__,  soubor))
        
        with VÝSTUP(soubor):
            self()
            
        


