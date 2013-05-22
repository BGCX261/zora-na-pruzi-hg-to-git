#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který vypíše data z databáze
'''

from pruga.grafomir.databáze.připojení.hlavní_databáze import g

def seznam_firem():
    '''
    zahájí běh programu
    '''
    firmy = g.firmy.get_all()
    for firma in firmy:
        print('{f.ičo} {f.jméno}, {f.adresa}'.format(f = firma))
        cypher_skript = '''START  firma = node:firma(`ičo` = {`ičo`})
                            MATCH firma-[:`firma_vystavila_fakturu`]->faktury
                            RETURN faktury'''
    
        params = {'ičo': firma.ičo}
#        faktury = g.faktury
        faktury = getattr(g,  'faktury')
        faktury = g.cypher.query(cypher_skript,  params)
        for faktura in faktury:
            print(faktura.datum_vystavení)
            print('\t{f.číslo_faktury} {f.datum_vystavení}'.format(f = faktura))

if __name__ == '__main__':

    print(__doc__)

    seznam_firem()
    


