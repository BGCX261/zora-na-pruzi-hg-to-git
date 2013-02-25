#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import networkx as nx

class GraphML(object):
    NS_GRAPHML = "http://graphml.graphdrawing.org/xmlns"
    NS_XSI = "http://www.w3.org/2001/XMLSchema-instance"
    #xmlns:y="http://www.yworks.com/xml/graphml"
    NS_Y = "http://www.yworks.com/xml/graphml"
    SCHEMALOCATION = \
        ' '.join(['http://graphml.graphdrawing.org/xmlns',
                  'http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd'])
    
    try:
        chr(12345)     # Fails on Py!=3.
        unicode = str  # Py3k's str is our unicode type
        long = int     # Py3K's int is our long type
    except ValueError:
        # Python 2.x
        pass

    types=[(int,"integer"), # for Gephi GraphML bug
           (str,"yfiles"),(str,"string"), (unicode,"string"),
           (int,"int"), (long,"long"),
           (float,"float"), (float,"double"),
           (bool, "boolean")]
    
    xml_type = dict(types)
    python_type = dict(reversed(a) for a in types)
    convert_bool={'true':True,'false':False, 
                  'True': True, 'False': False}


class GraphMLReader(GraphML):
    """Read a GraphML document.  Produces NetworkX graph objects.
    """
    def __init__(self, node_type=str):
        try:
            import xml.etree.ElementTree
        except ImportError:
             raise ImportError('GraphML reader requires '
                               'xml.elementtree.ElementTree')
        self.node_type=node_type
        self.multigraph=False # assume multigraph and test for parallel edges
        
#    def __call__(self, stream):
##        self.xml = ElementTree(file=stream)
#        self.xml = lxml.etree.parse(stream)#        ,  parser = parser
#        (keys,defaults) = self.find_graphml_keys(self.xml)
#        for g in self.xml.findall("{%s}graph" % self.NS_GRAPHML):
#            yield self.make_graph(g, keys, defaults)
            
    def make_graph(self, graph_xml, graphml_keys, defaults):
        # set default graph type
        edgedefault = graph_xml.get("edgedefault", None)
        if edgedefault=='directed':
            G=nx.MultiDiGraph()
        else:
            G=nx.MultiGraph()
        # set defaults for graph attributes
        G.graph['node_default']={}
        G.graph['edge_default']={}
        for key_id,value in defaults.items():
            key_for=graphml_keys[key_id]['for']
            name=graphml_keys[key_id]['name']
            python_type=graphml_keys[key_id]['type']
            if key_for=='node':
                G.graph['node_default'].update({name:python_type(value)})
            if key_for=='edge':
                G.graph['edge_default'].update({name:python_type(value)})
        # hyperedges are not supported
        hyperedge=graph_xml.find("{%s}hyperedge" % self.NS_GRAPHML)        
        if hyperedge is not None:
            raise nx.NetworkXError("GraphML reader does not support hyperedges")
        # add nodes
        for node_xml in graph_xml.findall("{%s}node" % self.NS_GRAPHML):        
            self.add_node(G, node_xml, graphml_keys)                            
        # add edges
        for edge_xml in graph_xml.findall("{%s}edge" % self.NS_GRAPHML):        
            self.add_edge(G, edge_xml, graphml_keys)                            
        # add graph data            
        data = self.decode_data_elements(graphml_keys, graph_xml)
        G.graph.update(data)

        # switch to Graph or DiGraph if no parallel edges were found.
        if not self.multigraph: 
            if G.is_directed():
                return nx.DiGraph(G)
            else:
                return nx.Graph(G)
        else:
            return G
            
    def add_node(self, G, node_xml, graphml_keys):
        """Add a node to the graph.
        """
        # warn on finding unsupported ports tag
        ports=node_xml.find("{%s}port" % self.NS_GRAPHML)
        if ports is not None:
            warnings.warn("GraphML port tag not supported.")
        # find the node by id and cast it to the appropriate type
        node_id = self.node_type(node_xml.get("id"))
        # get data/attributes for node
        data = self.decode_data_elements(graphml_keys, node_xml)
        G.add_node(node_id, data)
        
    def add_edge(self, G, edge_element, graphml_keys):
        """Add an edge to the graph.
        """
        # warn on finding unsupported ports tag
        ports=edge_element.find("{%s}port" % self.NS_GRAPHML)
        if ports is not None:
            warnings.warn("GraphML port tag not supported.")

        # raise error if we find mixed directed and undirected edges
        directed = edge_element.get("directed")
        if G.is_directed() and directed=='false':
            raise nx.NetworkXError(\
                "directed=false edge found in directed graph.")
        if (not G.is_directed()) and directed=='true':
            raise nx.NetworkXError(\
                "directed=true edge found in undirected graph.")

        source = self.node_type(edge_element.get("source"))
        target = self.node_type(edge_element.get("target"))
        data = self.decode_data_elements(graphml_keys, edge_element)
        # GraphML stores edge ids as an attribute
        # NetworkX uses them as keys in multigraphs too if no key
        # attribute is specified
        edge_id = edge_element.get("id")
        if edge_id:
            data["id"] = edge_id
        if G.has_edge(source,target):
            # mark this as a multigraph
            self.multigraph=True
        if edge_id is None:
            # no id specified, try using 'key' attribute as id
            edge_id=data.pop('key',None)
        G.add_edge(source, target, key=edge_id, **data)
            
    def decode_data_elements(self, graphml_keys, obj_xml):
        """Use the key information to decode the data XML if present."""
        data = {}
        for data_element in obj_xml.findall("{%s}data" % self.NS_GRAPHML): 
            key = data_element.get("key")
            try:
                data_name=graphml_keys[key]['name']
                data_type=graphml_keys[key]['type']
            except KeyError:
                raise nx.NetworkXError("Bad GraphML data: no key %s"%key)
            text=data_element.text
            # assume anything with subelements is a yfiles extension
            if text is not None and len(list(data_element))==0:
                if data_type==bool:
                    data[data_name] = self.convert_bool[text]
                else:
                    data[data_name] = data_type(text)
            elif len(list(data_element)) > 0:
                # Assume yfiles as subelements, try to extract node_label
                node_label = None
                for node_type in ['ShapeNode', 'SVGNode', 'ImageNode']:
                    geometry = data_element.find("{%s}%s/{%s}Geometry" % 
                                (self.NS_Y, node_type, self.NS_Y))
                    if geometry is not None:
                        data['x'] = geometry.get('x')
                        data['y'] = geometry.get('y')
                    if node_label is None:
                        node_label = data_element.find("{%s}%s/{%s}NodeLabel" % 
                                (self.NS_Y, node_type, self.NS_Y))
                if node_label is not None:
                    data['label'] = node_label.text
                edge_label = data_element.find("{%s}PolyLineEdge/{%s}EdgeLabel"%
                                               (self.NS_Y, (self.NS_Y)))
                if edge_label is not None:
                    data['label'] = edge_label.text
        return data
            
    def find_graphml_keys(self, graph_element):
        """Extracts all the keys and key defaults from the xml.
        """
        graphml_keys = {}
        graphml_key_defaults = {}
        for k in graph_element.findall("{%s}key" % self.NS_GRAPHML):
            attr_id = k.get("id")
            attr_type=k.get('attr.type')
            attr_name=k.get("attr.name")
            if attr_type is None:
                attr_name=k.get('yfiles.type')
                attr_type='yfiles'
            if attr_name is None:
                raise nx.NetworkXError("Unknown key type in file.")
            graphml_keys[attr_id] = {
                "name":attr_name,
                "type":self.python_type[attr_type],
                "for":k.get("for")}
            # check for "default" subelement of key element
            default=k.find("{%s}default" % self.NS_GRAPHML)
            if default is not None:
                graphml_key_defaults[attr_id]=default.text
        return graphml_keys,graphml_key_defaults
