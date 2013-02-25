import os
import lxml.etree


ADRESÁŘ_SCHÉMAT = os.path.dirname(__file__)  

def davaj_validátor(lxml_validátor,  přípona_schématu):

    class Validátor(object):
        
        __třída_validátoru = lxml_validátor
        __validátor = None
        __přípona_schématu = přípona_schématu
        __schéma = None
        __jméno_schématu = None
        
        def __init__(self,  schéma):
#            @TODO: umožnit zadat i externí schéma, například v url, nebo plnou cestu někam jinam
            self.__jméno_schématu = schéma
#            tree = lxml.etree.parse(schéma)
#            self.__validátor = self.__validátor(tree)
          
        @property
        def schéma(self):
            if self.__schéma is None:
                soubor_schématu = os.path.join(ADRESÁŘ_SCHÉMAT,  '{}.{}'.format(self.__jméno_schématu,  self.__přípona_schématu))
                if not os.path.isfile(soubor_schématu):
                    raise AttributeError('Soubor schématu {} nejestvuje.'.format(soubor_schématu))
                self.__schéma = soubor_schématu
            return self.__schéma
            
        @property
        def validátor(self):
            if self.__validátor is None:
                tree = lxml.etree.parse(self.schéma)
                self.__validátor = self.__třída_validátoru(tree)
            return self.__validátor
        
        def __call__(self,  soubor,  program = None):
            
            if not os.path.isfile(soubor):
                raise TypeError('Soubor {} nejestvuje, nelze provést validaci.'.format(soubor))
            
            if program is None:
                parsovaný_xml_soubor = lxml.etree.parse(soubor)
                return self.validátor(parsovaný_xml_soubor)
                
            program = program.format(schéma = self.schéma,  soubor = soubor)
            
            from zora_na_pruzi.strojmir.pomůcky.spustím_příkaz import spustím_příkaz
            return spustím_příkaz(program)

    return Validátor
