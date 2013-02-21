#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

import pytest
import os
import logging
from logging import debug,  info,  warning,  error,  critical
from .zobrazím_log import LOGUJ_DO_SOUBORU

PYTHON_BIN = 'python3'

logging.basicConfig(filename = LOGUJ_DO_SOUBORU,
                    filemode = 'w', 
                    format='<div class="%(levelname)s ramecek"><pre>%(message)s</pre></div>',
                    level = logging.DEBUG)

def spustím_test(soubor):
    info('<h1>spouštím test {}</h1>'.format(os.path.basename(soubor)))
    kód = pytest.main("-s {}".format(soubor))
    if kód == 0:
        info('... test proběhl v pořádku')
    else:
        error('... test selhal a vrátil kód číslo {}'.format(kód))

def zobrazím_log_jako_html_stránku():
    import subprocess
    spustím_soubor = os.path.join(os.path.dirname(__file__),  './zobrazím_log.py')
    subprocess.Popen([PYTHON_BIN,  spustím_soubor])
#    subprocess.call(['./zobrazím_log.py'])
