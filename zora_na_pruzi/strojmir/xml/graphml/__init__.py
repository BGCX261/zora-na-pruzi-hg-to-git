
import os

try:
    import lxml.etree
except ImportError:
     raise ImportError('Graf vyžaduje knihovnu lxml')
         
def davaj_parser():
    if getattr(davaj_parser,  'parser',  None) is None:
        
        from . import graphml_elementy
        
        class Lookup(lxml.etree.CustomElementClassLookup):
            def lookup(self, node_type, document, namespace, name):
                if node_type == 'element':
                    return getattr(graphml_elementy,  name.upper(),  None)
                
        parser = lxml.etree.XMLParser(remove_blank_text=True)
        parser.set_element_class_lookup(Lookup())
        davaj_parser.parser = parser
    return davaj_parser.parser
    
def načtu_graf(graphml_soubor):
    
    if not os.path.isfile(graphml_soubor):
        raise IOError('Soubor grafu {} nejestvuje.'.format(graphml_soubor))
    
    parser = davaj_parser()
    tree = lxml.etree.parse(graphml_soubor,  parser = parser)
    return tree
    
