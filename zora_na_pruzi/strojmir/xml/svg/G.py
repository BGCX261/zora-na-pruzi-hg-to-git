#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je třída, která ...
'''
#import lxml.etree
from . import __ELEMENT_SVG,  NAMESPACE


class G(__ELEMENT_SVG):
    
    TAG = '{{{}}}g'.format(NAMESPACE)
    
    def kružnice(self,  střed,  poloměr):
        circle = self.E.circle(cx = střed[0],  cy = střed[1],  r = poloměr)
        self.append(circle)
        return circle
    
 
