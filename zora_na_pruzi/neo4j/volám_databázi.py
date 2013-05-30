#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

def main():
    '''
    spouštím funkci main()
    '''
    from py2neo import neo4j

    graph_db = neo4j.GraphDatabaseService(neo4j.DEFAULT_URI)
    print(graph_db.neo4j_version)
    graph_db.clear()
    
    # create a single node
    alice, = graph_db.create({"name": "Alice"})
    print(alice)

def priklad():
    from py2neo import neo4j, cypher

    # attach to a local graph database service
    graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

    graph_db.clear()

    # create two nodes and a relationship between them
    #   (Alice)-[:KNOWS]->(Bob)
    alice, bob, ab = graph_db.create(
        dict(name="Alice"), dict(name="Bob"), (0, "KNOWS", 1)
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
    

if __name__ == '__main__':

    print(__doc__)

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

#    main()
    priklad()
