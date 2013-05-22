#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který získá údaje o firmě ze systému ares 
http://wwwinfo.mfcr.cz/ares/
'''

import os
import httplib2

from lxml import etree

from pruga.pohunci.logování import barevný_log
from logging import info


cache_dir = os.path.realpath(os.path.join(__file__,  '../../.cache'))

def najdi_firmu_podle_ičo(ičo):
    '''
    zahájí běh programu
    '''
    
    h = httplib2.Http(cache_dir)
    info('startuji httplib2 s cache adresářem {}'.format(cache_dir))
    
#    standartní dotaz
    url = 'http://wwwinfo.mfcr.cz/cgi-bin/ares/darv_std.cgi?ico={}'.format(ičo)
#    dotaz evidence ekonomických subjektů - včetně dph
    url = 'http://wwwinfo.mfcr.cz/cgi-bin/ares/ares_es.cgi?ico={}'.format(ičo)
    response, content = h.request(url)
    
    if response.status != 200:
        raise Exception('Nenašel jsem firmu ičo: {} v databázi'.format(ičo))
        
#    info(response)
#    info(content)
    print(content.decode('utf-8'))
    return 0
    zpracuji_xml_záznam(content)
#    

def zpracuji_xml_záznam(xml):
#    print(xml)
 
#    root = tree.getroot() 
    root = etree.XML(xml)

    print(root.tag)
    
    
    def projdi(element,  level = 0):
        
        for child in element:
            print ('\t'*level + child.tag)
            projdi(child,  level+1)

    projdi(root)

    
if __name__ == '__main__':

    print(__doc__)

    ičo = '27074358'
    najdi_firmu_podle_ičo(ičo)



