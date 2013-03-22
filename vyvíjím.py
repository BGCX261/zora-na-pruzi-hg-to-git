#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je skript, gde si zkúšám
'''

import os

from zora_na_pruzi.vidimir.Formátuji import TEXT

#from zora_na_pruzi.pohunci.obarvím_výpis.barevný_logger import daj_logovátka
#debug,  info,  warning,  error,  critical = daj_logovátka(__file__)


#def spustím(*příkaz):
##    PYTHON_BIN = 'python3'
#    import subprocess
#    
##    příkaz = [PYTHON_BIN]
##    příkaz.extend(parametry)
#    subprocess.Popen(příkaz)

def rebuild():
#    cdir = os.getcwd()
#    os.chdir('../')
    os.system('./rebuild.sh')
#    os.chdir(cdir)
    
def build():
#    cdir = os.getcwd()
#    os.chdir('../')
    os.system('./setup.py build')
#    os.chdir(cdir)
    
#build()


def pisar():
#    from zora_na_pruzi.vidimir.Pisar import Pisar
    
#    print(Pisar)
##    print(styl.H1) >> AttributeError
#    pisar = Pisar('barevná_konzole')
#    print(pisar.pohled)
#    print(pisar.pohled.H1)
    
    from zora_na_pruzi.vidimir.Formátuji import TEXT
    from zora_na_pruzi.vidimir.Formátuji import HTML
    
####    with Pisar('barevná_konzole') as pisar:
    print('tu še with' | TEXT.H1)
    
    
    from zora_na_pruzi.vidimir.formáty.barevná_konzole import TEST
#        print(TEXT.TEST.START) NotImplementedError
    print(type(TEST.START))
    from zora_na_pruzi.vidimir.stroj.Formát import Formát
    print('startuje test ' | Formát(TEST.START))
####        with Pisar('html') as pisar:
    print(type(HTML.H1))
    print('NADPIS' | HTML.H1)
#            print('startuje test ' | TEXT.TEST.START)
#        print(p)

def html_výpis():
    
    from zora_na_pruzi.vidimir.Formátuji import HTML
#    from zora_na_pruzi.vidimir.Pisar import Pisar
    
#    with Pisar(jméno_vidu = 'html'):
    print('NADPIS' | HTML.NADPIS)
    
#        from zora_na_pruzi.pisar.html.html import HTML,  E
#
#        odstavec = HTML(E.DIV(E.H4('NADPIS úrovně 4'),  E.P('tu je text:*** {} ***',  E.CLASS('css_třída'))))
    
    print('soubor {} je tu'.format(__file__ | HTML.SOUBOR) | HTML.INFO)
    print('soubor {} je tu'.format(__file__ | HTML.SOUBOR) | HTML.DIV)
    
def barevná_konzole():
    from zora_na_pruzi.vidimir.Formátuji import TEXT
    
    print('NADPIS' | TEXT.NADPIS)
    
    from zora_na_pruzi.vidimir.stroj.konzole.dekorátory import obarvi
    from zora_na_pruzi.vidimir.stroj.konzole.barvy import MODRÁ

#    modře = Obarvi(MODRÁ)
    @obarvi(MODRÁ)
    def modře(text):
        return text
        
    from zora_na_pruzi.vidimir.stroj.Formát import Formát
    
    print('soubor {} je tu'.format(__file__ | TEXT.SOUBOR) | TEXT.INFO)
    print('soubor {} je tu'.format(__file__ | TEXT.SOUBOR) | Formát(modře))


def   validátor():
    
    from zora_na_pruzi.strojmir.xml.schémata import Relax_NG,  Relax_NG_c,  XMLSchema,  DTD

#    rg = Relax_NG.Validátor('graphml')
#    dtd = DTD.Validátor('graphml')
#    x = XMLSchema.Validátor('graphml')
#    print(rg.medvěd,  dtd.medvěd,  x.medvěd)
#    return

    for schéma in Relax_NG,  Relax_NG_c,  XMLSchema,  DTD:
        print('*-*'*77)
        validátor = schéma.Validátor('graphml')
        print('validátor',  validátor)
        
        soubor_schématu = validátor.schéma
        print('schéma {}'.format(soubor_schématu))
        
       
        print(validátor.validátor)
        
        validní = validátor('./graf.graphml')
        print(validní)
        
        
        if validátor('./graf.graphml'):
            print('VALIDNÍ')
        else:
            print('NEVALIDNÍ')
#        print(schéma.mmml)

        validátor(soubor = './graf.graphml',  program = schéma.program)
        
    
def graf():
    
    from zora_na_pruzi.strojmir.xml.graphml import E
    import lxml.etree
    
    graf = E.GRAPHML()
    print(graf.TAG_NAME)
    edge = E.EDGE()
    print(edge.TAG_NAME)
    graf.append(edge)
    lxml.etree.tounicode(graf,  pretty_print=True)
    
    print(graf)
    
    graphml_soubor = './stroj/data/skupiny.graphml'
#    graphml_soubor = './stroj/data/networkx.graphml'
    cesta_k_graphml_souboru = os.path.join(os.path.dirname(__file__),  graphml_soubor)
    
    cesta_k_graphml_souboru = './zora_na_pruzi/strojmir/xml/graphml/testuji_vzorový_graf.graphml'
    
    root = E << cesta_k_graphml_souboru
    
#    uzly = list(root.uzly)
    print(root.TAG_NAME)
    
    print(E.DATA)
    T_data = E.DATA
    T_data.TAG
    print(T_data.TAG)
    
#    print(graphml)
     
    def piš(element,  level = 0):
        tag = element.__class__.__name__
        if tag in ('GRAPHML', 'GRAPH',  'NODE',  'EDGE'):
            print('\t'*level,  tag)
        elif tag in ('_Element', ):
            print('\t'*level,  element.tag)
        else:
            print('\t'*level,  tag)
        for potomek in element:
            piš(potomek,  level + 1)
    
    piš(root)
  

def e_factory():
#    from lxml.builder import ElementMaker
    from lxml.builder import E as EM
    import lxml.etree
#    
    from zora_na_pruzi.strojmir.xml.svg import E
    print('\n*** tu je od ElementMakera ***')
    el = EM.SVG(id = str(245))
    
#    input = EM.input()
#    input.checked = True
#    el.append(input)
#    el = E.SVG(id = 'x')
    print('type: ', type(el))
    print('tag: ',  el.tag)
    print('print: ',  el)
    print('str: ',  str(el))
    print('unicode html: ',  lxml.etree.tounicode(el,  pretty_print=True,  method="html"))
    print('unicode xml: ',  lxml.etree.tounicode(el,  pretty_print=True))
    
    print('\n*** tu je moje ***')
    el = E.SVG()
    print('type: ', type(el))
    print('tag: ',  el.tag)
    print('print: ',  el)
    print('str: ',  str(el))
    
    print('\n*** moj BUILDER ***')
    html_builder = E.SVG
    html_builder_2 = E('SVG')
    print('str 1: ',  str(html_builder))
    print('str 2: ',  str(html_builder_2))
    print()
    
    html_builder['id'] = 245
    html_builder_2 = E('SVG',  id = 245)
    
    print('str 1: ',  str(html_builder))
    print('str 2: ',  str(html_builder_2))
    print()
    
    html_builder['q'] = None
    html_builder_2 = E('SVG',  q = None)
    
    print('str 1: ',  str(html_builder))
    print('str 2: ',  str(html_builder_2))
    print()
    
    html = html_builder(číslo = 245)
    print(html)
    
    
#    el = E.h1() AttributeError
    

def open_xml():
    from zora_na_pruzi.strojmir.xml.svg.SVG import SVG
    
    svg = SVG() << './testuji.svg'
#    svg = SVG << './graf.graphml'
    print(svg)
    
    from zora_na_pruzi.strojmir.xml.svg.G import G
    g = G() << './testuji.svg'
    print(g)

def svg():
#    from zora_na_pruzi.strojmir.xml.svg import nové_svg,  načtu_svg,  NAMESPACE
    
    from zora_na_pruzi.strojmir.xml.svg import E
#    ,  NSMAP,  NAMESPACE
#    from zora_na_pruzi.strojmir.xml.svg.SVG import SVG
#    import lxml.etree
    
#    svg = SVG(id='44',  nsmap = NSMAP)
#    print(svg)
#    kod = lxml.etree.tounicode(svg,  pretty_print=True)
#    print(kod)
#    return
    
#    svg = SVG(id = 'prvni_svg')
#    print(svg.nsmap)
#    
    svg = E.SVG(id = 'prvni_svg')
    
#    print(svg.nsmap)
    print(type(svg))
    print(svg.TAG)
    print(svg.TAG_NAME)
    print(svg.tag)
    print(svg)
    return
#    svg = nové_svg() KeyError
#    svg = načtu_svg('testuji.svg')
#    print('TAG',  svg.TAG)
#    print('tag',  svg.tag)
#    print('TAG local',  svg.TAG.localname)
    print(E.DESC())
    
#    svg_vzor = E << './zora_na_pruzi/strojmir/xml/svg/__testuji_svg/prázdné.svg'
#    g = E << './zora_na_pruzi/strojmir/xml/svg/__testuji_svg/fragment_g.svg'
    
    print(E.G())
    
    načtené_svg = E << 'testuji.svg'
    
    print(načtené_svg)
    
#    graf = načítám_graf()
#    print(graf.tag)
#    print(svg.find('{{{}}}rect'.format(NAMESPACE)))
#    print(svg.__class__.__name__)
    
#    print(svg)
    svg.titulek = 'TITULEK'
#    print(svg)
#    svg.titulek = 'NOVÝ TITULEK'
    svg.popisek = 'popisuji svg'

    kruh = E.CIRCLE(cx = str(50),  cy = str(50),  r = str(30))
#    print('---')
#    print(kruh)
#    print('---')
    
    svg.append(kruh)
    
#    print(svg)
#    svg.titulek = None
    
    
    
    css = svg.CSS.get('circle')
    print(css)
    
    css.fill(0xFF0000)
    css.stroke(0x000000)
    from zora_na_pruzi.strojmir.css.jednotky import px
    css.stroke_width(*px(3))
    
    css = svg.css_dle_id.stroke(0x1100CC)
    
    kruh.css_dle_třídy('KOLO').fill(0xFFFF00)
    kruh.css_dle_třídy('KOLO',  True).fill(0xFFFF00).stroke(0x1100CC)
    
    print('*** PRINT ***')
    print(svg)
    print(kruh)
    print(svg.CSS)
    
#    print(svg)
    
    
    uložím_do_souboru = 'testuji.svg'
    
    svg.CSS >> '{}.{}'.format(os.path.splitext(uložím_do_souboru)[0],  'css')
    svg >> uložím_do_souboru
    
#    from zora_na_pruzi.system.html_prohlížeč import zobrazím_html_stránku
#    zobrazím_html_stránku(uložím_do_souboru)
    
#    import webbrowser
#    webbrowser.open(uložím_do_souboru)


def pygal():
    import pygal                                                       # First import pygal
    bar_chart = pygal.Bar()                                            # Then create a bar graph object
    bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])  # Add some values
    
    uložím_do_souboru = 'bar_chart.svg'
    bar_chart.render_to_file(uložím_do_souboru)
    
    from zora_na_pruzi.system.html_prohlížeč import zobrazím_html_stránku
    zobrazím_html_stránku(uložím_do_souboru)

def css():
#    import cssutils
#    print(cssutils)
#    
#    sheet = cssutils.css.CSSStyleSheet()
##    sheet.namespaces['xhtml'] = 'http://www.w3.org/1999/xhtml'
##    sheet.namespaces['atom'] = 'http://www.w3.org/2005/Atom'
#    sheet.namespaces['svg'] = 'http://www.w3.org/2000/svg'
#    sheet.add('svg|circle {fill: #FF0000; stroke: #000000; stroke-width: 3}')
#    print(sheet.cssText.decode('UTF-8'))

    from zora_na_pruzi.strojmir.css.CSS_TABULKA import CSS_TABULKA
    from zora_na_pruzi.strojmir.css.vlastnosti import VLASTNOSTI
    from zora_na_pruzi.strojmir.css.jednotky import px
    
    css = CSS_TABULKA()
    css_circle = VLASTNOSTI()

    css_circle.fill(0xFF0000)
    css_circle.stroke(0x000000)
    css_circle.stroke_width(*px(3))
    
    css['circle'] = css_circle
#    pravidlo.append(fill)
#    pravidlo.append(stroke_width)
#    pravidlo.append(stroke)
    
    print(css)

def html5():
    from zora_na_pruzi.strojmir.xml.html5 import E
    
    zdroj = './html_šablony/HTML5_reset/index.html'
#    stránka = E << './html_šablony/HTML5_boilerplate/index.html'
    stránka = E << zdroj
    
    print(stránka)
    
#    stránka >> 'testuji.html5'
    
#    os.system('kdiff3 ./html_šablony/HTML5_boilerplate/index.html testuji.html5 &')


    from zora_na_pruzi.system.print_do_souboru import DO_SOUBORU
    import lxml.etree
    import lxml.html
    
    doctype = 'html'
    
    with DO_SOUBORU('testuji_tounicode.html5'):
        print(lxml.etree.tounicode(stránka,  pretty_print=True,   doctype=doctype))
        
    with DO_SOUBORU('testuji_tounicode_html.html5'):
        print(lxml.etree.tounicode(stránka,  pretty_print=True,  method="html",  doctype=doctype))
        
#    with DO_SOUBORU('testuji_html_tostring.html5'):
#        print(lxml.html.tostring(stránka,  pretty_print=True).decode('UTF-8'))
    
#    from lxml.html import  html5parser
#    stránka2 = html5parser.parse(zdroj)
#    with DO_SOUBORU('testuji_html5_tostring.html5'):
#        print(lxml.html.tostring(stránka2,  pretty_print=True).decode('UTF-8'))
#    
    
    os.system('kdiff3 ./testuji_tounicode_html.html5 ./testuji_tounicode.html5 &')


if __name__ == '__main__':

    print(__doc__)
    
#    print('='*44)
#    pisar()
#    print('='*44)
#    barevná_konzole()
#    print('='*44)
#    html_výpis()   
#    print('='*44)
#else:
    
    def seznam_funkcí(imam):
        help = ['dostupné funkce' | TEXT.NADPIS]
        for jméno,  funkce in imam.items():
            if not jméno.startswith('__') and callable(funkce):
                help.append(jméno | TEXT.INFO)
                
        return imam,  '\n'.join(help)
    
    imam,  help = seznam_funkcí(dict(locals()))
    
    import argparse
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser(epilog = help,  formatter_class = argparse.RawDescriptionHelpFormatter)

#   a pak mu nastavím jaké příkazy a parametry má přijímat
#    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, искушител {}'.format(__version__))
    
    parser.add_argument('funkce',  nargs='+')
    
    #    a včíl to možu rozparsovat
    args = parser.parse_args()
    
    funkce = args.funkce
    
    for funkce in funkce:
        if funkce in imam:
            print('spouštím funkci {}'.format(funkce | TEXT.PŘÍKAZ) | TEXT.INFO)
            eval('{}()'.format(funkce))
        else:
            print('funkce {} nejestvuje'.format(funkce | TEXT.PŘÍKAZ)  | TEXT.CHYBA)
            print(help)
            break
    
#    @TODO: udělat z tohoto testy
#    pisar()
#    barevná_konzole()
#    html_výpis()
#    testování()
    
#    toto už test má
#    validátor()


#    načítám_graf()
#    pygal()
#    svg_graf()

#    zkúšám()

 
