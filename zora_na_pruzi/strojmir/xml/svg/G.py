#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je třída, která ...
'''
#import lxml.etree
from . import __ELEMENT_SVG,  E


class G(__ELEMENT_SVG):
    
    def kružnice(self,  střed,  poloměr):
        circle = E.CIRCLE(cx = str(střed[0]),  cy = str(střed[1]),  r = str(poloměr))
        self._ELEMENT.append(circle._ELEMENT)
        return circle
    
 
