#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

def davaj_importéra(jméno_základního_balíčku):
    
    def importuji(*args):
        try:
            args = list(args)
            jméno_objektu = args.pop()
            args.insert(0, jméno_základního_balíčku)
            jméno_modulu = '.'.join(args)
            modul = __import__(jméno_modulu, globals(), locals(), [jméno_objektu], 0)
            objekt = getattr(modul,  jméno_objektu)
            return objekt
        except ImportError as e:
            raise ImportError('V {} selhal import: {}'.format(__name__,  e)) from e
        except AttributeError as e:
            raise AttributeError('V {} selhalo získání {} z {}: {}'.format(__name__,  jméno_objektu, modul.__name__,  e)) from e
        
    return importuji
