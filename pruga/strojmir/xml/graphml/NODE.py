#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

from .__PRVEK_GRAFU import __PRVEK_GRAFU,  E

class NODE(__PRVEK_GRAFU):
    
    @property
    def graf(self):
        '''
        vrátí vložený graf, jestvuje-li
        '''
        return self.find(E.GRAPH.TAG)
