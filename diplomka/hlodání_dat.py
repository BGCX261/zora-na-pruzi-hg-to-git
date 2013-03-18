#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'


from zora_na_pruzi.strojmir.xml.html5 import E


def soubory():
    from z_webu import KAM_ULOŽÍM_CSV
    import glob
    maska = '{}/*.csv'.format(KAM_ULOŽÍM_CSV)
    
    for soubor in glob.glob(maska):
        yield soubor

def tabulka(soubor):
    '''
    spouštím funkci main()
    '''
    
    
    
#    class Tabulka(list):
#        
#        def __call__(self,  sloupec,  řádek):
#            if isinstance(sloupec,  str):
#                číslo_sloupce = self[0].index('"{}"'.format(sloupec))
#            else:
#                číslo_sloupce = int(sloupec)
#                
#            return(self[řádek][číslo_sloupce])
        
    tabulka = []
    
    for řádek in open(soubor,  mode='r',  encoding='windows-1250'):
        data = řádek.strip().split(';')
        data = list(map(bez_uvozovek,  data))
#        print(data)
        tabulka.append(data)
        
#    print(tabulka[0])
#    print(tabulka('polozka_nazev',  1))
    return tabulka


def bez_uvozovek(hodnota):
    return hodnota.strip('"')

def školení_a_vzdělávání(tabulka):
    
#    sloupec_kódu = tabulka[0].index('paragraf_kod')
#    sloupec_hodnoty = tabulka[0].index('hodnota')
#    sloupec_roku = tabulka[0].index('rok')
    sloupec_položka_kód = tabulka[0].index('polozka_kod')
    
    for řádek in tabulka[1:]:
        if  int(řádek[sloupec_položka_kód]) == 5167:
#            částka = řádek[sloupec_hodnoty]
#            rok = řádek[sloupec_roku]
#            print(rok,  ': ',  částka)
            print('{1} rok {4} {8} {12} {14}'.format(*řádek))
#            print(řádek)
            yield řádek

def html_stránka():
    from zora_na_pruzi.strojmir.xml.html5 import E
    from zora_na_pruzi.stroj.html5 import index_html
    
    stránka = index_html.stránka()
    return stránka

def zobrazím_v_prohlížeči(element,  soubor = 'data.html'):
    with open(soubor,  mode = 'w',  encoding = 'utf8') as html:
        html.write(str(element))
        
    import webbrowser
    webbrowser.open(soubor)

if __name__ == '__main__':

    print(__doc__)

    import argparse
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser()

#   a pak mu nastavím jaké příkazy a parametry má přijímat
    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, искушител {}'.format(__version__))
    
#    parser.add_argument('soubor')
    
    #    a včíl to možu rozparsovat
    args = parser.parse_args()
    
#    print('soubor',  args.soubor)

    html_tabulka = E.TABLE()

    import os

    výstup = {}
    for soubor in soubory():
        obec,  _ = os.path.splitext(os.path.basename(soubor))
        data_obce = {}
        data = tabulka(soubor)
        for řádek in školení_a_vzdělávání(data):
            rok = řádek[4]
            hodnota = řádek[14]
            data_obce[rok] = hodnota
        
        výstup[obec] = data_obce
            
    for obec,  roky in výstup.items():
        řádek = [obec]
        for rok in range(2008,  2012):
            hodnota = roky.get(str(rok),  'NIC')
            řádek.append(hodnota)
        html_tabulka.přidej_řádek(řádek)
        
    záhlaví = list(range(2008,  2012))
    záhlaví.insert(0,  'obec')
    html_tabulka.přidej_záhlaví(záhlaví)
        
    stránka = html_stránka()
    stránka.tělo.append(html_tabulka)
    zobrazím_v_prohlížeči(stránka)
