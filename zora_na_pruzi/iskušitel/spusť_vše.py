#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

from zora_na_pruzi.iskušitel import najdu_testovací_soubory

from zora_na_pruzi.pisar.styly.obarvím_výpis_konzole import *

import os,  sys

def provedu_testy(cesta,  styl):
    
    print('IDU DA NAJDU TESTY v adresáři {}'.format(cesta | styl.SOUBOR) | styl.H1)

    import time
    start = time.time()
    
    try:
        from spustím_test import spustím_test
        for číslo_testu,  testovací_soubor in enumerate(najdu_testovací_soubory(cesta),  start = 1):
            print('{} spouštím {}'.format(číslo_testu, testovací_soubor  | styl.SOUBOR) | styl.H2)
            spustím_test(testovací_soubor)
        print("Dotestováno. Čas běhu testu {čas:.3f} ms".format(čas = 1000*(time.time() - start)) | styl.INFO)
        print('Počet nalezených testovacích souborů je {}'.format(číslo_testu) | styl.INFO)
    except IOError as e :
        print('Hledání testovacích souborů selhalo:\n{}'.format(e) | styl.CHYBA)
#        print('<h1>spouštím test {}</h1>'.format(os.path.basename(soubor)))
#        kód = pytest.main("-s {}".format(soubor))
#        if kód == 0:
#            print('... test proběhl v pořádku')
#        else:
#            print('... test selhal a vrátil kód číslo {}'.format(kód))
#    finally:
        
        



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
    
    from zora_na_pruzi.iskušitel import davaj_styl
    
    if not args.text:
        
        from zora_na_pruzi.pisar.styly import výpisy_testů_html as styl
        davaj_styl(styl)
        
        from html_výstup import HTML_VÝSTUP,  VÝSLEDKY_TESTŮ_DO_SOUBORU
        print('Vypíšu výsledek do html souboru {}'.format(VÝSLEDKY_TESTŮ_DO_SOUBORU | SOUBOR) | INFO)
#            vypisuji_do = open(VÝSLEDKY_TESTŮ_DO_SOUBORU,  mode ='w',  encoding = 'UTF-8')
        
        with HTML_VÝSTUP(VÝSLEDKY_TESTŮ_DO_SOUBORU) as html:
            provedu_testy(cesta,  styl)
            
        if args.bez_prohlížeče:
            print('Výsledek jest uložen v souboru {}'.format(VÝSLEDKY_TESTŮ_DO_SOUBORU | SOUBOR) | INFO)
        else:
            print('Zobrazím výsledek v prohlížeči')
            from zobrazím_v_prohlížeči import zobrazím_v_prohlížeči
            zobrazím_v_prohlížeči(VÝSLEDKY_TESTŮ_DO_SOUBORU)
#            from zora_na_pruzi.system.html_prohlížeč import zobrazím_html_stránku
#            zobrazím_html_stránku(VÝSLEDKY_TESTŮ_DO_SOUBORU)
    else:
        from zora_na_pruzi.pisar.styly import obarvím_výpis_konzole as styl
        davaj_styl(styl)
        provedu_testy(cesta,  styl)
    

