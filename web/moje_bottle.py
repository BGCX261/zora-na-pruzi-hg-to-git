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

bottle.debug(True)
bottle.run(host='localhost', port=8080, reloader=True)
