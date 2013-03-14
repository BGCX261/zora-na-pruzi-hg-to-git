#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je třída, která přesměruje standartní výstup
'''

import sys

class DO_SOUBORU(object):
    
    '''
    přesměruje standartní výstup
    '''
    
    def __init__(self, jméno_souboru):
        if isinstance(jméno_souboru,  str):
            self.__jméno_souboru = jméno_souboru
            
    def __enter__(self):
        self.__původní_výstup = sys.stdout
        sys.stdout = open(self.__jméno_souboru,  mode ='w',  encoding = 'UTF-8')
        return sys.stdout
        
    def __exit__(self, *args):
        sys.stdout = self.__původní_výstup
