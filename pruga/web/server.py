#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

import os
import bottle

def static_file(filename, root, mimetype='auto', download=False):
    """ 
    Před spuštěním bottle.static_file překontroluje da-li jestvuje soubor a případně jej vytvoří
    """
    root_adresář = os.path.abspath(root) + os.sep
    web_soubor = os.path.abspath(os.path.join(root_adresář, filename.strip('/\\')))
    py_soubor = '{}.py'.format(web_soubor)

    if web_soubor.startswith(root_adresář):
        
        if os.path.exists(py_soubor) and os.path.isfile(py_soubor):
               
            import logging
            logger = logging.getLogger(__name__)
            debug = logger.debug
        
            def vytvoř():
                try:
                    import subprocess
                    vráceno = subprocess.check_output((py_soubor,  )).decode('utf-8')
                    debug('vrátil\n{}'.format(vráceno))
                except Exception as e:
                    debug('Selhalo: {}'.format(e))
                    raise e
            
            if not os.path.exists(web_soubor) or not os.path.isfile(web_soubor):
                debug('Nejestvuje soubor {}'.format(web_soubor))
                vytvoř()
            else:
                web_soubor_čas = os.stat(web_soubor).st_mtime
                py_soubor_čas = os.stat(py_soubor).st_mtime
                
                if(web_soubor_čas < py_soubor_čas):
                    debug('Aktualizuji soubor {}.'.format(web_soubor))
                    vytvoř()
        else:
            debug('Nejestvuje soubor {}, koji može vytvořit soubor {}'.format(py_soubor,  web_soubor))
            
    return bottle.static_file(filename, root, mimetype, download)
