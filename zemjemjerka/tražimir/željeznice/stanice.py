#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který hledá body, cesty a relace pro stanici
'''

from pruga.zemjemjerka.nastavení.databáze import davaj_připojení

db = davaj_připojení()

def davaj_seznam_stanic():
    dotaz = 'SELECT id, tags->\'name\' AS "jméno", tags FROM osm.nodes WHERE tags @> \'"railway"=>"station"\' ORDER BY jméno'
    pitanje = db.prepare(dotaz)
    return pitanje()

def davaj_body_stanic(jméno_stanice):
    '''
    najde bod, který znázorňuje železniční stanici,
    hledá podle názvu stanice
    '''
    
    dotaz = 'SELECT *, tags->\'name\' AS "jméno" FROM osm.nodes WHERE tags @> \'"railway"=>"station"\' AND tags->\'name\' LIKE \'{}\''.format(jméno_stanice)
    pitanje = db.prepare(dotaz)
    return pitanje()

def davaj_cesty_bodu(id_bodu):
    
    dotaz = 'SELECT way_id FROM osm.way_nodes WHERE node_id = {}'.format(id_bodu)
    pitanje = db.prepare(dotaz)
    return pitanje()
    
def davaj_relace_bodu(id_bodu):
    
    dotaz = 'SELECT relation_id FROM osm.relation_members WHERE member_type = \'N\' AND member_id = {}'.format(id_bodu)
    pitanje = db.prepare(dotaz)
    return pitanje()    
    
def davaj_relace_cesty(id_cesty):
    
    dotaz = 'SELECT relation_id FROM osm.relation_members WHERE member_type = \'W\' AND member_id = {}'.format(id_cesty)
    pitanje = db.prepare(dotaz)
    return pitanje()    


if __name__ == '__main__':

    import pprint
    import argparse

    print(__doc__)
    
    parser = argparse.ArgumentParser()
    parser.add_argument( '--hledej',  dest='jméno_stanice', metavar='jméno_stanice', type=str,  help='jméno železniční stanice, kterou chci najít')
    parser.add_argument('-s', '--seznam', action="store_true", default=False,   help='seznam všech stanic')
    args = parser.parse_args()
    
#    print(args)

    

    if args.seznam:
        seznam_stanic = davaj_seznam_stanic()
        pprint.pprint(seznam_stanic)
    else:

        stanice = davaj_body_stanic(args.jméno_stanice)
        
        print('Hledám stanici "{}"'.format(args.jméno_stanice))
        
        print('Nalezeno {} stanic'.format(len(stanice)))
        for stanica in stanice:
            print('#' * 22)
            print('\t{id} - {jméno}:{tags}'.format(**stanica))
            id_bodu = stanica['id']
            print('\tHledám cesty na kterých je stanice s id "{}"'.format(id_bodu))
            cesty = davaj_cesty_bodu(id_bodu)
            print('\ttato stanice je v {} cestách:'.format(len(cesty)))
            for cesta in cesty:
                print('\t{way_id}'.format(**cesta))
                id_cesty = cesta['way_id']
                print('\tHledám relace ve kterých je cesta s id "{}"'.format(id_bodu))
                relace_cesty = davaj_relace_cesty(id_cesty)
                print('\t\tcesta je v {} relacích:'.format(len(relace_cesty)))
                for relacia in relace_cesty:
                    print('\t\t{relation_id}'.format(**relacia))
                
            print('\tHledám relace na kterých je stanice s id "{}"'.format(id_bodu))
            relace_bodu = davaj_relace_bodu(id_bodu)
            print('\tstanice je sama o sobě v {} relacích:'.format(len(relace_bodu)))
            for relacia in relace_bodu:
                print('\t{relation_id}'.format(**relacia))
       




