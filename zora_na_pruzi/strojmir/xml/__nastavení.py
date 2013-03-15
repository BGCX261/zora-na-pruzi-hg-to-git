#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je třída, která umožní zadávat atributy do vyhledávacích řetězců pomocí operátoru plus
'''

typemap = {
    int: str
    }
    
def parser():
    '''
    Available boolean keyword arguments:

    attribute_defaults - read the DTD (if referenced by the document) and add the default attributes from it
    dtd_validation - validate while parsing (if a DTD was referenced)
    load_dtd - load and parse the DTD while parsing (no validation is performed)
    no_network - prevent network access when looking up external documents (on by default)
    ns_clean - try to clean up redundant namespace declarations
    recover - try hard to parse through broken XML
    remove_blank_text - discard blank text nodes between tags, also known as ignorable whitespace. This is best used together with a DTD or schema (which tells data and noise apart), otherwise a heuristic will be applied.
    remove_comments - discard comments
    remove_pis - discard processing instructions
    strip_cdata - replace CDATA sections by normal text content (on by default)
    resolve_entities - replace entities by their text value (on by default)
    huge_tree - disable security restrictions and support very deep trees and very long text content (only affects libxml2 2.7+)
    compact - use compact storage for short text content (on by default)

Other keyword arguments:

    encoding - override the document encoding
    target - a parser target object that will receive the parse events (see The target parser interface)
    schema - an XMLSchema to validate against (see validation)

    XMLParser(self,
                        encoding=None,
                        attribute_defaults=False,
                        dtd_validation=False,
                        load_dtd=False,
                        no_network=True,
                        ns_clean=False,
                        recover=False,
                        XMLSchema schema=None,
                        remove_blank_text=False,
                        resolve_entities=True,
                        remove_comments=False,
                        remove_pis=False,
                        strip_cdata=True,
                        target=None,
                        compact=True
                        )
    '''
    from lxml.etree import  XMLParser
    return XMLParser(
                     remove_blank_text = True, 
                     remove_comments = True, 
                     ns_clean = True
                     )
