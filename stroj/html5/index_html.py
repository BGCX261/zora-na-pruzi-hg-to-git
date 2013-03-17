#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

print('Jak udělám HTML5 soubor')

from zora_na_pruzi.strojmir.xml.html5 import E
from zora_na_pruzi.strojmir.hlavička import hlavička_automaticky_vytvořila

stránka = E.HTML()
stránka.set('lang',  'cz')

hlavička = stránka.hlavička
hlavička.append(E.META(charset = 'utf-8'))

hlavička.titulek = 'TITULEK'
hlavička.popisek = hlavička_automaticky_vytvořila()
#hlavička.autor = 

tělo = stránka.tělo


#svg.popisek = 'popisuji svg'
#kruh = E.G().kružnice(střed = (45,  50),  poloměr = 40)
#svg.append(kruh)
#css_kruhu = kruh.css_dle_třídy('KOLO',  element = True)
#css_kruhu.fill(0xFFFF00).stroke(0x1100CC).stroke_width(4,  'px')


print(stránka)

#uložím_do_souboru = 'index.html'
#import os
#svg.CSS >> '{}.{}'.format(os.path.splitext(uložím_do_souboru)[0],  'css')
#stránka >> uložím_do_souboru

#import webbrowser
#webbrowser.open(uložím_do_souboru)
