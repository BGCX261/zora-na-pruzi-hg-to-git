
#@TODO: Toto je téměř stejné s __init__ v graphml,  asi by to chtělo spojit dohromady

#import os

#try:
#    import lxml.etree
#except ImportError:
#     raise ImportError('SVG vyžaduje knihovnu lxml')

from ..__ELEMENT import __ELEMENT
from ..__DAVAJ_ELEMENT import __DAVAJ_ELEMENT as E

from zora_na_pruzi.strojmir.css.CSS_TABULKA import CSS_TABULKA

NAMESPACE = 'http://www.w3.org/2000/svg'
NSMAP = {None: NAMESPACE, 'xlink': 'http://www.w3.org/1999/xlink'}
E = E(str_z_balíčku = __name__,  namespace = NAMESPACE,  nsmap = NSMAP)


#PARSER = davaj_parser(elementMaker = E)

class __ELEMENT_SVG(__ELEMENT):
    
#    PARSER = PARSER
    CSS = CSS_TABULKA()
#    nsmap = {
#                            None: NAMESPACE,
#                            'xlink': 'http://www.w3.org/1999/xlink',
#                    }
    

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

    
    def __davaj_obsah(self,  třída_elementu):
        '''
        pomocná metoda, která vrací obsah nějakého vloženého elementu
        '''
        element = self.find(třída_elementu.TAG)
        if element is not None:
            return element.text
        return None
        
    def __nastav_obsah(self,  třída_elementu,  hodnota):
        '''
        pomocná metoda, která nastaví obsah nějakého vloženého elementu
        '''
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
#        from .TITLE import TITLE
        return self.__davaj_obsah(třída_elementu = E.TITLE)
        
    @titulek.setter
    def titulek(self,  hodnota):
#        from .TITLE import TITLE
        self.__nastav_obsah(třída_elementu = E.TITLE,  hodnota = hodnota)
        
    @property
    def popisek(self):
#        from .DESC import DESC
        return self.__davaj_obsah(třída_elementu = E.DESC)    
        
    @popisek.setter
    def popisek(self,  hodnota):
#        from .DESC import DESC
        self.__nastav_obsah(třída_elementu = E.DESC,  hodnota = hodnota)
        
      
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
    
#def načtu_svg(svg_soubor):
#    
#    if not os.path.isfile(svg_soubor):
#        raise IOError('Soubor grafu {} nejestvuje.'.format(svg_soubor))
#    
#    tree = lxml.etree.parse(svg_soubor,  parser = __ELEMENT_SVG.PARSER)
##    from ..__ELEMENT import print_info
##    print_info(tree)
#    return tree.getroot()
    
#def nové_svg(id = None):
#    from .SVG import SVG
#    
#    args = {
#            'nsmap': {
#                            None: NAMESPACE,
#                            'xlink': 'http://www.w3.org/1999/xlink',
#                    }, 
#                'version': '1.1'
#            
#            }
#    
#    if id is not None:
#        args['id'] = id
#    
#    svg = SVG(**args)
#
##    tree = lxml.etree.ElementTree(svg)
##    from ..__ELEMENT import print_info
##    print_info(svg)
#    return svg
#
