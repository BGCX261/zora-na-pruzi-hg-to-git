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

@bottle.route("/")
def index():
    return bottle.static_file("index.html", root=".")
  
@bottle.route('/css/<filename:path>')
def send_static(filename):
    return bottle.static_file(filename, root='./css')

@bottle.route('/js/<filename:path>')
def send_static(filename):
    return bottle.static_file(filename, root='./js')

@bottle.route("/<meno>",  method=["GET", "POST"])
def stránka(meno):
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
    bottle.debug(True)
    bottle.run(host='localhost', port=8080, reloader=True)
