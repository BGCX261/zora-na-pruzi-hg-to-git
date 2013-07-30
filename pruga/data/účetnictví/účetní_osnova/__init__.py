

from ... import Uzel,  VAZBA

from pruga.neomodel import (StructuredNode, StringProperty, IntegerProperty,
    RelationshipTo, RelationshipFrom)

ÚČTOVÁ_OSNOVA = 'Účtová osnova'
ÚČTOVÁ_TŔÍDA = 'Účtová třída'
ÚČTOVÁ_SKUPINA = 'Účtová skupina'
ÚČET = 'Účet'

ÚČTOVÁ_OSNOVA_MÁ_TŘÍDU = 'MÁ TŘÍDU'
ÚČTOVÁ_TŘÍDA_MÁ_SKUPINU = 'MÁ SKUPINU'
ÚČTOVÁ_SKUPINA_MÁ_ÚČET = 'MÁ ÚČET'


class Účtová_osnova(Uzel):
    __labels__ = ÚČTOVÁ_OSNOVA, 
    
    jméno = StringProperty(unique_index=True)
    
class Účtová_třída(Uzel):
    __labels__ = ÚČTOVÁ_OSNOVA, ÚČTOVÁ_TŔÍDA
    
    číslo = StringProperty(unique_index=True)
    jméno = StringProperty(unique_index=True)
    
class Účtová_skupina(Uzel):
    __labels__ = ÚČTOVÁ_OSNOVA, ÚČTOVÁ_SKUPINA
    
    číslo = StringProperty(unique_index=True)
    jméno = StringProperty(unique_index=True)

    
class Účet(Uzel):
    __labels__ = ÚČTOVÁ_OSNOVA, ÚČET
    
    číslo = StringProperty(unique_index=True)
    jméno = StringProperty(unique_index=True)
    
class MÁ_TŘÍDU(VAZBA):
    __počátek__ = Účtová_osnova, 
    __konec__ = Účtová_třída, 
    __jméno__ = ÚČTOVÁ_OSNOVA_MÁ_TŘÍDU
    
class MÁ_SKUPINU(VAZBA):
    __počátek__ = Účtová_třída, 
    __konec__ = Účtová_skupina, 
    __jméno__ = ÚČTOVÁ_TŘÍDA_MÁ_SKUPINU
    
class MÁ_ÚČET(VAZBA):
    __počátek__ = Účtová_skupina, 
    __konec__ = Účet, 
    __jméno__ = ÚČTOVÁ_SKUPINA_MÁ_ÚČET
