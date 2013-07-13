#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který vytvoří stránku index.html
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'


print('i3ek ',  __file__)

def main():
    '''
    spouštím funkci main()
    '''
    print(main.__doc__)

if __name__ == '__main__':

    print(__doc__)
    print('Stránka se nevytváří dynamicky. Ručně uprav soubor index.html')

#    import argparse
#    #  nejdříve si parser vytvořím
#    parser = argparse.ArgumentParser()
#
##   a pak mu nastavím jaké příkazy a parametry má přijímat
#    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, {}'.format(__version__))
#    
#    parser.add_argument('soubor')
#    
#    #    a včíl to možu rozparsovat
#    args = parser.parse_args()
#    
#    print('soubor',  args.soubor)

#    import pruga.web
#    from pruga.web.html.stránka import stránka
#    
#    stránka = stránka()
#
#    with pruga.web.DO_SOUBORU(__file__):
#        print(stránka)
