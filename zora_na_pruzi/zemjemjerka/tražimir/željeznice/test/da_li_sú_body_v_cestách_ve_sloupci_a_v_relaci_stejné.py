#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je test správného tvoření SQL dotazů Danimírem
'''

from pruga.zemjemjerka.tražimir.željeznice.proložím_trať import db,  davaj_cesty_z_relace

from pruga.danimir.příkazy import SELECT

id_relace = 48896

def test_esli_sú_nodes_stejné():
    '''
    Hen kontroluju, esli body ve sloupci nodes v tabulce ways su stejné jako body propojené přes tabulku way_nodes s tabulkou nodes
    '''
    cesty = davaj_cesty_z_relace(id_relace)
    počítátko_cest = 0
    počítátko_bodů = 0
    for cesta in cesty:
        select = SELECT('node_id')
        select.FROM(db.way_nodes)
        select.WHERE(db.way_nodes.way_id == cesta.id_cesty)
        select.ORDER_BY(db.way_nodes.sequence_id)
        body = db(select)
        počítátko_cest = počítátko_cest + 1
        for i,  bod in enumerate(body):
            počítátko_bodů = počítátko_bodů + 1
            
            assert bod.node_id ==  cesta.body_v_cestě[i]
            
    print('\nHOTOVO, prošel jsem {} bodů v {} cestách'.format(počítátko_bodů,  počítátko_cest))



