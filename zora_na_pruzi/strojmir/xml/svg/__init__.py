
#@TODO: Toto je téměř stejné s __init__ v graphml,  asi by to chtělo spojit dohromady

import os

try:
    import lxml.etree
except ImportError:
     raise ImportError('SVG vyžaduje knihovnu lxml')

from ..__ELEMENT import __ELEMENT
from zora_na_pruzi.strojmir.css.STYL import STYL

from ..davaj_parser import davaj_parser

NAMESPACE = 'http://www.w3.org/2000/svg'

class __ELEMENT_SVG(__ELEMENT):
    
    PARSER,  E = davaj_parser(jméno_balíčku = __name__)
    STYL = STYL()
    
    def __ior__(self,  css_vlastnost):
#        tag = lxml.etree.QName(self.tag)
        self.STYL[self.TAG_QNAME.localname] = css_vlastnost
        return self
        
    def __or__(self,  css_vlastnost):
        selektor = '#{}'.format(self.id)
        self.STYL[selektor] = css_vlastnost
        return self
    
    def __davaj_obsah(self,  třída_elementu):
        element = self.find(třída_elementu.TAG)
        if element is not None:
            return element.text
        return None
        
    def __nastav_obsah(self,  třída_elementu,  hodnota):
        element = self.find(třída_elementu.TAG)
        if hodnota is None:
            if element is not None:
                self.remove(element)
        else:
            if element is None:
                element = třída_elementu()
                element.text = hodnota
                self.append(element)
            return element.text
    
    @property
    def titulek(self):
        from .TITLE import TITLE
        return self.__davaj_obsah(třída_elementu = TITLE)
        
    @titulek.setter
    def titulek(self,  hodnota):
        from .TITLE import TITLE
        self.__nastav_obsah(třída_elementu = TITLE,  hodnota = hodnota)
        
    @property
    def popisek(self):
        from .DESC import DESC
        return self.__davaj_obsah(třída_elementu = DESC)    
        
    @popisek.setter
    def popisek(self,  hodnota):
        from .DESC import DESC
        self.__nastav_obsah(třída_elementu = DESC,  hodnota = hodnota)
    
def načtu_svg(svg_soubor):
    
    if not os.path.isfile(svg_soubor):
        raise IOError('Soubor grafu {} nejestvuje.'.format(svg_soubor))
    
    tree = lxml.etree.parse(svg_soubor,  parser = __ELEMENT_SVG.PARSER)
#    from ..__ELEMENT import print_info
#    print_info(tree)
    return tree.getroot()
    
def nové_svg(id = None):
    from .SVG import SVG
    
    args = {
            'nsmap': {
                            None: NAMESPACE,
                            'xlink': 'http://www.w3.org/1999/xlink',
                    }, 
                'version': '1.1'
            
            }
    
    if id is not None:
        args['id'] = id
    
    svg = SVG(**args)

#    tree = lxml.etree.ElementTree(svg)
#    from ..__ELEMENT import print_info
#    print_info(svg)
    return svg

