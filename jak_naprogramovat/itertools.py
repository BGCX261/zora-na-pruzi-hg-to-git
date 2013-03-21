#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import itertools

m = {'A': 1,  'B': 2}
s = [1, 2, 3, 4, 5]


#ze slovníku vrací jen klíče
#musím dát items() abych získal i data,  pak to vrací tuple(klíč,  hodnota)

for x in itertools.chain(m.items(),  s):
    print(type(x))
    print(x)
    
