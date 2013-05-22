#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který opraví způsob užití čísel účtů v databázi
'''
import postgresql
from pruga.knjigovod.nastavení.databáze import davaj_připojení,  JMÉNO_DATABÁZE_FLEXIBEE,  JMÉNO_DATABÁZE
#from pruga.web.prohlížeče.prohlížeč import spustím_prohlížeč


def upravím_způsob_číslování_účtů():
    '''
    provede import dle skriptu do určité tabulky
    '''
    db_výběr = davaj_připojení(JMÉNO_DATABÁZE)
    
    dotaz = 'SELECT "číslo_účtu_kód" FROM "účetní_osnova"'
    print("spouštím SQL příkaz:\n\t{}".format(dotaz))
    
    pitanje = db_výběr.prepare(dotaz)

#    dotaz = 'UPDATE "účetní_osnova" SET "syntetický_účet" = $1,  "analytický_účet" = $2 WHERE "číslo_účtu" LIKE $3'
    dotaz = 'UPDATE "účetní_osnova" SET "číslo_účtu" = (ROW($1, $2)) WHERE "číslo_účtu_kód" LIKE $3'
    print(dotaz)
    db = davaj_připojení(JMÉNO_DATABÁZE)
    insert_pitanje = db.prepare(dotaz)
    
    for hodnoty in pitanje:
        hodnota = hodnoty[0]
#        print(hodnota)
        insert_pitanje(int(hodnota[:3]),  int(hodnota[4:]),  hodnota)
    
    db_výběr.close()
    db.close()
 

    

if __name__ == '__main__':

    print(__doc__)

    upravím_způsob_číslování_účtů()


