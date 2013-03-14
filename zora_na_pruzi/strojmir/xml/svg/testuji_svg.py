#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

import py.test
import os

ADRESÁŘ_VZOROVÝCH_SVG = os.path.join(os.path.dirname(__file__),  './__testuji_svg')

#import lxml.etree
from . import E
#from .svg import svg
#from .g import g

#def soubor_svg_vzoru(číslo):
#    jméno = '{:0=3}.svg'.format(číslo)
#    return cesta_k_souboru(jméno)

def cesta_k_souboru(jméno_souboru):
    return os.path.join(ADRESÁŘ_VZOROVÝCH_SVG,  jméno_souboru)
    
def test_0001_načtu_svg():
    
#    with py.test.raises(TypeError):
#        svg = E << cesta_k_souboru('fragment_g.svg')
        
    from .G import G
    from .SVG import SVG
        
    g = E << cesta_k_souboru('fragment_g.svg')
    assert isinstance(g,  G)
    svg = E << cesta_k_souboru('prázdné.svg')
    assert isinstance(svg,  SVG)
    
def test_0002_vytvořím_nové_svg():
  
    svg = E.SVG()
    svg_vzor = E << cesta_k_souboru('prázdné.svg')
    
#    assert svg._ELEMENT.tag == svg_vzor._ELEMENT.tag
#    assert str(svg) != str(svg_vzor)
    
    
    print(svg)
    print(svg_vzor)
    assert str(svg) == str(svg_vzor)

#    cesta = soubor_svg_vzoru(1)
#    print(cesta)
    
#    assert GRAPH.TAG == '{{{}}}graph'.format(NAMESPACE)
#    assert NODE.TAG == '{{{}}}node'.format(NAMESPACE)

#def test_0002_načtu_graphml_soubor ():
#    '''
#    testuji
#    '''
#    
#    with py.test.raises(IOError):
#        parsuji_graf('nejestvující_soubor')
#    
#    tree,  root = parsuji_graf()
#    
#    assert isinstance(tree,  lxml.etree._ElementTree)
#    assert isinstance(root,  lxml.etree.ElementBase) 
#    
#    uzly = list(root.uzly)
#    assert len(uzly) == 14
#    
#    vazby = list(root.vazby)
#    assert len(vazby) == 12
#    
#    uzel = uzly[0]
#    
#    data = uzel.data
#    assert len(data) == 1
#    
#    údaj = data[0]
#    
#    assert údaj.jméno == 'jméno'
#    assert údaj.datový_typ == 'string'
#    assert údaj.default is None
#    
#    assert údaj.klíč == root.klíče['d2']
#    assert id(údaj.klíč) == id(root.klíče['d2'])
#    
##    druhý graf 
#    graphml_soubor = './testuji_vzorový_graf_2.graphml'
#    cesta_k_graphml_souboru = os.path.join(os.path.dirname(__file__),  graphml_soubor)
#    tree2,  root2 = parsuji_graf(cesta_k_graphml_souboru)
#    uzly = list(root2.uzly)
#    uzel = uzly[0]
#    data = uzel.data
#    
#    údaj = data[0]
#    assert údaj.jméno == 'jiné jméno' 
#    
#def test_0003_klíče ():
#        
#    tree,  root = parsuji_graf()
#    
#    klíče = root.klíče
#    from .seznam_klíčů import Seznam_klíčů
#    assert isinstance(klíče,  Seznam_klíčů)
#    
#    with py.test.raises(KeyError):
#        klíče['nejestvující klíč']
#        
#    assert isinstance(klíče['d1'],  graphml_elementy.KEY)
#
#def test_0004_grafy():
#    
#    tree,  root = parsuji_graf()
#    
#    graf = root.graf
#    assert isinstance(graf,  graphml_elementy.GRAPH)
#    
#    uzly_grafu = list(graf.uzly)
#    uzly_graphml = list(root.uzly)
#    
#    assert len(uzly_grafu) == 7
#    součet_uzlů = 0
#    for graf in root.grafy:
#        uzly = list(graf.uzly)
#        součet_uzlů = součet_uzlů + len(uzly)
#        
#    assert součet_uzlů == len(uzly_graphml)
#    
#def test_0005_grafy():
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
#
#
