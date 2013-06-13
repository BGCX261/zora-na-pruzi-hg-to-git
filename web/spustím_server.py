#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

import json

import bottle
from html.stránka import stránka,  E

@bottle.get("/text")
def text():
    return "Returning text"

@bottle.get("/data/get")
def get_data():
    try:
        position = bottle.request.params["position"]
    except:
        return {
                "result": "error-bad-data"
        }
    return {
        "result": "",
        "data": "Data on position %s" % position,
    }

@bottle.get("/data/getarray")
def get_array():
    bottle.response.content_type = "application/json"
    return json.dumps([ 1, 2, 3, 4, 5, ])


@bottle.route("/data/store", method=["GET", "POST"])
def store_data():
    try:
        if "position" in bottle.request.forms:
            position = bottle.request.forms["position"]
            data = bottle.request.forms["data"]
        else:
            position = bottle.request.params["position"]
            data = bottle.request.params["data"]
    except:
        return {
                "result": "error-bad-data"
        }

    if position.startswith("9"):    # to test an invalid position
        return {
                "result": "error-no-such-position"
        }
    return {
        "result": ""
    }

@bottle.get("/")
def index():
    return bottle.static_file("index.html", root=".")
  
@bottle.get('/css/<filename:path>')
def css_staticky(filename):
    return bottle.static_file(filename, root='./css')

@bottle.get('/js/<filename:path>')
def js_staticky(filename):
    return bottle.static_file(filename, root='./js')

@bottle.get("/<meno>")
def dávám_obsah(meno):
    print('IDZE {}'.format(meno.encode('latin1').decode('utf8') ))
    return 'IDZE {}'.format(meno.encode('latin1').decode('utf8') )
 
@bottle.route("/test",  method=["GET", "POST"])
def test():
    
    html = stránka(titulek = 'zkúšam s ajaxom')
    
    html.tělo << (E.H1('Testuji'))
    
    dl = html.tělo << E.DL()

    dl('is_xhr',  bottle.request.is_xhr or 'NE')
    print('is_xhr',  bottle.request.is_xhr or 'NE')
    dl('is_ajax',  bottle.request.is_ajax or 'NE')
    print('is_ajax',  bottle.request.is_ajax or 'NE')
   
    html.tělo << E.H2('davao GET')
    print('davao GET')
    dl = html.tělo << E.DL()
    for klíč,  hodnota in bottle.request.query.items():
        dl(klíč,  hodnota or 'NENÍ')
        print(klíč,  hodnota or 'NENÍ')
        
    html.tělo << E.H2('davao POST')
    print('davao POST')
    dl = html.tělo << E.DL()
    for klíč,  hodnota in bottle.request.forms.items():
        dl(klíč,  hodnota or 'NENÍ')
        print(klíč,  hodnota or 'NENÍ')
     
    print('JSON')
    print(bottle.request.json)
    print('BODY')
    print(bottle.request.body.getvalue())
    return str(html)

if __name__ == '__main__':
    
    import argparse
    import logging
    
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser()

#   a pak mu nastavím jaké příkazy a parametry má přijímat
    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, {}'.format(__version__))
    
    parser.add_argument('--graf_db',  default = 'testovací')
    parser.add_argument('--logovací_úroveň',  default = logging.DEBUG)
    
    #    a včíl to možu rozparsovat
    args = parser.parse_args()
    
    logging.basicConfig(level = args.logovací_úroveň)
    logger = logging.getLogger(__name__)
    debug = logger.debug
    
    debug('Spustím grafickou databázi {}'.format(args.graf_db))
    
    from pruga.databáze.Neo4j import Neo4j,  VYPNUTO
    
    neo4j = Neo4j(args.graf_db)
    
    stav,  status = neo4j.status()
    
    if stav == VYPNUTO:
        neo4j.start()
        
    neo4j_url = neo4j.url
    
    debug('Spustím bottle server')
    
    bottle.debug(True)
    bottle.run(host='localhost', port=8080, reloader=True)
