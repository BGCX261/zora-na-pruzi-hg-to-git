#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je třída, která umožní přístup k databázi
'''

import types
import postgresql

from .prvky_databáze.tabulka_databáze import tabulka_databáze

from .příkazy.select import SELECT

class databáze(object):
    
#    TODO: připojení zadávám předáním modulu s parametry, doplnit předávání i dalšími způsoby (přímo parametry připojení, url řetězec, ...)
    
    def __init__(self,  připojení,  schéma = None,  *argv,  **kwargs):
       
        jména_parametrů = {'host': 'SERVER', 
                                            'port': 'PORT',
                                            'user': 'UŽIVATEL', 
                                            'password': 'HESLO_UŽIVATELE', 
                                            'database': 'JMÉNO_DATABÁZE'
                                            }
        parametry = {}
       
        if isinstance(připojení,  types.ModuleType):
#            print('připojení získám z modulu {}'.format(připojení))
            for parametr,  uložen_jako in  jména_parametrů.items():
                if hasattr(připojení,  uložen_jako):
                    parametry[parametr] = getattr(připojení,  uložen_jako)

#            print('parametry připojení {}'.format(parametry))
#            self.__ovladač = postgresql.open(**parametry)
            db = postgresql.open(**parametry)
        elif isinstance(připojení,  postgresql.driver.pq3.Connection):
            db = připojení
        else:
            raise ValueError('Neznám připojení k databázi')
#        else:
#            db = postgresql.open(**kwargs)

        self.__dict__['_databáze__ovladač'] = db
        self.__dict__['_databáze__schéma'] = schéma

            
    def __call__(self,  příkaz):
        
        if not isinstance(příkaz,  SELECT):
            return self.__ovladač.execute(str(příkaz))  
            

        from .výsledky.objektový_přístup_k_výsledku import objektový_přístup_k_výsledku
        
#        print(self.__ovladač,  type(self.__ovladač))
        pitanje = self.__ovladač.prepare(str(příkaz))
        
        
        return objektový_přístup_k_výsledku(pitanje)
          
        
    def __getattr__(self,  jméno):
#        print('volám databáze __getattr__(self,  jméno)',  jméno)
        return tabulka_databáze(jméno,  schéma = self.__schéma)

    def __getitem__(self,  klíč):
        '''
        Toto je podpora pro schémata
        '''
        return databáze(připojení = self.__ovladač,  schéma = klíč)
        
        
#        
#    def __setattr__(self,  jméno,  hodnota):
#        print('volám databáze __setattr__(self,  jméno, hodnota)',  jméno,  hodnota)
#        self.__dict__[jméno] = hodnota
      
    def set_schema(self,  *args):
        příkaz = 'SET search_path TO {}'.format(','.join(args))
#        print(příkaz)
        self.__ovladač.execute(příkaz)
