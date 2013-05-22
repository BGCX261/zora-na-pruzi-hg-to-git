#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je definován uzel, který reprezentuje firmu
'''

from pruga1.grafomir.databáze.bulbs.model import Node,  Relationship
from pruga1.grafomir.databáze.bulbs.property import String, Integer, DateTime

class Firma(Node):
    '''
    firmy, dodavatelé, čo odběratelé, zkrátka účastníci obchodních vztahů
    '''
    element_type = "firma"
    
    ičo = String(unique = True,  nullable = False)
    dič = String(unique = True,  nullable = True)
    jméno = String(nullable = False)
    adresa = String(nullable = False)

class Firma_vystavila_fakturu(Relationship):
    '''
    Firma -> Faktura
    '''
    label = 'firma_vystavila_fakturu'

    
#class Firma_nabízí(Relationship):
#    '''
#    Firma -> Zboží
#    vyjadřuje, co firma prodává, či nabízí
#    je to vlastně jakoby položka ceníku
#    a výběr všech hran je vlastně ceník, kompletní nabídka
#    '''
#    label = 'firma_nabízí'
#    
#    zahájení_prodeje = DateTime(nullable=True,  default = None)
#    ukončení_prodeje = DateTime(nullable=True,  default = None)
#    
    
    
