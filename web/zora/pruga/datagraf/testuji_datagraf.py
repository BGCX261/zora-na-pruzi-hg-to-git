#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

import py.test
import os

from .instalace import instaluji_neo4j
   
JMÉNO_TESTOVACÍ_DATABÁZE = 'TOTO_JE_DATABÁZE_PRO_TESTOVACÍ_ÚČELY_A_BUDE_VZÁPĚTÍ_SMAZÁNA'
INSTALAČNÍ_SOUBOR = 'neo4j-community-2.0.0-M03-unix.tar.gz'
  
def test_0001_instalace():
    
    import shutil
    
    with py.test.raises(IOError):
        instaluji_neo4j(JMÉNO_TESTOVACÍ_DATABÁZE,  'nejestvující_soubor')
        
    from . import server
    
    databáze_nainstalována_do = os.path.join(os.path.dirname(server.__file__),  JMÉNO_TESTOVACÍ_DATABÁZE)
    
#    pokud jestvuje již od minule,  třeba že předchozí test skončil před smazáním tak jhi smažu včíl
    if server.jestvuje_databáze(JMÉNO_TESTOVACÍ_DATABÁZE):
        print('Mažu předchozí databázi {}'.format(JMÉNO_TESTOVACÍ_DATABÁZE))
        shutil.rmtree(databáze_nainstalována_do)
#        raise Exception('Nemožu testovat, jestvuje testovací databáze jménem "{}"'.format(JMÉNO_TESTOVACÍ_DATABÁZE))
    
    try:
        instaluji_neo4j(JMÉNO_TESTOVACÍ_DATABÁZE,  INSTALAČNÍ_SOUBOR)
    except AttributeError as e:
        raise e
        
#    opětovná instalace sleže
    with py.test.raises(AttributeError):
        instaluji_neo4j(JMÉNO_TESTOVACÍ_DATABÁZE,  INSTALAČNÍ_SOUBOR)
        
#    je v seznamu
    from .server import davaj_seznam_databází
    
    seznam_databází = davaj_seznam_databází()
    seznam_databází = tuple(seznam_databází)
    assert JMÉNO_TESTOVACÍ_DATABÁZE in seznam_databází
    
    from .server import davaj_server
    
    neo4j_server = davaj_server(JMÉNO_TESTOVACÍ_DATABÁZE)
    
    assert neo4j_server.status() == False
    
    neo4j_server.start()
    
    assert neo4j_server.status() == True
    
    neo4j_server.stop()
    
    assert neo4j_server.status() == False
        
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
    
    
