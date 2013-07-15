#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

from . import __ELEMENT_HTML5,  E

class TABLE(__ELEMENT_HTML5):
    
    def nový_řádek(self, sloupce,  *další_sloupce,  buňka = None):
        if not isinstance(sloupce,  list):
            sloupce = list(sloupce)
            
        if buňka is None:
            buňka = E.TD
            
        sloupce.extend(další_sloupce)
        
        tr = E.TR()
        
        for sloupec in sloupce:
            td = buňka()
            td.text = str(sloupec)
            tr.append(td)
            
        return tr
    
    def přidej_řádek(self,  sloupce,  *další_sloupce):
        tr = self.nový_řádek(sloupce,  *další_sloupce,  buňka = E.TD)
        self.append(tr)

    def přidej_záhlaví(self,  sloupce,  *další_sloupce):
        tr = self.nový_řádek(sloupce,  *další_sloupce,  buňka = E.TH)
        self.insert(0, tr)
