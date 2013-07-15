#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

import os
import mimetypes



from . import Response,  Hlavičky
        

class chybová_stránka(Response):
    
    def __call__(self,  kód,  hláška = None):
        if hláška is None:
            hláška = HTTP_Status[kód]
        
        status = '{} {}'.format(kód,  hláška)
        return status,  Hlavičky(content_type = 'text/html')(),  self.html.render(status = status).encode('utf-8')

chybová_stránka = chybová_stránka(__file__)


def soubor(jméno_souboru):
    
    root_adresář = os.path.abspath('./static')
    print('root_adresář',  root_adresář)
    cesta_k_souboru = os.path.abspath(os.path.join(root_adresář, jméno_souboru.strip('/\\')))
#    py_soubor = '{}.py'.format(web_soubor)

    if not cesta_k_souboru.startswith(root_adresář):
        status = '403 Nepovolený přístup k souboru.'
        return html_šablona(status)()
        
    if not os.path.exists(cesta_k_souboru) or not os.path.isfile(cesta_k_souboru):
        status = '404 Soubor nejestvuje.'
        return html_šablona(status)()
        
    if not os.access(cesta_k_souboru, os.R_OK):
        status = '403 Nemáš oprávnění přistupovat k požadovanému souboru.'
        return html_šablona(status)()
        
    mimetype, encoding = mimetypes.guess_type(cesta_k_souboru)
    hlavičky = Hlavičky(content_type = mimetype,  encoding = encoding)
    print('mimetype',  mimetype)
    print('encoding',  encoding)
        
    with open(cesta_k_souboru,  mode='rb') as s:
        obsah = s.read()
        
    return HTTP_Status[200],  hlavičky(),  obsah

def download(jméno_souboru):
#    jako soubor výšeif download:
#        a pqak ještě
#    if download:
#        download = os.path.basename(filename if download == True else download)
#        headers['Content-Disposition'] = 'attachment; filename="%s"' % download
    pass
        
def volej(py_funkce,   **kwargs):
    if not callable(py_funkce):
        raise TypeError('Volati je možné pouze funkci, či funkční objekt a nikolivěk {}.'.format(type(py_funkce)))
    
    return HTTP_Status[200],  Hlavičky(content_type = 'text/html')(),  str(py_funkce(**kwargs)).encode('utf-8')


def html_šablona(status):
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
        nonlocal status
        if isinstance(status,  int):
            status = HTTP_Status[status]
        return status,  Hlavičky(content_type = 'text/html')(),  html.format(status).encode('utf-8')
        
    return davaj_html

html400 = html_šablona(400)
html404 = html_šablona(404)
html500 = html_šablona(500)
    

