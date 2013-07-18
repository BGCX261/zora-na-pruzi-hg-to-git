#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

#from django.core.urlresolvers import ResolverMatch
from django.conf.urls import url as django_url,  include as django_include

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

from django.http import HttpResponse 
 
def davaj_pohled(model,  pohled = None):
    
    def view(request,  **kwargs):
        nonlocal  model
        
        if isinstance(model,  str):
            model,  funkce = model.split(':')
            
            model = __import__(model,  globals(), locals(), [funkce])
            model = getattr(model,  funkce)
             
        model = model(**kwargs)
        
        from zora.šablony import renderuj
        obsah = renderuj('{}.mako'.format(pohled),  model = model,  request = request)
        return HttpResponse(obsah)
        
    return view

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
