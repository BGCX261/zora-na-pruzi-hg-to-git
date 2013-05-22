#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

"""
Stáhnu data z internetu, používám zdroj http://download.geofabrik.de a formát pdf. 
Skript používá více procesů a spouští externí program, curl
PAZI wget nefunguje jak má, nestáhne celé soubory, možná nějaké nastavení, ale když curl funguje, použiji ten
"""
#import sys
#import os

#sys.path.insert(1,  os.path.realpath("../"))

from zora_na_pruzi.zemjemjerka.nastavení .adresáře import *

if __name__ == "__main__":
    
    import os
    import subprocess
    import time
    
#    print(__doc__)

    
    if not os.path.isdir(ADRESÁŘ_GDE_ULOŽÍM_STAŽENÁ_DATA_OSM_PBF):
        os.mkdir(ADRESÁŘ_GDE_ULOŽÍM_STAŽENÁ_DATA_OSM_PBF)
    
    procesy = {}
    with open(SEZNAM_SOUBORÚ_KE_STAŽENÍ,  "r",  encoding="utf8") as seznam_zdrojů:
        for url_souboru in seznam_zdrojů:
            url_souboru=url_souboru.strip()
            if not url_souboru:
                continue
            jméno_souboru = os.path.basename(url_souboru).strip()
            uložím_jako = os.path.join(ADRESÁŘ_GDE_ULOŽÍM_STAŽENÁ_DATA_OSM_PBF,  jméno_souboru)
            
            if os.path.isfile(uložím_jako):
                print("soubor {} již jestvuje, smaž ho, přepisovat ho nebudu".format(uložím_jako))
                continue
            
            příkaz = ["curl",   url_souboru,  "-o",  uložím_jako]
            print("stahuji '{}'".format(jméno_souboru))
#            os.system(příkaz)
#            print("staženo {}".format(os.path.basename(url_souboru).strip()))
            print(" ".join(příkaz))
            proces = subprocess.Popen(příkaz,  stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            procesy[jméno_souboru] = proces
        
    print("\t...průběh stahování\n")

    start = time.time()
    
    try:
        běžící_procesy = list(procesy.keys())
#        print(type(běžící_procesy),  běžící_procesy)
        while běžící_procesy:
            for jméno_souboru in běžící_procesy:
                proces = procesy[jméno_souboru]
                návratový_kód = proces.poll()
                if návratový_kód is not None:
                    běžící_procesy.remove(jméno_souboru)
#                    počet_procesů = len(procesy)
                    print("soubor '{}' byl stažen za {:.0f} vteřin. Stahování skončilo kódem {}".format(jméno_souboru,  time.time() - start,  návratový_kód))
    #        proces.wait()
    #        print(".",  end="")
    except KeyboardInterrupt as e:
        print("stahování zrušeno")
        for jméno_souboru in běžící_procesy:
            proces = procesy[jméno_souboru]
            proces.terminate()
#            procesy.pop(jméno_souboru)
            print("stahování souboru '{}' přerušeno po {:.0f} vteřinách.".format(jméno_souboru,  time.time() - start))
        
