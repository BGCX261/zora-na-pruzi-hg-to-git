#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je server
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

import logging

logger = logging.getLogger(__name__)
debug = logger.debug
error = logger.error

import wsgiref
from wsgiref.util import setup_testing_defaults

from wsgiref.simple_server import make_server

from pruga.web.Request import Request
from router import router

# A relatively simple WSGI application. It's going to print out the
# environment dictionary after being updated by setup_testing_defaults
def app(environ, start_response):
    setup_testing_defaults(environ)
    
    request = Request(environ)
    
    for odpověď in router.route(request):
        
        if odpověď is not None:
            status,  hlavičky,  obsah = odpověď
            break
    else:
        from pruga.web.response import html404
        status,  hlavičky,  obsah = html404()
        
    start_response(status,  hlavičky)
    yield obsah
        

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
    # Respond to requests until process is killed
    httpd.serve_forever()

    # Alternative: serve one request, then exit
#    httpd.handle_request()
