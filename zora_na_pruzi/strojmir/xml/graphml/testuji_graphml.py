#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

import py.test
import os

from zora_na_pruzi.vidimir import F

VZOROVÝ_GRAF = os.path.join(os.path.dirname(__file__),  './testuji_vzorový_graf.graphml')

#za účelem kontroly zda jsou objekty potomky správných instancí
from . import graphml_elementy
import lxml.etree

def parsuji_graf(soubor = VZOROVÝ_GRAF):
    from . import načtu_graf
#    import lxml.etree
    
    tree = načtu_graf(soubor)
    
    return tree,  tree.getroot()

def test_0001_načtu_graphml_soubor ():
    '''
    testuji
    '''
    
    with py.test.raises(IOError):
        parsuji_graf('nejestvující_soubor')
    
    tree,  root = parsuji_graf()
    
    assert isinstance(tree,  lxml.etree._ElementTree)
    assert isinstance(root,  lxml.etree.ElementBase) 
    
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
    tree2,  root2 = parsuji_graf(cesta_k_graphml_souboru)
    uzly = list(root2.uzly)
    uzel = uzly[0]
    data = uzel.data
    
    údaj = data[0]
    assert údaj.jméno == 'jiné jméno' 
    
def test_0002_klíče ():
        
    tree,  root = parsuji_graf()
    
    klíče = root.klíče
    from .seznam_klíčů import Seznam_klíčů
    assert isinstance(klíče,  Seznam_klíčů)
    
    with py.test.raises(KeyError):
        klíče['nejestvující klíč']
        
    assert isinstance(klíče['d1'],  graphml_elementy.key)

def test_0003_grafy():
    
    tree,  root = parsuji_graf()
    
    graf = root.graf
    assert isinstance(graf,  graphml_elementy.graph)
    
    uzly_grafu = list(graf.uzly)
    uzly_graphml = list(root.uzly)
    
    assert len(uzly_grafu) == 7
    součet_uzlů = 0
    for graf in root.grafy:
        uzly = list(graf.uzly)
        součet_uzlů = součet_uzlů + len(uzly)
        
    assert součet_uzlů == len(uzly_graphml)

if __name__ == '__main__':
    from zora_na_pruzi.iskušitel  import spustím_test
    from zora_na_pruzi.iskušitel.zobrazím_v_prohlížeči import zobrazím_v_prohlížeči

    spustím_test(__file__)
        
    zobrazím_v_prohlížeči()
