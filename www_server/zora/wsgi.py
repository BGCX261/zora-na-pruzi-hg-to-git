"""
WSGI config for zora project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zora.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

#def application(environ,  start_response):
#    
##    setup_testing_defaults(environ)
#
#    status = '200 OK'
##    headers = [('Content-type', 'text/plain; charset=utf-8')]
#    headers = [('Content-type', 'text/html; charset=UTF-8'), 
##                        ('X-Powered-By', 'Зора на прузи')
#                        ('X-Powered-By', 'Zora na pruzi')
#                        ]
##    print('start_response',  start_response)
#    start_response(status, headers)
#
##    print('{0[REQUEST_METHOD]} {0[wsgi.url_scheme]}/{0[HTTP_HOST]}/{0[PATH_INFO]}'.format(environ))
##    print('application_uri',  wsgiref.util.application_uri(environ))
##    print('request_uri',  wsgiref.util.request_uri(environ))
#
##    input = environ['wsgi.input']
##    print(dir(input))
##    print(input.__class__)
#
#    try:
#        return obsah(environ)
#    except (KeyboardInterrupt, SystemExit, MemoryError) as e:
#        raise e
#    except Exception as e:
#        print(e)
#
#
#def obsah(environ):
#    yield '<h1>idzu na {}</h1>'.format(environ['PATH_INFO']).encode('utf-8')
#    
#    yield '<dl>'.encode('utf-8')
#    for klíč,  hodnota in environ.items():
#        yield '<dt>{}</dt><dd>{}</dd>'.format(klíč,  hodnota).encode('utf-8')
#        
#    yield '</dl>'.encode('utf-8')
