#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

from collections import OrderedDict

class STYL(OrderedDict):
    
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
        
    def __rshift__(self,  soubor):
        '''
        operátor SOUBOR >> soubor:řetězec umožní uložit obsah do souboru
        '''
        if not isinstance(soubor,  (str, )):
            raise TypeError('Operátor >> očekává jméno souboru.'.format(self.tag))
        
        print('uložím objekt {0} do souboru {1}'.format(self.__class__.__name__,  soubor))
        
        with open(soubor,  mode ='w',  encoding = 'UTF-8') as otevřený_soubor:
#            otevřený_soubor.write(self.xml_hlavička)
            otevřený_soubor.write(str(self))
