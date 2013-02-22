import os
import lxml.etree


ADRESÁŘ_SCHÉMAT = os.path.dirname(__file__)  

class _Soubory_schémat(dict):
    
    def __init__(self,  přípona):
        self._přípona = přípona
        
    def __missing__(self,  jméno_schématu):
        self[jméno_schématu] = os.path.join(ADRESÁŘ_SCHÉMAT,  '{}.{}'.format(jméno_schématu,  self._přípona))
        return self[jméno_schématu]
        
class _Soubory_schémat_rnc_rng(_Soubory_schémat):
        
    def __missing__(self,  jméno_schématu):
        rnc_soubor = super().__missing__(jméno_schématu)
        rng_soubor = '{}.{}'.format(rnc_soubor,  'rng')
        from zora_na_pruzi.strojmir.pomůcky.spustím_příkaz import spustím_příkaz
        příkaz = 'trang {} {}'.format(rnc_soubor,  rng_soubor)
        spustím_příkaz(příkaz)
        self[jméno_schématu] = rng_soubor
        return self[jméno_schématu]

        
class _Validátory(dict):
    
    def __missing__(self,  soubor_schématu):
        tree = lxml.etree.parse(soubor_schématu)
        validátor = self._validátor(tree)
        def validuji(soubor):
            parsovaný_xml_soubor = lxml.etree.parse(soubor)
            return validátor(parsovaný_xml_soubor)
            
        self[soubor_schématu] = validuji
        return self[soubor_schématu]
        
class _Validátory_RelaxNG(_Validátory):
    _validátor = lxml.etree.RelaxNG
    
class _Validátory_XMLSchema(_Validátory):
    _validátor = lxml.etree.XMLSchema
#    tree = self.__parsuji_xml(self.__soubor_schématu)
#    return lxml.etree.XMLSchema(tree)
    
class _Validátory_DTD(_Validátory):
    
    def __missing__(self,  soubor_schématu):
        with open(soubor_schématu,  encoding='UTF-8',  mode='r') as soubor:
            validátor = lxml.etree.DTD(soubor)
        def validuji(soubor):
            parsovaný_xml_soubor = lxml.etree.parse(soubor)
            return validátor(parsovaný_xml_soubor)
            
        self[soubor_schématu] = validuji
        return self[soubor_schématu]
    

class _Schéma(object):
    
    _schémata = None
    _validátory = None
    
    _programy = None
    
    def __getattr__(self,  jméno_schématu):
        if not jméno_schématu.startswith('_'):
            
           
            soubor_schématu = self._schémata[jméno_schématu]
            if not os.path.isfile(soubor_schématu):
                raise AttributeError('Soubor schématu {} nejestvuje.'.format(soubor_schématu))
                
            def validuji(soubor,  program = None):
                if not os.path.isfile(soubor):
                    raise TypeError('Soubor {} nejestvuje, nelze provést validaci.'.format(soubor))
                    
                if program is not None:
                    return self._programy(program,  schéma = soubor_schématu,  soubor = soubor)
                else:
                    validátor = self._validátory[soubor_schématu]
                    return validátor(soubor)

            setattr(self,  jméno_schématu,  validuji)
            return validuji
            
        raise AttributeError('V objektu {} nejestvuje atribut {}.'.format(self.__class__.__name__,  jméno_schématu))


        
class Validuji_programem(object):
    
    def __init__(self,  výchozí,  **kwargs):
        self.__programy = kwargs
        self.__výchozí = výchozí
        
    def __call__(self,  program,  schéma,  soubor):
        if program == True:
            program = self.__výchozí
            
        program = self.__programy.get(program,  None)
        if program is None:
            raise AttributeError('V objektu {} nejestvuje atribut pro validační program {}.'.format(self.__class__.__name__,  program))
            
           
        program = program.format(schéma = schéma,  soubor = soubor)
        from zora_na_pruzi.strojmir.pomůcky.spustím_příkaz import spustím_příkaz
        return spustím_příkaz(program)
        
class Schéma_rng(_Schéma):
    _schémata = _Soubory_schémat(přípona = 'rng')
    _validátory = _Validátory_RelaxNG()
    _programy = Validuji_programem(
                                výchozí = 'jing', 
                                jing = 'jing {schéma} {soubor}'
                            )

class Schéma_rnc(Schéma_rng):
    _schémata = _Soubory_schémat_rnc_rng(přípona = 'rnc')
    _validátory = _Validátory_RelaxNG()
  
    
class Schéma_xsd(_Schéma):
    _schémata = _Soubory_schémat(přípona = 'xsd')
    _validátory = _Validátory_XMLSchema()
    _programy = Validuji_programem(
                                výchozí = 'xmllint', 
                                xmllint = 'xmllint --noout --schema {schéma} {soubor}'
                            )
    
class Schéma_dtd(_Schéma):
    _schémata = _Soubory_schémat(přípona = 'dtd')
    _validátory = _Validátory_DTD()
    _programy = Validuji_programem(
                                výchozí = 'xmllint', 
                                xmllint = 'xmllint --noout --dtdvalid {schéma} {soubor}'
                            )
                            
