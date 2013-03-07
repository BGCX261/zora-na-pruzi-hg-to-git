#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import lxml.etree

def davaj_parser(jméno_balíčku):
 
    class Lookup(lxml.etree.CustomElementClassLookup):
        def lookup(self, node_type, document, namespace, name):
            if node_type == 'element':
                jméno_třídy = name.upper()
                balíček = __import__(jméno_balíčku, globals(), locals(), [jméno_třídy], 0)
                třída = getattr(balíček,  jméno_třídy)
                
                if not isinstance(třída, type):
                    třída = getattr(třída,  jméno_třídy,  None)
                    
                if not issubclass(třída,  lxml.etree.ElementBase):
                    raise TypeError('Nenašel jsem třídu {} pro element <{} .. > v balíčku {}'.format(jméno_třídy,  name,  jméno_balíčku))
    #            try:
#                from zora_na_pruzi.system.python.načtu_modul import načtu_modul
#    #                return třídy_elementů[name.upper()]
#                
##                modul = načtu_modul_podle_balíčku(jméno_modulu = jméno_třídy,  podle_balíčku = jméno_balíčku,  v_adresáři = adresář)
#                modul = načtu_modul(jméno_modulu = jméno_třídy,  jméno_balíčku = jméno_balíčku,  adresář_modulu = adresář)
#                třída = getattr(modul, jméno_třídy,  None)
                return třída
    #            except KeyError as e:
    #                if not exception:
    #                    return výchozí_element
    #                else:
    #                    raise e

    parser = lxml.etree.XMLParser(remove_blank_text=True)
    parser.set_element_class_lookup(Lookup())
        
    return parser
    
    
