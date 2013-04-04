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

###################################
###         FILTROVANI DAT
###################################


def filtr_školení_a_vzdělávání(tabulka):
    
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
            


def filtr_příjmů_obce(tabulka_obce):
    

    sloupec_trida_kod = tabulka_obce[0].index('trida_kod')
    
    for řádek in tabulka_obce[1:]:
        if  int(řádek[sloupec_trida_kod]) in (1, 2, 3,  4):
            
#            print('rok {} třída {} částka {} položka {}'.format(rok,  třída,  částka,  položka))
#            print(řádek)
            yield řádek


def filtr_výdajů_obce(tabulka_obce):
    

    sloupec_trida_kod = tabulka_obce[0].index('trida_kod')
    
    for řádek in tabulka_obce[1:]:
        if  int(řádek[sloupec_trida_kod]) in (5, 6):
            
#            print('rok {} třída {} částka {} položka {}'.format(rok,  třída,  částka,  položka))
#            print(řádek)
            yield řádek
#################################

def html_stránka():
#    from zora_na_pruzi.strojmir.xml.html5 import E
    from zora_na_pruzi.stroj.html5 import index_html
    
    stránka = index_html.stránka()
    return stránka

def zobrazím_v_prohlížeči(element,  soubor = 'data.html'):
    with open(soubor,  mode = 'w',  encoding = 'utf8') as html:
        html.write(str(element))
        
    import webbrowser
    webbrowser.open(soubor)


########################################
#   DATA
############################################


def načtu_data(filtrovací_funkce):
    data_podle_roků = {}
    záhlaví = ['třída',  'položka']
    obce = []
    
    for soubor in soubory():
        obec,  _ = os.path.splitext(os.path.basename(soubor))
        data = tabulka(soubor)
        
        obce.append(obec)
        
        for řádek in filtrovací_funkce(data):
            rok = řádek[4]
            třída = řádek[6]
            položka = řádek[8]
            kód_položky  = řádek[7]
            částka = float(řádek[14].replace(',',  '.'))

            data_za_rok = data_podle_roků.get(rok, None)
            if data_za_rok is None:
                data_za_rok = {}
                data_podle_roků[rok] = data_za_rok
                
            řádek_položky = data_za_rok.get(kód_položky,  None)
            if řádek_položky is None:
                řádek_položky = {}
                data_za_rok[kód_položky] = řádek_položky
                řádek_položky['třída'] = třída
                řádek_položky['položka'] = položka
                
            
            if obec in řádek_položky:
#                raise KeyError('Už jestvuje položka {} pro rok {} v obci {}'.format(položka,  rok,  obec))
                print('Už jestvuje položka {} pro rok {} v obci {}'.format(položka,  rok,  obec))
                řádek_položky[obec] = řádek_položky[obec] + částka
            else:
                řádek_položky[obec] = částka
        
        
#    print(data_podle_roků)
#    print(výstup)
   
    obce.sort()
    záhlaví = záhlaví + obce
   
    stránka = html_stránka()
    html = stránka.tělo
    for rok,  data_obcí_za_rok in sorted(data_podle_roků.items()):
#        print('*'*44)
#        print(rok,  data_obcí_za_rok)
        nadpis = E.H1(rok)
        html.append(nadpis)
        html_tabulka = E.TABLE()
        html_tabulka.přidej_záhlaví(záhlaví)
        html.append(html_tabulka)
        
        for kód_položky,  řádek_dat in sorted(data_obcí_za_rok.items()):
#            print('*'*44)
#            print(kód_položky,  řádek_dat)
            
            řádek = [řádek_dat['třída'],  řádek_dat['položka']]
            print(řádek)

            for obec in obce:
                částka = řádek_dat.get(obec,  None)
                if částka is not None:
                    částka = str(částka).replace('.',  ',')
                else:
                    částka = ''
                print(obec,  částka)
                řádek.append(částka)

                
            html_tabulka.přidej_řádek(řádek)
        
    
    zobrazím_v_prohlížeči(stránka)


def načtu_data_podle_paragrafů(filtrovací_funkce,  do_souboru = 'data.html'):
    data_podle_roků = {}
    záhlaví = ['třída',  'položka',  'skupina',  'paragraf']
    obce = []
    
    for soubor in soubory():
        obec,  _ = os.path.splitext(os.path.basename(soubor))
        data = tabulka(soubor)
        
        obce.append(obec)
        
        for řádek in filtrovací_funkce(data):
            rok = řádek[4]
            třída = řádek[6]
            položka = řádek[8]
            skupina = řádek[10]
            paragraf = řádek[12]
#            kód_položky  = řádek[7]
            kód_paragrafu  = řádek[11]
            částka = float(řádek[14].replace(',',  '.'))

            data_za_rok = data_podle_roků.get(rok, None)
            if data_za_rok is None:
                data_za_rok = {}
                data_podle_roků[rok] = data_za_rok
                
            řádek_položky = data_za_rok.get(kód_paragrafu,  None)
            if řádek_položky is None:
                řádek_položky = {}
                data_za_rok[kód_paragrafu] = řádek_položky
                řádek_položky['třída'] = třída
                řádek_položky['položka'] = položka
                řádek_položky['skupina'] = skupina
                řádek_položky['paragraf'] = paragraf
                
            
            if obec in řádek_položky:
#                raise KeyError('Už jestvuje položka {} pro rok {} v obci {}'.format(položka,  rok,  obec))
                print('Už jestvuje položka {} pro rok {} v obci {}'.format(položka,  rok,  obec))
                řádek_položky[obec] = řádek_položky[obec] + částka
            else:
                řádek_položky[obec] = částka
        
        
#    print(data_podle_roků)
#    print(výstup)
   
    obce.sort()
    záhlaví = záhlaví + obce
   
    stránka = html_stránka()
    html = stránka.tělo
    for rok,  data_obcí_za_rok in sorted(data_podle_roků.items()):
#        print('*'*44)
#        print(rok,  data_obcí_za_rok)
        nadpis = E.H1(rok)
        html.append(nadpis)
        html_tabulka = E.TABLE()
        html_tabulka.přidej_záhlaví(záhlaví)
        html.append(html_tabulka)
        
        for kód_položky,  řádek_dat in sorted(data_obcí_za_rok.items()):
#            print('*'*44)
#            print(kód_položky,  řádek_dat)
            
            řádek = [řádek_dat['třída'],  řádek_dat['položka'],   řádek_dat['skupina'],   řádek_dat['paragraf']]

            for obec in obce:
                částka = řádek_dat.get(obec,  None)
                if částka is not None:
                    částka = str(částka).replace('.',  ',')
                else:
                    částka = ''
#                print(obec,  částka)
                řádek.append(částka)

                
            html_tabulka.přidej_řádek(řádek)
        
    
    zobrazím_v_prohlížeči(stránka,  do_souboru)

if __name__ == '__main__':

    print(__doc__)
    
    import locale
    locale.setlocale(locale.LC_ALL, '')


    import argparse
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser()

#   a pak mu nastavím jaké příkazy a parametry má přijímat
    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, искушител {}'.format(__version__))
    
#    parser.add_argument('soubor')
    
    #    a včíl to možu rozparsovat
    args = parser.parse_args()
    
#    print('soubor',  args.soubor)

    import os

#    načtu_data(filtr_příjmů_obce)
#    načtu_data(filtr_výdajů_obce)
    načtu_data_podle_paragrafů(filtr_příjmů_obce,  do_souboru = 'data_příjmy_podrobně.html')
    načtu_data_podle_paragrafů(filtr_výdajů_obce,  do_souboru = 'data_výdaje_podrobně.html')


