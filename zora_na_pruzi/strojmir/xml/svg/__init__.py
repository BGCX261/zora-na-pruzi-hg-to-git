
#@TODO: Toto je téměř stejné s __init__ v graphml,  asi by to chtělo spojit dohromady

import os

try:
    import lxml.etree
except ImportError:
     raise ImportError('SVG vyžaduje knihovnu lxml')
 

from ..__ELEMENT import __ELEMENT

from ..davaj_parser import davaj_parser

import sys

class __ELEMENT_SVG(__ELEMENT):
    NAMESPACE = 'http://www.w3.org/2000/svg'
    PARSER = davaj_parser(v_modulu = sys.modules[__name__])
    
def načtu_svg(svg_soubor):
    
    if not os.path.isfile(svg_soubor):
        raise IOError('Soubor grafu {} nejestvuje.'.format(svg_soubor))
    
    tree = lxml.etree.parse(svg_soubor,  parser = __ELEMENT_SVG.PARSER)
    return tree.getroot()
    
def nové_svg():
    from .SVG import SVG
    svg = SVG(nsmap={
                None: SVG.NAMESPACE,
                'xlink': 'http://www.w3.org/1999/xlink',
                    }
                    )
    
    from zora_na_pruzi import __version__,  __author__
    from datetime import date
        
    def rok():
        letos = date.today().timetuple()[0]
        if letos > 2012:
            return '2012 - {}'.format(letos)
        else:
            return '2012'
        
    svg.append(lxml.etree.Comment('Изготовила Зора на прузи {verze} ©Домоглед {autor} {rok} on {datum}'.format(verze = __version__, datum = date.today().isoformat(),  autor = __author__,  rok = rok())))
    svg.append(lxml.etree.Comment('http://domogled.eu'))
    svg.append(lxml.etree.Comment('http://code.google.com/p/zora-na-pruzi/'))


#    tree = etree.ElementTree(root)
    return svg

