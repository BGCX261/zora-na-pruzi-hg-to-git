
import os

CESTA_K_SERVERU = os.path.realpath(os.path.join(os.path.dirname(__file__),  '../../../..'))

NEO4J_SRC = os.path.join(CESTA_K_SERVERU,  'instalace/neo4j-community-2.0.0-M02-unix.tar.gz')
NEO4J_ADRESÁŘ_DATABÁZÍ = os.path.join(CESTA_K_SERVERU,  'databáze')
TEMP_ADRESÁŘ = os.path.join(CESTA_K_SERVERU,  'temp')

NEO4J_URL = 'http://localhost:7474/db/data/'
NEO4J_BIN = 'bin/neo4j'
NEO4J_SERVER_PROPERTIES = 'conf/neo4j-server.properties'
