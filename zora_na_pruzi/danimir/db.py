#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

def db(připojení = None):
    if připojení is not None:
        db.připojení = připojení
        
    return db.připojení
    
db.připojení = None
