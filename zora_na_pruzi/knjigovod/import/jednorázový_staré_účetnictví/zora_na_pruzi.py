#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který ...
'''

import logging
logging.basicConfig(level=logging.DEBUG)
from logging import debug,  info,  warning,  error,  critical

from pruga.připojení import testovací_databáze as připojení_databáze
#from pruga.připojení import vývojová_databáze as připojení_databáze

from pruga import Graf
from zora import Zora

graf = Graf(připojení_databáze)
zora = Zora(graf=graf)


