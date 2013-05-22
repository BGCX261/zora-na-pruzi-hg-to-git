#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který projde položky faktur a zapíše je do účetního deníku
neumí zaučtovat účet má_dáti u přijetí faktury a následné platby
na to je jiný skript zapíšu_chybějící_čísla_účtu_faktur_do_deníku.py
'''
#import postgresql
import datetime
from pruga.knjigovod.nastavení.databáze import davaj_připojení,   JMÉNO_DATABÁZE
#from pruga.web.prohlížeče.prohlížeč import spustím_prohlížeč
from pruga.danimir.insert import INSERT
from pruga.danimir.databázové_typy.účetnictví_číslo_účtu import ROW

def zapíšu_položky_faktur_do_deníku():
 
    '''
    provede import dle skriptu do určité tabulky
    '''
    db = davaj_připojení(JMÉNO_DATABÁZE)
    
    dotaz = 'SELECT * FROM "rozpis_přijatých_faktur" ORDER BY "datum_vystavení", "číslo_přijaté_faktury", "položky_pořadí_položky"'
    print("spouštím SQL příkaz:\n\t{}".format(dotaz))
    
    pitanje = db.prepare(dotaz)
    
    insert = INSERT(db = db,  tabulka = "účetní_deník")
    insert.sloupce("datum",	 
        "krok",	 
        "částka",	 
        "popis",
        "má_dáti",	 
        "dal", 
        "číslo_dokladu", 
        "pořadí_položky", 
        "druh_dokladu")
    
    datum = None
    číslo_dokladu = None
    krok = 1
    pořadí_položky = None
    druh_dokladu = 'PŘIJATÁ FAKTURA'
    hodina = 10
    suma = 0
    
#    účet_DPH_má_dáti = ROW(343, None)
    účet_DPH_má_dáti_dle_sazby = {10: ROW(343, 10),  14: ROW(343, 14),  20: ROW(343, 20)}
    
    účet_má_dáti = None
    účet_dal_hotově = ROW(211,1)
    účet_dal_faktura = ROW(321,1)
    účet_úhrada_má_dáti = ROW(321,1)
    účet_úhrada_dal = ROW(221,1)
    
    for hodnoty in pitanje:
        
        #nejprve si nachystáme datum zápisu do deníku, aby položky deníku byly chronologicky správně
        d = hodnoty['datum_vystavení']
        
        
        #        při každé změně dokladu přidáme záznam o uhrazení předchozí faktury
        if číslo_dokladu and číslo_dokladu != hodnoty['číslo_přijaté_faktury'] :
            if not hotově:
                krok = 1
#            print(datum,  krok,  suma,  'uhrazení faktury',  účet_úhrada_má_dáti ,  účet_úhrada_dal ,  číslo_dokladu,  druh_dokladu)
                datum_splatnosti = datetime.datetime(d.year,  d.month,  d.day + 14,  8,  0,  0)
                insert.hodnoty(datum_splatnosti ,  krok,  suma,  'uhrazení faktury',  účet_úhrada_má_dáti ,  účet_úhrada_dal ,  číslo_dokladu,  pořadí_položky,  druh_dokladu)
            suma = 0
            
        
#        máme nový den,  nastavíme hodiny zpět na výchozí hodnotu
        if datum and datum.day != d.day:
            hodina = 10
        else:
        #     den se nemění, ale máme novou fakturu,  posuneme o hodinu ať to není ve stejnou dobu
            if číslo_dokladu and číslo_dokladu != hodnoty['číslo_přijaté_faktury'] :
                hodina = hodina + 1
        
        minuta = 0
        sekunda = 0
        datum = datetime.datetime(d.year,  d.month,  d.day,  hodina,  minuta,  sekunda)
        
        číslo_dokladu = hodnoty['číslo_přijaté_faktury']
        pořadí_položky = hodnoty['položky_pořadí_položky']
        krok = 1
        
        if hodnoty['forma_úhrady'] == 'formaUhr.prevodem':
            hotově = False
        else:
            hotově = True
#        včíl zaučtujeme cenu
        cena = hodnoty['položky_cena_bez_dph']
        dph  = hodnoty['položky_DPH']
        sazba_dph  = hodnoty['položky_sazba_dph']
        suma = suma + cena + dph
       
#        nejdříve nákup
        if hotově:
            účet_dal = účet_dal_hotově
        else:
            účet_dal = účet_dal_faktura
            
#        print(datum,  krok,  cena,  'položka přijaté faktury',  účet_má_dáti,  účet_dal,  číslo_dokladu,  druh_dokladu)
        insert.hodnoty(datum,  krok,  cena,  'položka přijaté faktury',  účet_má_dáti,  účet_dal,  číslo_dokladu,  pořadí_položky,  druh_dokladu)
#            posuneme krok
        krok = krok + 1
#        a včíl dph
        if sazba_dph:
            účet_DPH_má_dáti = účet_DPH_má_dáti_dle_sazby[int(sazba_dph)]
#            print(datum,  krok,  dph,  'DPH položky přijaté faktury',  účet_DPH_má_dáti,  účet_dal,  číslo_dokladu,  druh_dokladu)
            insert.hodnoty(datum,  krok,  dph,  'DPH položky přijaté faktury',  účet_DPH_má_dáti,  účet_dal,  číslo_dokladu,  pořadí_položky,  druh_dokladu)
            #            posuneme krok - včíl se ale už nevyužije
#            krok = krok + 1
        
#        toto je uhrazení poslední faktury,  které se nemohlo zapsat,  bo cyklus už skončil    
    if not hotově:
        krok = 1
#        print(datum,  krok,  suma,  'uhrazení faktury',  účet_úhrada_má_dáti ,  účet_úhrada_dal ,  číslo_dokladu,  druh_dokladu)
        insert.hodnoty(datum,  krok,  suma,  'uhrazení faktury',  účet_úhrada_má_dáti ,  účet_úhrada_dal ,  číslo_dokladu,  pořadí_položky,  druh_dokladu)
            
#    print(insert_pitanje)  
#    print("spouštím SQL příkaz pro vložení dat")
#    print(insert)
    insert.vykonej()
    
    db.close()


if __name__ == '__main__':

    print(__doc__)

    zapíšu_položky_faktur_do_deníku()
