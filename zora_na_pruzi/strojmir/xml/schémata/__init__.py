import os
import lxml.etree

class Schéma(object):
    
    def __init__(self,  přípona):
        self.__adresář_schémat = os.path.dirname(__file__)
        self.__přípona = přípona
    
    def __getattr__(self,  jméno_schématu):
        '''
        vrátí validátor
        '''
        return Validátor(soubor_schématu = self % jméno_schématu,  přípona = self.__přípona)
       
        
    def __mod__(self,  jméno_schématu):
        '''
        operátor schéma:Schéma % jméno_schématu:str vrátí cestu k souboru se schématem
        '''
        if not isinstance(jméno_schématu,  str):
            raise TypeError('Operátor %  schématu očekává jako argument řetězec, vyjadřujíc jméno schématu a nikolivěk {}.'.format(jméno_schématu))

        soubor = os.path.join(self.__adresář_schémat,  '{}.{}'.format(jméno_schématu,  self.__přípona))
        if os.path.isfile(soubor):
            return soubor
            
        raise AttributeError('Soubor schématu {} nejestvuje.'.format(soubor))
        

class Validátor(object):
    
    
    def __init__(self,  soubor_schématu,  přípona = None):
        if přípona is None:
            přípona = os.path.splitext(soubor_schématu)[1]
            
        self.__soubor_schématu = soubor_schématu
        self.__přípona = přípona
      
    def __call__(self,  soubor):
        
        davaj_validátor = getattr(self,  '_{}__validátor_{}'.format(self.__class__.__name__,  self.__přípona))
        validátor = davaj_validátor()
        if not os.path.isfile(soubor):
            raise TypeError('Soubor {} nejestvuje, nelze provést validaci.'.format(soubor))

        parsovaný_xml_soubor = lxml.etree.parse(soubor)
        return validátor(parsovaný_xml_soubor)
        
    def __mod__(self,  soubor):
        '''
        operátor validátor:Validátor % jméno_souboru:str provede validaci externím programem
        '''
        if not os.path.isfile(soubor):
            raise TypeError('Operátor %  schématu očekává jako argument řetězec, vyjadřujíc jméno souboru, avšak tento soubor nejestvuje {}.'.format(soubor))


        davaj_příkaz = getattr(self,  '_{}__příkaz_externího_validátoru_{}'.format(self.__class__.__name__,  self.__přípona))
        příkaz = davaj_příkaz(soubor)
        from zora_na_pruzi.strojmir.pomůcky.spustím_příkaz import spustím_příkaz
        spustím_příkaz(příkaz)
        
    
  
  
    def __parsuji_xml(self,  soubor):
        return lxml.etree.parse(soubor)
  
    def __validátor_rng(self):
        tree = self.__parsuji_xml(self.__soubor_schématu)
        return lxml.etree.RelaxNG(tree)
        
    def __příkaz_externího_validátoru_rng(self,  soubor):
        return 'jing {schéma} {soubor}'.format(schéma = self.__soubor_schématu,  soubor = soubor)
    
    @property
    def __rnc_rng_soubor(self):
#        if not hasattr(self.__rnc_rng_soubor,  'soubor_rng'):
        from zora_na_pruzi.strojmir.pomůcky.spustím_příkaz import spustím_příkaz
        soubor_rng = '{}.{}'.format(self.__soubor_schématu,  'rng')
        příkaz = 'trang {} {}'.format(self.__soubor_schématu,  soubor_rng)
        spustím_příkaz(příkaz)
#        self.__rnc_rng_soubor.soubor_rng = soubor_rng
        return soubor_rng
            
#        return self.__rnc_rng_soubor.soubor_rng
        
    def __validátor_rnc(self):
#        import os
        soubor_rng = self.__rnc_rng_soubor
        tree = self.__parsuji_xml(soubor_rng)
        return lxml.etree.RelaxNG(tree)
        
    def __příkaz_externího_validátoru_rnc(self,  soubor):
        return 'jing {schéma} {soubor}'.format(schéma = self.__rnc_rng_soubor,  soubor = soubor)
        
    def __validátor_xsd(self):
        tree = self.__parsuji_xml(self.__soubor_schématu)
        return lxml.etree.XMLSchema(tree)
        
    def __příkaz_externího_validátoru_xsd(self,  soubor):
        return 'xmllint --noout --schema {schéma} {soubor}'.format(schéma = self.__soubor_schématu,  soubor = soubor)
        
    def __validátor_dtd(self):
        with open(self.__soubor_schématu,  encoding='UTF-8',  mode='r') as soubor:
            return lxml.etree.DTD(soubor)
            
    def __příkaz_externího_validátoru_dtd(self,  soubor):
        return 'xmllint --noout --dtdvalid {schéma} {soubor}'.format(schéma = self.__soubor_schématu,  soubor = soubor)
