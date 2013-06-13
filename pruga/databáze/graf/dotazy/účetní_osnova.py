#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

from py2neo import cypher,  node,  rel

ÚČTOVÁ_OSNOVA = '`Účtová osnova`'
ÚČTOVÁ_TŔÍDA = '`Účtová třída`'
ÚČTOVÁ_SKUPINA = '`Účtová skupina`'
ÚČET = '`Účet`'

ÚČTOVÁ_OSNOVA_MÁ_TŘÍDU = ':`MÁ TŘÍDU`'
ÚČTOVÁ_TŘÍDA_MÁ_SKUPINU = ':`MÁ SKUPINU`'
ÚČTOVÁ_SKUPINA_MÁ_ÚČET = ':`MÁ ÚČET`'

def data(gdb):
#    cypher("MATCH n:`Účtová třída` RETURN ID(n) AS id, n.`jméno` AS `jméno`, n.`číslo` AS `číslo`;", {}, pridam_uzly);
#    cypher("MATCH n:`Účtová skupina` RETURN ID(n) AS id, n.`jméno` AS `jméno`, n.`číslo` AS `číslo`;", {}, pridam_uzly);
#    cypher("MATCH n:`Účet` RETURN ID(n) AS id, n.`jméno` AS `jméno`, n.`číslo` AS `číslo`;", {}, pridam_uzly);
    dotaz = 'MATCH n:`Účtová třída` RETURN ID(n) AS id, n.`jméno` AS `jméno`, n.`číslo` AS `číslo`'
    data = gdb.cypher(dotaz)
    return data
 
def účetní_třídy(gdb):
    dotaz = 'MATCH n:`Účtová třída` RETURN ID(n) AS id, n.`jméno` AS `jméno`, n.`číslo` AS `číslo` ORDER BY n.`číslo`'
    data = gdb.cypher(dotaz)
    return data
    
def účetní_skupiny(gdb,  třída = None):
    if třída is None:
        dotaz = 'MATCH n:`Účtová skupina` RETURN ID(n) AS id, n.`jméno` AS `jméno`, n.`číslo` AS `číslo` ORDER BY n.`číslo`'
        return gdb.cypher(dotaz)
    else:
        dotaz = 'START u=node({id}) MATCH u-[:`MÁ SKUPINU`]->n:`Účtová skupina` RETURN ID(n) AS id, n.`jméno` AS `jméno`, n.`číslo` AS `číslo` ORDER BY n.`číslo`'
        return gdb.cypher(dotaz,  {'id': třída})
        
def účty(gdb,  skupina = None):
    if skupina is None:
        dotaz = 'MATCH n:`Účet` RETURN ID(n) AS id, n.`jméno` AS `jméno`, n.`číslo` AS `číslo` ORDER BY n.`číslo`'
        return gdb.cypher(dotaz)
    else:
        dotaz = 'START u=node({id}) MATCH u-[:`MÁ ÚČET`]->n:`Účet` RETURN ID(n) AS id, n.`jméno` AS `jméno`, n.`číslo` AS `číslo` ORDER BY n.`číslo`'
        return gdb.cypher(dotaz,  {'id': skupina})

def html(gdb):
    from pruga.strojmir.xml.html5 import E
    
    html = E.UL(id = 'účetní_osnova')
    
    for řádek in účetní_třídy(gdb):
        id,  jméno,  číslo = řádek
        li = html << E.LI()
        li << E.H1('{}: {}'.format(číslo,  jméno),  id = 'uzel_{}'.format(id))
        html_skupin = li << E.UL()
        for řádek in účetní_skupiny(gdb,  třída = id):
            id,  jméno,  číslo = řádek
            li_skupin = html_skupin << E.LI()
            li_skupin << E.H2('{}: {}'.format(číslo,  jméno),  id = 'uzel_{}'.format(id))
            html_účtů = li_skupin << E.UL()
            for řádek in účty(gdb,  skupina = id):
                id,  jméno,  číslo = řádek
                html_účtů << E.LI('{}: {}'.format(číslo,  jméno),  id = 'uzel_{}'.format(id))
        
    return str(html)
