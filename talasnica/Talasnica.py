#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je třída, která ...
'''

from talasnica.csv_data import data_z_csv,  info_z_csv,  Datum
import datetime,  pytz

from talasnica.konstanty import (
                                 OPEN_TIME, 
                                 OPEN,  HIGHT,  LOW,  CLOSE, 
                                 HORE,  DOLE, 
                                 VELIKOST,  ČAS_OTEVŘENÍ,  ČAS_ZAVŘENÍ,  
                                 OTEVÍRACÍ_CENA,  ZAVÍRACÍ_CENA, 
                                 SMÉR, 
                                 ZNAMÉNKO_SMÉRU
                                 )
#,  SWAP,  ULOŽENÝ_ZISK


def upravím_data_ceny_na_int(data,  mocnitel):
    data[OPEN] = cena_na_int(data[OPEN],  mocnitel)
    data[HIGHT] = cena_na_int(data[HIGHT] ,  mocnitel) 
    data[LOW] = cena_na_int(data[LOW],  mocnitel ) 
    data[CLOSE] = cena_na_int(data[CLOSE] ,  mocnitel) 
        
def cena_na_int(cena,  mocnitel):
    return int(cena * 10 ** mocnitel)
    
#def int_na_cenu(hodnota,  point):
#    return hodnota  * point
        


class __generátor_obchodů(object):
    def __init__(self,  start,  rozestup):
        self.start = start
        self.čekaná = start
        self.rozestup = rozestup

class generátor_býků(__generátor_obchodů):
#    směr = HORE
#    znaménko_směru = 1
    def __call__(self,  k_ceně):
        while k_ceně > self.čekaná:
            yield self.čekaná
            self.čekaná = self.čekaná + self.rozestup
            
class generátor_medvědů(__generátor_obchodů):
#    směr = DOLE
#    znaménko_směru = -1
    def __call__(self, k_ceně):
        while k_ceně < self.čekaná:
            yield self.čekaná
            self.čekaná = self.čekaná - self.rozestup

class seznam_obchodů(object):
    
    def __init__(self,  směr):
        self.směr = směr
        
        self.obchody = {}
        self.cena = 0
        self.velikost = 0
        
    def __call__(self,  čas,  cena,  velikost):
        if not cena in self.obchody:
            self.obchody[cena] = {SMÉR: self.směr,  VELIKOST: velikost,  ČAS_OTEVŘENÍ: čas,  OTEVÍRACÍ_CENA: cena}
            čitatel = self.velikost * self.cena + velikost * cena
            jmenovatel = self.velikost + velikost
            cena = čitatel / jmenovatel
            self.velikost = round(jmenovatel,  2)
            self.cena = int(cena)
      
    def __len__(self):
        return len(self.obchody)
  
    def __str__(self):
        return "cena {} velikost {}".format(self.cena,  self.velikost)
        
    def profit(self, od_ceny):
        return (od_ceny - self.cena) * self.velikost * ZNAMÉNKO_SMÉRU[self.směr]
        
    def zavři_vše(self, čas,  cena,  filtr = None):
        
        smazané_obchody = []
        smazané_klíče = []
        
        for klíč,  obchod in self.obchody.items():
            if callable(filtr):
                if not filtr(obchod):
                    continue
            obchod[ČAS_ZAVŘENÍ] = čas
            obchod[ZAVÍRACÍ_CENA] = cena
            smazané_obchody.append(obchod)
            smazané_klíče.append(klíč)
        
        for klíč in smazané_klíče:
            del self.obchody[klíč]
        
        self.cena = 0
        self.velikost = 0
        čitatel = 0
        jmenovatel = 0
        
        for zůstavší in self.obchody:
            čitatel = čitatel + zůstavší[VELIKOST] * zůstavší[OTEVÍRACÍ_CENA]
            jmenovatel = jmenovatel + zůstavší[VELIKOST]
            
        if jmenovatel > 0:
            cena = čitatel / jmenovatel
            self.velikost = round(jmenovatel,  2)
            self.cena = int(cena)
        
        return smazané_obchody


class Talasnica(object):
    
    obchody = {}
#    maximum = None
#    minimum = None
#    ohrada = None
    
    def __init__(self):
        self.info = None
        self.data = None
        
#        generátory nových pozic
        self.býčiště = None
        self.medvědiště = None
        
        self.obchody = {HORE: seznam_obchodů(směr = HORE),  DOLE: seznam_obchodů(směr = DOLE)}
        self.uzavřené_obchody = []
        self.uložený_zisk = 0
        self.swap = 0
        self.znamení_setby = None
        self.znamení_sklizně = None
        
#         při otevření svíce potřebuji profit pouze z obchodů, které byly otevřeny nejpopzději na předchozí svíci
#          při exportu s evšak k takové hodnotě nemohu dostat, neboť získávám až data s nově otevřenými obchody
#       proto si ten profit spočtu a uložím při započetí průchoud
        self.profit_při_otevření = None
        self.swap = 0.0
        self.__swapovací_den = None
        
    
    def __call__(self,  csv_soubor,  parametry = None):
        
        self.info = info_z_csv(csv_soubor)
        
        if parametry is not None:
            if isinstance(parametry,  dict):
                self.info.update(parametry)
            else:
                raise ValueError('Parametry musí být slovníkem a nikolivěk {}'. format(type(parametry)))
        
        for data in data_z_csv(csv_soubor):
            
            upravím_data_ceny_na_int(data,  self.info['DIGITS'])
            
            if data['OPEN'] == 0:
                continue
                
#            print('-' * 44)
#            print('BAR {} {}'.format(data['BAR'],  data['OPEN TIME']))
            
            self.data = data
            self.profit_při_otevření = self.profit(self.data['OPEN'])
            self.__přepočítám_swap()
            
            self.znamení_sklizně = self.__imam_znameni_ke_sklizni()
#            assert self.znamení_sklizně == data['znamení sklizně']
            
#            sklizeň
            if self.znamení_sklizně is True:
                if self.profit_při_otevření  + self.swap > self.info['sklízím při zisku']:
                    self.__zavřu_vše_při_otevření_svíce()
            
            
            self.znamení_setby = self.__da_li_třeba_zaset()
#            print('znamení_setby = ',  self.znamení_setby)
            
#            if self.maximum is None:
#                self.maximum = data[HIGHT]
#            else:
#                self.maximum = max(self.maximum,  data[HIGHT])
#                
#            if self.minimum is None:
#                self.minimum = data[LOW]
#            else:
#                self.minimum = max(self.minimum,  data[LOW])
                
            if self.znamení_setby is True:
#                vytáhnu z info
                odstup = self.info['odstup']
                rozestup = self.info['rozestup']
                spred = self.info['SPRED']
#                dosadím a spočítám
#                self.ohrada = {HORE: data[OPEN] + odstup + spred,  DOLE: data[OPEN] - odstup}
                self.medvědiště = generátor_medvědů(start = data[OPEN] - odstup,  rozestup = rozestup)
                self.býčiště = generátor_býků(start = data[OPEN] + odstup + spred, rozestup = rozestup)
                
            for čekaná,  směr,  klíč,  spred in (self.býčiště,  HORE,  HIGHT,  self.info['SPRED']),  (self.medvědiště,  DOLE,  LOW,  0):
                if čekaná is not None:
                    k_ceně = data[klíč] + spred
                    for nová_cena in čekaná(k_ceně):
                        #                    GAP
                        if (nová_cena - data[OPEN]) * ZNAMÉNKO_SMÉRU[směr] < 0:
                            obchod = {SMÉR: směr, 
                                      VELIKOST: self.info['sázím loty'], 
                                      ČAS_OTEVŘENÍ: Datum(0), 
                                      OTEVÍRACÍ_CENA: 0, 
                                      ČAS_ZAVŘENÍ: self.data['OPEN TIME'], 
                                      ZAVÍRACÍ_CENA: nová_cena
                                      }
                            self.uzavřené_obchody.append(obchod)
                
                        else:
                            self.obchody[směr](cena = nová_cena,  velikost = self.info['sázím loty'],  čas = self.data['OPEN TIME'])
#                        print('nový obchod z ' + směr,  nová_cena,  čekaná)
            
            yield self
            

    def __imam_znameni_ke_sklizni(self):
        return True
        
    def __da_li_třeba_zaset(self):

        if self.data['OPEN TIME'].datum < datetime.datetime(
                                                        year = 2010,
                                                        month = 4,
                                                        day = 9,
                                                        hour=10,
                                                        minute=0,
                                                        tzinfo = pytz.UTC
                                                        ):
#            print(self.data['OPEN TIME'])
            #print('neseju bo není správný čas')
            return False

        if self.medvědiště is None and self.býčiště is None:
            #print('seju bo {} + {} == 0'.format(self.čekaná[BUY],  self.čekaná[SELL]))
            return True
            
        #print('neseju bo {} + {} != 0'.format(self.čekaná[BUY],  self.čekaná[SELL]))
        return False
        
        
    def __přepočítám_swap(self,  *args):

        vcilkajsi_den = self.data['OPEN TIME'].datum.day

        if not self.__swapovací_den == vcilkajsi_den:
            
            if self.data['OPEN TIME'].datum.isoweekday() == 3:
                násobek = 3
            else:
                násobek = 1
                
            for hore_dole,  info_klíč in {HORE: 'býčí swap',  DOLE: 'medvědí swap'}.items():
                swap = násobek * self.info[info_klíč] * self.obchody[hore_dole].velikost
                self.swap = self.swap + swap

            self.__swapovací_den = vcilkajsi_den


    def profit(self,  při_ceně):
        profit_býků = self.obchody[HORE].profit(při_ceně)
        profit_medvědů = self.obchody[DOLE].profit(při_ceně + self.info['SPRED'])
        
        return (profit_býků + profit_medvědů) * self.info['TICKVALUE'] 

    def __zavřu_vše_při_otevření_svíce(self):
        
        self.uložený_zisk = self.uložený_zisk + self.profit(self.data['OPEN'])
        
        for hore_dole,  spred in (HORE,  0),  (DOLE,  self.info['SPRED']):
            čas = self.data['OPEN TIME']
            cena = self.data['OPEN'] + spred
            zavřelo_se = self.obchody[hore_dole].zavři_vše(čas,  cena,  filtr = None)
            self.uzavřené_obchody.extend(zavřelo_se)
            
        self.medvědiště = None
        self.býčiště = None

if __name__ == '__main__':
    from talasnica.testuji_talasnicu import csv_soubor
    talasnica = Talasnica()
    for data in talasnica(csv_soubor):
        continue
