#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''
#from zora_na_pruzi import vidimir as MODUL_VIDŮ

class _VIDY(dict):
        
    def __missing__(self,  jméno_vidu):
        from . import formáty
        from zora_na_pruzi.system.python.načtu_modul import načtu_modul_podle_balíčku
        return self.setdefault(jméno_vidu,  načtu_modul_podle_balíčku(podle_balíčku = formáty,  jméno_modulu =  jméno_vidu))
 
_VIDY = _VIDY()

class Formátuji(dict):
    
    __vid = 'barevná_konzole'
    
    def __get__(self,  instance,  owner):
        return self.__vid
        
    def __set__(self,  instance,  vid):
        from .Pisar import Pisar
        if not isinstance(instance,  Pisar):
            raise TypeError('Nastavit vid formátu može jenom potomek třídy Pisar a nikolivěk {}'.format(type(instance)))
        self.__vid = vid
        
    def __getattr__(self,  jméno_formátu):
        return self[self.__vid, jméno_formátu]
      
    def __key__(self, klíč):
        if isinstance(klíč,  str):
            klíč = (self.__vid,  klíč)
        return self[klíč]
    
    def __missing__(self,  klíč_formátu):
        return self.setdefault(klíč_formátu,  self.__načtu_formát(klíč_formátu[1]))
#        return getattr(self.__styl,  jméno)

    def __načtu_formát(self,  jméno_formátu):
        
        modul_vidu = _VIDY[self.__vid]
        
#        nejdřív zkusím načíst z modulu vidu 
        formát = getattr(modul_vidu,  jméno_formátu,  None)
        
        if formát is None:
            from zora_na_pruzi.system.python.načtu_modul import načtu_modul_podle_balíčku
            modul_formátu = načtu_modul_podle_balíčku(podle_balíčku = modul_vidu, jméno_modulu =  jméno_formátu)
            
            formát = getattr(modul_formátu,  jméno_formátu,  None)
            if formát is None:
                raise AttributeError('Formát {} nejestvuje v modulu {}'.format(jméno_formátu,  modul_formátu.__name__))

        return formát
        
Formátuji = Formátuji()
