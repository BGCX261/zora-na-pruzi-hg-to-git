#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

import sys
import regex as re
sys.modules['re'] = re

import os
import django

def routuj(cesta):
    '''
    spouštím funkci main()
    '''
    
    from zora.urls import urlpatterns
#    print(urlpatterns)
    
    for url in urlpatterns:
        try:
            naparsováno = url.resolve(cesta)
            print('>> ',  url.regex.pattern)
            print('\t',  naparsováno)
        except django.core.urlresolvers.Resolver404 as e:
            print('ERROR Resolver404',  url.regex.pattern,  e)
            
        

def aplikaci(cesta):
    from zora.wsgi import application
    
    import io
    environ = {'PATH_INFO': cesta, 
                   'REQUEST_METHOD': 'GET', 
                   'wsgi.input': io.BufferedReader(open('wsgi.input')), 
                   'SERVER_NAME': 'localhost', 
                   'SERVER_PORT':8000
                   }
                   
    výstup = application(environ,  print)
    print(výstup)

if __name__ == '__main__':

    print(__doc__)
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zora.settings")

    import argparse
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser()

#   a pak mu nastavím jaké příkazy a parametry má přijímat
    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, {}'.format(__version__))
    
    
    seznam_funkcí = {jméno: funkce for jméno,  funkce in locals().items()  if not jméno.startswith('__') and callable(funkce) }
    
    print(seznam_funkcí)
    
    parser.add_argument('příkaz',  choices= seznam_funkcí.keys())
    parser.add_argument('cesta')
    
    #    a včíl to možu rozparsovat
    args = parser.parse_args()
    
    spustím = seznam_funkcí[args.příkaz]
    
    odsek = 24
    print('-'*odsek)
    print('routuji cestu "{}"'.format(args.cesta))
    print('-'*odsek)

    spustím(args.cesta)
