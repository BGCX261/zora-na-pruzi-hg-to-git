#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je třída, která přesměruje standartní výstup
'''

import sys

class VÝSTUP(object):
    
    '''
    přesměruje standartní výstup
    '''
    
    def __init__(self, výstup):
        if isinstance(výstup,  str):
            výstup = open(výstup,  mode ='w',  encoding = 'UTF-8')
            self.__výstup = výstup


    def __enter__(self):
        self.__původní_výstup = sys.stdout
        sys.stdout = self.__výstup
        
    def __exit__(self, *args):
        sys.stdout = self.__původní_výstup
