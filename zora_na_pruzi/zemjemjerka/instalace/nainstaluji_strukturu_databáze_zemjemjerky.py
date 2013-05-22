#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

"""
provedu instalaci, postupně spustím jednotlivé instalační skripty ve správném pořadí a se správnými parametry
"""

from pruga.zemjemjerka.nastavení.databáze import UŽIVATEL

if __name__ == "__main__":
#    import sys

    from struktura_databáze_zemjemjerky.nainstaluji_schéma_a_funkce_zemjemjerky import nainstaluji_zemjemjerku
    from struktura_databáze_zemjemjerky.nastavím_výchozí_schémy_pro_uživatele import nastavím_výchozí_schémy
   
#    from pruga.pohunci.spouštění_programu import spúšťám_program
    
    print(__doc__)
    
    nainstaluji_zemjemjerku()
    print('{} je uživatel, kterému včíl nastavím potřebné výchozí schémy'.format(UŽIVATEL))
    nastavím_výchozí_schémy(UŽIVATEL)
