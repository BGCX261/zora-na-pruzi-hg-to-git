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


#class TAG_QNAME(dict):
#    
#    def __get__(self,  instance,  owner = None):
#        tag = instance.tag
#        if not tag in self:
#            self[instance.TAG] = lxml.etree.QName(tag)
#        return self[tag]

#class __ELEMENT(lxml.etree.ElementBase):
class __ELEMENT(object):
    
    _TAG = None
    _NAMESPACE = None
    _NSMAP = {}
    
    def __init__(self, __element = None,  **kwargs):
        
        if self._TAG is None:
            tag = self.__class__.__name__.lower()
        
        if self._NAMESPACE is not None:
            tag = '{{{}}}{}'.format(self._NAMESPACE,  tag)
        
        if __element is not None:
            if tag != __element.tag:
                tag_elementu = lxml.etree.QName(__element)
                if tag_elementu.namespace is None and tag_elementu.localname ==  self.__class__.__name__.lower():
                    self._ELEMENT = __element
                else:
                    raise TypeError('Třída {} očekává kořenový element {}, ale chceme jí předat element {}.'.format(self.__class__.__name__,  tag,  __element.tag))
            
        else:        
            
            self._ELEMENT = lxml.etree.Element(tag,  nsmap = self._NSMAP)
    
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
        return self.attrib['id']
    
    def __str__(self):
        return lxml.etree.tounicode(self._ELEMENT,  pretty_print=True)

    @property
    def xml_hlavička(self):
        xml_deklarace = lxml.etree.PI('xml', "version='1.0' encoding='UTF-8'")
        xml_deklarace= lxml.etree.tounicode(xml_deklarace,  pretty_print=True)
        
        from zora_na_pruzi.strojmir.hlavička import hlavička_automaticky_vytvořila, WEB_PROJEKTU,  WEB_ZDROJOVÝCH_KÓDŮ

        for komentář in self.iter(tag = lxml.etree.Comment):
            self.remove(komentář)
    
        self.insert(0, lxml.etree.Comment(hlavička_automaticky_vytvořila()))
        self.insert(1, lxml.etree.Comment(WEB_PROJEKTU))
        self.insert(2, lxml.etree.Comment(WEB_ZDROJOVÝCH_KÓDŮ))
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
