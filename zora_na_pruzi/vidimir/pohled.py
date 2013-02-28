#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''
#from zora_na_pruzi import vidimir as MODUL_VIDŮ

class _VIDY(dict):
        
    def __missing__(self,  jméno_vidu):
        from zora_na_pruzi.system.python.načtu_modul import načtu_modul_podle_třídy
        return self.setdefault(jméno_vidu,  načtu_modul_podle_třídy(podle_třídy = self,  v_adresáři = __file__,  jméno_modulu =  jméno_vidu))
    
    def __get__(self,  instance,  owner):
        vid = instance.aktivní_vid
        return self[vid]
 
_VIDY = _VIDY()

class pohled(dict):
    
    __vid = 'barevná_konzole'
    
    def __get__(self,  instance,  owner):
        return self.__vid
        
    def __set__(self,  instance,  vid):
        from .Pisar import Pisar
        if not isinstance(instance,  Pisar):
            raise TypeError('Nastavit vid pohledu može jenom potomek třídy Pisar a nikolivěk {}'.format(type(instance)))
        self.__vid = vid
        
    def __getattr__(self,  jméno_pohledu):
        return self[self.__vid, jméno_pohledu]
      
    def __key__(self, klíč):
        if isinstance(klíč,  str):
            klíč = (self.__vid,  klíč)
        return self[klíč]
    
    def __missing__(self,  klíč_pohledu):
        return self.setdefault(klíč_pohledu,  self.__načtu_pohled(klíč_pohledu[1]))
#        return getattr(self.__styl,  jméno)

    def __načtu_pohled(self,  jméno_pohledu):
        
        modul_vidu = _VIDY[self.__vid]
        
#        nejdřív zkusím načíst z modulu vidu 
        pohled = getattr(modul_vidu,  jméno_pohledu,  None)
        
        if pohled is None:
            from zora_na_pruzi.system.python.načtu_modul import načtu_modul_podle_modulu
            modul_pohledu = načtu_modul_podle_modulu(podle_modulu = modul_vidu, jméno_modulu =  jméno_pohledu)
            print(modul_pohledu)
            pohled = getattr(modul_pohledu,  jméno_pohledu,  None)
            if pohled is None:
                raise AttributeError('Pohled {} nejestvuje v modulu {}'.format(jméno_pohledu,  modul_pohledu.__name__))

        return pohled
        
        
        
pohled = pohled()
