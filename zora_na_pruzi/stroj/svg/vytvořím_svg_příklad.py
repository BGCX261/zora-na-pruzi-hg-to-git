#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

print('Jak udělám SVG soubor')

from zora_na_pruzi.strojmir.xml.svg import E

def davaj_svg():

    svg = E.SVG()

    svg.titulek = 'TITULEK'
    svg.popisek = 'popisuji svg'
    kruh = E.G().kružnice(střed = (45,  50),  poloměr = 40)
    svg.append(kruh)
    css_kruhu = kruh.css_dle_třídy('KOLO',  element = True)
    css_kruhu.fill(0xFFFF00).stroke(0x1100CC).stroke_width(4,  'px')
    
    return svg

if __name__ == '__main__':
    svg = davaj_svg()
    print(svg)

    uložím_do_souboru = 'testuji.svg'
    import os
    svg.CSS >> '{}.{}'.format(os.path.splitext(uložím_do_souboru)[0],  'css')
    svg >> uložím_do_souboru

    import webbrowser
    webbrowser.open(uložím_do_souboru)
