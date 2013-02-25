import lxml.etree

from . import davaj_validátor

Validátor = davaj_validátor(lxml_validátor = lxml.etree.RelaxNG,  přípona_schématu = 'rng')

program = 'jing {schéma} {soubor}'

jing = program
