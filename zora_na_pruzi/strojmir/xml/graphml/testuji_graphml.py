#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

import py.test
import os

from zora_na_pruzi.vidimir import F

def test_0001_načtu_graphml_soubor ():
    '''
    testuji
    '''
    
    from . import načtu_graf
    import lxml.etree
    
    graphml_soubor = './testuji_vzorový_graf.graphml'
    cesta_k_graphml_souboru = os.path.join(os.path.dirname(__file__),  graphml_soubor)
    
    with py.test.raises(IOError):
        načtu_graf('nejestvující_soubor')
    
    print('Testuji na testovacím grafu {}'.format(cesta_k_graphml_souboru | F.SOUBOR) | F.TEST.START)
    
    tree = načtu_graf(cesta_k_graphml_souboru)
    assert isinstance(tree,  lxml.etree._ElementTree)
    
    root = tree.getroot()
    
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
    
    tree2 = načtu_graf('/home/golf/vývoj/zora-na-pruzi/stroj/grafy/zora_na_pruzi.graphml')
    root2 = tree2.getroot()
    uzly = list(root2.uzly)
    uzel = uzly[0]
    print(uzel.jméno)
    data = uzel.data
    
    údaj = data[0]
    print(údaj.jméno)
    
    
#    with py.test.raises(AttributeError):
#        x.a
        
if __name__ == '__main__':
    from zora_na_pruzi.iskušitel  import spustím_test
    from zora_na_pruzi.iskušitel.zobrazím_v_prohlížeči import zobrazím_v_prohlížeči

    spustím_test(__file__)
        
    zobrazím_v_prohlížeči()
