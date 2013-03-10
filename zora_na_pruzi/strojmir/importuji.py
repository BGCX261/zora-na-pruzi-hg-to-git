#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

def davaj_importéra(jméno_balíčku):
    
    def najdu_třídu(jméno_třídy):
        balíček = __import__(jméno_balíčku, globals(), locals(), [jméno_třídy], 0)
        třída = getattr(balíček,  jméno_třídy)
            
        return třída
        
    return najdu_třídu
