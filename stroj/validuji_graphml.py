#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který překontroluje správnost graphml souboru
'''

from zora_na_pruzi.vidimir import F

def validuji(soubor,  schéma = None):
    '''
    spouštím funkci main()
    '''
    schéma = schéma or 'rng'
    
    if schéma in ('rng',  'relaxng'):
        from zora_na_pruzi.strojmir.xml.schémata import Relax_NG as modul_schématu
    elif schéma in ('rnc',  'relaxng compile'):
        from zora_na_pruzi.strojmir.xml.schémata import Relax_NG_c as modul_schématu
    elif schéma in ('xsd',  'xml schema'):
        from zora_na_pruzi.strojmir.xml.schémata import XMLSchema as modul_schématu
    elif schéma in ('dtd', ):
        from zora_na_pruzi.strojmir.xml.schémata import DTD as modul_schématu
    else:
        raise TypeError('Neznám schéma {}'.format(schéma))
        
    print('Validuji {} pomocí {}'.format(args.zdrojový_xml | F.SOUBOR,  modul_schématu.__name__) | F.INFO)

    validátor = modul_schématu.Validátor('graphml')
    
    validní = validátor(soubor)
    if validní:
        print('\tje validní' | F.TEST.OK)
    else:
        print('\tNENÍ VALIDNÍ' | F.TEST.CHYBA)
        validátor(soubor,   program = modul_schématu.program)


if __name__ == '__main__':

    print(__doc__)

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('zdrojový_xml')
    parser.add_argument('--schéma')
    args = parser.parse_args()
    
    validuji(soubor = args.zdrojový_xml,  schéma = args.schéma)
    
    
