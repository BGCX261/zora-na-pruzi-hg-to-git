#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

import logging

logger = logging.getLogger(__name__)
debug = logger.debug
error = logger.error

from pruga.web.Response import Response

from pruga.web.Router import Router as router

router = router()

@router.append
def firma(request):
    '''
    '''
    cesta = request.cesta
    if len(cesta) == 3 and cesta[:2] == ['firma',  'ičo']:
        ičo = cesta[2]
        if not ičo == 'ičo':
            pass
        from zora.firma import najdi_firmu
        return Response().obsah(najdi_firmu,  ičo = ičo)
#        .pohled('Firma')

    
@router.append
def výchozí_router(request):
    '''
    '''
    cesta = request.cesta
    cesta.insert(0, 'zora')
    funkce = cesta.pop()
    
    balíček = '.'.join(cesta)
    
    try:
        modul = __import__(balíček, globals(), locals(), [funkce], 0)
        return Response().obsah(modul,  **request.parametry)
    except TypeError as e:
        error('Selhalo volání modulu {} a funkce {}. CHYBA: {}'.format(balíček,  funkce,  e))
        return Response().html400()
    except ImportError as e:
        error('V modulu {} nije funkce {}. CHYBA: {}'.format(balíček,  funkce,  e))
        return Response().html404()
#        .pohled('Firma')
    
    
if __name__ == '__main__':

    print(__doc__)

    import argparse
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser()

#   a pak mu nastavím jaké příkazy a parametry má přijímat
    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, {}'.format(__version__))
    
    parser.add_argument('cesta',  nargs='?',  default='')
    parser.add_argument('--logovací_úroveň',  default = logging.DEBUG,  choices=[logging.DEBUG, logging.INFO,  logging.WARNING,  logging.ERROR])
    
    #    a včíl to možu rozparsovat
    args = parser.parse_args()
    
    logging.basicConfig(level = args.logovací_úroveň)
    
    odsek = 24
    print('-'*odsek)
    print('routuji cestu "{}"'.format(args.cesta))
    print('-'*odsek)
    
    environ = {'PATH_INFO': args.cesta
                   
                   }
     
    from pruga.web.Request import Request
    request = Request(environ)
    for i,  response in enumerate(router.route(request)):
        print('\t{} {}'.format(i,  response))
        print('\t', '.'*odsek, sep='')
        
        if response is not None:
        
            print('\t', '.'*odsek, sep='')
            for řádek in response():
                řádek = řádek.decode('utf-8').replace('\n', '\n\t')
                print('\t{}'.format(řádek))
            print('\t', '.'*odsek,  sep='')
