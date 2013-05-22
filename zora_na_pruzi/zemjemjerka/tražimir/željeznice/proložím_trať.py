#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který načte trať a dál ju bude upravovat
'''

from zora_na_pruzi.pruga.danimir import databáze
from zora_na_pruzi.pruga.danimir.příkazy import SELECT,  INSERT,  UPDATE
from zora_na_pruzi.pruga.danimir.připojení import zemjemjerka as nastavení_připojení_k_databázi

db = databáze(nastavení_připojení_k_databázi)

def davaj_cesty_z_relace(id_relace):
    
    tabulka_relací = db['osm'].relation_members
    tabulka_cest = db['osm'].ways
    
    select = SELECT(
                        tabulka_relací.member_id.AS('id_relace'),
                        tabulka_cest.id.AS('id_cesty'),
                        tabulka_relací .sequence_id.AS('pořadí_cesty'),
                        tabulka_cest.nodes.AS('body_v_cestě')
                        )
    select.FROM(tabulka_relací).JOIN(tabulka_relací.member_id,  tabulka_cest.id)
    where = tabulka_relací.relation_id == id_relace
    where.AND(tabulka_relací.member_type.LIKE('W'))
    select.WHERE(where)
    select.ORDER_BY(tabulka_relací .relation_id,  tabulka_relací .sequence_id)
#    print(select)
    return db(select)


def davaj_body_v_cestě(id_cesty,  otoč = None):
    
    db.set_schema('zemjemjerka', 'osm', 'postgis', 'public')
    
    tabulka_cest = db.way_nodes
    tabulka_bodů = db.osm_nodes_s_utm_souřadnicemi
    
    vyberu_sloupce = (

        )
    select = SELECT(
                            tabulka_cest.way_id.AS('id_cesty'),
                            tabulka_cest.node_id.AS('id_bodu'),
                            tabulka_cest.sequence_id.AS('pořadí_bodu'),
                            tabulka_bodů.tags.AS('značky'),
                            db['postgis'].x(tabulka_bodů.geom).AS('poledník'),
                            db['postgis'].y(tabulka_bodů.geom).AS('rovnoběžka'),
                            db['postgis'].x(tabulka_bodů.utm_souřadnice).AS('utm_x'),
                            db['postgis'].y(tabulka_bodů.utm_souřadnice).AS('utm_y') ,
                            tabulka_bodů.utm_zóna.AS('zóna'),
                            tabulka_bodů.utm_SRID.AS('utm_SRID')
                        )
    select.FROM(tabulka_cest)
    select.JOIN(tabulka_cest.node_id,  tabulka_bodů.id)
    select.WHERE(tabulka_cest.way_id == id_cesty)
    řazení = tabulka_cest.sequence_id
    if otoč:
        řazení = řazení.DESC()
    select.ORDER_BY(tabulka_cest.way_id,  řazení)

########################################################
#   tady si vypíšu sloupce, které si pak překopíruji do kódu a upravím - abych to nemsuel psát ručně
#    from pruga.danimir.nástroje.seznam_sloupců import seznam_sloupců_tabulky
#       
#    sloupce = seznam_sloupců_tabulky(databáze = db,  tabulka = tabulka_cest,  formát = 'tabulka_cest.{}') + seznam_sloupců_tabulky(databáze = db,  tabulka = tabulka_bodů,  formát = 'tabulka_bodů.{}')
#    print(', '.join(sloupce))
#    import sys
#    sys.exit()
#####################################################
    
#    print(select)

    body = db(select)
   
    return body

def davaj_trať(id_relace):
    '''
    zahájí běh programu
    '''
    
    from altgraph.Graph import  Graph
    
    graf = Graph()
    
    cesty = davaj_cesty_z_relace(id_relace)
    
#    vložím cesty do grafu
    for cesta in cesty:
        graf.add_edge(cesta.body_v_cestě[0], cesta.body_v_cestě[-1],  {'id': cesta.id_cesty,  'pořadí': cesta.pořadí_cesty})        
        
    print('graf má {} vrcholů a {} hran'.format(graf.number_of_nodes(),  graf.number_of_edges()))
    

#    projdu všechny vrcholy a vyberu ty,  které mají pouze jednu hranu
    jednohrané_vrcholy = []
    for bod in graf.node_list():
        if graf.all_degree(bod) == 1:
#            print("vrchol {} vstupuje {} a vystupuje {} hran, celkem {}".format(bod, graf.inc_degree(bod),    graf.out_degree(bod),   graf.all_degree(bod)))
            jednohrané_vrcholy.append(bod)
 
#    jednohrané vrcholy musí být právě dva
    if len(jednohrané_vrcholy) != 2:
        raise ValueError('Tož ale graf musí být právě jeden počátek a právě jeden konec')
        #        když má graf právě jeden začátek a právě jeden konec,  možeme srovnat hrany, otočit je do jednoho směru
    else:
        print('jednohrané vrcholy',  jednohrané_vrcholy)
#        tu práci obsatrá rekurzivně tato funkce,  která graf pozmění
        seřadím_hrany_v_grafu(graf,  jednohrané_vrcholy[0])


#včíl projdu už upravený,  správně natočený graf a načtu všechny body
    najdu_body_pro_hrany_v_grafu(graf)


def seřadím_hrany_v_grafu(graf,  počáteční_vrchol,  předchozí_hrana = None):
    
    počet_výchozích_hran = graf.out_degree(počáteční_vrchol)
    počet_vstupních_hran = graf.inc_degree(počáteční_vrchol)
    
    další_hrana = None
    
#    právě jedna hrana by měla být výchozí
    if počet_výchozích_hran == 1 and (počet_vstupních_hran == 0 if předchozí_hrana is None else počet_vstupních_hran == 1):
        další_hrana = graf.out_edges(počáteční_vrchol)[0]
#        něgdy sa stane,  že vstupují dvě hrany,  tu jednu musíme otočit
    elif počet_výchozích_hran == 0 and počet_vstupních_hran == 2:
        vstupní_hrany = graf.inc_edges(počáteční_vrchol)
        for další_hrana in vstupní_hrany:
#            print('PH',  další_hrana,  předchozí_hrana)
            if další_hrana != předchozí_hrana and předchozí_hrana is not None:
                data = graf.edge_data(další_hrana)
#                print('DATA', data)
                data['otoč'] = 1
#                print('DATA', data)
                V1 = graf.tail(další_hrana)
                V2 = graf.head(další_hrana)
                graf.add_edge(V1, V2 ,  data)
                graf.hide_edge(další_hrana)
                další_hrana = graf.edge_by_node(V1, V2)
#                print('nobva ph ',  další_hrana)
                break
#        print(další_hrana)
# toto je poslední hrana,  konečná, došli sme do koncového bodu
    elif počet_výchozích_hran == 0 and počet_vstupních_hran == 1 and předchozí_hrana is not None:
#        print('KONEC')
        return 1
    else:
        raise ValueError('Požaduji začít v bodě, ze kterého vede právě jedna hrana, z tadyma jich vede {} a vstupuje {}'.format(počet_výchozích_hran,  počet_vstupních_hran))
        
        
#    print('počáteční vrchol {} a tomu hrana {} - {} {}'.format(počáteční_vrchol, graf.head(další_hrana),  graf.tail(další_hrana),  graf.describe_edge(další_hrana)))

#    rekurzivně jdu dál grafem po další hraně
    seřadím_hrany_v_grafu(graf,  graf.tail(další_hrana),  další_hrana)

def najdu_body_pro_hrany_v_grafu(graf):
    for hrana in graf.edge_list():
        data = graf.edge_data(hrana)
        body = davaj_body_v_cestě(data['id'],  data.get('otoč',  None))
#        for bod in body:
#            print(bod)


def nakreslím_graf(graf):
    from altgraph import Dot
#    ,  GraphStat
    
    
#    statistika = GraphStat.degree_dist(graf)
#    print(statistika)
    
#    # create a dot representation of the graph
    dot = Dot.Dot(graf)
#
#    # display the graph
    dot.display()

    # save the dot representation into the mydot.dot file
#    dot.save_dot(file_name='mydot.dot')

    # save dot file as gif image into the graph.gif file
#    dot.save_img(file_name='graph', file_type='gif')
    
#    *******************************************************************************************
#    networkx.draw_graphviz(graf)
#    networkx.write_dot(graf,'file.dot')

#    import matplotlib.pyplot as plt
#    networkx.draw(graf)
#    plt.show()


if __name__ == '__main__':

    print(__doc__)

    id_relace = 48896
    
#    cesty = davaj_cesty_z_relace(id_relace)
#    print(cesty())

    davaj_trať(id_relace)
    




