#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

from .__PRVEK_GRAFU import __PRVEK_GRAFU,  E

class GRAPH(__PRVEK_GRAFU):
    
    @property
    def uzly(self):
        for uzel in self.findall(E.NODE.TAG_NAME):
            yield uzel
            
    @property
    def vazby(self):
        for vazba in self.findall(E.EDGE.TAG_NAME):
            yield vazba
    
