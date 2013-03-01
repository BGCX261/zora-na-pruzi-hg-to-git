#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je objekt, který upraví výpis
Nejdříve vytvoříš instanci Formátu a tu pak použiješ pomocí operátoru |
jméno = Formát('jméno: {} ')
kód = 'moje jméno' | jméno
print(kód)

'''


class Formát(object):
    
    def __init__(self,  formát):
#    def __init__(self,  barva, pozadí = None,  styl = None,  formát = None):
        
        self.__formát = formát
            
    def __ror__(self,  text):
        return self.__formát.format(text)
        
    def __str__(self):
        raise NotImplementedError('Formát není určen k tomu, aby se vypisoval, užívej pouze ve spojení s operátorem text | Formát')
