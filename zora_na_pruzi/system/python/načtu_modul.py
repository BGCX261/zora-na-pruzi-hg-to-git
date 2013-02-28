#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
hen dynamicky načítám moduly
'''

import imp
import os


def davaj_jméno_balíčku(jméno_modulu):
    cesta = jméno_modulu.split('.')
    return '.'.join(cesta[:-1])

def načtu_modul(jméno_modulu,  jméno_balíčku,  adresář_modulu):
    
    '''
    Načte modul "jméno_modulu", který je někde v balíčku "pod_modulem"
    '''
    celé_jméno_modulu = '.'.join((jméno_balíčku, jméno_modulu))
    try:
        file, pathname, description = imp.find_module(jméno_modulu,  [adresář_modulu,  ])
        modul = imp.load_module(celé_jméno_modulu,  file, pathname, description)
        return modul
    except ImportError as e:
        raise ImportError('Chybí modul {} v adresáři {}: {}'.format(jméno_modulu,  adresář_modulu,  e))

def načtu_modul_podle_balíčku(jméno_modulu,  podle_balíčku):
    
    '''
    Načte modul "jméno_modulu", který je ve stejném balíčku jako modul "podle_modulu"
    '''
    adresář_modulu = os.path.dirname(podle_balíčku.__file__)
    return načtu_modul(jméno_modulu = jméno_modulu,  adresář_modulu = adresář_modulu,  jméno_balíčku = podle_balíčku.__name__)

#def načtu_modul_podle_balíčku(jméno_modulu,  podle_modulu):
#    '''
#    Načte modul "jméno_modulu", který je ve stejném balíčku jako modul "podle_modulu"
#    '''
#    adresář_modulu = os.path.dirname(podle_modulu.__file__)
#    return načtu_modul(jméno_modulu = jméno_modulu,  adresář_modulu = adresář_modulu,  jméno_balíčku = davaj_jméno_balíčku(podle_modulu.__name__))


def načtu_modul_podle_třídy(jméno_modulu,  podle_třídy,  v_adresáři):
    '''
    Načte modul "jméno_modulu", který je někde v balíčku jako třída "podle_třídy"
    '''
    adresář_modulu = os.path.dirname(v_adresáři)
    return načtu_modul(jméno_modulu = jméno_modulu,  adresář_modulu = adresář_modulu,  jméno_balíčku = davaj_jméno_balíčku(podle_třídy.__module__))
    
