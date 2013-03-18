#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

def main():
    '''
    spouštím funkci main()
    '''
    print(main.__doc__)

if __name__ == '__main__':

    import os
    from zora_na_pruzi.system.print_do_souboru import DO_SOUBORU
    
    hen_adresář = os.getcwd()
    instalační_adresář = os.path.dirname(__file__)
    os.chdir(instalační_adresář)
    
    TAB = ' '*4
    KMENOVÁ_TŘÍDA = '__ELEMENT_HTML5'
    
    for TAG in ('HTML', 
                        'HEAD', 
                        'META', 
                        'TITLE', 
                        'LINK', 
                        'SCRIPT', 
                        'BODY', 
                        'TABLE', 
                        'TR', 
                        'TD', 
                        'TH'
                        ):
        jméno_souboru = '{}.py'.format(TAG)
        
        if os.path.isfile(jméno_souboru):
            print('Soubor {} již jestvuje, přeskakuji'.format(jméno_souboru))
            continue
        
        print('Vytvářím třídu pro tag {} v souboru {}'.format(TAG,  jméno_souboru))
        
        with DO_SOUBORU(jméno_souboru):
            print('#!/usr/bin/env python3')
            print('# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>')
            print('# @author Петр Болф <petr.bolf@domogled.eu>')
            print()
            print('from . import {}'.format(KMENOVÁ_TŘÍDA))
            print()
            print('class {}({}):'.format(TAG,  KMENOVÁ_TŘÍDA))
            print(TAB, 'pass',  sep = '')
            
    os.chdir(hen_adresář)
