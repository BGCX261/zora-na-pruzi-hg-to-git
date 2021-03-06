#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Tento skript spustí příkaz
'''

import subprocess
from zora_na_pruzi.vidimir.Formátuji import TEXT

def __sestavím_příkaz(*příkaz,  shell):
    if len(příkaz) == 1:
        if isinstance(příkaz[0],  str):
            if shell:
                return příkaz[0]
            else:
                #            rozdělíme podle mezer
                return příkaz[0].split()
                
        if isinstance(příkaz[0],  (tuple,  list)):
            if shell:
                return ' '.join(příkaz[0])
            else:
                return příkaz[0]
    else:
        if shell:
            return ' '.join(příkaz)
        return příkaz


def spustím_příkaz_a_vypíšu(*příkaz,  shell = True):
    
    příkaz = __sestavím_příkaz(*příkaz,  shell = shell)


    with subprocess.Popen(příkaz, stdout = subprocess.PIPE,  stderr = subprocess.PIPE,  shell=shell) as proc:
#        log.write(proc.stdout.read())
        if not shell:
            jméno_příkazu = příkaz[0]
            příkaz = ' '.join(příkaz)
        else:
            jméno_příkazu = příkaz.split()[0]
        print('spouštím: {}'.format(příkaz | TEXT.PŘÍKAZ) | TEXT.INFO )
        print(proc.stdout.read().decode('UTF-8') | TEXT.VÝPIS_PROGRAMU)
        print(proc.stderr.read().decode('UTF-8') | TEXT.CHYBA)
        
    
        
        print('ukončen: {}'.format(jméno_příkazu | TEXT.PŘÍKAZ) | TEXT.INFO )
    
    
def spustím_příkaz_a_vrátím(*příkaz,  shell = True):
    
    příkaz = __sestavím_příkaz(*příkaz,  shell = shell)


    with subprocess.Popen(příkaz, stdout = subprocess.PIPE,  stderr = subprocess.PIPE,  shell=shell) as proc:
        out = proc.stdout.read().decode('UTF-8')
        if out.strip():
            out = out | TEXT.VÝPIS_PROGRAMU
        err = proc.stderr.read().decode('UTF-8')
        if err.strip():
            err = err | TEXT.CHYBA
        
    return out,  err
