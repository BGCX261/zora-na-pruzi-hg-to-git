#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import os
import subprocess

from pruga.vidimir.Formátuji import TEXT


def grep(slovo,  adresář):
    
    if not os.path.isdir(adresář):
        raise IOError('Cesta "{}" není adresářem'.format(adresář))
    
    curdir = os.getcwd()
    os.chdir(adresář)
    příkaz = 'grep', '-n', '"{}"'.format(slovo), '*.py'
    
#    vráceno = subprocess.check_output(příkaz,  stderr=subprocess.STDOUT).decode('utf-8')
    with subprocess.Popen(příkaz, stdout = subprocess.PIPE,  stderr = subprocess.PIPE,  shell=True) as proc:
        out = proc.stdout.read().decode('UTF-8')
        err = proc.stderr.read().decode('UTF-8')
        
    os.chdir(curdir)
    
    if out.strip():
        print(adresář | TEXT.INFO)
        print(out | TEXT.VÝPIS_PROGRAMU)
    #    print(err | TEXT.CHYBA)
    
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
        if os.path.isdir('./build'):
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
