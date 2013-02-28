#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Tento skript spustí příkaz
'''

def změním_příponu(jméno,  přípona):
    import os
    return '{}.{}'.format(os.path.splitext(jméno)[0],  přípona)
