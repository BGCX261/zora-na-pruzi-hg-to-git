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
    
    def __init__(self,  debug = None):
         
        import logging
        logger = logging.getLogger(__name__)
        self.__debug = logger.debug
#        error = logger.error
    
    def append(self,  funkce):
        if self.__debug:
            debug = self.__debug
            import functools
            @functools.wraps(funkce)
            def wrapper(request):
                debug('IDU DA ROUTUJI {}'.format(funkce.__name__))
                debug('cesta: {}'.format(request.cesta) )
                result = funkce(request)
                if result is None:
                    debug('NEPROŠLO')
                else:
                    debug('PROŠLO, STATUS {}'.format(result[0]))
                return result
            super().append(wrapper)
            return wrapper
        
        super().append(funkce)
        return funkce
        
    def route(self,  request):
        for routovací_funkce in self:
            yield routovací_funkce(request)

