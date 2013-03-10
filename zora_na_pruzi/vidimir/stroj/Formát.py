#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je objekt, který upraví výpis
Nejdříve vytvoříš instanci Formátu a tu pak použiješ pomocí operátoru |
kód = 'moje jméno' | Formát(nějaké formátovací funkce)
print(kód)

'''


class Formát(object):
    
    def __init__(self,  *formátovací_funkce):
#    def __init__(self,  barva, pozadí = None,  styl = None,  formát = None):
        
        self.__formátovací_funkce = formátovací_funkce
            
    def __ror__(self,  text):
        for funkce in self.__formátovací_funkce:
            text = funkce(text)
        return text
        
    def __str__(self):
        raise NotImplementedError('Formát není určen k tomu, aby se vypisoval, užívej pouze ve spojení s operátorem text | Formát')
