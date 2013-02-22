#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je objekt, který obarvuje výpis
Nejdříve vytvoříš instanci a tu pak použiješ pomocí operátoru |
obarvi = Pisar(MODRÁ, NA_ČERVENÉ, TUČNÉ, PODTRŽENÉ)
barevný = 'nějaký text' | obarvi
print(barevný)

barvy jsou uvedeny v souboru barvy
'''

import os

class Pisar(object):

    OBARVI = '\033[{}m'
    RESET = '\033[0m'
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
#                nastavení = self.OBARVI.format(nastavení)
                barvím.append(nastavení)
                
#            if barva is not None:
#                barva = self.barvy[barva]
##                barvím.append(self.OBARVI.format(barva))
#                barvím.append(barva)
#            
#            if pozadí is not None:
#                pozadí = self.pozadí[pozadí]
##                barvím.append(self.OBARVI.format(pozadí))
#                barvím.append(pozadí)
#                
#            if styl is not None:
#                styl = self.styly[styl]
##                barvím.append(self.OBARVI.format(styl))
#                barvím.append(styl)
#                
#            self.BARVA = ''.join(barvím)
            barvím = ';'.join(barvím)
            self.BARVA = self.OBARVI.format(barvím)
            
    def __ror__(self,  text):
        text = self.FORMÁT.format(text)
        if self.BARVA is not None:
            text = text.replace(self.RESET,  '{}{}'.format(self.RESET,  self.BARVA))
            return '{}{}{}'.format(self.BARVA,  text,  self.RESET)
        return text
