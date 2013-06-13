import lxml.etree 

from . import __Schéma

class Schéma(__Schéma):
    
    __třída_validátoru = lxml.etree.XMLSchema
    __přípona_schématu = 'xsd'

program = 'xmllint --noout --schema {schéma} {soubor}'

xmllint = program
