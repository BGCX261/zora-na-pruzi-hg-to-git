#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

print('Jak udělám SVG soubor')

from zora_na_pruzi.strojmir.xml.svg import nové_svg

svg = nové_svg()

svg.titulek = 'TITULEK'
svg.popisek = 'popisuji svg'
kruh = svg.G.kružnice(střed = (45,  50),  poloměr = 40)
css_kruhu = kruh.css_dle_třídy('KOLO',  True)
css_kruhu.fill(0xFFFF00).stroke(0x1100CC).stroke_width(4,  'px')

print(svg)

uložím_do_souboru = 'testuji.svg'
import os
svg.CSS >> '{}.{}'.format(os.path.splitext(uložím_do_souboru)[0],  'css')
svg >> uložím_do_souboru

import webbrowser
webbrowser.open(uložím_do_souboru)
