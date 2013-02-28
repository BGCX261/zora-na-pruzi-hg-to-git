#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je objekt, který obarvuje výpis
Nejdříve vytvoříš instanci a tu pak použiješ pomocí operátoru |
obarvím = OBARVI(MODRÁ, NA_ČERVENÉ, TUČNÉ, PODTRŽENÉ)
barevný = 'nějaký text' | obarvím
print(barevný)

barvy jsou uvedeny v souboru barvy
'''

import os

class OBARVI(object):

    OBARVI = '\033[{}m'
    RESET = '\033[0;39;49m'
    
    formátuji = None
    nadtrhnu = None
    podtrhnu = None
    odsadím = None
    obarvím = None
    
    def __init__(self,  *args,  formát = None,  podtržítko = None,  nadtržítko = None,  odsazení = None):
#    def __init__(self,  barva, pozadí = None,  styl = None,  formát = None):
            
        if formát is not None:
            self.formátuji = self.__davaj_formát(formát)
            
        
        if podtržítko is not None:
            self.podtrhnu = self.__davaj_podtržítko(podtržítko)
           
            
        if nadtržítko is not None:
            self.nadtrhnu = self.__davaj_nadtržítko(nadtržítko)
        
        
        if os.getenv('ANSI_COLORS_DISABLED') is None:
        
            barvím = []
            
            for nastavení in args:
                if not int(nastavení) in range(1, 109):
                    raise ValueError('Nelze nastavit kód barvy {}'.format(str(nastavení)))
                barvím.append(nastavení)
             
            if barvím:
                barvím = ';'.join(barvím)
                barvím = self.OBARVI.format(barvím)
                self.obarvím = self.__davaj_barvím(barvím)
            
        if odsazení is not None:
            self.odsadím = self.__davaj_odsazení(odsazení)

            
    def __ror__(self,  text):
        
        if callable(self.formátuji):
            text = self.formátuji(text)
           
        řádky = []
        
        if callable(self.nadtrhnu):
            řádky.append(self.nadtrhnu(text))
            
        řádky.append(text)
            
        if callable(self.podtrhnu):
            řádky.append(self.podtrhnu(text))
            
        text = '\n'.join(řádky)
        řádky = None
        
        if callable(self.odsadím):
            text = self.odsadím(text)

        if callable(self.obarvím):
            text = self.obarvím(text)
        
        return text

    def __davaj_formát(self,  formát):
        def formátuji(text):
            return formát.format(text)
        return formátuji
            
    def __davaj_barvím(self,  barvy):
        def barvím(text):
            text = text.replace(self.RESET,  '{}{}'.format(self.RESET,  barvy))
            return '{}{}{}'.format(barvy,  text,  self.RESET)
        return barvím
        
    def __davaj_podtržítko(self,  podtržítko):
        délka_podtržítka = len(podtržítko)
        def podtrhuji(text):
            opakování  = int(len(text)/délka_podtržítka + 1)
            return podtržítko * opakování
        return podtrhuji
        
    def __davaj_nadtržítko(self,  nadtržítko):
        délka_nadtržítka = len(nadtržítko)
        def nadtrhuji(text):
            opakování  = int(len(text)/délka_nadtržítka + 1)
            return nadtržítko * opakování
        return nadtrhuji
        
    def __davaj_odsazení(self,  o_kolik):
        odsazení = ' ' * o_kolik
        def odsazuji(text):
            text = text.replace('\n',  '{}{}'.format('\n',  odsazení))
            return ''.join((odsazení, text))
        return odsazuji
