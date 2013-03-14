#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import lxml.etree
import lxml.builder


#class __ElementMaker(lxml.builder.ElementMaker):
class __DAVAJ_ELEMENT(dict):
    
    __parser = None
    __namespace = None
    
    _typemap = {
               int: str
               }
               

    def __init__(self, str_z_balíčku, 
                 typemap=None,
                 namespace=None, nsmap=None):
                     
        self.__str_z_balíčku = str_z_balíčku
                     
        if namespace is not None:
            self.__namespace = namespace

        if nsmap:
            self._nsmap = dict(nsmap)
#        else:
#            self._nsmap = None

        if typemap is not None:
            self._typemap.update(typemap)

    def __call__(self, TAG, **atributy):
        
        class __NSMAP_ELEMENT(object):
#            __slots__ = ('__TŘÍDA_ELEMENTU',  '__NSMAP')
            __NSMAP = self._nsmap
            def __init__(self,  TŘÍDA,  **atributy):
                self.__TŘÍDA_ELEMENTU = TŘÍDA
                
            def __getattr__(self,  klíč):
                return getattr(self.__TŘÍDA_ELEMENTU,  klíč)
                
            def __call__(self,  *args,  **atributy):
                if 'nsmap' in atributy:
                    raise NotImplementedError('NSMAP nebereme, nastavíme si ho sami.')
                if len(args) > 0:
                    raise NotImplementedError('Tož ale argumenty zahodíme, toto nevím co je {}.'.format(str(args)))
                element =  self.__TŘÍDA_ELEMENTU(nsmap = self.__NSMAP,  **atributy)
                for klíč, hodnota in atributy.items():
                    if not isinstance(hodnota, str):
                        hodnota = self._typemap[type(hodnota)](hodnota)
                    element.set(klíč,  hodnota)

                return element
        
        TŘÍDA_ELEMENTU = self[TAG]
        return __NSMAP_ELEMENT(TŘÍDA_ELEMENTU, **atributy)

    def __getattr__(self, TAG):
        return self(TAG)
#        from functools import partial
#        return partial(self, self[TAG])
#        return self[TAG]

    def __missing__(self,  TAG):
        try:
            jméno_modulu = '{}.{}'.format(self.__str_z_balíčku, TAG)
            modul = __import__(jméno_modulu, globals(), locals(), [TAG], 0)
            TŘÍDA_ELEMENTU = getattr(modul,  TAG)
            
            tag = TAG.lower()
            
            TŘÍDA_ELEMENTU.TAG = tag
            TŘÍDA_ELEMENTU.NAMESPACE = self.__namespace
            if self.__namespace is not None:
                TŘÍDA_ELEMENTU.TAG_NAME = '{{{}}}{}'.format(self.__namespace,  tag)
            else:
                TŘÍDA_ELEMENTU.TAG_NAME = tag
                
            TŘÍDA_ELEMENTU.PARSER = self.parser
            
            self[TAG] = TŘÍDA_ELEMENTU
            return self[TAG]
        except ImportError as e:
            raise ImportError('V {} selhal __import__({}, globals(), locals(), [{}], 0): {}'.format(__name__,jméno_modulu, TAG,   e)) from e
        except AttributeError as e:
            raise AttributeError('V {} selhalo získání {} z {}: {}'.format(__name__,  TAG, modul.__name__,  e)) from e
        raise KeyError('Neznámá chyba při hledání třídy')

    def __lshift__(self,  cesta_k_souboru):
        '''
        operátor SOUBOR << soubor:řetězec umožní načíst obsah ze souboru
        '''
        import os
        if not os.path.isfile(cesta_k_souboru):
            raise IOError('Soubor {} nejestvuje.'.format(cesta_k_souboru))
    
        try:
            tree = lxml.etree.parse(cesta_k_souboru,  parser = self.parser)
        except AttributeError as e:
            raise IOError('Soubor {} nelze načíst pro element {}.'.format(cesta_k_souboru,  self.__name__)) from e
    
        root = tree.getroot()
        return root
        
#        if self.TAG != root.TAG:
#            raise TypeError('Soubor {} má kořenový element {}, ale chceme jej načíst pro element {}.'.format(cesta_k_souboru,  root.TAG,  self.TAG))

        tag = lxml.etree.QName(root)

        TŘÍDA_ELEMENTU = getattr(self,  tag.localname.upper())
        
        try:
            element =  TŘÍDA_ELEMENTU(_ELEMENT = root)
        except TypeError as e:
#            raise e
#@TODO: Nyní vypnuté,  kontrolu provedu jen na tag,  nikolivěk na namespace
            raise TypeError('Soubor {} s kořenovým elementem {} se nepodařilo načíst do třídy {}.'.format(cesta_k_souboru,  root.tag,  TŘÍDA_ELEMENTU.__name__)) from e

        return element

    @property
    def parser(self):
     
        if self.__parser is None:
     
            davaj_element = self
         
            class Lookup(lxml.etree.CustomElementClassLookup):
                def lookup(self, node_type, document, namespace, name):
                    if node_type == 'element':
                        třída = davaj_element[name.upper()]
                        return třída

            parser = lxml.etree.XMLParser(remove_blank_text=True)
            parser.set_element_class_lookup(Lookup())
            
            self.__parser = parser

        return self.__parser 
        
        
