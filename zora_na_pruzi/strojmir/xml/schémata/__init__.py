import os
import lxml.etree


ADRESÁŘ_SCHÉMAT = os.path.dirname(__file__)  

#def davaj_validátor(lxml_validátor,  přípona_schématu):

class __Schéma(object):
    
    __třída_validátoru = None
    __validátor = None
    __přípona_schématu = None
    __soubor_schématu = None
    __jméno_schématu = None
    
    def __init__(self,  schéma):
#            @TODO: umožnit zadat i externí schéma, například v url, nebo plnou cestu někam jinam
        self.__jméno_schématu = schéma
#            tree = lxml.etree.parse(schéma)
#            self.__validátor = self.__validátor(tree)
      
    @property
    def soubor_schématu(self):
        if self.__soubor_schématu is None:
            soubor_schématu = os.path.join(ADRESÁŘ_SCHÉMAT,  '{}.{}'.format(self.__jméno_schématu,  self.__přípona_schématu))
            if not os.path.isfile(soubor_schématu):
                raise AttributeError('Soubor schématu {} nejestvuje.'.format(soubor_schématu))
            self.__soubor_schématu = soubor_schématu
        return self.__soubor_schématu
        
    @property
    def validátor(self):
        if self.__validátor is None:
            tree = lxml.etree.parse(self.soubor_schématu)
            print(self.__třída_validátoru)
            self.__validátor = self.__třída_validátoru(tree)
        return self.__validátor
    
    def __call__(self,  soubor,  program = None):
        
        if not os.path.isfile(soubor):
            raise TypeError('Soubor {} nejestvuje, nelze provést validaci.'.format(soubor))
        
        if program is None:
            parsovaný_xml_soubor = lxml.etree.parse(soubor)
            return self.validátor(parsovaný_xml_soubor)
            
        program = program.format(schéma = self.soubor_schématu,  soubor = soubor)
        
        from zora_na_pruzi.system.spustím_příkaz import spustím_příkaz
        return spustím_příkaz(program)

#    return Validátor
