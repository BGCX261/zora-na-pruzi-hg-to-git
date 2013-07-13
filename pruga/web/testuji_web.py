#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

import py.test
#import os

#from .html5 import E
#from .html5.HTML import HTML

from pruga.web.Request import Request
#from pruga.web.response import *

from pruga.web.Router import Router as router

router = router()

environ = {'PATH_INFO': '/toto/je/testovací/url/s/číslem/25'
                   
                   }
     



def test_0001_request():
    request = Request(environ)
    
    assert request.cesta == environ['PATH_INFO'].strip('/').split('/')

def test_0002_router():
    
    @router.append
    def první_routa(request):
        pass
        
    assert router[0] == první_routa
    
    

    
    
