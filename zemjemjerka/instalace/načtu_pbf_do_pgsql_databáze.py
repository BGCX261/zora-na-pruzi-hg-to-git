#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který převede pbf soubor do pgsql databáze pomocí programu osmosis

Pro import do databáze toto již nepoužívám, funguje mi lépe přímý import
pomocí skriptu načtu_pbf_do_pgsql_databáze
'''

import os
from pruga.zemjemjerka.nastavení.databáze import SERVER,  UŽIVATEL, HESLO_UŽIVATELE,   JMÉNO_DATABÁZE
from pruga.zemjemjerka.nastavení.adresáře import DOČASNÝ_ADRESÁŘ_PRO_IMPORT_PBF
from pruga.pohunci.spouštění_programu import spúšťám_program


def načtu_pbf_do_pgsql_databáze(jméno_pbf_souboru):
    '''
    načtu pbf soubor do postgresql databáze pomocí programu osmosis
    '''
   
    print("Zpracuji soubor '{}' a výsledky uložím do databáze '{}'.".format(jméno_pbf_souboru, JMÉNO_DATABÁZE))

    if not os.path.isdir(DOČASNÝ_ADRESÁŘ_PRO_IMPORT_PBF):
        raise Exception('Nejestvuje dočasný adresář "{}" pro import pbf'.format(DOČASNÝ_ADRESÁŘ_PRO_IMPORT_PBF))

    if not os.access(DOČASNÝ_ADRESÁŘ_PRO_IMPORT_PBF, os.W_OK):
        raise Exception('Do dočasného adresáře "{}" pro import pbf nelze zapisovat.'.format(DOČASNÝ_ADRESÁŘ_PRO_IMPORT_PBF))

    spúšťám_program(['JAVACMD_OPTIONS="-Djava.io.tmpdir={}"'.format(DOČASNÝ_ADRESÁŘ_PRO_IMPORT_PBF), 
                                "osmosis", 
                                "--read-pbf", 
                                "file={}".format(jméno_pbf_souboru), 
                                "--write-pgsql", 
                                "host={}".format(SERVER), 
                                "database={}".format(JMÉNO_DATABÁZE), 
                                "user={}".format(UŽIVATEL), 
                                "password={}".format(HESLO_UŽIVATELE), 
                                ])



if __name__ == '__main__':

    import argparse

    print(__doc__)

    parser = argparse.ArgumentParser()
    parser.add_argument('jméno_pbf_souboru', metavar='jméno_pbf_souboru', type=str,  help='název souboru, který chci načíst do databáze')
    args = parser.parse_args()
    
    načtu_pbf_do_pgsql_databáze(args.jméno_pbf_souboru)



