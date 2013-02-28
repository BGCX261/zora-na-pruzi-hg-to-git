#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

from zora_na_pruzi.iskušitel import najdu_testovací_soubory

import os,  sys

from zora_na_pruzi.vidimir import pohled as p

def provedu_testy(cesta):
    
    print('IDU DA NAJDU TESTY v adresáři {}'.format(cesta | p.SOUBOR) | p.H1)

    import time
    start = time.time()
    
    try:
        from spustím_test import spustím_test
        for číslo_testu,  testovací_soubor in enumerate(najdu_testovací_soubory(cesta),  start = 1):
            print('{} spouštím {}'.format(číslo_testu, testovací_soubor  | p.SOUBOR) | p.H2)
            spustím_test(testovací_soubor)
        print("Dotestováno. Čas běhu testu {čas:.3f} ms".format(čas = 1000*(time.time() - start)) | p.INFO)
        print('Počet nalezených testovacích souborů je {}'.format(číslo_testu) | p.INFO)
    except IOError as e :
        print('Hledání testovacích souborů selhalo:\n{}'.format(e) | p.CHYBA)

if __name__ == '__main__':

    __version__ = 0.2

    import argparse
#    import os
#    import glob
#    import sys
    
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser()

#   a pak mu nastavím jaké příkazy a parametry má přijímat
    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, искушител {}'.format(__version__))
    
    parser.add_argument('--text',  action='store_true',  help = 'výsledek se neuloží do html souboru, ale vypíše se přímo do konzole')
    parser.add_argument('--bez_prohlížeče',  action='store_true',  help = 'Běžně spustí prohlížeč, tato volba vypne toto chování, nespustí se prohlížeč a nezobrazí se html soubor s výsledky testů')

    parser.add_argument('cesta')
#    parser.add_argument('maska_souborů')
    
    #    a včíl to možu rozparsovat
    args = parser.parse_args()
    
    cesta = args.cesta
    
    if not args.text:
        
        from html_výstup import VÝSLEDKY_TESTŮ_DO_SOUBORU,  hlavička,  patička
        from zora_na_pruzi.vidimir.Pisar import Pisar
        
        print('Vypíšu výsledek do html souboru {}'.format(VÝSLEDKY_TESTŮ_DO_SOUBORU | p.SOUBOR) | p.INFO)
#            vypisuji_do = open(VÝSLEDKY_TESTŮ_DO_SOUBORU,  mode ='w',  encoding = 'UTF-8')
        
        with Pisar(výstup = VÝSLEDKY_TESTŮ_DO_SOUBORU,  jméno_vidu = 'html',  proglas = hlavička,  metaglas = patička) as html:
            provedu_testy(cesta)
            
        if args.bez_prohlížeče:
            print('Výsledek jest uložen v souboru {}'.format(VÝSLEDKY_TESTŮ_DO_SOUBORU | p.SOUBOR) | p.INFO)
        else:
            print('Zobrazím výsledek v prohlížeči')
            from zobrazím_v_prohlížeči import zobrazím_v_prohlížeči
            zobrazím_v_prohlížeči(VÝSLEDKY_TESTŮ_DO_SOUBORU)
#            from zora_na_pruzi.system.html_prohlížeč import zobrazím_html_stránku
#            zobrazím_html_stránku(VÝSLEDKY_TESTŮ_DO_SOUBORU)
    else:
        provedu_testy(cesta)
    

