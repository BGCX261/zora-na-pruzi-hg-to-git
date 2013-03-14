
#import os
#
#try:
#    import lxml.etree
#except ImportError:
#     raise ImportError('Graf vyžaduje knihovnu lxml')
    
from ..__ELEMENT import __ELEMENT
from ..__DAVAJ_ELEMENT import __DAVAJ_ELEMENT as E

#from zora_na_pruzi.strojmir.css.CSS_TABULKA import CSS_TABULKA

#from ..PATH import ATRIBUT



NAMESPACE = 'http://graphml.graphdrawing.org/xmlns'
NSMAP = {None: NAMESPACE, 'xlink': 'http://www.w3.org/1999/xlink'}
E = E(str_z_balíčku = __name__,  namespace = NAMESPACE,  nsmap = NSMAP)

class __ELEMENT_GRAFU(__ELEMENT):
    pass
