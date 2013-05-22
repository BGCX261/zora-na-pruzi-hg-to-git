#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je definován uzel, který reprezentuje zboží
'''

from pruga.grafomir.databáze.bulbs.model import Node,  Relationship
from pruga.grafomir.databáze.bulbs.property import String, Integer, DateTime,  Float,  Integer

class Faktura(Node):
    '''
    
    '''
    element_type = "faktura"
    
    číslo_faktury = String(nullable = False)

    datum_vystavení = DateTime(nullable=False)
    datum_splatnosti = DateTime(nullable=False)
    datum_zdanitelného_plnění = DateTime(nullable=True)
#    @TODO: Tohle používá flexibee,  uvidíme či to k něčemu je, zatím neimplementuji
#    datum_zdanitelného_plnění_účto = DateTime(nullable=False)
    
class Položka_faktury(Node):

    element_type = "položka_faktury"
    
    název = String(nullable = False)
    popis = String(nullable = True)
    
    množství = Float(nullable = False)
    jednotka = String(nullable = False)
    jednotková_cena = Float(nullable = False)
    sazba_dph = Float(nullable = False)
    celková_cena = Float(nullable = False)
    základ_dph = Float(nullable = False)
    dph = Float(nullable = False)
    
class Položka_přidána_do_faktury(Relationship):
    '''
    Položka_faktury -> Faktura
    '''
    label = 'položka_přidána_do_faktury'
    
    pořadí = Integer(nullable = False)
