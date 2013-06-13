#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>


from ..__ELEMENT import __ELEMENT
from ..__DAVAJ_ELEMENT import __DAVAJ_ELEMENT as E

from ...css.CSS_TABULKA import CSS_TABULKA

from . import __nastavení
__nastavení.balíček = __name__
E = E(__nastavení)


class __ELEMENT_SVG(__ELEMENT):
    
    CSS = CSS_TABULKA()

    @property
    def css_dle_elementu(self):
        return self.CSS.get(self.TAG_QNAME.localname)
      
    @property
    def css_dle_id(self):
        selektor = '#{}'.format(self.id)
        return self.CSS.get(selektor)
      
    def css_dle_třídy(self,  třída,  element = None):
        if element is None:
            selektor = '.{}'.format(třída)
        else:
            selektor = '{}.{}'.format(self.TAG,  třída)
        self.__class(třída)
        return self.CSS.get(selektor)
        
    def __class(self,  třída):
        '''
        přidá třídu do atributu class
        tuto metodu používám při přiřazení CSS stylu dle třídy
        '''
        třídy = self.attrib.get('class',  '')
        class_elementu = set(třídy.split())
        class_elementu.add(třída)     
        self.attrib['class'] = ' '.join(class_elementu)
    
    @property
    def titulek(self):
#        from .TITLE import TITLE
        return self._davaj_obsah_jedinečného(třída_elementu = E.TITLE)
        
    @titulek.setter
    def titulek(self,  hodnota):
#        from .TITLE import TITLE
        self._nastav_obsah_jedinečného(třída_elementu = E.TITLE,  hodnota = hodnota)
        
    @property
    def popisek(self):
#        from .DESC import DESC
        return self._davaj_obsah_jedinečného(třída_elementu = E.DESC)    
        
    @popisek.setter
    def popisek(self,  hodnota):
#        from .DESC import DESC
        self._nastav_obsah_jedinečného(třída_elementu = E.DESC,  hodnota = hodnota)
        
      
    def definuji(self,  element):
        id = element.attrib['id']
        self.DEFS.append(element)
    
#    def __getattr__(self,  klíč):
#        klíč = klíč.upper()
#        element = getattr(E,  klíč)
#        jestvuje = self.findall(element.TAG)
#        nalezeno = len(jestvuje)
#        if nalezeno == 1:
#            return jestvuje[0]
#        elif nalezeno == 0:
#            element = element()
#            self.append(element)
#            return element
#        else:
#            raise ValueError('Pro klíč nalezeno více elementů {} v {}'.format(klíč,  element.__class__.__name__,  self.__class__.__name__))
    
