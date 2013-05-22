#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který zpětně propojí účetní deník a položky faktur, zapíše čísla řádku z účetního deníku do položek faktur
'''
import postgresql
from pruga.knjigovod.nastavení.databáze import davaj_připojení,  JMÉNO_DATABÁZE_FLEXIBEE,  JMÉNO_DATABÁZE
#from pruga.web.prohlížeče.prohlížeč import spustím_prohlížeč


def zapíšu_zaúčtování_do_položek_faktur():
    '''
    zapíše čísla řádku z účetního deníku do položek faktur
    '''
    db = davaj_připojení(JMÉNO_DATABÁZE)
    
    dotaz = 'SELECT "id", "číslo_dokladu", "popis", "id_faktury",	"pořadí_položky_faktury" FROM "rozpis_zaúčtovaných_položek_faktur_v_účetním_deníku" WHERE "druh_dokladu" LIKE \'PŘIJATÁ FAKTURA\''
    print("spouštím SQL příkaz:\n\t{}".format(dotaz))
    
    pitanje = db.prepare(dotaz)
    
    dotaz_nákupu = 'UPDATE "přijaté_faktury_položky" SET "{1}" = {0[0]} WHERE "id_faktury" = {0[3]} and "pořadí_položky" = {0[4]}'
    
    sloupce = {'položka přijaté faktury': 'zaúčtován_nákup',  'DPH položky přijaté faktury': 'zaúčtováno_dph',  'uhrazení faktury': 'zaúčtována_platba'}
    
    for řádek in pitanje():
        druh_operace = řádek[2]
        dotaz = dotaz_nákupu.format(řádek,  sloupce[druh_operace])
        update = db.prepare(dotaz)
        update()
        
    db.close()
 

    

if __name__ == '__main__':

    print(__doc__)

    zapíšu_zaúčtování_do_položek_faktur()


