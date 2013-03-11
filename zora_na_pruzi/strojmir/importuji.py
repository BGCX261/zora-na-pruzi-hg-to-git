#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

def davaj_importéra(jméno_modulu):
    
    def importuji(jméno_objektu):
        modul = __import__(jméno_modulu, globals(), locals(), [jméno_objektu], 0)
        objekt = getattr(modul,  jméno_objektu)
            
        return objekt
        
    return importuji
