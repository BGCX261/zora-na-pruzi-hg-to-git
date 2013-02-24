#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který překontroluje správnost graphml souboru
'''

#SCHÉMA = './schémata/graphml.rng'

def načtu_graph_tool_graf(xml_soubor):
    '''
    spouštím funkci main()
    '''
    from graph_tool.all import Graph,  load_graph
    
    if xml_soubor.endswith('graphml'):
        fmt='xml'
    else:
        fmt='auto'
    
    graf = load_graph(xml_soubor,  fmt)
    print(graf)
    
def načtu_networkx_graf(xml_soubor):
    from networkx import read_graphml,  get_node_attributes
    
    graf = read_graphml(xml_soubor)
    print(graf)
    print(type(graf))
    for uzel,  atributy in graf.nodes(data = True):
        print('uzel ',  uzel)
        for jméno,  hodnota in atributy.items():
            print('\tattr ',  jméno,  hodnota)
            
    jména = get_node_attributes(graf,  'jméno')
    print(jména)
        
def vytvořím_networkx_graf():
    from networkx import DiGraph,  write_graphml
    
    graf = DiGraph()
    graf.add_node(1,  time='5pm')
    graf.add_node(2)
    graf.add_edge(1,2,  weught=25)
    
    write_graphml(graf,  './data/networkx.graphml')
 
def vytvořím_graph_tool_graf():
    from graph_tool.all import Graph
    
    graf = Graph()
    u1 = graf.add_vertex()
    u2 = graf.add_vertex()
    graf.add_edge(u1,  u2)
    
    vprop_double = graf.new_vertex_property("double")            # Double-precision floating point
    vprop_double[graf.vertex(1)] = 3.1416

    vprop_vint = graf.new_vertex_property("vector<int>")         # Vector of ints
    vprop_vint[graf.vertex(0)] = [1, 3, 42, 54]

    eprop_dict = graf.new_edge_property("object")                # Arbitrary python object. In this case, a dictionary.
    eprop_dict[graf.edges().next()] = {"foo": "bar", "gnu": 42}

    gprop_bool = graf.new_graph_property("bool")                  # Boolean
    gprop_bool[graf] = True
    
    graf.save('./data/graph_tool.graphml',  fmt='xml')


if __name__ == '__main__':

    print(__doc__)

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('zdrojový_xml')
    parser.add_argument('--typ')
    args = parser.parse_args()
    
#    if args.typ is None or args.typ in ('graph-tool',  'graphtool',  'g'):
#        načtu_graph_tool_graf(xml_soubor = args.zdrojový_xml)
#    elif args.typ in ('networkx',  'n'):
#        načtu_networkx_graf(xml_soubor = args.zdrojový_xml)
    
    vytvořím_networkx_graf()
    vytvořím_graph_tool_graf()
