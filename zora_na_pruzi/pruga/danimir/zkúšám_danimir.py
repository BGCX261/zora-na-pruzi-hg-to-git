#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který ...
'''

from pruga.pohunci.logování.termcolor.termcolor import cprint

from pruga.danimir import databáze


def zkúšám_připojení(soubor_příkazů):
    '''
    zahájí běh programu
    '''
    
    from pruga.danimir.připojení import testovací_databáze
    from pruga.danimir.příkazy import SELECT,  INSERT,  UPDATE
    
    db = databáze(testovací_databáze)
    
    tabulka = db.první_tabulka
    print('tabulka',  tabulka,  type(tabulka))
    
    x = 2
    
    with open(file = soubor_příkazů,  encoding='utf8',  mode='r') as soubor:
        for řádek in soubor:
            cprint("\n" + '-'*45,  color='green')
            cprint(řádek,  color='green')
            try:
                příkaz = eval(řádek)
                cprint(příkaz,  color='magenta')
#                cprint(příkaz(),  color='blue')
#                příkaz(db)
                cprint(type(příkaz),  color='grey')
            except (TypeError,  ValueError) as e:
                cprint(e,  color = 'red')
                cprint(type(e),  color='grey')
            finally:
                cprint('-'*45 + "\n",  color='green')
         
    
def vytvořím_testy(soubor_příkazů):
    '''
    zahájí běh programu
    '''
    
    from pruga.danimir.připojení import testovací_databáze
    from pruga.danimir.příkazy import SELECT,  INSERT,  UPDATE
    
    db = databáze(testovací_databáze)
    
    tabulka = db.první_tabulka
    
    x = 2
    
    with open(file = soubor_příkazů,  encoding='utf8',  mode='r') as soubor:
        for číslo_testu,  řádek in enumerate(soubor):
            try:
                
                if řádek.startswith('SELECT'):
                    print('def test_{}_SELECT_ (self):'.format(str(číslo_testu).zfill(4)))
                elif řádek.startswith('INSERT'):
                    print('def test_{}_INSERT_ (self):'.format(str(číslo_testu).zfill(4)))
                elif řádek.startswith('UPDATE'):
                    print('def test_{}_UPDATE_ (self):'.format(str(číslo_testu).zfill(4)))
                elif řádek.startswith('DELETE'):
                    print('def test_{}_DELETE_ (self):'.format(str(číslo_testu).zfill(4)))
                    
                print('\tdef příkaz():')
                print('\t\treturn str({})'.format(řádek.strip())) 
                
                příkaz = eval(řádek)
                
                print("\tmá_být = '''\n{}\n'''".format(příkaz()))
                print("\tvrátilo_sa = příkaz()")
                print('\tself.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))')
             
            except (TypeError,  ValueError) as e:
                if isinstance(e,  ValueError):
                    print("\tself.assertRaises(ValueError, příkaz)")
                if isinstance(e,  TypeError):
                    print("\tself.assertRaises(TypeError, příkaz)")

            print('\n')
            
if __name__ == '__main__':

#    print(__doc__)

    

    soubor_příkazů = 'zkúšám_danimír_eval.py'
    soubor_příkazů = 'zkúšám_danimír_hstore_eval.py'
    zkúšám_připojení(soubor_příkazů)
#    vytvořím_testy(soubor_příkazů)




