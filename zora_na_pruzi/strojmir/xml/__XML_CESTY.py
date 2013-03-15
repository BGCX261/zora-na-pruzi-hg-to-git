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
    
    def __init__(self,  _klíč = None,  _hodnota = None,  **kwargs):
        self.__zápis = ''
        
        if _klíč is not None:
            self.__atribut(_klíč,  _hodnota)
            
        for _klíč,  _hodnota in kwargs.items():
            self.__atribut(_klíč,  _hodnota)
            
            
    def __atribut(self,  klíč,  hodnota):
        if hodnota is None:
            zápis = '[@{}]'.format(klíč)
        else:
            zápis = '[@{}="{}"]'.format(klíč,  hodnota)
            
        self.__zápis = self.__zápis + zápis
            
    def __radd__(self,  tag):
        return '{}{}'.format(str(tag),  self.__zápis)

    def __str__(self):
        return self.__zápis
