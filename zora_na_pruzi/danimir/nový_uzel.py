#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

def nový_uzel(jméno_uzlu):
    '''
    vytvořím nový uzel
    '''
    from zora_na_pruzi.danimir.Uzel import Uzel
    
    from zora_na_pruzi.danimir.db import db
    db = db()
    
    vytvořím_nový_uzel = db.proc('vytvořím_nový_uzel(character varying)')
    id_uzlu = vytvořím_nový_uzel(jméno_uzlu)
    print(id_uzlu)
    
    return Uzel(id_uzlu)

if __name__ == '__main__':

    print(__doc__)

    import argparse
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser()

#   a pak mu nastavím jaké příkazy a parametry má přijímat
    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, {}'.format(__version__))
    
    parser.add_argument('uzel')
    
    #    a včíl to možu rozparsovat
    args = parser.parse_args()
    
    print('uzel',  args.uzel)

    id_uzlu = nový_uzel(args.uzel)
    print(id_uzlu)
