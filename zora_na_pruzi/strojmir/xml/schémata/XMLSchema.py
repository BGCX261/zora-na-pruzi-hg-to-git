import lxml.etree 

from . import davaj_validátor

Validátor = davaj_validátor(lxml_validátor = lxml.etree.XMLSchema,  přípona_schématu = 'xsd')

program = 'xmllint --noout --schema {schéma} {soubor}'

xmllint = program
