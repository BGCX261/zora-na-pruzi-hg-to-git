#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je třída, který načte graf z graphml souboru 
'''

class Graf(object):
    
    def __init__(self,  graphml_soubor):
        from . import načtu_graf
        self.graf = načtu_graf(graphml_soubor)
        return 
        
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
        return str(self.__graphml)
        
    @property
    def uzly(self):
        return self.__graphml.uzly
#        for uzel in self.__graphml.vertices():
#            yield uzel
  
    @property
    def vazby(self):
        return self.__graphml.vazby
        
    @property
    def vlastnosti(self):
        return []
        
    @property
    def xml(self):
        return self.__xml
        
    @property
    def graphml(self):
        return self.__graphml
  
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

    
