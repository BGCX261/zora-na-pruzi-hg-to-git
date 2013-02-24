#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který překontroluje správnost graphml souboru
'''

from zora_na_pruzi.strojmir.pomůcky.obarvím_výpis import PŘÍKAZ,  INFO,  SOUBOR,  CHYBA

def validuji(soubor,  schéma = None):
    '''
    spouštím funkci main()
    '''
    schéma = schéma or 'rng'
    
    if schéma in ('rng',  'relaxng'):
        from zora_na_pruzi.strojmir.xml.schémata import Schéma_rng as Schéma
    elif schéma in ('rnc',  'relaxng compile'):
        from zora_na_pruzi.strojmir.xml.schémata import Schéma_rnc as Schéma
    elif schéma in ('xsd',  'xml schema'):
        from zora_na_pruzi.strojmir.xml.schémata import Schéma_xsd as Schéma
    elif schéma in ('dtd', ):
        from zora_na_pruzi.strojmir.xml.schémata import Schéma_dtd as Schéma
    else:
        raise TypeError('Neznám schéma {}'.format(schéma))
        
    print('Validuji {} pomocí {}'.format(args.zdrojový_xml | SOUBOR,  Schéma.__name__) | INFO)
    
#    if schéma is None:
##        from nástroje.obarvím_výpis import obarvi_upozornění_print
##        obarvi_upozornění_print('použiju výchozí schéma {}'.format(SCHÉMA),  end = None)
#        schéma = SCHÉMA

    schéma = Schéma()
    validátor = schéma.graphml
    
    validní = validátor(soubor)
    if validní:
        print('\ttje validní' | INFO)
    else:
        print('\tNENÍ VALIDNÍ' | CHYBA)
        validátor(soubor,  program = True)


if __name__ == '__main__':

    print(__doc__)

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('zdrojový_xml')
    parser.add_argument('--schéma')
    args = parser.parse_args()
    
    validuji(soubor = args.zdrojový_xml,  schéma = args.schéma)
    
    
