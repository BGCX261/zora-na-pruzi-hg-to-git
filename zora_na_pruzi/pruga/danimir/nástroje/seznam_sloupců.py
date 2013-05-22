#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který ...
'''

#Tohle je zatím k ničemu,  neumím rozlišit ke které tabulce patří jednotlivé sloupce,  doporučuji používat další funkci pro každou tabulku zvlášť
#def seznam_sloupců_z_dotazu(databáze,  select):
#    '''
#    vrátí seznam sloupců v dotazu
#    '''
#    výsledek = databáze(select)
#    print(select)
#    for sloupec in výsledek.sloupce():
#        print(sloupec)
    
def seznam_sloupců_tabulky(databáze,  tabulka,  formát = '{}'):
    '''
    vrátí seznam sloupců tabulky naformátopvaný jak potřebuji dle parametru formát
    '''
    
    dotaz = '''SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.Columns WHERE
TABLE_NAME = \'{}\''''.format(str(tabulka).replace('"',  ''))

#    print("spouštím SQL příkaz:\n\t{}".format(dotaz))

    pitanje = databáze(dotaz)
    
    sloupce = []
    
    for sloupec in pitanje:
        sloupce.append(formát.format(*sloupec))
    return sloupce
    

