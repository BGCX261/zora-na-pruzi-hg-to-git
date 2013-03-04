'''
Created on 19.3.2011

tento skript stáhne zdrojové kódy ke knize Dive into Python 3 od Martina Pilgrama.
Tato kniha je dostupná i v české verzi, avšak jen ve formátu pdf
a zdrojové knihy lze stáhnout jen na stránkách anglického originálu.

http://diveintopython3.org/examples/

Používám tu dvě externí knihovny, které Pilgram ve své knize doporučuje:
httplib2
lxml

Adresář, kam se výsledné soubory uloží je třeba změnit přímo ve zdrojovém kódu
adresář_kam_uložím_skripty = "e:\programovani\zora_na_pruzi\python\knihy a příklady\Ponořte se do Pythonu 3"

@todo: Umožnit vybrat cílový adresář, ať se nemusí přepisovat v kódu

Soubory se uloží
@author: Golf
'''

#adresář_kam_uložím_skripty = "e:\programovani\zora_na_pruzi\python\knihy a příklady\Ponořte se do Pythonu 3"
adresář_kam_uložím_skripty = "/home/python/návody/příklady z knih/Ponořte se do Pythonu 3"

#from lxml import html
import lxml.html
#import xml.etree.ElementTree as etree

#html = lxml.html.fromstring(stranka_vypisujici_soubory)
#print(html)
url_souborů = 'http://diveintopython3.org/examples/'

etree = lxml.html.parse(url_souborů)
#print(etree)
html = etree.getroot()
#print(html)

#lxml.html.open_in_browser(etree)

import httplib2
import os
#import re
h = httplib2.Http('.cache')

for odkaz in etree.findall("//a"):
    jméno_souboru = odkaz.attrib['href']
    print("stahuji soubor", jméno_souboru)
    url_souboru = url_souborů + jméno_souboru
    print("z adresy", url_souboru)
    hlavička, content = h.request(url_souboru)
    print("hlavička:", hlavička)
    
    #print(re.sub('[^a-zA-Z0-9_-.() ]+', '', jméno_souboru))
    #re.sub('[^a-zA-Z0-9_-.() ]+', '', jméno_souboru)
    uložím_do_souboru = os.path.join(adresář_kam_uložím_skripty, jméno_souboru.replace("?", "_"))
    if uložím_do_souboru == "/":
        continue
    print("ukládám soubor", uložím_do_souboru)
        

    if hlavička['content-type'] in ['image/jpeg'] or jméno_souboru == "entry.pickle":
        with open(uložím_do_souboru, mode='wb') as proud:
            proud.write(content)
    else:
        with open(uložím_do_souboru, mode='w', encoding='utf-8') as proud:
            proud.write(content.decode('utf-8'))
    #stranka_vypisujici_soubory = content.decode('utf-8')
    #print(stranka_vypisujici_soubory)
    print("\n*******************************\n")


