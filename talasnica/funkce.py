#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

def PŘESNOST_CENY(cena):
    return round(cena,  2)
    
def PŘESNOST_LOTU(velikost):
    return round(velikost,  2)
    
def PŘESNOST_PŘEPOČTU_PROFITU(velikost):
    return round(velikost,  4)

def max_nákupu(první_cena,  druhá_cena):
    if první_cena.nákup > druhá_cena.nákup:
        return první_cena
    return druhá_cena
        
def min_prodeje(první_cena,  druhá_cena):
    if první_cena.prodej == 0:
        return druhá_cena
        
    if druhá_cena.prodej == 0:
        return první_cena
    
    if první_cena.prodej < druhá_cena.prodej:
        return první_cena
    return druhá_cena
    
def zaokrouhlím_cenu(cena,  rozestup):
    
    return cena // rozestup * rozestup
