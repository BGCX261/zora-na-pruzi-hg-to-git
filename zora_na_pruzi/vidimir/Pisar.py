#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je třída, která umožní upravovat výpisy pomocí stylů
umí přesměrovat výstup
'''
import sys
from .pohled import pohled

class Pisar(object):
    
    __nastavení_pohledu = pohled
    __výstup_do_souboru = None
    
    def __init__(self,  jméno_vidu = None,  výstup = None,  proglas = None,  metaglas = None):
        '''
       
        '''
            
        self.__nastavení = {'jméno_vidu':  jméno_vidu,
                                'výstup':  výstup,
                                'proglas':  proglas,
                                'metaglas':  metaglas
                       }
            
    @property
    def pohled(self):
        return pohled
    
    def __enter__(self):
        
        self.__původní_nastavení = {'jméno_vidu':  self.__nastavení_pohledu,
                                'výstup':  sys.stdout
                       }
                       
        self.__nastavím_výstup(self.__nastavení['výstup'])
        self.__nastavím_jméno_vidu(self.__nastavení['jméno_vidu'])
        self.__vypíšu_přídavek(self.__nastavení['proglas'])
        
        return self
        
    def __exit__(self, *args):
        
        self.__vypíšu_přídavek(self.__nastavení['metaglas'])
        self.__nastavím_jméno_vidu(self.__původní_nastavení['jméno_vidu'])
        self.__nastavím_výstup(self.__původní_nastavení['výstup'])
        if self.__výstup_do_souboru is not None:
            self.__výstup_do_souboru.close()
        
    def __nastavím_jméno_vidu(self,  jméno_vidu):
        if jméno_vidu is not None:
            self.__nastavení_pohledu = jméno_vidu
            
    def __nastavím_výstup(self,  výstup):
        if výstup is None:
            return
        
#        předpokládám,  že to je název souboru
        if isinstance(výstup,  str):
            výstup = open(výstup,  mode ='w',  encoding = 'UTF-8')
            self.__výstup_do_souboru = výstup
            
        sys.stdout = výstup
            
    def __vypíšu_přídavek(self,  přídavek):
        if přídavek is None:
            return
            
        if callable(přídavek):
            přídavek = přídavek()
        print(přídavek)
        if self.__výstup_do_souboru:
            self.__výstup_do_souboru.flush()
            

