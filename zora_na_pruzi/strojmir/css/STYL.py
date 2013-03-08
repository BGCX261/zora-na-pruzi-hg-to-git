#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

from collections import OrderedDict
from zora_na_pruzi.strojmir.SOUBOR import SOUBOR

class STYL(OrderedDict,  SOUBOR):
    
#    def __init__(self,  soubor):
    
    def __str__(self):
        import io
        
        output_buffer = io.StringIO('')
        
        for selektor,  vlastnosti in self.items():
            print(selektor,  '{',  file=output_buffer)
        
            for vlastnost in vlastnosti:
                print('\t',  vlastnost,  file=output_buffer)
                
            print('}',  file=output_buffer)
            
        obsah = output_buffer.getvalue()
        output_buffer.close()
        return obsah
        
    def __setitem__(self, selektor, vlastnost):
        if selektor not in self:
            super().__setitem__(selektor,  [])
            
        self[selektor].append(vlastnost)
        
