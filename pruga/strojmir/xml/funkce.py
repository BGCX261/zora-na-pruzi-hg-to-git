#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je třída, která umožní zadávat atributy do vyhledávacích řetězců pomocí operátoru plus
'''

import functools

def davaj_jedinečného(element,  třída_hledaného_elementu): #,  **atributy
    '''
    vrací jedinečného potomka
    '''
    
#    for atribut,  hodnota in atributy.items():
#        třída_hledaného_elementu[atribut]  = hodnota
        
    
    elementy = element.findall(str(třída_hledaného_elementu))
    počet_elementů = len(elementy)
    
    if počet_elementů == 0:
        return None
        
    if počet_elementů == 1:
        return elementy[0]
        
    raise ValueError('Žádáš jedinečného potomka {}, ale ten se v {} nachází {} krát.'.format(třída_elementu.TAG_NAME,  self.tag,  počet_elementů))
     
   

#def davaj_či_vytvoř_jedinečného(funkce):
#    @functools.wraps(funkce)
#    def wrapper(self):
#        třída_elementu = funkce(self)
#        element = self._davaj_jedinečného(třída_elementu)
#        if element is None:
#            element = třída_elementu()
#            self.append(element)
#        return element
#        
#    return wrapper
#
#def davaj_obsah_jedinečného(funkce):
#    '''
#   dekorátor, který vrací obsah nějakého vloženého elementu
#    '''
#    @functools.wraps(funkce)
#    def wrapper(self):
#        třída_elementu = funkce(self)
#        element = self._davaj_jedinečného(třída_elementu)
#        if element is not None:
#            return element.text
#        return None
#        
#def nastav_obsah_jedinečného(funkce):
#    '''
#    dekorátor, který nastaví obsah nějakého vloženého elementu
#    '''
#    @functools.wraps(funkce)
#    def wrapper(self,  hodnota): 
#        třída_elementu = funkce(self,  hodnota)
#        if hodnota is None:
#            element = self._davaj_jedinečného(třída_elementu)
#            if element is not None:
#                self.remove(element)
#        else:
#            element = self._davaj_či_vytvoř_jedinečného(třída_elementu)
#            element.text = hodnota
