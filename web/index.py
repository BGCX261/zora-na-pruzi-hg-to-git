#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'



if __name__ == '__main__':

    import bottle
#    from bottle import route, run,  debug,  template

    @bottle.route('/hello')
    def hello():
        return "Hello World!"
        
    @bottle.get('/firma/<ičo>')
    def firma(ičo=None):
        return bottle.template('firma.tpl', ičo=ičo)
    #    return bottle.template('firma.tpl', ico=ico)

    bottle.debug(True)
#    bottle.run(host='localhost', port=8081)
    
#    tpl = bottle.template('firma.tpl',  template_lookup = ('./pohledy', ),  ičo = '458855')
#    print(tpl)
