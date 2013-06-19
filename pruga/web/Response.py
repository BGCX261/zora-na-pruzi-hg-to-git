#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

from pruga.web.HTTP_Status import HTTP_Status

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
        return html.format(chyba)
    
    return davaj_html

class Response(object):
    
    __encoding = 'UTF-8'
    __content_type = 'text/html'
    __status = 200
    __obsah = html_šablona('500: Nebyl určen obsah stránky')
    __argumenty = {}
    
    def __init__(self):
        pass
       
    def obsah(self,  obsah,   **kwargs):
        if not callable(obsah):
            raise TypeError('Obsah objektu Response musí da je funkcí, či funkčním objektem a nikolivěk {}.'.format(type(obsah)))
        self.__obsah = obsah
        self.__argumenty = kwargs
        return self
        
    def html400(self):
        self.__status = 400
        self.__obsah = html_šablona(self.status)
        self.__argumenty = {}
        return self
        
    def html404(self):
        self.__status = 404
        self.__obsah = html_šablona(self.status)
        self.__argumenty = {}
        return self
        
    def html500(self,  exception = None):
        print(exception)
        self.__status = 500
        self.__obsah = html_šablona(self.status)
        self.__argumenty = {}
        return self
       
    def __call__(self):
        yield str(self.__obsah(**self.__argumenty)).encode(self.__encoding)
        
        
    @property
    def status(self):
        return HTTP_Status[self.__status]
        
    @property
    def content_type(self):
        return self.__content_type
        
    @property
    def encoding(self):
        return self.__encoding
        
    @property
    def headers(self):
        headers = [('Content-type', '{}; charset={}'.format(self.content_type,  self.encoding)), 
#                        ('X-Powered-By', 'Зора на прузи')
                        ('X-Powered-By', 'Zora na pruzi')
                        ]
        return headers
        
        
    
