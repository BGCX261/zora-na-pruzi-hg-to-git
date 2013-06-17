#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který umožní vytvářet soubory pomocí přesměrování
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

    
import sys,  os

class DO_SOUBORU(object):
    
    '''
    přesměruje standartní výstup
    '''
    
    def __init__(self, jméno_souboru):
        if isinstance(jméno_souboru,  str):
            self.__jméno_souboru = self.__upravím_příponu(jméno_souboru)
        else:
            raise TypeError('Jméno souboru musí býti řetězcem a nikolivěk {}'.format(type(jméno_souboru)))
            
    def __enter__(self):
        self.__původní_výstup = sys.stdout
        sys.stdout = open(self.__jméno_souboru,  mode ='w',  encoding = 'UTF-8')
        return sys.stdout
        
    def __exit__(self, *args):
        sys.stdout = self.__původní_výstup


    def __upravím_příponu(self,  jméno_souboru):
        jméno,  přípona = os.path.splitext(jméno_souboru)
        
        if přípona == '.py':
            return self.__upravím_příponu(jméno)
            
        přípony = '.html',  '.js',  '.css'
        if přípona in přípony:
            return jméno_souboru
            
        raise ValueError('Neplatná přípona souboru "{}", umím pouze přípony {}'.format(přípona, ', '.join(přípony)))
            

