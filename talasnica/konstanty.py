#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

import datetime,  pytz
UNIX_EPOCH = datetime.datetime(1970, 1, 1, 0, 0, tzinfo = pytz.utc)

BUY = 'nákup'
SELL = 'prodej'
PROFIT_OPEN = 'profit při otevření'
PROFIT_HORE = 'profit hore'
PROFIT_DOLE = 'profit dole'
PROFIT_CLOSE = 'profit při zavření'
SWAP = 'celkový swap'
ULOŽENÝ_ZISK = 'celkové uložené zisky'

#OPEN_TIME = 'OPEN TIME'
OPEN = 'OPEN'
HIGHT = 'HIGHT'
LOW = 'LOW'
CLOSE = 'CLOSE'

HORE = 'býk'
DOLE = 'medvěd'

#VELIKOST = 'velikost obchodu'
#ČAS_OTEVŘENÍ = 'čas otevření'
#ČAS_ZAVŘENÍ = 'čas zavření'
#OTEVÍRACÍ_CENA = 'otevírací cena'
#ZAVÍRACÍ_CENA = 'zavírací cena'
#SMÉR = 'směr'
#ZNAMÉNKO_SMÉRU = {HORE: 1,  DOLE: -1}

JMÉNO_GRAFU = {
               1: 'minutový', 
               5: 'pětiminutový',
               15: 'čtvrthodinový', 
               30:  'půlhodinový',
               60: 'hodinový',
               240: 'čtyřhodinový',
               1440: 'denní',
               10080: 'týdenní',
               43200: 'měsíční',
               }

