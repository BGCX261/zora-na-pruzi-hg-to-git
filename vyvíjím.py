#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je skript, gde si zkúšám
'''

import os

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
    from zora_na_pruzi.vidimir.Pisar import Pisar
    print(Pisar)
#    print(styl.H1) >> AttributeError
    pisar = Pisar('barevná_konzole')
    print(pisar.pohled)
    print(pisar.pohled.H1)
    
    with Pisar('barevná_konzole') as p:
        print('tu 3e with',  p,  pisar)
        p.pohled.H1
        with Pisar('html') as p:
            print(pisar.pohled.H1)
        print(p)

def html_výpis():
    
    from zora_na_pruzi.vidimir import pohled as p
    
    print('NADPIS' | p.NADPIS)
    
    from zora_na_pruzi.pisar.html.html import HTML,  E

    odstavec = HTML(E.DIV(E.H4('NADPIS úrovně 4'),  E.P('tu je text:*** {} ***',  E.CLASS('css_třída'))))
    print('soubor {} je tu'.format(__file__ | p.SOUBOR) | p.INFO)
    print('soubor {} je tu'.format(__file__ | p.SOUBOR) | odstavec)
    
def barevná_konzole():
    from zora_na_pruzi.vidimir import pohled as p
    
    print('NADPIS' | p.NADPIS)
    
    from zora_na_pruzi.pisar.konzole.obarvi import OBARVI
    from zora_na_pruzi.pisar.konzole.barvy import MODRÁ

    modře = OBARVI(MODRÁ)
    print('soubor {} je tu'.format(__file__ | p.SOUBOR) | p.INFO)
    print('soubor {} je tu'.format(__file__ | p.SOUBOR) | modře)

def testování():
    from zora_na_pruzi.iskušitel import najdu_testovací_soubory
    
    adresář = './zora_na_pruzi'
    print('vše v adresáři {}'.format(adresář | SOUBOR) | INFO)
    for testovací_soubor in najdu_testovací_soubory(adresář):
        print(testovací_soubor)
        
    soubor = './zora_na_pruzi/strojmir/xml/graphml/testuji_graphml.py'
    print('přímo testovací soubor {}'.format(soubor | SOUBOR) | INFO)
    for testovací_soubor in najdu_testovací_soubory(soubor):
        print(testovací_soubor)
     
    soubor = 'nejestvující.soubor'
    print('nejestvující soubor {}'.format(soubor | SOUBOR) | INFO)
    try:
        for testovací_soubor in najdu_testovací_soubory(soubor):
            print(testovací_soubor)
    except IOError as e :
        print('vyjímka {}'.format(e.__class__.__name__ | OBJEKT) | CHYBA)
        print(e)
        
    soubor = __file__
    print('soubor {}, koj neodpovídá masce'.format(soubor | SOUBOR) | INFO)
    try:
        for testovací_soubor in najdu_testovací_soubory(soubor):
            print(testovací_soubor)
    except IOError as e :
        print('vyjímka {}'.format(e.__class__.__name__ | OBJEKT) | CHYBA)
        print(e)
        
    adresář = './prázdný_adresář'
    if os.path.isdir(adresář):
        raise IOError('Tož tento adresář "{}" chci použít pro testování, ale on už jestvuje'.format(adresář))
    os.mkdir(adresář)
    print('adresář {}, koji nemá žádných testů'.format(adresář | SOUBOR) | INFO)
    try:
        for testovací_soubor in najdu_testovací_soubory(adresář):
            print(testovací_soubor)
    except IOError as e :
        print('vyjímka {}'.format(e.__class__.__name__ | OBJEKT) | CHYBA)
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
    
    
    print('GRAFY' | NADPIS)
    for graf in zora_na_pruzi_graf,  networkx_graf,  graph_tool_graf:
        print(graf.__class__.__name__ | INFO)
        print(graf)
        
    print('UZLY' | NADPIS)
    for graf in zora_na_pruzi_graf,  networkx_graf,  graph_tool_graf:
        print(graf.__class__.__name__ | INFO)
        for uzel in graf.uzly:
            print(uzel)
            
    print('HRANY' | NADPIS)
    for graf in zora_na_pruzi_graf,  networkx_graf,  graph_tool_graf:
        print(graf.__class__.__name__ | INFO)
        for vazba in graf.vazby:
            print(vazba)
            
    print('VLASTNOSTI' | NADPIS)
    for graf in zora_na_pruzi_graf,  networkx_graf,  graph_tool_graf:
        print(graf.__class__.__name__ | INFO)
        for vlastnosti in graf.vlastnosti:
            for vlastnost in vlastnosti:
                print(vlastnost)
    
    

if __name__ == '__main__':

    print(__doc__)
    
#    @TODO: udělat z tohoto testy
    pisar()
    barevná_konzole()
    html_výpis()
#    testování()
    
#    toto už test má
#    validátor()



#    zkúšám()

    
