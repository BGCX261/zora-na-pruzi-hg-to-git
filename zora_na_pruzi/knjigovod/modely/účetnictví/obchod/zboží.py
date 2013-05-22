#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je definován uzel, který reprezentuje zboží
'''

from bulbs.model import Node,  Relationship
from bulbs.property import String, Integer, DateTime,  Float

print('*'*145,  'toto je zatím nepoužívané, možná to úplně zruším')

#class Nabízené_zboží(Node):
#    '''
#    zboží, či služba, cokoliv co firma nabízí a prodává
#    má vždy jedinou vstupní hranu, která vyjadřuje, která firma zboží vlastní, tedy nabízí
#    je to tato hrana 
#    class Firma_nabízí(Relationship):
#        label = 'firma_nabízí'
#    '''
#    element_type = "nabízené_zboží"
#    
#    název = String(nullable = False)
#    
#class Obchodované_zboží(Node):
#    '''
#    zboží, které je právě předmětem prodeje
#    má vždy jedinou vstupní hranu, která vyjadřuje, o jaké zboží se jedná
#    a dvě výstupní hrany, které vyjadřují
#    - zaučtování jako položka faktury
#    - 
#    '''
#    element_type = "obchodované_zboží"
#    
#
#
#class Zboží_bylo_objednáno(Relationship):
#    '''
#    Nabízené_zboží -> Obchodované_zboží
#    '''
#    label = 'zboží_bylo_objednáno'
#
#    
#

    
#class Zboží_se_předalo(Relationship):
#    '''
#    Zboží -> Zboží (či jinam)
#    vyjadřuje, přesun zboží, buď jinému vlastníkovi,
#    nebo někam jinam
#    '''
#    label = 'zboží_se_předalo'
#    
#    zahájení_prodeje = DateTime(nullable=True,  default = None)
#    ukončení_prodeje = DateTime(nullable=True,  default = None)
#    
##    datum_vydání = DateTime(nullable=True)
##    datum_dodeje = DateTime(nullable=True)
#    
#    
    
    
    
