#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je třída, která umožní zadávat atributy do vyhledávacích řetězců pomocí operátoru plus
'''

class TAGY(dict):
    
    def __init__(self,  namespace):
        self.__NAMESPACE = namespace
        
    def __getattr__(self,  tag):
        return self[tag]
        
    def __missing__(self,  tag):
        if self.__NAMESPACE is not None:
            self[tag] = '{{{}}}{}'.format(self.__NAMESPACE,  tag)
        else:
            self[tag] = tag
            
        return self[tag]

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
