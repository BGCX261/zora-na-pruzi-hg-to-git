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
            yield uzel.attrib['id']
            
    @property
    def vazby(self):
        for uzel in self.getroottree().findall('//{}'.format(NS_GRAPHML.edge)):
            yield uzel.attrib['id']
    
class key(__ELEMENT):
    __default = None
    @property
    def default(self):
        if self.__default is None:
            default=self.find(NS_GRAPHML.default)
            if default is not None:
                self.__default = default.text
        return self.__default
    
class graph(__ELEMENT):
    pass
    
class node(__ELEMENT):
    pass
    
class edge(__ELEMENT):
    pass
    
#class default(__ELEMENT):
#    pass

#class data(__ELEMENT):
#    pass
