#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je třída, který načte graf z graphml souboru 
'''



class Seznam_klíčů(dict):
    
    def __init__(self,  for_element,  xml):
        if not for_element in ('graph',  'node',  'edge'):
            raise TypeError('Seznam klíčů může být pouze pro graph, edge, nebo node.')
        
        self.__for_element = for_element
        self.__xml = xml
        self.__klíče = None
       
    def __getitem__(self,  klíč):

        def najdi_definici(klíč):
            definice_klíče = self.__xml.find(NS_GRAPHML(NS_GRAPHML.key,  klíč = 'id',  hodnota = klíč))
            
            if definice_klíče is None:
                raise KeyError('Klíč <key id = "{}" ... > nejestvuje.'.format(klíč))
            for_element = definice_klíče.attrib.get('for')
            if for_element != self.__for_element:
                raise TypeError('Klíč pro <key id = "{id}" for = "{for_element}" ... > není určen elementu "{má_být}" ale elementu "{for_element}"'.format(id = klíč,  má_být = self.__for_element,  for_element = for_element))
        
            return definice_klíče
            
        return self.setdefault(klíč,  najdi_definici(klíč))
      
#    def __missing__(self,  klíč):
#        print('MISSING',  klíč)
        
    def get(self,  klíč,  default  = None):
        try:
            return self.__getitem__(klíč)
        except KeyError:
            return default
        
    def items(self):
        for klíč in self.keys():
            yield (klíč,  self[klíč])
        
    def __iter__(self):
        if self.__klíče is None:
            klíče = []
            print('AAA ',  NS_GRAPHML(NS_GRAPHML.key,  klíč = 'for',  hodnota = self.__for_element))
            print(self.__for_element)
            for definice in self.__xml.findall(NS_GRAPHML(NS_GRAPHML.key,  klíč = 'for',  hodnota = self.__for_element)):
                print('KEZ ',  definice.attrib['id'],  definice.attrib['for'])
                klíče.append(definice.attrib['id'])
            self.__klíče = klíče
        return iter(self.__klíče)
       
#    funkce keys() dělá totéž co __iter__
    keys = __iter__


class Graf(object):
    
    def __init__(self,  graphml_soubor):
        
        from . import načtu_graf
        self.graf = načtu_graf(graphml_soubor).getroot()
        
        return 
        
        
        try:
            import lxml.etree
        except ImportError:
             raise ImportError('Graf, třída {} vyžaduje knihovnu lxml'.format(self.__class__.__name__))
        
        
        xml = self.xml = lxml.etree.parse(graphml_soubor)#        ,  parser = parser
        
        vlastnosti_grafů = Seznam_klíčů(for_element = 'graph',  xml = xml)
        vlastnosti_uzlů = Seznam_klíčů(for_element = 'node',  xml = xml)
        vlastnosti_vazeb = Seznam_klíčů(for_element = 'edge',  xml = xml)
        
        print(vlastnosti_grafů.get('hroch'))
        
#        toto jestvuje a najde???
        print(vlastnosti_vazeb.get('d1'))
#       assert TypeError
#        print(vlastnosti_uzlů.get('d1'))
       
#        assert(KeyError)
#        print(vlastnosti_grafů['medvěd'])

#        assert(TypeError)
#        print(vlastnosti_grafů['d0'])
        
        print(vlastnosti_uzlů['d0'])
#        has key 'd0' and it is elemnt Element

        for klíč,  element in vlastnosti_uzlů.items():
            print(klíč)
        
        print('key')
        print(list(vlastnosti_uzlů.keys()))
        print('-'*44)
        print(list(vlastnosti_vazeb.keys()))
        print('-'*44)
        
################        
        
        from .Reader import GraphMLReader
        
        reader = GraphMLReader()
        
        
        (keys,defaults) = reader.find_graphml_keys(self.xml)
        print('XXXXXXX')
        print(keys,defaults)
#        NS_GRAPHML = "http://graphml.graphdrawing.org/xmlns"
        for g in self.xml.findall(NS_GRAPHML.graph):
#            yield
            reader.make_graph(g, keys, defaults)
        
#        from graph_tool import libgraph_tool_core as libcore
#        print(dir(libcore))
        
    def __str__(self):
        return str(self.graf)
        
    @property
    def uzly(self):
        return self.graf.uzly
#        for uzel in self.graf.vertices():
#            yield uzel
  
    @property
    def vazby(self):
        return []
        
    @property
    def vlastnosti(self):
        return []
  
class Graf_NetworkX(object):
    
    def __init__(self,  graphml_soubor):
        from networkx import read_graphml
        self.graf = read_graphml(graphml_soubor)
        
    @property
    def uzly(self):
        return self.graf.nodes_iter(data = True)
        
    @property
    def vazby(self):
        return self.graf.edges_iter(data = True)

    @property
    def vlastnosti(self):
        return []

            
#    get_node_attributes(G, name)
    
class Graf_Graph_tool(object):
    
    def __init__(self,  graphml_soubor):
        from graph_tool.all import load_graph
    
        if graphml_soubor.endswith('graphml'):
            fmt='xml'
        else:
            fmt='auto'
        self.graf = load_graph(graphml_soubor,  fmt)
        
    @property
    def uzly(self):
        print()
        for uzel in self.graf.vertices():
            yield uzel
            
    @property
    def vazby(self):
        for vazba in self.graf.edges():
            yield vazba
            
    @property
    def vlastnosti(self):
        print('list')
        self.graf.list_properties()
        print('/list')
        
        return self.graf.graph_properties,  self.graf.edge_properties,  self.graf.vertex_properties

        
        
if __name__ == '__main__':

    print(__doc__)

    
