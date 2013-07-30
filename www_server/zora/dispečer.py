#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

#from django.core.urlresolvers import ResolverMatch
#from django.conf.urls import url as django_url,  include as django_include

#class Routa(object):
#    '''
#    nahrazuje django.core.urlresolvers.RegexURLPattern
#    '''
#    
#    def __init__(self,  regex,  callback,  default_args=None,  name = None):
#        self.regex = regex
#        self._callback = callback
#        self.default_args = default_args or {}
#        self.name = name
#    
#    def resolve(self, path):
#        match = self.regex.search(path)
#        if match:
#            # If there are any named groups, use those as kwargs, ignoring
#            # non-named groups. Otherwise, pass all non-named arguments as
#            # positional arguments.
#            kwargs = match.groupdict()
#            if kwargs:
#                args = ()
#            else:
#                args = match.groups()
#            # In both cases, pass any extra_kwargs as **kwargs.
#            kwargs.update(self.default_args)
#
#            return ResolverMatch(self._callback, args, kwargs, self.name)

from django.http import HttpResponse,  HttpResponseRedirect
 
def url(jméno_routy,  *args,  **kwargs):
    from django.core.urlresolvers import reverse
    
    url = reverse(jméno_routy,  None,  args,  kwargs,  None,  None)
    return url

#    url = 'url do {}'.format(str(kwargs))
#    return url

def url_souboru(cesta):
    from django.templatetags.static import static
    
    return static(cesta)
 
class POHLED(object):
    
    def __init__(self,  pohled):
        self._pohled = pohled
        
    def __call__(self,  request,  *args,  **kwargs):
        from zora.šablony import renderuj
        obsah = renderuj('{}.mako'.format(self._pohled),  *args,  request = request,  **kwargs)
        return HttpResponse(obsah)
 
class MODEL(POHLED):
    
    def __init__(self,  model,  pohled = None):
        super().__init__(pohled)
        self._model = model
      
    @property
    def model(self):
        if isinstance(self._model,  str):
            modul,  funkce = self._model.split(':')
            
            modul = __import__(modul,  globals(), locals(), [funkce])
            funkce = getattr(modul,  funkce)
            self._model = funkce
            
        return self._model
    
    def __call__(self,  request,  *args,  **kwargs):
            
        model_vrátil = self.model(*args,  **kwargs)
        
        if self._pohled is not None:
            return super().__call__(request,  *args,  model = model_vrátil,  **kwargs)
        return HttpResponse(model_vrátil)
 
 
class POST(MODEL):
    def __init__(self,  model,  redirect):
        self._model = model
        self._redirect = redirect
 
    def __call__(self,  request,  *args,  **kwargs):
        
        if not request.method == 'POST':
            raise TypeError('Enom POST sem patří')

        obsah = self.model(** request.POST)
        
        from django.contrib import messages
        messages.add_message(request, messages.INFO, obsah)
        
        return HttpResponseRedirect(url(self._redirect))
#        return HttpResponse(obsah)
        
class FLASH(POHLED):
 
    def __call__(self,  request,  *args,  **kwargs):
        
        if not request.method == 'GET':
            raise TypeError('Enom GET sem patří')

        from django.contrib import messages
        obsah = messages.get_messages(request)
        for message in obsah:
            print(message)
        print('MESSAGES',  obsah)
        
        return super().__call__(request,  *args,  model = obsah,  **kwargs)
        
#class reverse(dict):
#    def __call__(self,  klíč,  **kwargs):
#        django_regex = self.get(klíč,  None)
#        if django_regex is not None:
#            regex = django_regex.regex
#            pattern = regex.pattern
#            print(pattern)
#            print(regex.groups)
#            print(regex.groupindex)
#            očekává_parametry = regex.groupindex
#            
#    
#reverse = reverse()
#
#def url(regex, model,  pohled = None, kwargs=None, name=None, prefix=''):
#    #    '''
#    #    nahrazuje django.conf.urls.url
#    #    '''
##    print('-'*12,  regex,  model)
#    pohled = davaj_pohled(model,  pohled)
#    regex = django_url(regex, pohled, kwargs, name, prefix)
#    reverse[model] = regex
#    return regex
##    import re
##    pattern = re.compile(regex)
##    return Routa(pattern,  pohled,  kwargs,  name)
#
#def include(regex,  urls_modul):
#    #    '''
#    #    nahrazuje django.conf.urls.include
#    #    '''
#    
#    return django_url(regex, django_include(urls_modul))
