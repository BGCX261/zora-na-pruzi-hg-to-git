#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

import py.test
import os

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
    
    print('Testuji na testopvacím grafu {}'.format(cesta_k_graphml_souboru))
    
    tree = načtu_graf(cesta_k_graphml_souboru)
    assert isinstance(tree,  lxml.etree._ElementTree)
    
    root = tree.getroot()
    
    assert isinstance(root,  int)    
    
    
#    with py.test.raises(AttributeError):
#        x.a
        
if __name__ == '__main__':
    from zora_na_pruzi.iskušitel  import spustím_test,  zobrazím_log_jako_html_stránku

    spustím_test(__file__)
        
    zobrazím_log_jako_html_stránku()
