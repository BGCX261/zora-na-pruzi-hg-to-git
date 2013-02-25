#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který načte graphml soubor do grafu
'''

#SCHÉMA = './schémata/graphml.rng'

import networkx as nx
import os

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
    return graf
    
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
    return graf
        

def vykreslím_networkx_graf(graf,  jméno):
    print(':'*44)
    print('vykreslím_networkx_graf')
    
    import matplotlib.pyplot as plt

    import networkx
#toto vyžaduje pygraphviz,  ale to není pro python3 dostupné
#ale sat49 nainstalovat pzdot
#    networkx.draw_graphviz(graf)
    networkx.write_dot(graf, 'data/networkx_{}.dot'.format(jméno))

#    nx.draw(graf)
##    nx.draw_random(graf)
##    nx.draw_circular(graf)
##    nx.draw_spectral(graf)
##    
#    plt.show()

def vykreslím_graph_tool_graf(graf,  jméno):
    graf.save('data/graph_tool_{}.dot'.format(jméno))
    
    from graph_tool.all import graph_draw
    
    graph_draw(graf,  output= 'data/graph_tool_{}.pdf'.format(jméno))

if __name__ == '__main__':

    print(__doc__)

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('zdrojový_xml')
    parser.add_argument('--typ')
    args = parser.parse_args()
    
    if args.typ in ('graph-tool',  'graphtool',  'g'):
        nxgraf = načtu_graph_tool_graf(xml_soubor = args.zdrojový_xml)
    elif args.typ in ('networkx',  'n'):
        gt_graf = načtu_networkx_graf(xml_soubor = args.zdrojový_xml)
    else:
#        načtu oboje
        print('NETWORKFX')
        nxgraf = načtu_networkx_graf(xml_soubor = args.zdrojový_xml)
        print('GRAPH_TOOL')
        gt_graf = načtu_graph_tool_graf(xml_soubor = args.zdrojový_xml)

    jméno = os.path.basename(args.zdrojový_xml)
    
    jméno = os.path.splitext(jméno)[0]
    
    vykreslím_networkx_graf(nxgraf,  jméno)
    vykreslím_graph_tool_graf(gt_graf,  jméno)
