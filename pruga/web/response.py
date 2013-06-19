#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

from pruga.web.HTTP_Status import HTTP_Status

def hlavičky(content_type = 'text/html',  encoding = 'utf-8'):
        headers = [('Content-type', '{}; charset={}'.format(content_type,  encoding)), 
#                        ('X-Powered-By', 'Зора на прузи')
                        ('X-Powered-By', 'Zora na pruzi')
                        ]
        return headers

def volej(py_funkce,   **kwargs):
    if not callable(py_funkce):
        raise TypeError('Volati je možné pouze funkci, či funkční objekt a nikolivěk {}.'.format(type(py_funkce)))
    
    return HTTP_Status[200],  hlavičky(content_type = 'text/html'),  str(py_funkce(**kwargs)).encode('utf-8')


def html_šablona(chyba):
    html = '''
<!DOCTYPE html>
<html lang="cz">
    <head>
        <meta charset="utf-8">
        <title>Зора на прузи</title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    </head>
    <body>
        <header class="ui-widget-header ui-corner-all"><h1>CHYBA</h1></header>
        
        
        <div class="error">{}</div>
        
        
        <footer class="ui-widget-header ui-corner-all">Изготовила Зора на прузи<small id="copyright">©Домоглед, Петр Болф 2012-2013</small></footer>
    </body>
</html>
    '''
    
    def davaj_html(**kwargs):
        status = HTTP_Status[chyba]
        return HTTP_Status[chyba],  hlavičky(content_type = 'text/html'),  html.format(status).encode('utf-8')
        
    return davaj_html

html400 = html_šablona(400)
html404 = html_šablona(404)
html500 = html_šablona(500)
    

