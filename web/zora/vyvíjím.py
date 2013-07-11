#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

import os
import django

def urlpatterns(cesta):
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
            
        

def app(cesta):
    from zora.wsgi import application
    
    import io
    environ = {'PATH_INFO': cesta, 
                   'REQUEST_METHOD': 'GET', 
                   'wsgi.input': io.BufferedReader(open('wsgi.input'))
                   }
                   
    application(environ,  print)
#    print(x)

if __name__ == '__main__':

    print(__doc__)
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zora.settings")

    import argparse
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser()

#   a pak mu nastavím jaké příkazy a parametry má přijímat
    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, {}'.format(__version__))
    
    parser.add_argument('cesta')
    
    #    a včíl to možu rozparsovat
    args = parser.parse_args()
    
    odsek = 24
    print('-'*odsek)
    print('routuji cestu "{}"'.format(args.cesta))
    print('-'*odsek)

    urlpatterns(args.cesta)
#    app(args.cesta)
