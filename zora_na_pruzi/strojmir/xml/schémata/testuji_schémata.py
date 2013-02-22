#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

import py.test



def test_0001_schémata ():
    '''
    testuji schémata
    '''
    
    from zora_na_pruzi.strojmir.xml.schémata import Schéma_rng,  Schéma_rnc,  Schéma_xsd,  Schéma_dtd
    
    for Schéma in Schéma_rng, Schéma_rnc,  Schéma_xsd,  Schéma_dtd:
    
        schéma = Schéma()
    
#        assert isinstance(schéma.graphml,  Validátor)
        assert callable(schéma.graphml)
    
        with py.test.raises(AttributeError):
            schéma.nejestvující_schéma
        
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
    from zora_na_pruzi.iskušitel  import spustím_test,  zobrazím_log_jako_html_stránku

    spustím_test(__file__)
        
    zobrazím_log_jako_html_stránku()
