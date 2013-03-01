#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který zobrazí log jako html stránku
'''
import pytest

from zora_na_pruzi.vidimir import F

def spustím_test(soubor):
    
    import time
    
    start = time.time()
    
#    import py
#    py.std.sys.stdout = open('hen',  mode = 'w',  encoding = 'UTF-8')
    kód = pytest.main("-s {}".format(soubor))
    if kód == 0:
        print('... test proběhl v pořádku' | F.INFO)
    else:
        print('... test selhal a vrátil kód číslo {}'.format(kód) | F.CHYBA)
    
    print("čas běhu testu {čas:.3f} ms".format(čas = 1000*(time.time() - start)) | F.INFO)

