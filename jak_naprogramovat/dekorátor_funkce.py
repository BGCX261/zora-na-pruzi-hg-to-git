#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import functools

def je_kladné(funkce):
    @functools.wraps(funkce)
    def wrapper(*args,  **kwargs):
        print(funkce.__name__)
        vrací = funkce(*args,  **kwargs)
        assert vrací > 0
        return vrací
    return wrapper
    
def je_liché(funkce):
    @functools.wraps(funkce)
    def wrapper(*args,  **kwargs):
        print(funkce.__name__)
        vrací = funkce(*args,  **kwargs)
        assert vrací % 2 == 0
        return vrací
    return wrapper

def je_větší(než):
    než = než + 1
    def dekorátor(funkce):
        @functools.wraps(funkce)
        def wrapper(*args,  **kwargs):
            print(funkce.__name__)
            vrací = funkce(*args,  **kwargs)
            assert vrací > než
            return vrací
        return wrapper
    return dekorátor

@je_kladné
@je_liché
@je_větší(než = 2)
def dej_číslo(číslo):
    return číslo
    
print('a')
dej_číslo(6)
#dej_číslo(-5)
