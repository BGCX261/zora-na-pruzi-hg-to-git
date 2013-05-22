#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který vrátí relaci 
'''

from pruga.zemjemjerka.nastavení.databáze import davaj_připojení

db = davaj_připojení()


def davaj_relaci(id_relace):
    '''
    najde relaci
    '''
    print('Hledám relaci "{}"'.format(id_relace))
    dotaz = 'SELECT * FROM zemjemjerka."davaj_body_relace"({})'.format(id_relace)
    pitanje = db.prepare(dotaz)
    return pitanje


def davaj_cesty_v_relaci(id_relace):
    sql = 'SELECT '

if __name__ == '__main__':

    print(__doc__)

    id_relace = '48896'

    trať = davaj_relaci(id_relace)
    
    print(trať.column_names)
    
    for úsek in trať():
        print(úsek)



