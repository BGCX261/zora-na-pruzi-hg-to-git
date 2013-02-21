#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>


'''
Hen je logger, který vypisuje různěbarevné zprávy
'''

import logging

from . import davaj_obarvovací_funkci

#jména úrovní jsou přeložena do jazyka českého
jména_úrovní = {
                'DEBUG': 'LADÍM', 
                'INFO': 'HLÁSÍM', 
                'WARNING': 'POZOR', 
                'ERROR': 'CHYBA', 
                'CRITICAL': 'PROGRAM SELHAL'
                }
                        

class Obarvovač():
    
    obarvovače = {}
    
    def davaj_obarvovač_pro_DEBUG(self):
       return davaj_obarvovací_funkci(barva = 'blue',  pozadí = 'on_dark_green',  styl = None,  vypíšu = False)
       
    def davaj_obarvovač_pro_INFO(self): 
        return davaj_obarvovací_funkci(barva = 'dark_blue',  pozadí = 'on_yellow',  styl = None,  vypíšu = False)
        
    def davaj_obarvovač_pro_ERROR(self):
        return davaj_obarvovací_funkci(barva = 'dark_blue',  pozadí = 'on_dark_red',  styl = None,  vypíšu = False)
        
    def davaj_obarvovač_pro_WARNING(self):
      return davaj_obarvovací_funkci(barva = 'dark_magenta',  pozadí = 'on_yellow',  styl = None,  vypíšu = False)
      
    def davaj_obarvovač_pro_CRITICAL(self):
        return davaj_obarvovací_funkci(barva = 'yellow',  pozadí = 'on_dark_red',  styl = None,  vypíšu = False)
        
    def __call__(self,  jméno):
        obarvovač = self.obarvovače.setdefault(jméno, getattr(self,  'davaj_obarvovač_pro_{}'.format(jméno))())
        return obarvovač

#formater umožní naformátovat výpis
class ColoredFormatter(logging.Formatter):

    obarvovač = None
    
    def __init__(self,  fmt=None, datefmt=None, style='%',  obarvovač = None):
        super().__init__(fmt,  datefmt,  style)
        
        if obarvovač is None:
            self.obarvovač = Obarvovač()

    def format(self, record):
        levelname = record.levelname
        record.levelname = jména_úrovní.get(levelname,  levelname)
        
#            record.levelname = obarvi(record.levelname, levelname)
#            record.name = (obarvi(record.name,  'jméno_loggeru'))
#            record.message = (obarvi(record.message,  'zpráva_loggeru'))
#            record.filename = (obarvi(record.filename,  'jméno_souboru_loggeru'))
#            record.lineno = (obarvi(record.lineno,  'číslo_řádky_loggeru'))
     
#        if self.use_color and levelname in COLORS:
#            levelname_color = COLOR_SEQ % (30 + COLORS[levelname]) + levelname + RESET_SEQ
#            record.levelname = levelname_color
        text = super().format(record)
        
        obarvovací_funkce = self.obarvovač(levelname)
        
        return obarvovací_funkce(text)[0]

def daj_logger(module,  level = None):
    """
    
    """

    import os

    # Create Logger
    jméno = getattr(module,  '__file__',  str(module))
    logger = logging.getLogger(os.path.basename(jméno))
    logger.setLevel(level or logging.DEBUG)

    # Create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Create formatter
#    formatter = logging.Formatter(_LOGGING_FORMAT)
    formatter = ColoredFormatter('{name}: {message}',  style='{')

    # Add formatter to ch
    ch.setFormatter(formatter)

    # Add ch to logger
    logger.addHandler(ch)

    
    return logger
 

def daj_logovátka(module = None,  logger = None,  level = None):
    if logger is None:
        logger = daj_logger(module,  level)
    return logger.debug,  logger.info,  logger.warning,  logger.error,  logger.critical

#logger = daj_logger()
#debug = logger.debug
#info = logger.info
#warning = logger.warning
#error = logger.error
#critical = logger.critical
