#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je skript, gde si zkúšám
'''

import os

#from zora_na_pruzi.pohunci.obarvím_výpis.barevný_logger import daj_logovátka
#debug,  info,  warning,  error,  critical = daj_logovátka(__file__)

from zora_na_pruzi.vidimir import F

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
    from zora_na_pruzi.vidimir.Pisar import Pisar
    
#    print(Pisar)
##    print(styl.H1) >> AttributeError
#    pisar = Pisar('barevná_konzole')
#    print(pisar.pohled)
#    print(pisar.pohled.H1)
    
    from zora_na_pruzi.vidimir import F
    
    with Pisar('barevná_konzole') as pisar:
        print('tu še with' | F.H1)
#        print(F.TEST.START) NotImplementedError
        print(type(F.TEST.START))
        print('startuje test ' | F.TEST.START)
        with Pisar('html') as pisar:
            print(type(F.H1))
            print('NADPIS' | F.H1)
#            print('startuje test ' | F.TEST.START)
#        print(p)

def html_výpis():
    
    from zora_na_pruzi.vidimir import F
    from zora_na_pruzi.vidimir.Pisar import Pisar
    
    with Pisar(jméno_vidu = 'html'):
        print('NADPIS' | F.NADPIS)
        
#        from zora_na_pruzi.pisar.html.html import HTML,  E
#
#        odstavec = HTML(E.DIV(E.H4('NADPIS úrovně 4'),  E.P('tu je text:*** {} ***',  E.CLASS('css_třída'))))
        
        print('soubor {} je tu'.format(__file__ | F.SOUBOR) | F.INFO)
        print('soubor {} je tu'.format(__file__ | F.SOUBOR) | F.DIV)
    
def barevná_konzole():
    from zora_na_pruzi.vidimir import F
    
    print('NADPIS' | F.NADPIS)
    
    from zora_na_pruzi.vidimir.stroj.konzole.Obarvi import Obarvi
    from zora_na_pruzi.vidimir.stroj.konzole.barvy import MODRÁ

    modře = Obarvi(MODRÁ)
    print('soubor {} je tu'.format(__file__ | F.SOUBOR) | F.INFO)
    print('soubor {} je tu'.format(__file__ | F.SOUBOR) | modře)

def testování():
    from zora_na_pruzi.iskušitel import najdu_testovací_soubory
    from zora_na_pruzi.vidimir import F
    
    adresář = './zora_na_pruzi'
    print('vše v adresáři {}'.format(adresář | F.SOUBOR) | F.INFO)
    for testovací_soubor in najdu_testovací_soubory(adresář):
        print(testovací_soubor)
        
    soubor = './zora_na_pruzi/strojmir/xml/graphml/testuji_graphml.py'
    print('přímo testovací soubor {}'.format(soubor | F.SOUBOR) | F.INFO)
    for testovací_soubor in najdu_testovací_soubory(soubor):
        print(testovací_soubor)
     
    soubor = 'nejestvující.soubor'
    print('nejestvující soubor {}'.format(soubor | F.SOUBOR) | F.INFO)
    try:
        for testovací_soubor in najdu_testovací_soubory(soubor):
            print(testovací_soubor)
    except IOError as e :
        print('vyjímka {}'.format(e.__class__.__name__ | F.OBJEKT) | F.CHYBA)
        print(e)
        
    soubor = __file__
    print('soubor {}, koj neodpovídá masce'.format(soubor | F.SOUBOR) | F.INFO)
    try:
        for testovací_soubor in najdu_testovací_soubory(soubor):
            print(testovací_soubor)
    except IOError as e :
        print('vyjímka {}'.format(e.__class__.__name__ | F.OBJEKT) | F.CHYBA)
        print(e)
        
    adresář = './prázdný_adresář'
    if os.path.isdir(adresář):
        raise IOError('Tož tento adresář "{}" chci použít pro testování, ale on už jestvuje'.format(adresář))
    os.mkdir(adresář)
    print('adresář {}, koji nemá žádných testů'.format(adresář | F.SOUBOR) | F.INFO)
    try:
        for testovací_soubor in najdu_testovací_soubory(adresář):
            print(testovací_soubor)
    except IOError as e :
        print('vyjímka {}'.format(e.__class__.__name__ | F.OBJEKT) | F.CHYBA)
        print(e)
    os.rmdir(adresář)
    

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
        


def   zkúšám():
    import lxml.etree
    from zora_na_pruzi.strojmir.xml.graphml import NS_GRAPHML
    graphml_soubor = './graf.graphml'
    tree = lxml.etree.parse(graphml_soubor)
    print('TREE',  id(tree))
    root = tree.getroot()
    
    for node in root.findall('/'.join((NS_GRAPHML.graph,  NS_GRAPHML.node))):
        print('node',  id(node))
        print('tree',  id(node.getroottree()))
        
    nt = node.getroottree()
       
    print('GRAPH')   
       
    for graph in root.findall('/'.join((NS_GRAPHML.graph,  ))):
        print('graph',  id(graph))
        print('tree',  id(graph.getroottree()))
        
    if nt == graph.getroottree():
        print('SA TETET')
    else:
        print('SA IN TTT')
    return
    
    import py
    
    print(py.std.sys.stdout)
    py.std.sys.stdout = open('hen',  mode = 'w',  encoding = 'UTF-8')
    return
    
#    from zora_na_pruzi.strojmir.xml.graphml import načtu_graf,  NS_GRAPHML
    
    from zora_na_pruzi.strojmir.xml.graphml.Graf import Graf,  Graf_Graph_tool,  Graf_NetworkX
    
    graphml = './stroj/data/nested.graphml'
#    graphml = './stroj/grafy/zora_na_pruzi.graphml'
    
#    tree = načtu_graf(graphml)
#    print(tree)
#    root = tree.getroot()
#    print(root.__class__.__name__)
#    
#    for klíč in root.findall(NS_GRAPHML.key):
#        print(klíč.__class__.__name__,  klíč.attrib)
#        
#    print('***********')
#    for klíč in root.findall('{}[@for="edge"][@id]'.format(NS_GRAPHML.key)):
#        print(klíč.__class__.__name__,  klíč.attrib)
    
    
    
    zora_na_pruzi_graf = Graf(graphml)
    
    kód = zora_na_pruzi_graf.graf %  ('graphml',  'hen.graphml')
    print(kód)
    
    return
    
    networkx_graf = Graf_NetworkX(graphml)
    
    
    graph_tool_graf = Graf_Graph_tool(graphml)
    
    
    print('GRAFY' | F.NADPIS)
    for graf in zora_na_pruzi_graf,  networkx_graf,  graph_tool_graf:
        print(graf.__class__.__name__ | F.INFO)
        print(graf)
        
    print('UZLY' | F.NADPIS)
    for graf in zora_na_pruzi_graf,  networkx_graf,  graph_tool_graf:
        print(graf.__class__.__name__ | F.INFO)
        for uzel in graf.uzly:
            print(uzel)
            
    print('HRANY' | F.NADPIS)
    for graf in zora_na_pruzi_graf,  networkx_graf,  graph_tool_graf:
        print(graf.__class__.__name__ | F.INFO)
        for vazba in graf.vazby:
            print(vazba)
            
    print('VLASTNOSTI' | F.NADPIS)
    for graf in zora_na_pruzi_graf,  networkx_graf,  graph_tool_graf:
        print(graf.__class__.__name__ | F.INFO)
        for vlastnosti in graf.vlastnosti:
            for vlastnost in vlastnosti:
                print(vlastnost)
    
def graf():
    from zora_na_pruzi.strojmir.xml.graphml.Graf import Graf
    from zora_na_pruzi.strojmir.xml.graphml import načtu_graf
    import lxml.etree
    
    graphml_soubor = './testuji_vzorový_graf.graphml'
    cesta_k_graphml_souboru = os.path.join(os.path.dirname(__file__),  graphml_soubor)
    
   
    
    print('Testuji na testovacím grafu {}'.format(cesta_k_graphml_souboru | F.SOUBOR) | F.TEST.START)
    
#    graf = Graf(cesta_k_graphml_souboru)
#    tree = graf.xml
    tree = načtu_graf(graphml_soubor)
    assert isinstance(tree,  lxml.etree._ElementTree)
    
    root = tree.getroot()
    
    assert isinstance(root,  lxml.etree.ElementBase) 
    
    uzly = list(root.uzly)
    assert len(uzly) == 14
    
    vazby = list(root.vazby)
    assert len(vazby) == 12
    
    uzel = uzly[0]
    
    data = uzel.data
    assert len(data) == 1
    
    údaj = data[0]
    
    assert údaj.jméno == 'jméno'
    print(údaj.jméno)
    print(údaj)
    assert údaj.datový_typ == 'string'
    assert údaj.default is None
    assert údaj.klíč == root.klíče['d2']
    assert id(údaj.klíč) == id(root.klíče['d2'])
    
#    druhý graf 
    graphml_soubor = './testuji_vzorový_graf_2.graphml'
    cesta_k_graphml_souboru = os.path.join(os.path.dirname(__file__),  graphml_soubor)
#    graf2 = Graf(cesta_k_graphml_souboru)
#    tree2 = graf2.xml
    tree2 = načtu_graf(graphml_soubor)
    root2 = tree2.getroot()
    uzly = list(root2.uzly)
    uzel = uzly[0]
    print(uzel.jméno)
    data = uzel.data
    
    údaj = data[0]
    print(údaj.jméno)
    print(údaj)
    assert údaj.jméno == 'jiné jméno'   
  

if __name__ == '__main__':

    print(__doc__)
    
#    @TODO: udělat z tohoto testy
#    pisar()
#    barevná_konzole()
#    html_výpis()
#    testování()
    
#    toto už test má
#    validátor()


    graf()

#    zkúšám()

 
