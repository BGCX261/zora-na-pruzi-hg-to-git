#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

class SOUBOR(object):
    
    def __init__(self,  jméno_souboru):
        pass
        
    def __rshift__(self,  soubor):
        '''
        operátor ELEMENT >> soubor:řetězec umožní uložit xml do souboru
        '''
        if not isinstance(soubor,  (str, )):
            raise TypeError('Operátor >> elementu <{}> očekává jméno souboru.'.format(self.tag))
        
        print('uložím objekt {0} do souboru {1}'.format(self.__class__.__name__,  soubor))
          
        with open(soubor, 'w', encoding='utf-8') as zdrojový_soubor:
            zdrojový_soubor.write(self.hlavička_souboru(soubor))
            
            kód = str(self)
            zdrojový_soubor.write(kód)
            
            zdrojový_soubor.write(self.patička_souboru(soubor))
            return kód
            
        raise IOError('Selhalo zapsání elementu <{0} ... >...</{0}> do souboru {}'.format(self.tag,  soubor))

    def hlavička_souboru(self,  jméno_souboru):
        return ''
        
    def patička_souboru(self,  jméno_souboru):
        return ''
