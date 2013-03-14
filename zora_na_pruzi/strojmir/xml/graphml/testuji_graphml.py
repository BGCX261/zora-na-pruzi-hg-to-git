#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

import py.test
import os

#from zora_na_pruzi.vidimir import F

VZOROVÝ_GRAF = os.path.join(os.path.dirname(__file__),  './testuji_vzorový_graf.graphml')

import lxml.etree
from . import E

def parsuji_graf(soubor = VZOROVÝ_GRAF):
    
#    import lxml.etree
    
    graf = E << soubor
    
    return graf

def test_0001_namespace ():
    from . import NAMESPACE,  E
    
    assert E.GRAPH.TAG_NAME == '{{{}}}graph'.format(NAMESPACE)
    assert E.NODE.TAG_NAME == '{{{}}}node'.format(NAMESPACE)

def test_0002_načtu_graphml_soubor ():
    '''
    testuji
    '''
    
    with py.test.raises(IOError):
        parsuji_graf('nejestvující_soubor')
    
    root = parsuji_graf()
    
    assert isinstance(root,  lxml.etree._Element) 
    
    uzly = list(root.uzly)
    assert len(uzly) == 14
    
    vazby = list(root.vazby)
    assert len(vazby) == 12
    
    uzel = uzly[0]
    
    data = uzel.data
    assert len(data) == 1
    
    údaj = data[0]
    
    assert údaj.jméno == 'jméno'
    assert údaj.datový_typ == 'string'
    assert údaj.default is None
    
    assert údaj.klíč == root.klíče['d2']
    assert id(údaj.klíč) == id(root.klíče['d2'])
    
#    druhý graf 
    graphml_soubor = './testuji_vzorový_graf_2.graphml'
    cesta_k_graphml_souboru = os.path.join(os.path.dirname(__file__),  graphml_soubor)
    root2 = parsuji_graf(cesta_k_graphml_souboru)
    uzly = list(root2.uzly)
    uzel = uzly[0]
    data = uzel.data
    
    údaj = data[0]
    assert údaj.jméno == 'jiné jméno' 
    
def test_0003_klíče ():
        
    root = parsuji_graf()
    
    klíče = root.klíče
    from .seznam_klíčů import Seznam_klíčů
    assert isinstance(klíče,  Seznam_klíčů)
    
    with py.test.raises(KeyError):
        klíče['nejestvující klíč']
        
    assert isinstance(klíče['d1'],  E.KEY)

def test_0004_grafy():
    
    root = parsuji_graf()
    graf = root.graf
    
    from .GRAPH import GRAPH
    assert isinstance(graf,  GRAPH)
    
    uzly_grafu = list(graf.uzly)
    uzly_graphml = list(root.uzly)
    
    assert len(uzly_grafu) == 7
    součet_uzlů = 0
    for graf in root.grafy:
        uzly = list(graf.uzly)
        součet_uzlů = součet_uzlů + len(uzly)
        
    assert součet_uzlů == len(uzly_graphml)
    
#def test_0005_atributy():
#    
#    from .graphml_elementy import ATRIBUT
#    
#    id = ATRIBUT('id')
#    
#    assert str(id) == '[@id]'
#    
#    assert 'node' + id == 'node[@id]'
#    assert 'node' + ATRIBUT('id',  'moje_id') == 'node[@id="moje_id"]'
#    assert 'node' + ATRIBUT('id',  'moje_id') + ATRIBUT('jméno',  'uzlík') == 'node[@id="moje_id"][@jméno="uzlík"]'


