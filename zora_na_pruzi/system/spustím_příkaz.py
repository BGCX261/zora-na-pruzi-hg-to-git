#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Tento skript spustí příkaz
'''

import subprocess
from zora_na_pruzi.pisar.styly.obarvím_výpis_konzole import PŘÍKAZ,  INFO,  VÝPIS_PROGRAMU

def __sestavím_příkaz(*příkaz):
    if len(příkaz) == 1:
        if isinstance(příkaz[0],  str):
#            rozdělíme podle mezer
            return příkaz[0].split()
        if isinstance(příkaz[0],  (tuple,  list)):
            return příkaz[0]
    else:
        return příkaz

def spustím_příkaz(*příkaz):
    
    příkaz = __sestavím_příkaz(*příkaz)

    print('spouštím: {}'.format(' '.join(příkaz) | PŘÍKAZ) | INFO )
#    if check:
#        returncode = subprocess.check_call(příkaz)
#        print('ukončen:' | INFO,  příkaz[0] | PŘÍKAZ,  's kódem {}'.format(returncode) | INFO)
#    else:
##        returncode = subprocess.call(příkaz)
##        os.system(' '.join(příkaz))
    ret = subprocess.Popen(příkaz, stdout=subprocess.PIPE)
    výstup = ret.stdout.read()
    print('ukončen:' | INFO,  příkaz[0] | PŘÍKAZ,  'vrátil:' | VÝPIS_PROGRAMU)
    print(výstup.decode('UTF-8'))
    print('.'*64)
    
