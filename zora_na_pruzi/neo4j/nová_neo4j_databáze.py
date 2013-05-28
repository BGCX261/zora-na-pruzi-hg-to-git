#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import os
import shutil

from zora_na_pruzi.neo4j import *

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

def jestvuje_rozbalený_neo4j_v_tempu(adresář):
    if os.path.isdir(adresář):
        print('mažu {}'.format(adresář))
        shutil.rmtree(adresář)

def rozbalím_neo4j(jméno_databáze,  NEO4J_SRC):
    '''
    spouštím funkci rozbalím_neo4j()
    '''
    import tarfile
    
    if not os.path.isfile(NEO4J_SRC):
        raise IOError('Nejestvuje zdrojový soubor neo4j databáze {}.'.format(NEO4J_SRC,  NEO4J_ADRESÁŘ_DATABÁZÍ))
        
    
    cesta_k_nové_databázi = os.path.join(NEO4J_ADRESÁŘ_DATABÁZÍ,  jméno_databáze)
    if os.path.isdir(cesta_k_nové_databázi):
        raise IOError('Databáze jménem {} již jestvuje v adresáři {}.'.format(jméno_databáze,  NEO4J_ADRESÁŘ_DATABÁZÍ))
        
    
    print('rozbalím {}'.format(NEO4J_SRC))
    tar = tarfile.open(NEO4J_SRC, 'r')
    
    jméno_src_adresáře = tar.members[0].name
    cesta_temp_src = os.path.join(TEMP_ADRESÁŘ,  jméno_src_adresáře)
    
    jestvuje_rozbalený_neo4j_v_tempu(cesta_temp_src)
    
#    for item in tar:
#        print(item)
    print('rozbaluji {} do {}'.format(NEO4J_SRC,  cesta_temp_src))
    tar.extractall(TEMP_ADRESÁŘ)
    
    
    
    print('přesouvám {} do {}'.format(cesta_temp_src,  cesta_k_nové_databázi))
    shutil.move(cesta_temp_src,  cesta_k_nové_databázi)

if __name__ == '__main__':

    print(__doc__)

    import argparse
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser()

#   a pak mu nastavím jaké příkazy a parametry má přijímat
    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, {}'.format(__version__))
    
    parser.add_argument('jméno_databáze')
    
    #    a včíl to možu rozparsovat
    args = parser.parse_args()
    
    print('vytvořím databázi',  args.jméno_databáze)

    try:
        rozbalím_neo4j(args.jméno_databáze,  NEO4J_SRC)
    except IOError as e:
        print(e)
    
