#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

import py.test

#from logging import debug,  info
from zora_na_pruzi.pisar import styl as s

def test_0001_schémata ():
    '''
    testuji schémata
    '''
    
    from zora_na_pruzi.strojmir.xml.schémata import Relax_NG,  Relax_NG_c,  XMLSchema,  DTD
    
    from zora_na_pruzi.strojmir.xml.schémata import davaj_validátor
    Validátor = davaj_validátor(lxml_validátor = None,  přípona_schématu = None)
    
    for schéma in Relax_NG,  Relax_NG_c,  XMLSchema,  DTD:
        
        print('Testuji modul validátoru {}'.format(schéma.__name__) | s.TEST_START)
        
        validátor = schéma.Validátor('graphml')
        
        assert callable(validátor)
        print('validátor is callable' | s.TEST_OK)
        
        assert validátor.__class__.__name__ == Validátor.__name__
        print('je potomkem třídy Validátor' | s.TEST_OK)
        
        soubor_schématu = validátor.schéma
        print('jestvuje schéma {}'.format(soubor_schématu | s.SOUBOR) | s.TEST_OK)
        
        print('VALIDUJI' | s.TEST_START)
        
        if validátor('./graf.graphml'):
            print('VALIDNÍ' | s.TEST_OK)
        else:
            print('NEVALIDNÍ' | s.TEST_CHYBA)

        print('Program {}'.format(schéma.program | s.PŘÍKAZ)  | s.TEST_START)

        validátor(soubor = './graf.graphml',  program = schéma.program)
        
    
        
#def test_0002_schéma_rnc ():
#    '''
#    testuji schémata
#    '''
#    
#    schéma = Schéma(přípona = 'rnc')
#    
#    assert isinstance(schéma.graphml,  lxml.etree.RelaxNG)
#    
#    with py.test.raises(AttributeError):
#        schéma.nejestvující_schéma
#        
#def test_0003_schéma_xsd ():
#    '''
#    testuji schémata
#    '''
#    
#    schéma = Schéma(přípona = 'xsd')
#    
#    assert isinstance(schéma.graphml,  lxml.etree.XMLSchema)
#    
#    with py.test.raises(AttributeError):
#        schéma.nejestvující_schéma
#        
#def test_0004_schéma_dtd ():
#    '''
#    testuji schémata
#    '''
#    
#    schéma = Schéma(přípona = 'dtd')
#    
#    assert isinstance(schéma.graphml,  lxml.etree.DTD)
#    
#    with py.test.raises(AttributeError):
#        schéma.nejestvující_schéma
    
#    for přípona in ,  'xsd',  'dtd',  'rnc':
##        print('-'*44)
##        print('přípona {}'.format(přípona))
#        
##        soubor = schéma % 'graphml'
##        print('soubor {}'.format(soubor))
##        if os.path.isfile(soubor):
##            print('\tjestvuje')
##        else:
##            print('\tnejestvuje')
##        print(schéma.graphml)
##        print(schéma.mmml)
##        print('-'*44)
#
#        
#        assert schéma.graphml is not None
#    
#        
        
if __name__ == '__main__':
    from zora_na_pruzi.iskušitel  import spustím_test,  zobrazím_v_prohlížeči

    spustím_test(__file__)
        
    zobrazím_v_prohlížeči()
