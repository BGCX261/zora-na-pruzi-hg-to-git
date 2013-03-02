import lxml.etree

from . import __Schéma

class Schéma(__Schéma):
    
    __třída_validátoru = lxml.etree.RelaxNG
    __přípona_schématu = 'rng'


program = 'jing {schéma} {soubor}'

jing = program
