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
    BARVA = None
    
    def __init__(self,  *args,  formát = None):
#    def __init__(self,  barva, pozadí = None,  styl = None,  formát = None):
        
        if formát is None:
            formát = '{}'
            
        self.FORMÁT = formát
        
        if os.getenv('ANSI_COLORS_DISABLED') is None:
        
            barvím = []
            
            for nastavení in args:
                if not int(nastavení) in range(1, 109):
                    raise ValueError('Nelze nastavit kód barvy {}'.format(str(nastavení)))
                barvím.append(nastavení)
                
            barvím = ';'.join(barvím)
            self.BARVA = self.OBARVI.format(barvím)
            
    def __ror__(self,  text):
        text = self.FORMÁT.format(text)
        if self.BARVA is not None:
            text = text.replace(self.RESET,  '{}{}'.format(self.RESET,  self.BARVA))
            return '{}{}{}'.format(self.BARVA,  text,  self.RESET)
        return text
