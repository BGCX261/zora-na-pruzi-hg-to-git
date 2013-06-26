#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'


from pruga.web.response import Response

#from pruga.web import 

def najdi_firmu(ičo):
    '''
    spouštím funkci main()
    '''
    return 'Firma ičo {}'.format(ičo)
    
    
firma = Response(__file__)
