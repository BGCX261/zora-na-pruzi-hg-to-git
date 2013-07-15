#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

import logging
logging.basicConfig(level = logging.DEBUG)
logger = logging.getLogger(__name__)
debug = logger.debug

def připojím_neo4j_server():
    from pruga.databáze.Neo4j import Neo4j
    
    neo4j = Neo4j('testovací')
    
    from pruga.databáze.graf.Graf import Graf
    graf_db = Graf(neo4j.url)
    
    return graf_db
    
def vyprázdním_neo4j():
    
#    graf_db.neo4j.clear()
    cypher = '''START n=node(*)
MATCH n-[r?]-()
WHERE ID(n) <> 0
DELETE n,r'''

    return cypher


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


    graf_db = připojím_neo4j_server()

    cypher = vyprázdním_neo4j()
    graf_db.cypher(cypher)
    
    from importuji_účetnictví.účetní_osnova import davaj_cypher_pro_import_účetní_osnovy,  davaj_cypher_pro_indexy
    
    for cypher in davaj_cypher_pro_import_účetní_osnovy():
        graf_db.cypher(cypher)
        
    for cypher in davaj_cypher_pro_indexy():
        graf_db.cypher(cypher)

