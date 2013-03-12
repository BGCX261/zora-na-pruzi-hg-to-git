#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import lxml.etree
import lxml.builder


#class __ElementMaker(lxml.builder.ElementMaker):
class __ElementMaker(object):
    
    _typemap = {
               int: str
               }
               

    def __init__(self, str_z_balíčku, 
                 typemap=None,
                 namespace=None, nsmap=None):
                     
        self.__str_z_balíčku = str_z_balíčku
                     
        if namespace is not None:
            self._namespace = '{' + namespace + '}'
        else:
            self._namespace = None

        if nsmap:
            self._nsmap = dict(nsmap)
        else:
            self._nsmap = None

        if typemap is not None:
            self._typemap.update(typemap)

    def __call__(self, tag, **atributy):
        
        třída_elementu = self._davaj_třídu_elementu(tag)
        
        element = třída_elementu(nsmap=self._nsmap)
            
        for klíč, hodnota in atributy.items():
            if not isinstance(hodnota, str):
                hodnota = self._typemap[type(hodnota)](hodnota)
            element.attrib[klíč] = hodnota

        return element

    def __getattr__(self, tag):
        from functools import partial
        return partial(self, tag)

    def _davaj_třídu_elementu(self,  tag):
        try:
            jméno_modulu = '{}.{}'.format(self.__str_z_balíčku, tag)
            modul = __import__(jméno_modulu, globals(), locals(), [tag], 0)
            objekt = getattr(modul,  tag)
            return objekt
        except ImportError as e:
            raise ImportError('V {} selhal import: {}'.format(__name__,  e)) from e
        except AttributeError as e:
            raise AttributeError('V {} selhalo získání {} z {}: {}'.format(__name__,  tag, modul.__name__,  e)) from e
            

# create factory object
#E = ElementMaker()


def davaj_parser(elementMaker):
 
#    from zora_na_pruzi.strojmir import importuji
#    najdu_třídu = importuji.davaj_importéra(jméno_balíčku)
#    
#    def najdu_třídu_pro_element(tag):
#        jméno_třídy = tag.lower()
#        třída = najdu_třídu(jméno_třídy,  jméno_třídy)
##        esli to není třída,  ale modul,  načteme třídu z toho modulu
##        if not isinstance(třída, type):
##            třída = getattr(třída,  jméno_třídy,  None)
#        if not issubclass(třída,  lxml.etree.ElementBase):
#            raise TypeError('Nenašel jsem třídu {} pro element <{} .. > v balíčku {}'.format(jméno_třídy,  tag,  jméno_balíčku))
#        return třída
 
    class Lookup(lxml.etree.CustomElementClassLookup):
        def lookup(self, node_type, document, namespace, name):
            if node_type == 'element':
                třída = elementMaker._davaj_třídu_elementu(tag = name)
                return třída
    #            except KeyError as e:
    #                if not exception:
    #                    return výchozí_element
    #                else:
    #                    raise e

    parser = lxml.etree.XMLParser(remove_blank_text=True)
    parser.set_element_class_lookup(Lookup())

#    def make_element(tag, nsmap = None):
#        třída = najdu_třídu_pro_element(tag)
#        return třída(nsmap = NSMAP)

#    def číslo_na_řetězec(none,  hodnota):
#        return str(hodnota)

    
#    element_builder = __ElementMaker(makeelement = make_element,  typemap = typemap,  nsmap = NSMAP)
#    element_builder = __ElementMaker(str_z_balíčku = jméno_balíčku, nsmap = NSMAP)
        
    return parser
    
    
