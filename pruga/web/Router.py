#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

    
class Router(list):
    '''
    Tato funkce se používá jako dekorátor
    
    Router pracuje takto:
    na webu si vytvořím soubor router.py
    v něm bude:
    
    from pruga.web.Router import Router as router
    router = router()
    
    a pak routy udělám z funkcí pomocí dekorátoru
    
    @router.append
    def routuji_tam_a_tam(request):
    
    '''
    def append(self,  funkce):
        super().append(funkce)
        return funkce
        
    def route(self,  request):
        for routovací_funkce in self:
            yield routovací_funkce(request)

