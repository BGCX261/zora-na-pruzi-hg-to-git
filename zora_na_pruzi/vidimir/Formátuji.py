#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''
#from zora_na_pruzi import vidimir as MODUL_VIDŮ

from zora_na_pruzi.strojmir.importuji import davaj_importéra

class DAVAJ_FORMÁT(dict):
    
    
    def __init__(self,  balíček):
        self.najdu_třídu = davaj_importéra(balíček)
    
    def __getattr__(self,  jméno_formátu):
        from .stroj.Formát import Formát
        formátovací_funkce = self[jméno_formátu]
        return Formát(formátovací_funkce)
        
    def __missing__(self,  jméno_formátu):
        TŘÍDA = self.najdu_třídu(jméno_formátu)
        self[jméno_formátu] = TŘÍDA
#        if not callable(TŘÍDA):
#            TŘÍDA = getattr(TŘÍDA,  jméno_formátu)
        return self[jméno_formátu]

TEXT = DAVAJ_FORMÁT(balíček = 'zora_na_pruzi.vidimir.formáty.barevná_konzole')
HTML = DAVAJ_FORMÁT(balíček = 'zora_na_pruzi.vidimir.formáty.html')
