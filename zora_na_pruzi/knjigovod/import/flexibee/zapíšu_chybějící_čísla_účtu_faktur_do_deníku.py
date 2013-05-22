#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který projde položky faktur už zapsané v účetním deníku a přiřadí účty platby z pokaldny, či z účtu
'''
#import postgresql
import datetime
from pruga.knjigovod.nastavení.databáze import davaj_připojení,   JMÉNO_DATABÁZE
#from pruga.web.prohlížeče.prohlížeč import spustím_prohlížeč
from pruga.danimir.update import UPDATE
from pruga.danimir.databázové_typy.účetnictví_číslo_účtu import ROW
from pruga.danimir.sql.formát import formát_názvu,  formát_hodnoty

def opravím_položky_faktur_v_deníku():
 
    '''
    provede import dle skriptu do určité tabulky
    '''
    db = davaj_připojení(JMÉNO_DATABÁZE)
    
    dotaz = '''SELECT * FROM "rozpis_zaúčtovaných_položek_faktur_v_účetním_deníku"
                        
                        WHERE "popis" LIKE 'uhrazení faktury'
                        AND
                        "má_dáti" is NULL

                        ORDER BY "datum", "číslo_dokladu", "krok"
                        
                       '''
    print("spouštím SQL příkaz:\n\t{}".format(dotaz))
    
    pitanje = db.prepare(dotaz)
    update = UPDATE(db = db,  tabulka = "účetní_deník")
    
    for položka in pitanje:
        
        platba = položka['forma_úhrady']
        
        if platba == 'formaUhr.prevodem':
            účet = ROW(221, 1)
        else:
            účet = ROW(211, 1)
    
        where = '{} LIKE {} AND {} = {} AND {} = {}'.format(formát_názvu('číslo_dokladu'),  formát_hodnoty(položka['číslo_dokladu']), 
                                                        formát_názvu('krok'),  formát_hodnoty(položka['krok']), 
                                                        formát_názvu('datum'),  formát_hodnoty(položka['datum']))
        update.where(where)
        update.sloupce("má_dáti")
        update.hodnoty(účet)

        print("spouštím SQL příkaz pro vložení dat")
        update.vykonej()
    
    db.close()
 
    

if __name__ == '__main__':

    print(__doc__)

    opravím_položky_faktur_v_deníku()
