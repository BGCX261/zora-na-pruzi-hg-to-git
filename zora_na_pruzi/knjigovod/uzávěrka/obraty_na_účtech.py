#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který vytvoří uzávěrku
'''

from pruga.knjigovod.nastavení.databáze import davaj_připojení,   JMÉNO_DATABÁZE
import postgresql

def spočítám_obraty_na_účtech(rok):
    '''
    spočítám obraty na účtech
    '''
    print('obraty na účtech v roce {}'.format(rok))
    
    db = davaj_připojení(JMÉNO_DATABÁZE)
    dotaz_má_dáti = 'SELECT "má_dáti" AS "číslo_účtu", sum(částka)  AS "obrat_má_dáti" FROM "účetní_deník" WHERE extract(YEAR from "datum") = {} GROUP BY "má_dáti"'.format(rok)
    dotaz_dal = 'SELECT "dal"  AS "číslo_účtu", sum(částka) AS "obrat_dal" FROM "účetní_deník" WHERE extract(YEAR from "datum") = {} GROUP BY "dal"'.format(rok)

    tabulka = {}

    for dotaz in dotaz_má_dáti,  dotaz_dal:
        pitanje = db.prepare(dotaz)
        for řádek in pitanje():
            číslo_účtu = řádek["číslo_účtu"]
            hodnoty = tabulka.get(číslo_účtu)
            nové_hodnoty = {k:v for k,  v in řádek.items()}
            if not hodnoty:
                tabulka[číslo_účtu] = nové_hodnoty
            else:
                hodnoty.update(nové_hodnoty)

    for řádek in tabulka.values():
        sql_insert = 'INSERT INTO "uzávěrka_obraty_účtů"("rok", "číslo_účtu", "obrat_má_dáti", "obrat_dal") VALUES({rok}, ROW{číslo_účtu}, {obrat_má_dáti}, {obrat_dal})'.format(
                                rok = rok, 
                                číslo_účtu = řádek["číslo_účtu"], 
                                 obrat_má_dáti  = řádek.get("obrat_má_dáti",  0.0), 
                                 obrat_dal = řádek.get("obrat_dal",  0.0) 
                                )
        print('{} md: {} d: {}'.format(řádek["číslo_účtu"],  řádek.get("obrat_má_dáti",  0.0),  řádek.get("obrat_dal",  0.0)))
        insert = db.prepare(sql_insert)
        try:
            insert()
        except postgresql.exceptions.UniqueError:
            print('již jestvuje zápis účtu {}'.format(řádek["číslo_účtu"]))
            continue
        

def spočítám_konečné_zůstatky():
    
    db = davaj_připojení(JMÉNO_DATABÁZE)
    
    sql = '''SELECT "uzávěrka_obraty_účtů"."rok",
                            "uzávěrka_obraty_účtů"."číslo_účtu", 
                            "uzávěrka_obraty_účtů"."obrat_má_dáti",
                            "uzávěrka_obraty_účtů"."obrat_dal",
                            "uzávěrka_obraty_účtů"."konečný_zůstatek",
                            "osnova"."druh_účtu"
                    FROM "uzávěrka_obraty_účtů"
                    JOIN "účetní_osnova" as "osnova"
                    ON "uzávěrka_obraty_účtů"."číslo_účtu" = "osnova"."číslo_účtu"
                    
                    --- WHERE "konečný_zůstatek" is NULL
                    
                    ORDER BY "rok", "číslo_účtu"
                    '''
                    
    pitanje = db.prepare(sql)
    
    aktiva = pasiva = náklady = výnosy = 0
    for řádek in pitanje():
        konečný_zůstatek = None
       
        if řádek["druh_účtu"] == 'druhUctu.aktivni':
            konečný_zůstatek = řádek["obrat_má_dáti"] - řádek["obrat_dal"]
            aktiva = aktiva + konečný_zůstatek
          
#        TODO:   toto nevím esli je dobře
        if řádek["druh_účtu"] == 'druhUctu.aktpasvy':
            konečný_zůstatek = řádek["obrat_má_dáti"] - řádek["obrat_dal"]
            aktiva = aktiva + konečný_zůstatek            

        if řádek["druh_účtu"] == 'druhUctu.pasivni':
            konečný_zůstatek = řádek["obrat_dal"] - řádek["obrat_má_dáti"] 
            pasiva = pasiva + konečný_zůstatek
            
        if řádek["druh_účtu"] == 'druhUctu.naklady':
            konečný_zůstatek = řádek["obrat_má_dáti"] - řádek["obrat_dal"]
            náklady = náklady + konečný_zůstatek

        if řádek["druh_účtu"] == 'druhUctu.vynosy':
            konečný_zůstatek = řádek["obrat_dal"] - řádek["obrat_má_dáti"] 
            výnosy = výnosy + konečný_zůstatek
         
        if konečný_zůstatek is not None:
            sql = 'UPDATE "uzávěrka_obraty_účtů" SET "konečný_zůstatek" = {0} WHERE "rok" = {1[rok]} and "číslo_účtu" = ROW{1[číslo_účtu]}'.format(konečný_zůstatek,  řádek)
#            print(sql)
            update = db.prepare(sql)
            update()
#    print(řádek["číslo_účtu"],  konečný_zůstatek)
    zisk = výnosy - náklady
    print('AKTIVA {}\nPASIVA {}\nA-P {}\n-----------\nNÁKLADY {}\nVÝNOSY {}\n------------\nZISK {}'.format(aktiva,  pasiva,  aktiva-pasiva,  náklady,  výnosy,  zisk))

if __name__ == '__main__':

    print(__doc__)

    import argparse

    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser(description='Uzávěrka, spočtu obraty účtů.')

#   a pak mu nastavím jaké příkazy a parametry má přijímat
#    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, pruga verze: Пруга {}'.format(__version__))

    parser.add_argument('rok',  type=int)
    args = parser.parse_args()
    
    spočítám_obraty_na_účtech(args.rok)
    spočítám_konečné_zůstatky()



