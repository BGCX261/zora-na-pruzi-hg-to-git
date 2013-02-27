#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

from .najdu_testovací_soubory import najdu_testovací_soubory

def davaj_styl(styl = None):
    
    if styl is not None:
        davaj_styl.styl = styl
        
    return davaj_styl.styl
