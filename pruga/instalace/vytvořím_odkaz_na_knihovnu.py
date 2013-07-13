#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který vytvoří v systému odkaz na vývojový balíček prugy
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

import sys,  os


PRUGA = 'pruga'
ZORA = 'zora'
ROOT_DIR = '../../'

def nastavím_adresáře(python_dir,  balíček):
    '''
    spouštím funkci main()
    '''
    
    print('-'*24)
    print('nastavím balíček {}'.format(balíček))
    print('-'*24)
    
    cesta_k_balíčku = davaj_cestu_k_balíčku(adresář_balíčku = balíček)
    
    try:
#        import pruga
        modul = __import__(balíček, globals(), locals(), [], 0)
    except ImportError:
        kontroluji_python_dir(python_dir)
        python_dir = os.path.join(python_dir,  balíček)
        vytvořím_odkaz(zdroj = cesta_k_balíčku,  cíl = python_dir)
#        return True
        
    python_dir = os.path.dirname(getattr(modul,  '__file__'))
    print('Balíček {} v systému jestvuje, je v adresáři {}'.format(balíček, python_dir))
    
    if not os.path.samefile(cesta_k_balíčku,  python_dir):
        raise ValueError('Balíček {} se neodkazuje na tento adresář {}'.format(balíček,  cesta_k_balíčku))
    else:
        print('A správně se odkazuje hen {}.'.format(cesta_k_balíčku))
    
#    return False

def kontroluji_python_dir(python_dir):
    
    if not python_dir in sys.path:
        raise ValueError('Python adresář {} není uveden v sys.path a proto jej nemohu použít.'.format(python_dir))
        
    if not os.path.isdir(python_dir):
        raise ValueError('Python adresář {} nejestvuje'.format(python_dir))
        
    print('adresář balíčků pro python je hen:',  python_dir)

def davaj_cestu_k_balíčku(adresář_balíčku):
    hen = os.path.dirname(__file__)
    abs_cesta = os.path.realpath(os.path.join(hen, ROOT_DIR,  adresář_balíčku))
    
    print('cesta pro {} je hen {}'.format(adresář_balíčku,  abs_cesta))
    return abs_cesta
     
def vytvořím_odkaz(zdroj,  cíl):

        if os.path.exists(cíl) and os.path.samefile(zdroj,  cíl):
            print('Odkaz {} -> {} je v pořádku'.format(zdroj,  cíl))
            return True
            
        print('Vytvořím odkaz {} -> {}.'.format(zdroj,  cíl))
        
        if os.path.islink(cíl):
            if input('Zda-li mám smazat odkaz {} -> {}?\n da - ne >>  '.format(cíl,  os.path.realpath(cíl))) in ('da'):
                os.unlink(cíl)
                print('\tsmazáno')
            else:
                print('Tož dobrá, ale nebude to správně nastavené.')
                return False
                
        if os.path.isdir(cíl):
            raise NotImplementedError('Odkaz {} jestvuje jako adresář, ale to zatím neumím řešit. Zkus jej ručně smazat, nebo přesunout.'.format(cíl))
            
        if os.path.isfile(cíl):
            raise NotImplementedError('Odkaz {} jestvuje jako soubor, ale to zatím neumím řešit. Zkus jej ručně smazat, nebo přesunout.'.format(cíl))
        
        příkaz = 'ln -s {} {}'.format(zdroj,  cíl)
        print('spouštím',  příkaz)
        os.system(příkaz)
        
if __name__ == '__main__':

    print(__doc__)

    import argparse
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser()

#   a pak mu nastavím jaké příkazy a parametry má přijímat
    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, {}'.format(__version__))
    
    parser.add_argument('--python_dir',  default = '/usr/local/lib/python3.2/dist-packages')
    
    #    a včíl to možu rozparsovat
    args = parser.parse_args()
    
    nastavím_adresáře(python_dir = args.python_dir,  balíček = PRUGA)
    nastavím_adresáře(python_dir = args.python_dir,  balíček = ZORA)
