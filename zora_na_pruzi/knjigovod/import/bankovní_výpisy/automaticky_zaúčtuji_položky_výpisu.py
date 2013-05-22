#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který se pokusí automaticky zaúčtovat položky výpisu
'''

import locale
locale.setlocale(locale.LC_ALL, '')

from datetime import date

from pruga.knjigovod.nastavení.databáze import davaj_připojení,   JMÉNO_DATABÁZE
from pruga.danimir.insert import INSERT
from pruga.danimir.databázové_typy.účetnictví_číslo_účtu import ROW

TABULKA_BANKOVNÍ_VÝPISY = "bankovní_výpisy"
TABULKA_ÚČETNÍ_DENÍK = "účetní_deník"
    
def zaúčtuji_položky_bankovního_výpisu():
    global TABULKA_BANKOVNÍ_VÝPISY
    global ČÍSLO_ÚČTU
    
    db = davaj_připojení(JMÉNO_DATABÁZE)
    dotaz = 'SELECT "id", "id_bankovního_účtu", "datum", "částka", "variabilní_symbol", "specifický_symbol", "poznámka", "druh_platby", "protiúčet_číslo_účtu",	"protiúčet_kód_banky" FROM "{}" WHERE "zaúčtováno" is null'.format(TABULKA_BANKOVNÍ_VÝPISY)
    pitanje = db.prepare(dotaz)
    
    sloupce = ["datum",  "částka",  "popis",  "má_dáti",  "dal",  "druh_dokladu"]
    insert = INSERT(db = db,  tabulka = TABULKA_ÚČETNÍ_DENÍK)
    insert.sloupce(*sloupce)
    
    šablona_sql_update = 'UPDATE "{}" SET "zaúčtováno" = (SELECT currval(pg_get_serial_sequence(\'účetní_deník\', \'id\'))) WHERE "id" = {{}}'.format(TABULKA_BANKOVNÍ_VÝPISY)
    
                          
    for řádek in pitanje():
        
        popis = řádek["poznámka"] or "výpis z účtu"
        druh_platby = řádek["druh_platby"]
        
        účet_md,  účet_dal = běžné_účetní_postupy(**řádek)
        
        if účet_md and  účet_dal:
            print('účtuji {} {} - {}'.format(řádek["id"],  popis,  druh_platby))
            with db.xact():
                insert.vyčisti_hodnoty()
                insert.hodnoty(řádek["datum"],  kladný(řádek["částka"]),  popis,  účet_md,  účet_dal,  druh_platby)
                sql_update = šablona_sql_update.format(řádek["id"])
                insert.vykonej()
                update = db.prepare(sql_update)
                update()
    
    import sys
    sys.exit()
    

def kladný(číslo):
    if číslo < 0:
        číslo = -1 * číslo
        
    return číslo

def běžné_účetní_postupy(*args,  **kwargs):
    
#    Připsaný úrok
    if kwargs["poznámka"] == "Připsaný úrok":
        if kwargs["částka"] > 0:
            return ROW(221, kwargs["id_bankovního_účtu"]),  ROW(662,  100)
       
#    poplatek - platební karta
    if kwargs["druh_platby"] == "Poplatek - platební karta" and kwargs["protiúčet_číslo_účtu"] is None and kwargs["protiúčet_kód_banky"] is None:
        if kwargs["částka"] < 0:
            return ROW(568,  100),  ROW(221, kwargs["id_bankovního_účtu"])
      
#    vratka DPH
    if kwargs["protiúčet_číslo_účtu"] == '705-7624721' and kwargs["protiúčet_kód_banky"] == '0710' and kwargs["variabilní_symbol"] == '29191360':
        if kwargs["částka"] > 0:
            return ROW(221, kwargs["id_bankovního_účtu"]),  ROW(343,  100)
            
#Vklad pokladnou
    if kwargs["druh_platby"] == "Vklad pokladnou" and kwargs["protiúčet_číslo_účtu"] is None and kwargs["protiúčet_kód_banky"] is None:
        if kwargs["částka"] > 0:
            return ROW(221, kwargs["id_bankovního_účtu"]), ROW(211,  1)

#Výběr pokladnou
    if kwargs["druh_platby"] == "Výběr pokladnou" and kwargs["protiúčet_číslo_účtu"] is None and kwargs["protiúčet_kód_banky"] is None:
        if kwargs["částka"] < 0:
            return ROW(211,  1),  ROW(221, kwargs["id_bankovního_účtu"])
            
            
            #            Platba kartou - je ve skutečnosti výběr kartou a zaučtuji jako výběr do pokladny
    if kwargs["druh_platby"] == "Platba kartou" and kwargs["protiúčet_číslo_účtu"] is None and kwargs["protiúčet_kód_banky"] is None:
        if kwargs["částka"] < 0:
            return ROW(211,  1),  ROW(221, kwargs["id_bankovního_účtu"])
            
#            platby na slovensko - jako do pokladny číslo 4
#    if kwargs["druh_platby"] == "Platba v jiné měně":
#        if kwargs["částka"] < 0:
#            return ROW(211,  4),  ROW(221, kwargs["id_bankovního_účtu"])
            
#     půjčky Pacov, pak vráceno na jiné účty
#    if kwargs["protiúčet_číslo_účtu"] == '2700182115' and kwargs["protiúčet_kód_banky"] == '2010':
#        if kwargs["částka"] < 0:
#            return ROW(211,  3),  ROW(221, kwargs["id_bankovního_účtu"])

#    Martinovi - stavba DPH garáže
#    if kwargs["protiúčet_číslo_účtu"] == '670100-2207768534' and kwargs["protiúčet_kód_banky"] == '6210':
#        if kwargs["částka"] < 0:
#            return ROW(211,  5),  ROW(221, kwargs["id_bankovního_účtu"])
            
#    moje různé výdaje - zelení, le. podpis atd.
    if kwargs["protiúčet_číslo_účtu"] == '2900027355' and kwargs["protiúčet_kód_banky"] == '2010':
        if kwargs["částka"] < 0:
            return ROW(211,  6),  ROW(221, kwargs["id_bankovního_účtu"])
            
    return (None,  None)

if __name__ == '__main__':

    print(__doc__)

    zaúčtuji_položky_bankovního_výpisu()
    

