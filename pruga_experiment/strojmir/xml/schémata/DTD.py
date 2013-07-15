import lxml.etree

from . import __Schéma

class Schéma(__Schéma):
    
    __třída_validátoru = lxml.etree.DTD
    __přípona_schématu = 'dtd'
#    __validátor = None
    
    @property
    def validátor(self):
        if self.__validátor is None:
            with open(self.soubor_schématu,  encoding='UTF-8',  mode='r') as soubor:
                self.__validátor = lxml.etree.DTD(soubor)
        return self.__validátor
        
program = 'xmllint --noout --dtdvalid {schéma} {soubor}'

xmllint = program
