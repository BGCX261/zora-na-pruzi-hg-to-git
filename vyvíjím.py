#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je skript, gde si zkúšám
'''

import os

#from zora_na_pruzi.pohunci.obarvím_výpis.barevný_logger import daj_logovátka
#debug,  info,  warning,  error,  critical = daj_logovátka(__file__)

#def spustím(*příkaz):
##    PYTHON_BIN = 'python3'
#    import subprocess
#    
##    příkaz = [PYTHON_BIN]
##    příkaz.extend(parametry)
#    subprocess.Popen(příkaz)


def rebuild():
#    cdir = os.getcwd()
#    os.chdir('../')
    os.system('./rebuild.sh')
#    os.chdir(cdir)
    
def build():
#    cdir = os.getcwd()
#    os.chdir('../')
    os.system('./setup.py build')
#    os.chdir(cdir)
    
#build()




def   zkúšám():
    
    from zora_na_pruzi.strojmir.xml.schémata import Schéma
    for přípona in 'rng',  'rnc',  'xsd',  'dtd':
        print('-'*44)
        print('přípona {}'.format(přípona))
        schéma = Schéma(přípona = přípona)
        soubor = schéma % 'graphml'
        print('soubor {}'.format(soubor))
        if os.path.isfile(soubor):
            print('\tjestvuje')
        else:
            print('\tnejestvuje')
            
        validátor = schéma.graphml
        
        if validátor('./graf.graphml'):
            print('VALIDNÍ')
        else:
            print('NEVALIDNÍ')
#        print(schéma.mmml)

        validátor % './graf.graphml'
        print('-'*44)

if __name__ == '__main__':

    print(__doc__)

    zkúšám()

    
