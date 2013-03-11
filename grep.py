#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import os
from zora_na_pruzi.system.spustím_příkaz import spustím_příkaz_a_vrátím

from zora_na_pruzi.vidimir.Formátuji import TEXT


def grep(slovo,  adresář):
    
    if not os.path.isdir(adresář):
        raise IOError('Cesta "{}" není adresářem'.format(adresář))
    
    curdir = os.getcwd()
    os.chdir(adresář)
    příkaz = 'grep -n "{}" *.py'.format(slovo)
    out,  err = spustím_příkaz_a_vrátím(příkaz)
    os.chdir(curdir)
    if out.strip():
        print(adresář | TEXT.INFO)
        print(out)
    
    for soubor in os.listdir(adresář):
        cesta = os.path.join(adresář, soubor)
        if os.path.isdir(cesta):
            if not soubor.startswith('.') and not soubor in ignoruj_všechny and not ignoruj(cesta):
                grep(slovo,  cesta)



if __name__ == '__main__':

    
    
    import argparse  
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser()
    parser.add_argument('slovo')
    parser.add_argument('adresáře',  nargs='*')
#    parser.add_argument('maska_souborů')
    #    a včíl to možu rozparsovat
    args = parser.parse_args()
#    print(args)

    ignoruj_všechny = ('.hg',  '__pycache__')
    def ignoruj(cesta):
        for ignorovaná in ('./build',  ):
            if os.path.samefile(cesta,  ignorovaná) is True:
                return True
        return False

    adresáře = args.adresáře
    slovo = args.slovo
    if not adresáře:
        adresáře = [os.path.dirname(__file__)]
   
    for adresář in adresáře:
        grep(slovo,  adresář)
        
         
#    příkaz = 'grep -R "{}" *'.format(args.slovo)
#
#    spustím_příkaz_a_vypíšu(příkaz)
