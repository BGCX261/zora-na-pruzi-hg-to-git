#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který překontroluje správnost graphml souboru
'''

#SCHÉMA = './schémata/graphml.rng'

def najdu_databáze(xml_soubor):
    import lxml.etree
    
    Databáze = None
    id_class_mapping = {'Databáze' : Databáze}
    lookup = lxml.etree.AttributeBasedElementClassLookup('třída', id_class_mapping)
    parser = lxml.etree.XMLParser()
    parser.set_element_class_lookup(lookup)
    
    tree = lxml.etree.parse(xml_soubor,  parser = parser)
    root = tree.getroot()
    
    databáze = tree.findall('//{http://graphml.graphdrawing.org/xmlns}node[@třída="Databáze"]')
    for db in databáze:
        print(db)
    
    def projdi(el,  tab = 0):
        for e in el:
            print('\t'*tab,  e.tag)
            projdi(e,  tab + 1)
            
    projdi(root)
    
    
    
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
 



if __name__ == '__main__':

    print(__doc__)

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('zdrojový_xml')
#    parser.add_argument('--typ')
    args = parser.parse_args()
    
#    if args.typ is None or args.typ in ('graph-tool',  'graphtool',  'g'):
#        načtu_graph_tool_graf(xml_soubor = args.zdrojový_xml)
#    elif args.typ in ('networkx',  'n'):
#        načtu_networkx_graf(xml_soubor = args.zdrojový_xml)
    

#    najdu_databáze(args.zdrojový_xml)
