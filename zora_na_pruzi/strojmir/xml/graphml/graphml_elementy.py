#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import lxml.etree
from . import NS_GRAPHML

class Vid(object):
    pass

class SOUBOR(object):
    
    def __init__(self,  jméno_souboru):
        pass

class __ELEMENT(lxml.etree.ElementBase):
    
    vid = Vid()
    
    def __str__(self):
        return lxml.etree.tounicode(self,  pretty_print=True)
        
    def __rshift__(self,  soubor):
        '''
        operátor ELEMENT >> soubor:řetězec umožní uložit xml do souboru
        '''
        if not isinstance(soubor,  (str, )):
            raise TypeError('Operátor >> elementu <{}> očekává jméno souboru.'.format(self.tag))
        
        print('uložím element <{0} ... >...</{0}> do souboru {1}'.format(self.tag,  soubor))
          
        with open(soubor, 'w', encoding='utf-8') as zdrojový_soubor:
            kód = str(self)
            zdrojový_soubor.write(kód)
            return kód
            
        raise IOError('Selhalo zapsání elementu <{0} ... >...</{0}> do souboru {}'.format(self.tag,  soubor))


    def __mod__(self,  vrátím):
        '''
        operátor element:ELEMENT % vid:str vrátí reprezentaci uzlu v požadovaném pohledu
        operátor element:ELEMENT % (vid:str, soubor:str) uloží reprezentaci uzlu v požadovaném pohledu do souboru a také ji vrátí
        '''
        
        if isinstance(vrátím,  (tuple,  list)):
            vid,  soubor = vrátím
        else:
            vid,  soubor = vrátím,  None
        
        if not isinstance(vid,  (str,  SOUBOR)):
            raise TypeError('Operátor %  elementu očekává jako argument název souboru šablon, což musí býti řetězec a nikolivěk {}.'.format(type(vid)))

        aktuální_vid = self.vid
        self.vid = vid
        if soubor is None:
            kód = str(self)
        else:
            kód = self >> soubor
        self.vid = aktuální_vid
        return kód

class graphml(__ELEMENT):
        
    @property
    def uzly(self):
        for uzel in self.getroottree().findall('//{}'.format(NS_GRAPHML.node)):
            yield uzel
            
    @property
    def vazby(self):
        for vazba in self.getroottree().findall('//{}'.format(NS_GRAPHML.edge)):
            yield vazba
    
class key(__ELEMENT):
    __default = None
    
    
    @property
    def jméno(self):
        return self.attrib['attr.name']
        
    @property
    def datový_typ(self):
        return self.attrib['attr.type']
    
    @property
    def default(self):
        if self.__default is None:
            default=self.find(NS_GRAPHML.default)
            if default is not None:
                self.__default = default.text
        return self.__default
 

#########################

#class Seznam_klíčů(dict):
#    
#    def __init__(self,  for_element,  xml):
#        if not for_element in ('graph',  'node',  'edge'):
#            raise TypeError('Seznam klíčů může být pouze pro graph, edge, nebo node.')
#        
#        self.__for_element = for_element
#        self.__xml = xml
#        self.__klíče = None
#       
#    def __getitem__(self,  klíč):
#
#        def najdi_definici(klíč):
#            definice_klíče = self.__xml.find(NS_GRAPHML(NS_GRAPHML.key,  klíč = 'id',  hodnota = klíč))
#            
#            if definice_klíče is None:
#                raise KeyError('Klíč <key id = "{}" ... > nejestvuje.'.format(klíč))
#            for_element = definice_klíče.attrib.get('for')
#            if for_element != self.__for_element:
#                raise TypeError('Klíč pro <key id = "{id}" for = "{for_element}" ... > není určen elementu "{má_být}" ale elementu "{for_element}"'.format(id = klíč,  má_být = self.__for_element,  for_element = for_element))
#        
#            return definice_klíče
#            
#        return self.setdefault(klíč,  najdi_definici(klíč))
#      
##    def __missing__(self,  klíč):
##        print('MISSING',  klíč)
#        
#    def get(self,  klíč,  default  = None):
#        try:
#            return self.__getitem__(klíč)
#        except KeyError:
#            return default
#        
#    def items(self):
#        for klíč in self.keys():
#            yield (klíč,  self[klíč])
#        
#    def __iter__(self):
#        if self.__klíče is None:
#            klíče = []
#            print('AAA ',  NS_GRAPHML(NS_GRAPHML.key,  klíč = 'for',  hodnota = self.__for_element))
#            print(self.__for_element)
#            for definice in self.__xml.findall(NS_GRAPHML(NS_GRAPHML.key,  klíč = 'for',  hodnota = self.__for_element)):
#                print('KEZ ',  definice.attrib['id'],  definice.attrib['for'])
#                klíče.append(definice.attrib['id'])
#            self.__klíče = klíče
#        return iter(self.__klíče)
#       
##    funkce keys() dělá totéž co __iter__
#    keys = __iter__

###################

#class DATA(object):
#    
#    def __init__(self,  for_element):
#        self.__for_element = for_element
#        self.__klíče = None
#    
#    def __get__(self,  instance,  owner):
#        data = instance.findall(NS_GRAPHML.data)
#        if self.__klíče is None:
#            self.__klíče = Seznam_klíčů(for_element = self.__for_element,  xml = instance.getroottree())
#
##        for klíč,  hodnota in self.__klíče.items():
##            print(klíč, ' -> ',  hodnota)
#            
#        for údaj in data:
#            print('JMÉNO ÚDAJE',  údaj.jméno)
#            print('DATOVÝ TYP ÚDAJE',  údaj.datový_typ)
#        return data
 
class __PRVEK_GRAFU(__ELEMENT):
    @property
    def jméno(self):
        return self.attrib['id']

    @property
    def data(self):
        return self.findall(NS_GRAPHML.data)

class graph(__PRVEK_GRAFU):
    pass
    
class node(__PRVEK_GRAFU):
    pass
    
class edge(__PRVEK_GRAFU):
    pass
    
#class default(__ELEMENT):
#    pass


class KLÍČE(dict):
    __xml_id = None
    def __get__(self,  instance,  owner):
        id_klíče = instance.attrib['key']
        
        def najdi_definici(id_klíče):
            xml = instance.getroottree()
#            @TODO enom esli se mi tu nebuddu m9chat ruyn0 grafz
            print('SE HEN')
            hash = str(xml.getroot())
            print(hash)
            if self.__xml_id is None:
                self.__xml_id = hash
            else:
                if self.__xml_id != hash:
                    print(self.__xml_id,  hash)
                    raise RuntimeError('Inu tož míchajú sa grafy různé')
                
            definice_klíče = xml.find(NS_GRAPHML(NS_GRAPHML.key,  klíč = 'id',  hodnota = id_klíče))
            
            if definice_klíče is None:
                raise KeyError('Klíč <key id = "{}" ... > nejestvuje.'.format(id_klíče))
            
            for_element_klíče = definice_klíče.attrib.get('for')
            for_element_údaje = instance.getparent().tag
            if  not for_element_údaje.endswith(for_element_klíče):
                raise TypeError('Klíč pro <key id = "{id}" for = "{for_element}" ... > není určen elementu "{má_být}" ale elementu "{for_element}"'.format(id = id_klíče,  má_být = for_element_údaje,  for_element = for_element_klíče))
        
            return definice_klíče
            
        return  self.setdefault(id_klíče,  najdi_definici(id_klíče))
        
        

class data(__ELEMENT):
    
    __klíč = KLÍČE()
    
    @property
    def jméno(self):
        return self.__klíč.jméno
        
    @property
    def datový_typ(self):
        return self.__klíč.datový_typ
    
    @property
    def default(self):
        return self.__klíč.default
