import lxml.etree

from . import __Schéma

class Schéma(__Schéma):
    
    __třída_validátoru = lxml.etree.RelaxNG
    __přípona_schématu = 'rnc'
#    __soubor_schématu = None
    
    @property
    def soubor_schématu(self):
        if self.__soubor_schématu is None:
            rnc_soubor = super().soubor_schématu
            rng_soubor = '{}.{}'.format(rnc_soubor,  'rng')
            from zora_na_pruzi.system.spustím_příkaz import spustím_příkaz_a_vypíšu
            příkaz = 'trang {} {}'.format(rnc_soubor,  rng_soubor)
            spustím_příkaz_a_vypíšu(příkaz)
            self.__soubor_schématu = rng_soubor
        return self.__soubor_schématu    
    
program = 'jing {schéma} {soubor}'
jing = program
