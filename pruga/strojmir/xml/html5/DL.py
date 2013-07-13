#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

from . import __ELEMENT_HTML5,  E

class DL(__ELEMENT_HTML5):
    
    def __call__(self,  dt,  dd):
        
        self << E.DT(dt) << E.DD(dd)
