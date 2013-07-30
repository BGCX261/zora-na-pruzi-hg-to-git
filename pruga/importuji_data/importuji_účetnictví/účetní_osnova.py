#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'


import regex as re

from pruga.data.účetnictví.účetní_osnova import Účtová_osnova,  Účtová_třída,  Účtová_skupina,  Účet,  MÁ_ÚČET,  MÁ_SKUPINU,  MÁ_TŘÍDU

ÚČTOVÁ_OSNOVA = '`Účtová osnova`'
ÚČTOVÁ_TŔÍDA = '`Účtová třída`'
ÚČTOVÁ_SKUPINA = '`Účtová skupina`'
ÚČET = '`Účet`'

ÚČTOVÁ_OSNOVA_MÁ_TŘÍDU = ':`MÁ TŘÍDU`'
ÚČTOVÁ_TŘÍDA_MÁ_SKUPINU = ':`MÁ SKUPINU`'
ÚČTOVÁ_SKUPINA_MÁ_ÚČET = ':`MÁ ÚČET`'

účtová_osnova = Účtová_osnova(jméno = 'česká účetní osnova')
účty = {}
graf_obsahuje = [účtová_osnova]

#class CREATE():
#    
#    def __init__(self):
#        self.__prvky = ['uctova_osnova:{}'.format(ÚČTOVÁ_OSNOVA)]
#        
#    def __call__(self,  kód):
#        self.__prvky.append(kód)
#        
#    def __str__(self):
#        
#        příkaz = [
#        'MATCH uctova_osnova:{}'.format(ÚČTOVÁ_OSNOVA), 
#        'WITH count(uctova_osnova) as pocet', 
#        'WHERE pocet = 0 ', 
#        'CREATE', 
#        ',\n'.join(self.__prvky)
#        ]
#        
#        příkaz = '\n'.join(příkaz)
#        return '{};'.format(příkaz)
#        
#CREATE = CREATE()

def toto_je_záhlaví_tabulky(řádek):
    assert řádek == ['Název účtu', 'Položka rozvahy', '', 'Položka výkazu zisku a ztráty']
    
def toto_je_podzáhlaví_tabulky(řádek):
#    print('toto_je_podzáhlaví_tabulky: ',  řádek)
    assert řádek == ['', 'Aktiva', 'Pasiva']
    
def toto_je_účtová_třída(řádek,  číslo,  jméno):
    
    kontroluji_pořadí_účtové_třídy(číslo)
    
    assert len(řádek) == 1
    
    uzel = Účtová_třída(číslo = číslo,  jméno = jméno)
    graf_obsahuje.append(uzel)
    
    účty[číslo] = uzel
    
    vazba = MÁ_TŘÍDU(účtová_osnova,  uzel)
    graf_obsahuje.append(vazba)
    
    
    
#    CREATE('n_{}:{} {}'.format(číslo,  labels(ÚČTOVÁ_TŔÍDA,  ÚČTOVÁ_OSNOVA),  vlastnosti(číslo = číslo,  jméno = jméno)))
#    CREATE('(uctova_osnova)-[{}]->(n_{})'.format(ÚČTOVÁ_OSNOVA_MÁ_TŘÍDU,  číslo))
    
    
def toto_je_účtová_třída_8_a_9(řádek,  číslo,  jméno):
    
    toto_je_účtová_třída(řádek,  "8",  jméno)
    toto_je_účtová_třída(řádek,  "9",  jméno)
    


def toto_je_účtová_skupina(řádek,  číslo,  jméno):
    
    assert len(řádek) == 1
    
    uzel = Účtová_skupina(číslo = číslo,  jméno = jméno)
    graf_obsahuje.append(uzel)
    
    účty[číslo] = uzel
    
    vazba = MÁ_SKUPINU(účty[číslo[:-1]],  uzel)
    graf_obsahuje.append(vazba)
    
#    CREATE('n_{}:{} {}'.format(číslo,  labels(ÚČTOVÁ_SKUPINA,  ÚČTOVÁ_OSNOVA),  vlastnosti(číslo = číslo,  jméno = jméno)))
#    
##    (n)-[:LOVES {since: {value}}]->(m)
#    CREATE('(n_{})-[{}]->(n_{})'.format(číslo[:-1],  ÚČTOVÁ_TŘÍDA_MÁ_SKUPINU,  číslo))
    
def toto_je_soupis_skupin_7x(řádek,  číslo,  jméno):
    
    assert len(řádek) == 1
    
def toto_je_účet(řádek,  číslo,  jméno):
    
    uzel = Účet(číslo = číslo,  jméno = jméno)
    graf_obsahuje.append(uzel)
    
    účty[číslo] = uzel
    
    vazba = MÁ_ÚČET(účty[číslo[:-1]],  uzel)
    graf_obsahuje.append(vazba)
    
#    CREATE('n_{}:{} {}'.format(číslo,  labels(ÚČET,  ÚČTOVÁ_OSNOVA),  vlastnosti(číslo = číslo,  jméno = jméno)))
#    
#    CREATE('(n_{})-[{}]->(n_{})'.format(číslo[:-1],  ÚČTOVÁ_SKUPINA_MÁ_ÚČET,  číslo))
    


parsovací_funkce = {re.compile(r'^Název účtu'): toto_je_záhlaví_tabulky, 
                            re.compile(r'^$'): toto_je_podzáhlaví_tabulky, 
                                re.compile(r'^ÚČTOVÁ\s+TŘÍDA\s+(?P<číslo>[0-9])[ \t]-[ \t](?P<jméno>.+)'): toto_je_účtová_třída, 
                                re.compile(r'^(?P<číslo>[0-9]{2})x?[ \t]-[ \t](?P<jméno>.+)'): toto_je_účtová_skupina, 
                              re.compile(r'^(?P<číslo>[0-9]{3})[ \t]-[ \t](?P<jméno>.+)'): toto_je_účet , 
                              re.compile(r'^ÚČTOVÉ\s+TŘÍDY\s+(?P<číslo>[0-9]) A 9[ \t]-[ \t](?P<jméno>.+)'): toto_je_účtová_třída_8_a_9, 
                              re.compile(r'^(?P<číslo>[0-9]{2}) až 79[ \t]-[ \t](?P<jméno>.+)'): toto_je_soupis_skupin_7x 
                                }

def kontroluji_pořadí_účtové_třídy(číslo):
    if not kontroluji_pořadí_účtové_třídy.číslo_třídy == int(číslo):
        raise ValueError('Chyba pořadí účtové třídy, očekávám {} ale číslo je {}'.format(kontroluji_pořadí_účtové_třídy.číslo_třídy, číslo))
        
    kontroluji_pořadí_účtové_třídy.číslo_třídy = kontroluji_pořadí_účtové_třídy.číslo_třídy + 1

kontroluji_pořadí_účtové_třídy.číslo_třídy = 0

def davaj_cypher_pro_import_účetní_osnovy():
    '''
    spouštím funkci main()
    '''
#    db = připojím_postgrersql()
    
#    (n:Person { name : 'Andres' , title : 'Developer' })
    
    
    
    for řádek in csv_účetní_osnova():
#        print('main: ',  řádek)
        
        kód = None
        
        for r,  funkce in parsovací_funkce.items():
            zachyceno = r.match(řádek[0])
            if zachyceno:
#                print('main: ',  řádek,  'zachycen do: ',  funkce.__name__)
                try:
                    zachycené_parametry = zachyceno.groupdict()
                    funkce(řádek,  **zachycené_parametry)
                    break
                except TypeError as e:
                    print('funkci {} dávám {} a ta to nebere'.format(funkce.__name__,  zachycené_parametry))
                    raise e
                
        else:
            raise ValueError('Neumím zpracovat tento řádek: "{}"'.format(' | '.join(řádek)))
            
#    yield CREATE
    return graf_obsahuje
 
def davaj_cypher_pro_indexy():
    příkazy = [
    
        'CREATE INDEX ON :{}(`číslo`)'.format(ÚČTOVÁ_TŔÍDA), 
        'CREATE INDEX ON :{}(`jméno`)'.format(ÚČTOVÁ_TŔÍDA),
        'CREATE INDEX ON :{}(`číslo`)'.format(ÚČTOVÁ_SKUPINA), 
        'CREATE INDEX ON :{}(`jméno`)'.format(ÚČTOVÁ_SKUPINA),
        'CREATE INDEX ON :{}(`číslo`)'.format(ÚČET), 
        'CREATE INDEX ON :{}(`jméno`)'.format(ÚČET)
        ]
        
    for příkaz in příkazy:
        yield '{};'.format(příkaz)
    

def csv_účetní_osnova():
    import os
    zdrojový_soubor = 'jak_se-dělají_výkazy_účty.csv'
    soubor = os.path.join(os.path.dirname(__file__),  zdrojový_soubor)
    
    with open(soubor,  mode='r',  encoding='utf-8') as soubor:
        for řádek in soubor:
            řádek = řádek.strip()
            yield řádek.split(';')
            
#def parsuji_řádek_csv(řádek):
    

if __name__ == '__main__':
   
    import argparse
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser()

#   a pak mu nastavím jaké příkazy a parametry má přijímat
    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, {}'.format(__version__))
    
    parser.add_argument('akce',  choices = ['data', 'indexy'])
    
    
    #    a včíl to možu rozparsovat
    args = parser.parse_args()
    
#    print('soubor',  args.soubor)

    if args.akce == 'data':
        for cypher in davaj_cypher_pro_import_účetní_osnovy():
            print(cypher)
        
    if args.akce == 'indexy':
        for cypher in davaj_cypher_pro_indexy():
            print(cypher)
