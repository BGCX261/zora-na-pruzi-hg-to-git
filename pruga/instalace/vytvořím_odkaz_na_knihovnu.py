#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

import sys,  os


PRUGA = 'pruga'
PRUGA_DIR = '../../{}'.format(PRUGA)

def main(python_dir):
    '''
    spouštím funkci main()
    '''
    
    pruga_dir = davaj_adresář_prugy()
    
    try:
        import pruga
    except ImportError:
        kontroluji_python_dir(python_dir)
        python_dir = os.path.join(python_dir,  PRUGA)
        vytvořím_odkaz(zdroj = pruga_dir,  cíl = python_dir)
        return True
        
    python_dir = os.path.dirname(pruga.__file__)
    print('Balíček pruga v systému jestvuje, je v adresáři {}'.format(python_dir))
    
    if not os.path.samefile(pruga_dir,  python_dir):
        raise ValueError('Pruga se neodkazuje na tento balíček {}'.format(pruga_dir))
    else:
        print('A správně se odkazuje hen {}.'.format(pruga_dir))
    
    return False

def kontroluji_python_dir(python_dir):
    
    if not python_dir in sys.path:
        raise ValueError('Python adresář {} není uveden v sys.path a proto jej nemohu použít.'.format(python_dir))
        
    if not os.path.isdir(python_dir):
        raise ValueError('Python adresář {} nejestvuje'.format(python_dir))
        
    print('adresář balíčků pro python je hen:',  python_dir)

def davaj_adresář_prugy():
    hen = os.path.dirname(__file__)
    pruga_dir = os.path.realpath(os.path.join(hen,  PRUGA_DIR))
    
    print('pruga je hen:',  pruga_dir)
    return pruga_dir
     
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
    
    main(python_dir = args.python_dir)
