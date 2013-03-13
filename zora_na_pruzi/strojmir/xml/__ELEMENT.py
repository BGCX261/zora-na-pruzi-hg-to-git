#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

#import os

try:
    import lxml.etree
except ImportError:
     raise ImportError('Potřebuji knihovnu lxml')


def print_info(tree):
    
    if not isinstance(tree,  lxml.etree._ElementTree):
        tree = tree.getroottree()
        
    docinfo = tree.docinfo
    
    print('-'*9)
    print('| ',  'DOCINFO',  ' |')
    print('-'*9)
    for parametr in 'URL', 'doctype',  'encoding',  'externalDTD',  'internalDTD', 'public_id',  'root_name',  'standalone',  'system_url',  'xml_version':
        print('{}: {}'.format(parametr,  getattr(docinfo,  parametr)))
    
    print('-'*44)


class __METATŘÍDA_ELEMENTU(type):
    
    def __init__(cls,  classname,  bases,  dictionary):
        if not 'TAG' in dictionary:
            setattr(cls,  'TAG',  classname.lower())
            
        namespace = getattr(cls, 'NAMESPACE',  None)
            
        if namespace is not None:
            cls.TAG_NAME = '{{{}}}{}'.format(namespace,  cls.TAG)
        else:
            cls.TAG_NAME = cls.TAG
            
        return super().__init__(classname,  bases,  dictionary)

class __ELEMENT(object,  metaclass = __METATŘÍDA_ELEMENTU):
    
    _NSMAP = {}
    
    def __init__(self, _ELEMENT = None,  **kwargs):
        
        if _ELEMENT is not None:
            if  _ELEMENT.tag not in (self.TAG_NAME,  self.TAG):
                    raise TypeError('Třída {} očekává kořenový element {}, ale chceme jí předat element {}.'.format(self.__class__.__name__,  self.TAG_NAME,  _ELEMENT.tag))
            else:
                self._ELEMENT = _ELEMENT
        else:        
            try:
                self._ELEMENT = lxml.etree.Element(self.TAG_NAME,  nsmap = self._NSMAP,  **kwargs)
            except TypeError as e:
                raise TypeError('Selhalo lxml.etree.Element({},  nsmap = {},  **{})'.format(self.TAG_NAME, self._NSMAP,   kwargs)) from e
        
#    @property
#    def TAG(self):
#        if self._TAG is not None:
#            return self._TAG
#        if self._NAMESPACE is not None:
#            return '{{{}}}{}'.format(NAMESPACE,  self.__class__.__name__)
#        return self.__class__.__name__
#    TAG_QNAME = TAG_QNAME()
    
#    def __getattr__(self,  tag):
#        return self.ELEMENT(tag)
        
    @property
    def id(self):
#        _id = self.attrib.get('id',  None)
#        if _id is None:
#            self.attrib['id'] = '{}_{}'.format(self.__class__.__name__,  id(self))
        return self._ELEMENT.attrib['id']
    
    def __str__(self):
        return lxml.etree.tounicode(self._ELEMENT,  pretty_print=True)

    @property
    def xml_hlavička(self):
        xml_deklarace = lxml.etree.PI('xml', "version='1.0' encoding='UTF-8'")
        xml_deklarace= lxml.etree.tounicode(xml_deklarace,  pretty_print=True)
        
        from zora_na_pruzi.strojmir.hlavička import hlavička_automaticky_vytvořila, WEB_PROJEKTU,  WEB_ZDROJOVÝCH_KÓDŮ

        _ELEMENT = self._ELEMENT

        for komentář in _ELEMENT.iter(tag = lxml.etree.Comment):
            self.remove(komentář)
    
        _ELEMENT.insert(0, lxml.etree.Comment(hlavička_automaticky_vytvořila()))
        _ELEMENT.insert(1, lxml.etree.Comment(WEB_PROJEKTU))
        _ELEMENT.insert(2, lxml.etree.Comment(WEB_ZDROJOVÝCH_KÓDŮ))
        return xml_deklarace

    def __rshift__(self,  soubor):
        '''
        operátor SOUBOR >> soubor:řetězec umožní uložit obsah do souboru
        '''
        if not isinstance(soubor,  (str, )):
            raise TypeError('Operátor >> očekává jméno souboru.'.format(self.tag))
        
        print('uložím objekt {0} do souboru {1}'.format(self.__class__.__name__,  soubor))
        
        with open(soubor,  mode ='w',  encoding = 'UTF-8') as otevřený_soubor:
            otevřený_soubor.write(self.xml_hlavička)
            otevřený_soubor.write(str(self))



#    def __mod__(self,  vrátím):
#        '''
#        operátor element:ELEMENT % vid:str vrátí reprezentaci uzlu v požadovaném pohledu
#        operátor element:ELEMENT % (vid:str, soubor:str) uloží reprezentaci uzlu v požadovaném pohledu do souboru a také ji vrátí
#        '''
#        
#        if isinstance(vrátím,  (tuple,  list)):
#            vid,  soubor = vrátím
#        else:
#            vid,  soubor = vrátím,  None
#        
#        if not isinstance(vid,  (str,  SOUBOR)):
#            raise TypeError('Operátor %  elementu očekává jako argument název souboru šablon, což musí býti řetězec a nikolivěk {}.'.format(type(vid)))
#
#        aktuální_vid = self.vid
#        self.vid = vid
#        if soubor is None:
#            kód = str(self)
#        else:
#            kód = self >> soubor
#        self.vid = aktuální_vid
#        return kód
