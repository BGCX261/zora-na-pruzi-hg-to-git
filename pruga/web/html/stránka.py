#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

from pruga.strojmir.xml.html5 import E
from pruga.strojmir import hlavička as HLAVIČKA

def stránka(**nastavení):
    return \
    E.HTML(
        E.HEAD(
                E.META(charset = nastavení.get('kódování', 'utf-8')), 
                E.TITLE(nastavení.get('titulek', 'Зора на прузи')),
                E.META(name = 'description',  content = nastavení.get('meta_popisek', HLAVIČKA.hlavička_automaticky_vytvořila()))
        ),
        E.BODY(
               
        ), 
        lang = nastavení.get('jazyk', 'cz'), 
        )

def stránka2():

    stránka = E.HTML()
    stránka.set('lang',  'cz')

    hlavička = stránka.hlavička
    hlavička.append(E.META(charset = 'utf-8'))

    hlavička.titulek = 'TITULEK'
    hlavička.popisek = HLAVIČKA.hlavička_automaticky_vytvořila()
    #hlavička.autor = 


    #svg.popisek = 'popisuji svg'
    #kruh = E.G().kružnice(střed = (45,  50),  poloměr = 40)
    #svg.append(kruh)
    #css_kruhu = kruh.css_dle_třídy('KOLO',  element = True)
    #css_kruhu.fill(0xFFFF00).stroke(0x1100CC).stroke_width(4,  'px')


    #uložím_do_souboru = 'index.html'
    #import os
    #svg.CSS >> '{}.{}'.format(os.path.splitext(uložím_do_souboru)[0],  'css')
    #stránka >> uložím_do_souboru

    #import webbrowser
    #webbrowser.open(uložím_do_souboru)

    return stránka


if __name__ == '__main__':
    print('Jak udělám HTML5 soubor')
    stránka = stránka()
    
    tělo = stránka.tělo
    
    tělo.záhlaví.text = 'záhlaví stránky'
    
    zápatí = tělo.zápatí
    zápatí.text =  HLAVIČKA.vytvořila()
    práva = E.SMALL(id = 'copyright')
    zápatí.append(práva)
    práva.text = HLAVIČKA.práva()
    
    print(stránka)
