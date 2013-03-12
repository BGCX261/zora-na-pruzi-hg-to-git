#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import lxml.etree
import lxml.builder

def davaj_parser(jméno_balíčku,  NSMAP):
 
    from zora_na_pruzi.strojmir import importuji
    najdu_třídu = importuji.davaj_importéra(jméno_balíčku)
    
    def najdu_třídu_pro_element(tag):
        jméno_třídy = tag.upper()
        třída = najdu_třídu(jméno_třídy)
#        esli to není třída,  ale modul,  načteme třídu z toho modulu
        if not isinstance(třída, type):
            třída = getattr(třída,  jméno_třídy,  None)
        if not issubclass(třída,  lxml.etree.ElementBase):
            raise TypeError('Nenašel jsem třídu {} pro element <{} .. > v balíčku {}'.format(jméno_třídy,  tag,  jméno_balíčku))
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

    def make_element(tag, nsmap = NSMAP):
        třída = najdu_třídu_pro_element(tag)
        return třída(nsmap = NSMAP)

    def číslo_na_řetězec(none,  hodnota):
        return str(hodnota)

    typemap = {
               int: číslo_na_řetězec
               }
    element_builder = lxml.builder.ElementMaker(makeelement = make_element,  typemap = typemap)
        
    return parser,  element_builder
    
    
