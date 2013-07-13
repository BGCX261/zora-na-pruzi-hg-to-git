#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen jsou dekorátory, který upraví text, který vrací funkce

barvy jsou uvedeny v souboru barvy
'''

import os
import functools

__OBARVI = '\033[{}m'
__RESET = '\033[0;39;49m'

def obarvi(*args):
    if len(args) > 3:
        raise ValueError('davaj_obarvovací_funkci očekává nejvýše tři parametry, barvu písma, barvu pozadí a styl, přičemž parametry možno zadati v libovolném pořadí')
    
    if os.getenv('ANSI_COLORS_DISABLED') is None:
        
        barvím = []
        
        for nastavení in args:
            if not int(nastavení) in range(1, 109):
                raise ValueError('Nelze nastavit kód barvy, či stylu {}'.format(str(nastavení)))
            barvím.append(nastavení)
         
        if barvím:
            barvím = ';'.join(barvím)
            barvím = __OBARVI.format(barvím)
            
            def dekorátor(funkce):
                
                @functools.wraps(funkce)
                def wrapper(*args,  **kwargs):
                    text = funkce(*args,  **kwargs)
                    text = text.replace(__RESET,  '{}{}'.format(__RESET,  barvím))
                    return '{}{}{}'.format(barvím,  text,  __RESET)
                return wrapper
                
            return dekorátor
              
        raise ValueError('Selhalo nastavení obarvovací funkce s parametry {}'.format(args))
              
    else:
#        return None
        return lambda text: text


def orámuj(hore = None,   dole = None):
    def dekorátor(funkce):
        
        @functools.wraps(funkce)
        def wrapper(*args,  **kwargs):
            text = funkce(*args,  **kwargs)
            déka_textu = len(text)
            nový_text = []
            for znak in hore,  dole:
                if znak is not None:
                    opakování  = int(déka_textu/len(znak))
                    nový_text.append(znak*opakování)
                else:
                    nový_text.append(None)
                    
            nový_text.insert(1,  text)
            výpis = [text for text in nový_text if not None]
            return '\n'.join(výpis)
                    
            
        return wrapper
    return dekorátor


def odsaď(o_kolik):
    odsazení = ' '*o_kolik
    
    def dekorátor(funkce):
        @functools.wraps(funkce)
        def wrapper(*args,  **kwargs):
            text = funkce(*args,  **kwargs)
            text = text.replace('\n',  '{}{}'.format('\n', odsazení))
            return '{}{}'.format(odsazení,  text)       
            
        return wrapper
    return dekorátor
