#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

def nalinkuji(modul):
    import os
    print(modul.__file__)
    adresář = os.path.dirname(modul.__file__)
    if not os.path.isdir(adresář):
        raise ValueError('Nejestvuje adresář {}'.format(adresář))
        
    nalinkuji_do = os.path.join(os.path.dirname(__file__), '../cizí_zdroje',  os.path.basename(adresář))
    příkaz = 'ln -s {} {}'.format(adresář,  nalinkuji_do)
    print('spouštím příkaz {}'.format(příkaz))
    os.system(příkaz)
    
def načtu_modul(celé_jméno_modulu):
    '''
    spouštím funkci main()
    '''
    import imp
    import sys
    
    rozdělené_jméno_balíčku = celé_jméno_modulu.split('.')
    jméno_modulu = rozdělené_jméno_balíčku.pop()
    print('jméno modulu {} cesta k balíčku {}'.format(jméno_modulu,  rozdělené_jméno_balíčku))
    try:
        file, pathname, description = imp.find_module(jméno_modulu, sys.path)
        modul = imp.load_module(celé_jméno_modulu,  file, pathname, description)
        return modul
    except ImportError as e:
        raise ImportError('Chybí modul {}: {}'.format(celé_jméno_modulu,  e))


if __name__ == '__main__':

    print(__doc__)

    import argparse
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser()

#   a pak mu nastavím jaké příkazy a parametry má přijímat
    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, искушител {}'.format(__version__))
    
    parser.add_argument('knihovna')
    
    #    a včíl to možu rozparsovat
    args = parser.parse_args()
    
    print('knihovna',  args.knihovna)

    modul = načtu_modul(args.knihovna)
    nalinkuji(modul)
