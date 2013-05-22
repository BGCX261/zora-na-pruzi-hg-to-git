#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který převede pbf soubor do pgsql dump
'''

import os
import shutil
from pruga.zemjemjerka.nastavení .adresáře import ADRESÁŘ_GDE_ULOŽÍM_DATA_PŘEVEDENÁ_Z_OSM_PBF_DO_PGSQL_DUMP
from pruga.pohunci.spouštění_programu import spúšťám_program


def převedu_pbf_do_pgsql_dump(jméno_pbf_souboru):
    '''
    převede pbf na pgsql dump pomocí programu osmosis
    '''
    
    adresáře_pro_sql_dump = os.path.join(ADRESÁŘ_GDE_ULOŽÍM_DATA_PŘEVEDENÁ_Z_OSM_PBF_DO_PGSQL_DUMP,  os.path.splitext(os.path.basename(jméno_pbf_souboru))[0])
    print("Zpracuji soubor '{}' a výsledky uložím do adresáře '{}'.".format(jméno_pbf_souboru, adresáře_pro_sql_dump))

    if os.path.isdir(adresáře_pro_sql_dump):
        print("odstraním stará data uložená v {}".format(adresáře_pro_sql_dump))
        shutil.rmtree(adresáře_pro_sql_dump)
        
    print("vytvořím adresář {}".format(adresáře_pro_sql_dump))
    os.mkdir(adresáře_pro_sql_dump)

    spúšťám_program(["osmosis",  "--read-pbf",  "file={}".format(jméno_pbf_souboru),  "--write-pgsql-dump",  "directory={}".format(adresáře_pro_sql_dump)])



if __name__ == '__main__':

    import argparse

    print(__doc__)

    parser = argparse.ArgumentParser()
    parser.add_argument('jméno_pbf_souboru', metavar='jméno_pbf_souboru', type=str,  help='název souboru, který chci načíst do databáze')
    args = parser.parse_args()
    
    převedu_pbf_do_pgsql_dump(args.jméno_pbf_souboru)



