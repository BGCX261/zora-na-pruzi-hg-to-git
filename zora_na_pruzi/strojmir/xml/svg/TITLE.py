#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je třída, která ...
'''
#import lxml.etree
from . import __ELEMENT_SVG,  NAMESPACE


class TITLE(__ELEMENT_SVG):
#    pass
    
    TAG = '{{{}}}title'.format(NAMESPACE)
    
 
