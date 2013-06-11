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


class __ELEMENT(lxml.etree.ElementBase):
        
    @property
    def id(self):
#        _id = self.attrib.get('id',  None)
#        if _id is None:
#            self.attrib['id'] = '{}_{}'.format(self.__class__.__name__,  id(self))
        return self.attrib['id']
    
    def __str__(self):
        return lxml.etree.tounicode(self,  pretty_print=True)

    @property
    def xml_hlavička(self):
        xml_deklarace = lxml.etree.PI('xml', "version='1.0' encoding='UTF-8'")
        xml_deklarace= lxml.etree.tounicode(xml_deklarace,  pretty_print=True)
        
        from zora_na_pruzi.strojmir.hlavička import hlavička_automaticky_vytvořila, WEB_PROJEKTU,  WEB_ZDROJOVÝCH_KÓDŮ

        for komentář in self.iterchildren(tag = lxml.etree.Comment):
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
            raise TypeError('Operátor >> očekává jméno souboru.')
        
        print('uložím element <{2} ... > ... </{2}> třídy {0} do souboru {1}'.format(self.__class__.__name__,  soubor,  self.tag))
        
        with open(soubor,  mode ='w',  encoding = 'UTF-8') as otevřený_soubor:
            otevřený_soubor.write(self.xml_hlavička)
            otevřený_soubor.write(str(self))
            
    def __lshift__(self,  element):
        '''
        operátor TENTO_ELEMENT << PODELEMENT umožní vložit podlement
        '''
        if not isinstance(element,  (lxml.etree.ElementBase, )):
            raise TypeError('Operátor << očekává element a nikolivěk {}.'.format(type(element)))
        
        self.append(element)
        return element

    def _davaj_jedinečného(self,  třída_elementu):
        '''
        pomocná metoda, která vrací jedinečného potomka
        '''
        elementy = self.findall(str(třída_elementu))
        počet_elementů = len(elementy)
        
        if počet_elementů == 0:
            return None
            
        if počet_elementů == 1:
            return elementy[0]
            
        raise ValueError('Žádáš jedinečného potomka {}, ale ten se v {} nachází {} krát.'.format(třída_elementu.TAG_NAME,  self.tag,  počet_elementů))
            

    def _davaj_či_vytvoř_jedinečného(self,  třída_elementu):
        element = self._davaj_jedinečného(třída_elementu)
        if element is None:
            element = třída_elementu()
            self.append(element)
        return element

    def _davaj_obsah_jedinečného(self,  třída_elementu):
        '''
        pomocná metoda, která vrací obsah nějakého vloženého elementu
        '''
        element = self._davaj_jedinečného(třída_elementu)
        if element is not None:
            return element.text
        return None
        
    def _nastav_obsah_jedinečného(self,  třída_elementu,  hodnota):
        '''
        pomocná metoda, která nastaví obsah nějakého vloženého elementu
        '''
        
        if hodnota is None:
            element = self._davaj_jedinečného(třída_elementu)
            if element is not None:
                self.remove(element)
        else:
            element = self._davaj_či_vytvoř_jedinečného(třída_elementu)
            element.text = hodnota
