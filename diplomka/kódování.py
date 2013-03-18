#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

def kódování():
    '''
    spouštím funkci main()
    '''
    for řádek in open('csv/Babice.csv',  mode='r',  encoding='windows-1250'):
        print(řádek)

if __name__ == '__main__':

    print(__doc__)

    import argparse
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser()

#   a pak mu nastavím jaké příkazy a parametry má přijímat
    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, искушител {}'.format(__version__))
    
#    parser.add_argument('soubor')
    
    #    a včíl to možu rozparsovat
    args = parser.parse_args()
    
#    print('soubor',  args.soubor)

    kódování()
