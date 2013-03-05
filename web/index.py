#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'



if __name__ == '__main__':

    from bottle import route, run,  debug

    @route('/hello')
    def hello():
        return "Hello World!"

    debug(True)
    run(host='localhost', port=8080)
