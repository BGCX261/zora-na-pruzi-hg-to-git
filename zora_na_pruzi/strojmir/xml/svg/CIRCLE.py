#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je třída, která ...
'''
#import lxml.etree
from . import __ELEMENT_SVG,  NAMESPACE


class CIRCLE(__ELEMENT_SVG):
    
    TAG = '{{{}}}circle'.format(NAMESPACE)
    
 
