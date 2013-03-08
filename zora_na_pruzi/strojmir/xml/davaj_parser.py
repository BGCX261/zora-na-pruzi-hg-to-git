#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import lxml.etree
import lxml.builder

def davaj_parser(jméno_balíčku):
 
    from zora_na_pruzi.strojmir import importuji
    najdu_třídu = importuji.davaj_třídu(jméno_balíčku)
    
    def najdu_třídu_pro_element(tag):
        třída = najdu_třídu(tag.upper())
        if not issubclass(třída,  lxml.etree.ElementBase):
            raise TypeError('Nenašel jsem třídu pro element <{} .. > v balíčku {}'.format(tag,  jméno_balíčku))
        return třída
 
    class Lookup(lxml.etree.CustomElementClassLookup):
        def lookup(self, node_type, document, namespace, name):
            if node_type == 'element':
                třída = najdu_třídu_pro_element(tag = name)
                return třída
    #            except KeyError as e:
    #                if not exception:
    #                    return výchozí_element
    #                else:
    #                    raise e

    parser = lxml.etree.XMLParser(remove_blank_text=True)
    parser.set_element_class_lookup(Lookup())

    def make_element(tag, nsmap = None):
        třída = najdu_třídu_pro_element(tag)
        return třída()

    element_builder = lxml.builder.ElementMaker(makeelement = make_element)
        
    return parser,  element_builder
    
    
