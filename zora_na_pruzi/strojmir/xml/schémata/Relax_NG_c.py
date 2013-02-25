import lxml.etree

from . import davaj_validátor

Validátor = davaj_validátor(lxml_validátor = lxml.etree.RelaxNG,  přípona_schématu = 'rnc')

class Validátor(Validátor):
    
    __schéma = None
    
    @property
    def schéma(self):
        if self.__schéma is None:
            rnc_soubor = super().schéma
            rng_soubor = '{}.{}'.format(rnc_soubor,  'rng')
            from zora_na_pruzi.strojmir.pomůcky.spustím_příkaz import spustím_příkaz
            příkaz = 'trang {} {}'.format(rnc_soubor,  rng_soubor)
            spustím_příkaz(příkaz)
            self.__schéma = rng_soubor
        return self.__schéma    
    
program = 'jing {schéma} {soubor}'
jing = program
