#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import lxml.etree


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
          
        xml_deklarace = lxml.etree.PI('xml', "version='1.0' encoding='UTF-8'")
        xml_deklarace= lxml.etree.tounicode(xml_deklarace,  pretty_print=True)
          
        with open(soubor, 'w', encoding='utf-8') as zdrojový_soubor:
            zdrojový_soubor.write(xml_deklarace)
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
