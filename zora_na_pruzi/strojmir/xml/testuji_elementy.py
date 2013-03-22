#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

import py.test
import os

from .html5 import E
from .html5.HTML import HTML

    
def test_0001_tvořím_elementy():
    
    html_třída = E['HTML']
    
    assert issubclass(html_třída,  HTML)
    assert html_třída ==  HTML
    
    html_builder = E.HTML
    html_builder_2 = E('HTML')
    assert html_builder.__class__.__name__ == html_builder_2.__class__.__name__
    assert str(html_builder) == str(html_builder_2)
    
#############    
    
    html = html_builder(id = 11)
    html_2 = html_builder_2(id = 11)
    assert str(html) == str(html_2)
    
    html_builder = E.HTML
    html_builder['id'] = 245
    html_builder_2 = E('HTML',  id = 245)
    assert str(html_builder) == str(html_builder_2)
    
    html_builder = E.HTML
    html_builder['q'] = None
    html_builder_2 = E('HTML',  q = None)
    assert str(html_builder) == str(html_builder_2)
    
    assert str(html_builder()) == str(html_builder_2())
    
        
#    from .G import G
#    from .SVG import SVG
#        
#    g = E << cesta_k_souboru('fragment_g.svg')
#    assert isinstance(g,  G)
#    svg = E << cesta_k_souboru('prázdné.svg')
#    assert isinstance(svg,  SVG)
    
