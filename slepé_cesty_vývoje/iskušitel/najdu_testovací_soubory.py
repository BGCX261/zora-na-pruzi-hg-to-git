#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

import os,  fnmatch

MASKA_TESTOVACÍCH_SOUBORŮ = 'testuji_*.py'

def najdu_testovací_soubory(cesta):
    
    počet_nalezených_testů = 0
    
    if os.path.isdir(cesta):
        
        for cesta_do_adresáře, nalezené_adresáře, nalezené_soubory in os.walk(cesta):
            for jméno_nalezeného_souboru in nalezené_soubory:
                if fnmatch.fnmatch(jméno_nalezeného_souboru, MASKA_TESTOVACÍCH_SOUBORŮ):
#                    if jméno_nalezeného_souboru.endswith('.py')  and not  jméno_nalezeného_souboru.startswith('__init__'):
                    cesta_k_nalezenému_souboru = os.path.join(cesta_do_adresáře, jméno_nalezeného_souboru)
                    počet_nalezených_testů = počet_nalezených_testů + 1
                    yield cesta_k_nalezenému_souboru
    else:
        if os.path.isfile(cesta):
            if fnmatch.fnmatch(os.path.basename(cesta), MASKA_TESTOVACÍCH_SOUBORŮ):
                počet_nalezených_testů = počet_nalezených_testů + 1
                yield cesta
            else:
                raise IOError('Soubor testu "{}" neodpovídá masce {}'.format(cesta,  MASKA_TESTOVACÍCH_SOUBORŮ))
        else:
            raise IOError('Soubor testu "{}" nejestvuje'.format(cesta))
            
    if počet_nalezených_testů == 0:
        raise IOError('Nenašel jsem žádný testovací soubor v cestě "{}" za pomocí masky "{}"'.format(cesta,  MASKA_TESTOVACÍCH_SOUBORŮ))

