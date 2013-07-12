#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

import py.test
import os

from .instalace import instaluji_neo4j
   
JMÉNO_TESTOVACÍ_DATABÁZE = 'jméno_pro_testování_instalace_databáze'
INSTALAČNÍ_SOUBOR = 'neo4j-community-2.0.0-M03-unix.tar.gz'
  
def test_0001_instalace():
    
    import shutil
    
    with py.test.raises(IOError):
        instaluji_neo4j(JMÉNO_TESTOVACÍ_DATABÁZE,  'nejestvující_soubor')
        
    from . import server
    
    databáze_nainstalována_do = os.path.join(os.path.dirname(server.__file__),  JMÉNO_TESTOVACÍ_DATABÁZE)
    
    if server.jestvuje_databáze(JMÉNO_TESTOVACÍ_DATABÁZE):
        shutil.rmtree(databáze_nainstalována_do)
#        raise Exception('Nemožu testovat, jestvuje testovací databáze jménem "{}"'.format(JMÉNO_TESTOVACÍ_DATABÁZE))
    
    try:
        instaluji_neo4j(JMÉNO_TESTOVACÍ_DATABÁZE,  INSTALAČNÍ_SOUBOR)
    except AttributeError as e:
        raise e
        
    with py.test.raises(AttributeError):
        instaluji_neo4j(JMÉNO_TESTOVACÍ_DATABÁZE,  INSTALAČNÍ_SOUBOR)
        
#        uklidím po sobě svinčík
    
    
    shutil.rmtree(databáze_nainstalována_do)
    
#    soubor_nastavení = os.path.join(NEO4J_ADRESÁŘ_DATABÁZÍ,  'testovací',  NEO4J_SERVER_PROPERTIES)
#    from zora_na_pruzi.neo4j import pyproperties
#    nastavení = pyproperties.Properties(soubor_nastavení)
#    
#    nastavení.store(os.path.join(os.path.dirname(__file__),  'testuji.properties'))
    
#    import filecmp
#    assert filecmp.cmp(soubor_nastavení, 'testuji.properties')
#    with open()
    
    
