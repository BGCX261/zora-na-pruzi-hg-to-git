#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

from py2neo import neo4j, cypher,  node,  rel

def main(graph_db):
    '''
    spouštím funkci main()
    '''
    

    graph_db = neo4j.GraphDatabaseService(neo4j.DEFAULT_URI)
    print(graph_db.neo4j_version)
    graph_db.clear()
    
    # create a single node
    alice, = graph_db.create({"name": "Alice"})
    print(alice)

def priklad(graph_db):
    

    # attach to a local graph database service
    

    graph_db.clear()

    # create two nodes and a relationship between them
    #   (Alice)-[:KNOWS]->(Bob)
    alice, bob, ab = graph_db.create(
        node(name="Alice"), node(name="Bob"), rel(0, "KNOWS", 1)
    )

    # build a Cypher query and related parameters
    query = (
        "START a = node({A}) "
        "MATCH (a)-[:KNOWS]->(b) "
        "RETURN a, b"
    )
    params = {"A": alice.id}

    # define a row handler
    def print_row(row):
        print("imam ",  row)
        a, b = row
        print(a["name"] + " knows " + b["name"])

    # execute the query
    x = cypher.execute(graph_db, query, params, row_handler=print_row)
    print(x)
  
def cypherem_vypíšu_vše(graph_db):
    cypher_query = 'MATCH n RETURN n'
    
    def row_handler(row):
        print('ROW HANDLER')
        print(row)
        print('-'*20)
        
    def metadata_handler(data):
        print('METADATA HANDLER')
        print(data)
        print('-'*20)
        
    def error_handler(error):
        print('ERROR HANDLER')
        print(error)
        print('-'*20)
        
    x = cypher.execute(graph_db, cypher_query, params=None, row_handler=row_handler, metadata_handler=metadata_handler, error_handler=error_handler)
    print(x)

if __name__ == '__main__':

    print(__doc__)

    import logging
    
    logging.basicConfig(level = logging.DEBUG)

#    import argparse
#    #  nejdříve si parser vytvořím
#    parser = argparse.ArgumentParser()
#
##   a pak mu nastavím jaké příkazy a parametry má přijímat
#    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, {}'.format(__version__))
#    
#    parser.add_argument('soubor')
#    
#    #    a včíl to možu rozparsovat
#    args = parser.parse_args()
#    
#    print('soubor',  args.soubor)

    graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")
#    graph_db.clear()
#    main(graph_db)
    priklad(graph_db)
#    cypherem_vypíšu_vše(graph_db)
