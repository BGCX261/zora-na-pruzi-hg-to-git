#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je nástroj, který obarví výpis
'''

from zora_na_pruzi.pisar.html.html import HTML,  E

H1 = HTML(E.H1('{}'))
H2 = HTML(E.H2('{}'))
H3 = HTML(E.H3('{}'))
H4 = HTML(E.H4('{}'))
H5 = HTML(E.H5('{}'))
H6 = HTML(E.H6('{}'))

NADPIS = H1

P = HTML(E.P('{}'))

INFO = HTML(E.DIV(E.H2('INFO'),  E.P('INFO:{}',  E.CLASS('info'))))

SOUBOR = HTML(E.SPAN(E.CLASS('jmeno_souboru'),  E.I('"{}"')))


