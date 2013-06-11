#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'


import re

ÚČTOVÁ_OSNOVA = '`Účtová osnova`'
ÚČTOVÁ_TŔÍDA = '`Účtová třída`'
ÚČTOVÁ_SKUPINA = '`Účtová skupina`'
ÚČET = '`Účet`'

ÚČTOVÁ_OSNOVA_MÁ_TŘÍDU = ':`MÁ TŘÍDU`'
ÚČTOVÁ_TŘÍDA_MÁ_SKUPINU = ':`MÁ SKUPINU`'
ÚČTOVÁ_SKUPINA_MÁ_ÚČET = ':`MÁ ÚČET`'

class CREATE():
    
    def __init__(self):
        self.__prvky = ['uctova_osnova:{}'.format(ÚČTOVÁ_OSNOVA)]
        
    def __call__(self,  kód):
        self.__prvky.append(kód)
        
    def __str__(self):
        
        příkaz = [
        'MATCH uctova_osnova:{}'.format(ÚČTOVÁ_OSNOVA), 
        'WITH count(uctova_osnova) as pocet', 
        'WHERE pocet = 0 ', 
        'CREATE', 
        ',\n'.join(self.__prvky)
        ]
        
        příkaz = '\n'.join(příkaz)
        return '{};'.format(příkaz)
        
CREATE = CREATE()

def vlastnosti(**kwargs):
    seznam = []
    for klíč,  hodnota in kwargs.items():
        klíč = cypherové_uvozovky(klíč)
        if isinstance(hodnota,  str):
            hodnota = '"{}"'.format(hodnota) 
           
        záznam = '{}: {}'.format(klíč,  hodnota) 
          
        seznam.append(záznam)
        
    return '{{{}}}'.format(','.join(seznam))

def labels(*args):
    return ':'.join(args)

def cypherové_uvozovky(slovo):
    return '`{}`'.format(slovo)

def toto_je_záhlaví_tabulky(řádek,  číslo_účtu,  jméno):
    assert řádek == ['Název účtu', 'Položka rozvahy', '', 'Položka výkazu zisku a ztráty']
    
def toto_je_podzáhlaví_tabulky(řádek,  číslo_účtu,  jméno):
#    print('toto_je_podzáhlaví_tabulky: ',  řádek)
    assert řádek == ['', 'Aktiva', 'Pasiva']
    
def toto_je_účtová_třída(řádek,  číslo_účtu,  jméno):
    
    kontroluji_pořadí_účtové_třídy(číslo_účtu)
    
    assert len(řádek) == 1
    
    CREATE('n_{}:{} {}'.format(číslo_účtu,  labels(ÚČTOVÁ_TŔÍDA,  ÚČTOVÁ_OSNOVA),  vlastnosti(číslo = číslo_účtu,  jméno = jméno)))
    CREATE('(uctova_osnova)-[{}]->(n_{})'.format(ÚČTOVÁ_OSNOVA_MÁ_TŘÍDU,  číslo_účtu))
    
    
def toto_je_účtová_třída_8_a_9(řádek,  číslo_účtu,  jméno):
    
    toto_je_účtová_třída(řádek,  8,  jméno)
    toto_je_účtová_třída(řádek,  9,  jméno)
    


def toto_je_účtová_skupina(řádek,  číslo_účtu,  jméno):
    
    assert len(řádek) == 1
    
    CREATE('n_{}:{} {}'.format(číslo_účtu,  labels(ÚČTOVÁ_SKUPINA,  ÚČTOVÁ_OSNOVA),  vlastnosti(číslo = číslo_účtu,  jméno = jméno)))
    
#    (n)-[:LOVES {since: {value}}]->(m)
    CREATE('(n_{})-[{}]->(n_{})'.format(číslo_účtu[:-1],  ÚČTOVÁ_TŘÍDA_MÁ_SKUPINU,  číslo_účtu))
    
def toto_je_soupis_skupin_7x(řádek,  číslo_účtu,  jméno):
    
    assert len(řádek) == 1
    
def toto_je_účet(řádek,  číslo_účtu,  jméno):
    
    CREATE('n_{}:{} {}'.format(číslo_účtu,  labels(ÚČET,  ÚČTOVÁ_OSNOVA),  vlastnosti(číslo = číslo_účtu,  jméno = jméno)))
    
    CREATE('(n_{})-[{}]->(n_{})'.format(číslo_účtu[:-1],  ÚČTOVÁ_SKUPINA_MÁ_ÚČET,  číslo_účtu))
    


parsovací_funkce = {re.compile(r'^Název účtu'): toto_je_záhlaví_tabulky, 
                            re.compile(r'^$'): toto_je_podzáhlaví_tabulky, 
                                re.compile(r'^ÚČTOVÁ\s+TŘÍDA\s+(?P<czislo>[0-9])[ \t]-[ \t](?P<jmeno>.+)'): toto_je_účtová_třída, 
                                re.compile(r'^(?P<czislo>[0-9]{2})x?[ \t]-[ \t](?P<jmeno>.+)'): toto_je_účtová_skupina, 
                              re.compile(r'^(?P<czislo>[0-9]{3})[ \t]-[ \t](?P<jmeno>.+)'): toto_je_účet , 
                              re.compile(r'^ÚČTOVÉ\s+TŘÍDY\s+(?P<czislo>[0-9]) A 9[ \t]-[ \t](?P<jmeno>.+)'): toto_je_účtová_třída_8_a_9, 
                              re.compile(r'^(?P<czislo>[0-9]{2}) až 79[ \t]-[ \t](?P<jmeno>.+)'): toto_je_soupis_skupin_7x 
                                }

def kontroluji_pořadí_účtové_třídy(číslo_účtu):
    if not kontroluji_pořadí_účtové_třídy.číslo_třídy == int(číslo_účtu):
        raise ValueError('Chyba pořadí účtové třídy, očekávám {} ale číslo je {}'.format(kontroluji_pořadí_účtové_třídy.číslo_třídy, číslo_účtu))
        
    kontroluji_pořadí_účtové_třídy.číslo_třídy = kontroluji_pořadí_účtové_třídy.číslo_třídy + 1

kontroluji_pořadí_účtové_třídy.číslo_třídy = 0

def parsuji_zachycené(regex_zachyceno):
    
    try:
        číslo_účtu,  jméno = regex_zachyceno.group('czislo',  'jmeno')
        return číslo_účtu,  jméno
    except IndexError:
        return None,  None

def main():
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
                funkce(řádek,  *parsuji_zachycené(zachyceno))
                break
        else:
            raise ValueError('Neumím zpracovat tento řádek: "{}"'.format(' | '.join(řádek)))
            
    print(CREATE)
        
def csv_účetní_osnova():
    
    with open('jak_se-dělají_výkazy_účty.csv',  mode='r',  encoding='utf-8') as soubor:
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
    
    parser.add_argument('--data',  action='store_true')
    parser.add_argument('--indexy',  action='store_true')
    
    #    a včíl to možu rozparsovat
    args = parser.parse_args()
    
#    print('soubor',  args.soubor)

    if args.data:
        main()
        
    if args.indexy:
        příkazy = [
    
        'CREATE INDEX ON :{}(`číslo`)'.format(ÚČTOVÁ_TŔÍDA), 
        'CREATE INDEX ON :{}(`jméno`)'.format(ÚČTOVÁ_TŔÍDA),
        'CREATE INDEX ON :{}(`číslo`)'.format(ÚČTOVÁ_SKUPINA), 
        'CREATE INDEX ON :{}(`jméno`)'.format(ÚČTOVÁ_SKUPINA),
        'CREATE INDEX ON :{}(`číslo`)'.format(ÚČET), 
        'CREATE INDEX ON :{}(`jméno`)'.format(ÚČET)
        ]
        
        print(';\n'.join(příkazy) + ';')
