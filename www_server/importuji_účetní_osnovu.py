#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

import logging
logger = logging.getLogger(__name__)
debug = logger.debug
#logging.basicConfig(level = logging.DEBUG)

from pruga.neomodel import (StructuredNode, StringProperty, IntegerProperty,
    RelationshipTo, RelationshipFrom)

class Country(StructuredNode):
    code = StringProperty(unique_index=True, required=True)

    # traverse incoming IS_FROM relation, inflate to Person objects
    inhabitant = RelationshipFrom('Person', 'IS_FROM')


class Person(StructuredNode):
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)

    # traverse outgoing IS_FROM relations, inflate to Country objects
    country = RelationshipTo(Country, 'IS_FROM')

class Účet(StructuredNode):
    číslo = StringProperty(unique_index=True)

if __name__ == '__main__':

#    print(__doc__)

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


    import os
    from pruga.servery import medvěd
    if not medvěd.status():
        medvěd.start()
#    print(medvěd.status())
    os.environ['NEO4J_REST_URL'] = medvěd.url()

#    jim = Person(name='Jim', age=3)
#    jim.refresh()
#    print(jim)
#    jim.age = 4
#    jim.save() # validation happens here
#    print(jim)
#    jim.delete()
#    jim.refresh() # reload properties from neo
#    print(jim)
    
    účet302 = Účet(číslo = '302')
#    účet302x = Účet(číslo = '302')
#    účet302x.refresh()
#    
#    účet302.save()
#    účet302x.save()

    from pruga.importuji_data.importuji_účetnictví.účetní_osnova import davaj_cypher_pro_import_účetní_osnovy

    from pruga.cython import CREATE

    #for řádek in davaj_cypher_pro_import_účetní_osnovy():
    #    print(řádek)
    
    cql = ',\n'.join(CREATE(* davaj_cypher_pro_import_účetní_osnovy()))
    print('CREATE\n{};'.format(cql))
    

    

   
