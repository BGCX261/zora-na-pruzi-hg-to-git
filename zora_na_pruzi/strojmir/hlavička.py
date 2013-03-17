#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

from zora_na_pruzi import __version__,  __author__
from datetime import date

def práva_od_roku(od_roku):
    
    letos = date.today().timetuple()[0]
    if letos > 2012:
        return '2012 - {}'.format(letos)
    else:
        return '2012'
        
 
WEB_PROJEKTU = 'http://domogled.eu'
WEB_ZDROJOVÝCH_KÓDŮ = 'http://code.google.com/p/zora-na-pruzi/'

def hlavička_automaticky_vytvořila():
    hlavička = 'Изготовила Зора на прузи {verze} ©Домоглед {autor} {rok} б ден {datum}'.format(verze = __version__, datum = date.today().isoformat(),  autor = __author__,  rok = práva_od_roku(2005))
    return hlavička
