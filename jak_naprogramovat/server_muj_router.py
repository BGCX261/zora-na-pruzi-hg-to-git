#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je server
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

import wsgiref
from wsgiref.util import setup_testing_defaults

from wsgiref.simple_server import make_server, demo_app

routing = (
           (1, 2, 3, 4, 5, 6), 
           ('a'), 
           ('a',  2,  3,  4,  5)
           )
           


# A relatively simple WSGI application. It's going to print out the
# environment dictionary after being updated by setup_testing_defaults
def simple_app(environ, start_response):
    setup_testing_defaults(environ)

    status = '200 OK'
#    headers = [('Content-type', 'text/plain; charset=utf-8')]
    headers = [('Content-type', 'text/html; charset=UTF-8'), 
#                        ('X-Powered-By', 'Зора на прузи')
                        ('X-Powered-By', 'Zora na pruzi')
                        ]
#    print('start_response',  start_response)
    start_response(status, headers)

    print('request_uri',  wsgiref.util.request_uri(environ))
    
    cesta = environ['PATH_INFO'] or ''
    print(cesta)
    
    cesta = cesta.strip('/').split('/')
    print(cesta,  len(cesta))
    
    for route in routing:
        if not len(cesta) == len(route):
            print('CONTINUE různé délky ',  len(cesta),  ' ',  len(route))
            continue
            
        print(zip(cesta,  route))
        for z in zip(cesta,  route):
            má_býti,  je = z
            print(má_býti,  je)
            if isintance(je,  str):
                if not má_býti == je:
                    print('BREAK nerovna se string ',  má_býti,  ' ',  je)
                    break
            if callable(je):
                if not je(má_být):
                    print('BREAK funkce vrací NE ',  je(má_být))
                    break
                    
            for typ in int,  float:
                if isintance(je,  typ):
                    má_býti = typ(má_býti)
                    if not má_býti == je:
                        print('BREAK nerovna se typem string ',  typ,  ' ',  má_býti,  ' ',  je)
                        break

    try:
        return obsah(environ)
    except (KeyboardInterrupt, SystemExit, MemoryError) as e:
        raise e
    except Exception as e:
        print(e)


def obsah(environ):
    yield '<h1>idzu na {}</h1>'.format(environ['PATH_INFO']).encode('utf-8')
    
    yield '<dl>'.encode('utf-8')
    for klíč,  hodnota in environ.items():
        yield '<dt>{}</dt><dd>{}</dd>'.format(klíč,  hodnota).encode('utf-8')
        
    yield '</dl>'.encode('utf-8')

if __name__ == '__main__':
    port = 8000
    httpd = make_server('', port, simple_app)
#    httpd = make_server('', 8000, demo_app)
    print("Spustil jsem server na portu {} ...".format(port))
    # Respond to requests until process is killed
    httpd.serve_forever()

    # Alternative: serve one request, then exit
#    httpd.handle_request()
