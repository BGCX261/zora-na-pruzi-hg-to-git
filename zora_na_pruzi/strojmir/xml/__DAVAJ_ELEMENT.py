#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import lxml.etree


#class __ElementMaker(lxml.builder.ElementMaker):
class __DAVAJ_ELEMENT(dict):
    
    __parser = None
    
    class X(object):
        pass

    def __init__(self, nastavení):
        '''
        nastavení je modul, kde jsou uvedeny všechny předvolby
        '''
        self.__nastavení = nastavení
        
        NSMAP = self.__nastavení.nsmap
        TYPEMAP = self.__nastavení.typemap
        
        TYPEMAP.setdefault(str,  lambda x: x)
        
        import itertools
        
        class __NSMAP_ELEMENT(dict):
#            __slots__ = ('__TŘÍDA_ELEMENTU',  '__NSMAP')

#            __NSMAP = nsmap
#            typemap = _typemap
            
            def __init__(self,  TŘÍDA,  **atributy):
                self.__TŘÍDA_ELEMENTU = TŘÍDA
                self.update(atributy)
                
            def __getattr__(self,  klíč):
                return getattr(self.__TŘÍDA_ELEMENTU,  klíč)
                
            def __str__(self):
                zápis = []
                for atribut,  hodnota in self.items():
                    if hodnota is None:
                        zápis.append('[@{}]'.format(atribut))
                    else:
                        hodnota = TYPEMAP[type(hodnota)](hodnota)
                        zápis.append('[@{}="{}"]'.format(atribut,  hodnota))
                        
                return '{}{}'.format(self.TAG_NAME, ''.join(zápis))
                
            def __call__(self,  *args,  **atributy):
                if 'nsmap' in atributy:
                    raise NotImplementedError('NSMAP nebereme, nastavíme si ho sami.')
                if len(args) > 0:
                    raise NotImplementedError('Tož ale argumenty zahodíme, toto nevím co je {}.'.format(str(args)))
                    
                element =  self.__TŘÍDA_ELEMENTU(nsmap = NSMAP)
                
#                nejdříve původní atributy
                for klíč, hodnota in itertools.chain(self.items(),  atributy.items()):
                    if hodnota is None:
#                        @TODO: chtěl bych v duchu HTML nikoliv psát <input require="required" > ale prosto <input required >
                        hodnota = klíč
                        
                    hodnota = TYPEMAP[type(hodnota)](hodnota)
                    element.set(klíč,  hodnota)

                return element

        self.__NSMAP_ELEMENT = __NSMAP_ELEMENT

    def __call__(self, TAG, **atributy):
        
        TŘÍDA_ELEMENTU = self[TAG]
        return self.__NSMAP_ELEMENT(TŘÍDA_ELEMENTU, **atributy)

    def __getattr__(self, TAG):
        return self(TAG)

    def __missing__(self,  TAG):
        try:
            jméno_modulu = '{}.{}'.format(self.__nastavení.balíček, TAG)
            modul = __import__(jméno_modulu, globals(), locals(), [TAG], 0)
            TŘÍDA_ELEMENTU = getattr(modul,  TAG)
            
            tag = TAG.lower()
            namespace = self.__nastavení.namespace
            TŘÍDA_ELEMENTU.TAG = tag
            if namespace is not None:
                TŘÍDA_ELEMENTU.NAMESPACE = namespace
                TŘÍDA_ELEMENTU.TAG_NAME = '{{{}}}{}'.format(namespace,  tag)
            else:
                TŘÍDA_ELEMENTU.TAG_NAME = tag
                
            TŘÍDA_ELEMENTU.PARSER = self.parser
            
            self[TAG] = TŘÍDA_ELEMENTU
            return self[TAG]
        except ImportError as e:
            raise ImportError('V {} selhal __import__({}, globals(), locals(), [{}], 0): {}'.format(__name__,jméno_modulu, TAG,   e)) from e
        except AttributeError as e:
            raise AttributeError('V {} selhalo získání {} z {}: {}'.format(__name__,  TAG, jméno_modulu,  e)) from e
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

            parser = self.__nastavení.parser()
            parser.set_element_class_lookup(Lookup())
            
            self.__parser = parser

        return self.__parser 
        
        
