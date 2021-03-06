#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

from collections import OrderedDict

class CSS_TABULKA(OrderedDict):
    
    __soubor = None
#    def __init__(self,  soubor):
    
    def __str__(self):
        import io
        
        output_buffer = io.StringIO('')
        
        for selektor,  vlastnosti in self.items():
            print(selektor,  '{',  file=output_buffer)
        
            for vlastnost,  hodnota in vlastnosti.items():
                print('\t{}: {};'.format(vlastnost,  hodnota),  file=output_buffer)
                
            print('}',  file=output_buffer)
            
        obsah = output_buffer.getvalue()
        output_buffer.close()
        return obsah
        
    def __setitem__(self, selektor, vlastnosti):
        if selektor in self:
            print('přepisuji nastavení CSS pro {}'.format(selektor))
            print('původní')
            print(self[selektor])
            print('nové')
            print(vlastnosti)
         
        if not isinstance(vlastnosti,  (dict,  )):
            raise TypeError('Vlastnosti musí být slovníkem a nikolivěk {}'.format(type(vlastnosti)))
            
        super().__setitem__(selektor, vlastnosti)
     
    def get(self,  selektor,  default = None):
        if default is None:
            from zora_na_pruzi.strojmir.css.vlastnosti import VLASTNOSTI
            default = VLASTNOSTI()
        return self.setdefault(selektor,  default)
        
  
    def __rshift__(self,  soubor):
        '''
        operátor SOUBOR >> soubor:řetězec umožní uložit obsah do souboru
        '''
        if not isinstance(soubor,  (str, )):
            raise TypeError('Operátor >> očekává jméno souboru.'.format(self.tag))
        
        print('uložím kaskádové styly z objektu {0} do souboru {1}'.format(self.__class__.__name__,  soubor))
        
        with open(soubor,  mode ='w',  encoding = 'UTF-8') as otevřený_soubor:
#            otevřený_soubor.write(self.xml_hlavička)
            otevřený_soubor.write(str(self))
            
        self.__soubor = soubor
        
    @property
    def soubor(self):
        return self.__soubor
