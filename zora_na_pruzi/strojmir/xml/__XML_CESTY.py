#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je třída, která umožní zadávat atributy do vyhledávacích řetězců pomocí operátoru plus
'''

class ATRIBUT(object):
    '''
    Tato třída umožní vytvořit vyhledávací parametr pomocí operátoru +
    '''
    
    def __init__(self,  klíč,  hodnota = None):
        if hodnota is None:
            self.__zápis = '[@{}]'.format(klíč)
        else:
            self.__zápis = '[@{}="{}"]'.format(klíč,  hodnota)
            
    def __radd__(self,  tag):
        return '{}{}'.format(tag,  self.__zápis)

    def __str__(self):
        return self.__zápis
