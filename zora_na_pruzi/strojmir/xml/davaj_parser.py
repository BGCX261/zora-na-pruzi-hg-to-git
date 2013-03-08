#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import lxml.etree
import lxml.builder

def davaj_parser(jméno_balíčku):
 
    def najdu_třídu(tag,  nsmap = None):
        jméno_třídy = tag.upper()
        balíček = __import__(jméno_balíčku, globals(), locals(), [jméno_třídy], 0)
        třída = getattr(balíček,  jméno_třídy)
        
        if not isinstance(třída, type):
            třída = getattr(třída,  jméno_třídy,  None)
            
        if not issubclass(třída,  lxml.etree.ElementBase):
            raise TypeError('Nenašel jsem třídu {} pro element <{} .. > v balíčku {}'.format(jméno_třídy,  tag,  jméno_balíčku)) 
 
        return třída
 
    class Lookup(lxml.etree.CustomElementClassLookup):
        def lookup(self, node_type, document, namespace, name):
            if node_type == 'element':
                třída = najdu_třídu(tag = name)
                return třída
    #            except KeyError as e:
    #                if not exception:
    #                    return výchozí_element
    #                else:
    #                    raise e

    parser = lxml.etree.XMLParser(remove_blank_text=True)
    parser.set_element_class_lookup(Lookup())

    def make_element(tag, nsmap = None):
        třída = najdu_třídu(tag)
        return třída()

    element_builder = lxml.builder.ElementMaker(makeelement = make_element)
        
    return parser,  element_builder
    
    
