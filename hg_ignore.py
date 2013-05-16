#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který přidá soubor do hgignore
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'


import os
import glob

def čtu_hg_ignore():
    '''
    spouštím funkci main()
    '''
    
    with open('.hgignore',  mode='r',  encoding = 'UTF-8') as soubor:
        for ignore in soubor:
            print(ignore)
            if ignore.startswith('glob'):
                glob_cesta = ignore.split(':')[1]
                glob_cesta = glob_cesta.strip()
            else:
                glob_cesta = ignore
            
            print('HLEDÁM {}'.format(glob_cesta))
                
            for soubor in glob.glob(glob_cesta):
                print(soubor)

def do_ignore(soubor):
    if not os.path.isfile(soubor) and not os.path.isdir(soubor):
        raise ValueError('Soubor {} nejestvuje'.format(soubor))
        
    soubor = os.path.relpath(os.path.abspath(soubor),  os.path.dirname(__file__))
    
    if soubor.startswith('..'):
        raise ValueError('Soubor {} není v adresáři projektu.'.format(soubor))
        
    
    with open('.hgignore',  mode='a',  encoding = 'UTF-8') as hgignore:
        hgignore.write(soubor)
        hgignore.write('\n')
        
    print('Soubor {} úspěšně přidán do .hgignore.'.format(soubor))

if __name__ == '__main__':

    print(__doc__)

    import argparse
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser()

#   a pak mu nastavím jaké příkazy a parametry má přijímat
    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, искушител {}'.format(__version__))
    
    parser.add_argument('soubor')
    
    #    a včíl to možu rozparsovat
    args = parser.parse_args()
    
    print('soubory {} přidám do .hgignore'.format(args.soubor))

#    čtu_hg_ignore()

    for soubor in glob.glob(args.soubor):
        print('soubor {} přidám do .hgignore'.format(soubor))
        do_ignore(soubor)
#    do_ignore(args.soubor)
