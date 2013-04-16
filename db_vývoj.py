#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je skript, gde si zkúšám
'''

import os

def db():
    from zora_na_pruzi.danimir.připojení.postgresql import pruga_test
    from zora_na_pruzi.danimir.připojení.připojím_postgresql import postgresql_připojím_se_k_databázi
    
    db_připojení = postgresql_připojím_se_k_databázi(pruga_test)
    
    from zora_na_pruzi.danimir.db import db
    db = db(db_připojení)
    
    from zora_na_pruzi.danimir.najdu_či_vytvořím_klíč import najdu_či_vytvořím_klíč
    id_klíče = najdu_či_vytvořím_klíč('jméno',  'medvěd')
    print(id_klíče)
    
#    from zora_na_pruzi.danimir.nový_uzel import nový_uzel
#    firma = nový_uzel('firma')
    
    

if __name__ == '__main__':

    print(__doc__)
    
#    print('='*44)
#    pisar()
#    print('='*44)
#    barevná_konzole()
#    print('='*44)
#    html_výpis()   
#    print('='*44)
#else:
    
    db()
 
