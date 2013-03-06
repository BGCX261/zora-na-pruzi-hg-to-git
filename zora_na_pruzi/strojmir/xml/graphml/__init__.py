
import os

try:
    import lxml.etree
except ImportError:
     raise ImportError('Graf vyžaduje knihovnu lxml')
    
def načtu_graf(graphml_soubor):
    
    if not os.path.isfile(graphml_soubor):
        raise IOError('Soubor grafu {} nejestvuje.'.format(graphml_soubor))
    
    from .graphml_elementy import GRAPHML
    tree = lxml.etree.parse(graphml_soubor,  parser = GRAPHML.PARSER)
    return tree
    
