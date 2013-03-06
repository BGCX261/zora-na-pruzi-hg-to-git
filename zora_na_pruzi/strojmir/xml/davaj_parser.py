#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import lxml.etree

from .__ELEMENT import __ELEMENT

class __Hledám_třídu_pro_element(dict):
    
    def __init__(self,  v_modulu):
        self.__modul = v_modulu
    
    def get(self,  klíč,  default = None):
        try:
            return self[klíč]
        except AttributeError:
            return default
        
    def __missing__(self,  klíč):
        #        nejdřív zkusím načíst
        print('Hledám třídu elementu {} v {}'.format(klíč,  self.__modul))
        třída = getattr(self.__modul,  klíč,  None)
        
        if třída is None:
#            včíl zkusím ještě najít modul,  ak je v samostatném modulu
            print('Nenašel. Tož včíl hledám třídu elementu v modulu')
            from zora_na_pruzi.system.python.načtu_modul import načtu_modul_podle_balíčku
            try:
                modul_třídy = načtu_modul_podle_balíčku(podle_balíčku = self.__modul, jméno_modulu =  klíč)
            except ImportError as e:
                raise KeyError('Modul s Třídou pro element {} nejestvuje v balíčku {}'.format(klíč,  self.__modul.__name__),  e)
            
            třída = getattr(modul_třídy,  klíč,  None)
            if třída is None:
                raise KeyError('Třída pro element {} nejestvuje v modulu {}'.format(klíč,  modul_třídy.__name__))

        self[klíč] = třída
        return třída


def davaj_parser(v_modulu,  výchozí_element = __ELEMENT,  exception = True):
   
    třídy_elementů = __Hledám_třídu_pro_element(v_modulu = v_modulu)
   
    class Lookup(lxml.etree.CustomElementClassLookup):
        def lookup(self, node_type, document, namespace, name):
            if node_type == 'element':
                try:
                    return třídy_elementů[name.upper()]
                except KeyError as e:
                    if not exception:
                        return výchozí_element
                    else:
                        raise e
            
    parser = lxml.etree.XMLParser(remove_blank_text=True)
    parser.set_element_class_lookup(Lookup())
        
    return parser
    
    
