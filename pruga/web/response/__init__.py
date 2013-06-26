import os

from pruga.web.HTTP_Status import HTTP_Status

class HTML(object):
    
    def __get__(self,  instance,  owner):
       
        cesta = '{}.{}'.format(os.path.splitext(instance._cesta)[0],  'mako')
        from mako.template import Template

        mytemplate = Template(filename=cesta, module_directory='/tmp/mako_modules',  input_encoding = 'utf-8')
        return mytemplate

class Response(object):
    html = HTML()
    
    def __init__(self,  cesta):
        self._cesta = cesta
        
    def __call__(self, **kwargs):
        return HTTP_Status[200],  Hlavičky(content_type = 'text/html')(),  self.html.render(**kwargs).encode('utf-8')
        
class Hlavičky(dict):
    
    def __init__(self, content_type = None,  encoding = None):
        self['content_type'] = content_type or 'text/html'
        self['encoding'] = encoding or 'utf-8'
        
        
    def __call__(self):
        headers = [('Content-type', '{}; charset={}'.format(self['content_type'],  self['encoding'])), 
#                        ('X-Powered-By', 'Зора на прузи'.encode('utf-8').decode('latin-1')), 
                        ('X-Powered-By', 'Zora na pruzi')
                        ]
        for klíč,  hodnota in self.items():
            if klíč not in ('content_type',  'encoding'):
                headers[klíč] = hodnota
        return headers
