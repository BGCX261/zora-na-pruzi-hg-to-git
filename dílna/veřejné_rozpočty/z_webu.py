#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'


import lxml.html
import os
import httplib2

#import re


KAM_ULOŽÍM_CSV = os.path.join(os.path.dirname(__file__),  'csv')

def seznam_obcí():
    
    with open('obce.txt',  mode='r',  encoding='UTF-8') as seznam:
        for obec in seznam:
            obec = obec.strip().split(';')
            url = obec[1]
            print('-'*44)
            print('Otvírám rozklikávací rozpočet pro obec {} {}'.format(obec[0],  obec[1]))
            
            tree = lxml.html.parse(url)
            root = tree.getroot()
            
            hledám_element = tree.findall('//div[@id="diskuse"]/div/div/div/ul/li/a')
            
            csv_link = None
            
            for element in hledám_element:
                if element.text == 'CSV české':
#                if element.text == 'CSV anglické':
                    
                    csv_link = element.attrib['href']
                    csv_link = 'http://www.rozpocetobce.cz{}'.format(csv_link)
#                    if len(obec) == 3:
#                        assert obec[2] == csv_link
                    stáhnu_csv(odkaz = csv_link,  obec = obec[0])
#                  stáhnu_csv_urllib(odkaz = csv_link,  obec = obec[0])
            
            if csv_link is None:
                raise valueError('Nenašel jsem odkaz na csv pro dědinu {}'.format(obec[0]))
#            když zkúšam a je zbytečné aby to dělalo všecky obce,  vyzkúšám enom na první
#            break;
            

def stáhnu_csv(obec,  odkaz):
    '''
    spouštím funkci main()
    '''
    print('STÁHNU csv pro obec {} {}'.format(obec,  odkaz))
    
    h = httplib2.Http('.cache')
    
    hlavička, obsah = h.request(odkaz)
    
    jméno_souboru = obec
    
#    if 'content-disposition' in hlavička:
#        # If the response has Content-Disposition, we take filename from it
#        jméno_souboru = hlavička['content-disposition'].split('filename=')[1]
#        if jméno_souboru[0] == '"' or jméno_souboru[0] == "'":
#            jméno_souboru = jméno_souboru[1:-1]

    jméno_souboru = os.path.join(KAM_ULOŽÍM_CSV,  '{}.csv'.format(jméno_souboru))
        
    print('\t do {}'.format(jméno_souboru))
    print("hlavička:", hlavička)
#    print(type(obsah))
#    print(obsah.decode('utf-8'))

    with open(jméno_souboru,  mode = 'wb') as soubor:
        soubor.write(obsah)

#    with open(jméno_souboru,  mode = 'w',  encoding = 'UTF-8') as soubor:
#        soubor.write(obsah.decode('latin-1'))
        
def stáhnu_csv_urllib(obec,  odkaz): 
    import urllib.request
    data = urllib.request.urlopen(odkaz).read()
    type(data)    
    print(data.decode('utf-8'))
  


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

    seznam_obcí()
