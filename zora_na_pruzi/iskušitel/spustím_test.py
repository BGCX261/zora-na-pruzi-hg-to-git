#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který zobrazí log jako html stránku
'''
import pytest

from zora_na_pruzi.vidimir import pohled as p

def spustím_test(soubor):
    
    import time
    
    start = time.time()
    
    kód = pytest.main("-s {}".format(soubor))
    if kód == 0:
        print('... test proběhl v pořádku' | p.INFO)
    else:
        print('... test selhal a vrátil kód číslo {}'.format(kód) | p.CHYBA)
    
    print("čas běhu testu {čas:.3f} ms".format(čas = 1000*(time.time() - start)) | p.INFO)

