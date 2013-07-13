#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

import py.test
import os

from zora_na_pruzi.neo4j import *
    
def test_0001_tvořím_elementy():
    
    soubor_nastavení = os.path.join(NEO4J_ADRESÁŘ_DATABÁZÍ,  'testovací',  NEO4J_SERVER_PROPERTIES)
    from zora_na_pruzi.neo4j import pyproperties
    nastavení = pyproperties.Properties(soubor_nastavení)
    
    nastavení.store(os.path.join(os.path.dirname(__file__),  'testuji.properties'))
    
#    import filecmp
#    assert filecmp.cmp(soubor_nastavení, 'testuji.properties')
#    with open()
    
    
