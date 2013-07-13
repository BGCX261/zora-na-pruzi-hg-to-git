#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je server
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

import os
import mimetypes
import logging

logger = logging.getLogger(__name__)
debug = logger.debug
error = logger.error

#import wsgiref
from wsgiref.util import setup_testing_defaults

from wsgiref.simple_server import make_server

from pruga.web.Request import Request
#import router

from pruga.web.response.chybová_stránka import chybová_stránka
from pruga.web.HTTP_Status import HTTP_Status

ADRESÁŘ_APLIKACE =  os.path.abspath(os.path.join(os.path.dirname(__file__), './aplikace')) 
PŘÍPONY_SOUBORŮ = '.js',  '.html',  '.css',  '.html5'

# A relatively simple WSGI application. It's going to print out the
# environment dictionary after being updated by setup_testing_defaults
def app(environ, start_response):
    setup_testing_defaults(environ)
    
    request = Request(environ)
    cesta = request.cesta
    
    if len(cesta) == 0 or (len(cesta) == 1 and not cesta[0]):
        cesta = ['index.html']
    
    cesta_k_souboru = os.path.abspath(os.path.join(ADRESÁŘ_APLIKACE, os.path.join(*cesta)))
    
    _,  přípona = os.path.splitext(cesta_k_souboru)
    
    if přípona in PŘÍPONY_SOUBORŮ:
        print('želim soubor {}'.format(cesta_k_souboru))
        status,  hlavičky,  obsah =  __davaj_soubor(cesta_k_souboru)
    else:
        print('želim da spustim modul {}'.format(cesta_k_souboru))
        status,  hlavičky,  obsah =  __spustím_modul(request)
    
    start_response(status,  hlavičky)
    yield obsah
        

def __davaj_soubor(cesta_k_souboru):
    if not cesta_k_souboru.startswith(ADRESÁŘ_APLIKACE):
        error('Požadován soubor  {}, kopji je mimo aplikační adresář'.format(cesta_k_souboru))
        return chybová_stránka(403,  'Nepovolený přístup k souboru.')
        
    if os.path.isfile(cesta_k_souboru):

        try:
            with open(cesta_k_souboru,  mode='rb') as s:
                obsah = s.read()
               
            mimetype, encoding = mimetypes.guess_type(cesta_k_souboru)
            hlavičky = response.Hlavičky(content_type = mimetype,  encoding = encoding)
            print('mimetype',  mimetype)
            print('encoding',  encoding)
            return HTTP_Status[200],  hlavičky(),  obsah
        except IOError:
            error('neoprávněný přístup k souboru {}'.format(cesta_k_souboru))
            return chybová_stránka(403,  'Nemáš oprávnění přistupovat k požadovanému souboru.')
      
    error('Požadován nejestvujicí soubor {}'.format(cesta_k_souboru))
    return chybová_stránka(404,  'Soubor nejestvuje.')

def __spustím_modul(request):
    
    cesta = request.cesta
    cesta.insert(0, 'zora')
    
    parametry = []
    
    def davaj_funkci(cesta):
#        funkce = cesta.pop()
        funkce = cesta[-1]
        balíček = '.'.join(cesta)
        print('Hledám funkci {} balíčku {}'.format(funkce,  balíček))
        
        try:
            modul = __import__(balíček, globals(), locals(), [funkce], 0)
            print(modul,  modul.__name__)
            funkce = getattr(modul,  cesta[-1])
            print(funkce)
            return funkce
        except ImportError:
            parametry.insert(0, cesta.pop())
            return davaj_funkci(cesta)
        

    funkce = davaj_funkci(cesta)
    return funkce()
#    return funkce(request,  *parametry)
   
if __name__ == '__main__':
    
    print(__doc__)

    import argparse
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser()

#   a pak mu nastavím jaké příkazy a parametry má přijímat
    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, {}'.format(__version__))
    
    parser.add_argument('port',  nargs='?',  default=8080)
    parser.add_argument('--logovací_úroveň',  default = logging.DEBUG,  choices=[logging.DEBUG, logging.INFO,  logging.WARNING,  logging.ERROR])
    
    #    a včíl to možu rozparsovat
    args = parser.parse_args()
    
    
    logging.basicConfig(level = args.logovací_úroveň)
    
    httpd = make_server('', args.port, app)
#    httpd = make_server('', 8000, demo_app)
    print("Spustil jsem server na portu {} ...".format(args.port))
    print("adresář aplikace {} ...".format(ADRESÁŘ_APLIKACE))
    # Respond to requests until process is killed
    httpd.serve_forever()

    # Alternative: serve one request, then exit
#    httpd.handle_request()
