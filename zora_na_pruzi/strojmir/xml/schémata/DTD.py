import lxml.etree

from . import davaj_validátor

Validátor = davaj_validátor(lxml_validátor = lxml.etree.DTD,  přípona_schématu = 'dtd')

class Validátor(Validátor):
    
    __validátor = None
    
    @property
    def validátor(self):
        if self.__validátor is None:
            with open(self.schéma,  encoding='UTF-8',  mode='r') as soubor:
                self.__validátor = lxml.etree.DTD(soubor)
        return self.__validátor
        
program = 'xmllint --noout --dtdvalid {schéma} {soubor}'

xmllint = program
