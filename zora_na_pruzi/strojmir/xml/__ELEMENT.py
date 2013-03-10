#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import lxml.etree


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


class TAG_QNAME(dict):
    
    def __get__(self,  instance,  owner = None):
        tag = instance.tag
        if not tag in self:
            self[instance.TAG] = lxml.etree.QName(tag)
        return self[tag]

class __ELEMENT(lxml.etree.ElementBase):
    
    
    TAG_QNAME = TAG_QNAME()
    
#    def __getattr__(self,  tag):
#        return self.ELEMENT(tag)
        
    @property
    def id(self):
#        _id = self.attrib.get('id',  None)
#        if _id is None:
#            self.attrib['id'] = '{}_{}'.format(self.__class__.__name__,  id(self))
        return self.attrib['id']
    
    def __str__(self):
        return lxml.etree.tounicode(self,  pretty_print=True)

    @property
    def xml_deklarace(self):
        xml_deklarace = lxml.etree.PI('xml', "version='1.0' encoding='UTF-8'")
        xml_deklarace= lxml.etree.tounicode(xml_deklarace,  pretty_print=True)
        return xml_deklarace

    def __rshift__(self,  soubor):
        '''
        operátor SOUBOR >> soubor:řetězec umožní uložit obsah do souboru
        '''
        if not isinstance(soubor,  (str, )):
            raise TypeError('Operátor >> očekává jméno souboru.'.format(self.tag))
        
        print('uložím objekt {0} do souboru {1}'.format(self.__class__.__name__,  soubor))
        
        from zora_na_pruzi.strojmir.VÝSTUP import DO_SOUBORU
        
        with DO_SOUBORU(soubor):
            print(self)

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
