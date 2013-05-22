#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je výraz používaný ve where, join on atd.
'''

from .formát import formát_hodnoty

class výraz(object):
    
    def __init__(self,  pravý,  operátor,  levý):
        
#        if isinstance(levý,  str):
        levý = formát_hodnoty(levý)
        
        self.__slova = (pravý,  operátor,  levý)
        
    def __str__(self):
        return ''.join(map(str,  self.__slova))
        
    def __rozšířím_výraz(self,  other,  operátor):
        slova = ['(']
        slova.extend(self.__slova)
        slova.append(')')
        slova.append(operátor)
        
        if isinstance(other,  výraz):
            slova.append('(')
            slova.append(other)
            slova.append(')')
        else:
            raise TypeError('druhý člen pro AND musí být také výraz')
        self.__slova = slova
        return self

    def AND(self,  other):
        self.__rozšířím_výraz(other,  ' AND ')
        return self
    
    def OR(self,  other):
        self.__rozšířím_výraz(other,  ' OR ')
        return self
