#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

import py.test

#from logging import debug,  info
from zora_na_pruzi.vidimir import F

def test_0001_schémata ():
    '''
    testuji schémata
    '''
    
    from zora_na_pruzi.strojmir.xml.schémata import Relax_NG,  Relax_NG_c,  XMLSchema,  DTD
    
    from zora_na_pruzi.strojmir.xml.schémata import __Schéma
    
    for modul_schématu in Relax_NG,  Relax_NG_c,  XMLSchema,  DTD:
        
#        print('Testuji modul schématu {}'.format(modul_schématu.__name__) | F.TEST.START)
        
        schéma = modul_schématu.Schéma('graphml')
        
        assert callable(schéma)
#        print('schéma is callable' | F.TEST.OK)
        
        assert isinstance(schéma,  __Schéma)
        assert isinstance(schéma,  modul_schématu.Schéma)
#        print('je potomkem třídy Schéma' | F.TEST.OK)
        
        soubor_schématu = schéma.soubor_schématu
#        print('jestvuje schéma {}'.format(soubor_schématu | F.SOUBOR) | F.TEST.OK)
        
        print('VALIDUJI {}'.format(soubor_schématu))
        
        if schéma('./graf.graphml'):
            print('\t...VALIDNÍ')
        else:
            print('\t...NEVALIDNÍ' | F.CHYBA)

#        print('Program {}'.format(modul_schématu.program | F.PŘÍKAZ)  | F.TEST.START)

        schéma(soubor = './graf.graphml',  program = modul_schématu.program)
        
        nejestvující_schéma = modul_schématu.Schéma('nejestvující_schéma')
        with py.test.raises(AttributeError):
            nejestvující_schéma.soubor_schématu
          
        with py.test.raises(AttributeError):  
            nejestvující_schéma.validátor
        
    
        
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
    from zora_na_pruzi.iskušitel  import spustím_test
    from zora_na_pruzi.iskušitel.zobrazím_v_prohlížeči import zobrazím_v_prohlížeči

    spustím_test(__file__)
        
    zobrazím_v_prohlížeči()
