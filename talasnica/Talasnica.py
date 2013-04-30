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
                                 ZNAMÉNKO_SMÉRU, 
                                 JMÉNO_GRAFU
                                 )
#,  SWAP,  ULOŽENÝ_ZISK


class __generátor_obchodů(object):
    
    def __init__(self,  start,  rozestup):
        if self.start is None:
            raise ValueError('Nema start')
        self.čekaná = self.start
        self.rozestup = rozestup

class generátor_býků(__generátor_obchodů):
#    směr = HORE
#    znaménko_směru = ZNAMÉNKO_SMÉRU[HORE]

    def __init__(self,  start,  odstup,  rozestup):
        self.start = start.nákup + odstup
        super().__init__(start,  rozestup)

    def __call__(self,  k_ceně):
        while k_ceně.nákup > self.čekaná:
            yield self.čekaná
            self.čekaná = self.čekaná + self.rozestup
            
    def __lt__(self,  k_ceně):
        return self.čekaná > 0 and self.čekaná < k_ceně.nákup
            
class generátor_medvědů(__generátor_obchodů):
#    směr = DOLE
#    znaménko_směru = ZNAMÉNKO_SMÉRU[DOLE]

    def __init__(self,  start,  odstup,  rozestup):
        self.start = start.prodej - odstup
        super().__init__(start,  rozestup)

    def __call__(self, k_ceně):
        while k_ceně.prodej < self.čekaná:
            yield self.čekaná
            self.čekaná = self.čekaná - self.rozestup
            
    def __lt__(self,  k_ceně):
        return self.čekaná > k_ceně.prodej

def upravím_data_ceny_na_int(data,  davaj_cenu):
    for klíč in OPEN,  HIGHT,  LOW,  CLOSE:
        cena = data[klíč]
        if cena is None or cena == 0:
            data[klíč] = None
        else:
            data[klíč] = davaj_cenu(cena,  cena_na_int = True)
    
def davaj_cenu(spred,  přesnost,  point):

    class Cena(object):
        
        def __init__(self,  prodej,  nákup = None,  cena_na_int = None):
            
            if cena_na_int is not None:
                prodej = int(prodej * 10 ** přesnost)
                if nákup is not None:
                    nákup = int(nákup * 10 ** přesnost)
            
            if nákup is None:
                self.nákup = prodej + spred
            else:
                self.nákup = nákup
                
            self.prodej = prodej
            
        def __str__(self):
            return 'nákup {1:.{0}f}, prodej {2:.{0}f}, spred {3:.{0}f}'.format(přesnost,  self.nákup * point,  self.prodej * point,  self.spred * point)
            
        @property
        def spred(self):
            return self.nákup - self.prodej
            
        def __add__(self,  posun_ceny):
            if isinstance(posun_ceny,  int):
                self.prodej = self.prodej + posun_ceny
                self.nákup = self.nákup + posun_ceny
                return self
                
                raise TypeError('TypeError: nepodporuji operátor sčítání {} + {}'.format(type(self),  type(posun_ceny)))
                
        def __sub__(self,  posun_ceny):
            if isinstance(posun_ceny,  int):
                self.prodej = self.prodej - posun_ceny
                self.nákup = self.nákup - posun_ceny
                return self
                
                raise TypeError('TypeError: nepodporuji operátor sčítání {} + {}'.format(type(self),  type(posun_ceny)))
                
            
    return Cena

class Obchod(object):
    
    def __init__(self,  cena,  velikost,  čas_otevření = None):
        
        if not isinstance(cena,  int):
            raise TypeError('Cena je {}'.format(type(cena)))
        
        self.cena_otevření = cena
        
        self.cena_zavření = None
        self.velikost = velikost
        self.čas_otevření = čas_otevření
        self.čas_zavření = None
        self.swap = 0
        
        
    def zavřu(self,  čas,  cena):
        if not isinstance(cena,  int):
            raise TypeError('Cena je {}'.format(type(cena)))
        self.cena_zavření = cena
        self.čas_zavření = čas
            
    def __call__(self):
        return 
        
    def __str__(self):
        return "směr {} cena otevření {} velikost {} čas otevření {} čas zavření {}".format(self.směr,  self.cena_otevření,  self.velikost,  self.čas_otevření,  self.čas_zavření)
        
    def __radd__(self,  další_obchod):
        if další_obchod is None:
            return type(self)(self.cena_otevření,  self.velikost,  self.čas_otevření)
            
        raise TypeError('TypeError: nepodporuji operátor sčítání {} + {}'.format(type(další_obchod),  type(self)))
        
    def __add__(self,  další_obchod):
            if další_obchod is None:
                return self
                
            if isinstance(další_obchod,  type(self)):
                čitatel = self.velikost * self.cena_otevření + další_obchod.velikost * další_obchod.cena_otevření
                jmenovatel = self.velikost + další_obchod.velikost
                cena = čitatel / jmenovatel
                self.velikost = round(jmenovatel,  2)
                self.cena_otevření = int(cena)
                return self
                
            raise TypeError('TypeError: nepodporuji operátor sčítání {} + {}'.format(type(další_obchod),  type(self)))
        
    @property
    def otevřeno(self):
        return self.čas_otevření is not None and self.čas_zavření is None

class Býk(Obchod):
    směr = HORE
    
class Medvěd(Obchod):
    směr = DOLE


class Seznam_obchodů(object):
    
    def __init__(self):
            
        self.obchod = None
        
        self.obchody = {}
        self._swap = None
        
#        self.cena = 0
#        self.velikost = 0
        
    def __call__(self,  čas,  cena,  velikost):
        if not cena in self.obchody:
            obchod = self.TŘÍDA_OBCHODŮ(cena = cena,  velikost = velikost,  čas_otevření = čas)
            
#            self.obchody[cena] = {SMÉR: self.směr,  VELIKOST: velikost,  ČAS_OTEVŘENÍ: čas,  OTEVÍRACÍ_CENA: cena}
            self.obchody[obchod.cena_otevření] = obchod
            
#            print(obchod)
            self.obchod = self.obchod + obchod
                
#            čitatel = self.velikost * self.cena + velikost * cena
#            jmenovatel = self.velikost + velikost
#            cena = čitatel / jmenovatel
#            self.velikost = round(jmenovatel,  2)
#            self.cena = int(cena)
      
    def swapuji(self,  swap_za_lot):
        for obchod in self.obchody.values():
            if obchod.otevřeno is True:
                swap = swap_za_lot * obchod.velikost
                obchod.swap = obchod.swap + swap
                self._swap = self._swap + swap
      
    @property
    def cena(self):
        if self.obchod is None:
            return 0
            
        return self.obchod.cena_otevření
        
    @property
    def velikost(self):
        if self.obchod is None:
            return 0
        return self.obchod.velikost
        
    @property
    def swap(self):
        if self._swap is None:
            self._swap = 0
            for obchod in self.obchody.values():
                self._swap = self._swap + obchod.swap
            
        return self._swap
        
    def __len__(self):
        return len(self.obchody)
  
    def __str__(self):
        return "směr {} cena {} velikost {}".format(self.směr,  self.cena,  self.velikost)
        
    def zavři_vše(self, čas,  cena,  filtr = None):
        
        smazané_obchody = []
        smazané_klíče = []
        
        for klíč,  obchod in self.obchody.items():
            if callable(filtr):
                if not filtr(obchod):
                    continue
#            obchod[ČAS_ZAVŘENÍ] = čas
#            obchod[ZAVÍRACÍ_CENA] = cena
            obchod.zavřu(čas,  cena)
            smazané_obchody.append(obchod)
            smazané_klíče.append(klíč)
        
        for klíč in smazané_klíče:
            del self.obchody[klíč]
        
#        self.cena = 0
#        self.velikost = 0
#        čitatel = 0
#        jmenovatel = 0
        self.obchod = None
        
        for zůstavší in self.obchody:
            self.obchod = self.obchod + zůstavší
#            čitatel = čitatel + zůstavší[VELIKOST] * zůstavší[OTEVÍRACÍ_CENA]
#            jmenovatel = jmenovatel + zůstavší[VELIKOST]
#            
#        if jmenovatel > 0:
#            cena = čitatel / jmenovatel
#            self.velikost = round(jmenovatel,  2)
#            self.cena = int(cena)
        
        return smazané_obchody


class Seznam_býků(Seznam_obchodů):
    TŘÍDA_OBCHODŮ = Býk
    
    def profit(self, od_ceny):
        if self.obchod is None:
            return 0
        return (od_ceny.prodej - self.cena) * self.velikost
    
class Seznam_Medvědů(Seznam_obchodů):
    TŘÍDA_OBCHODŮ = Medvěd
    
    def profit(self, od_ceny):
        if self.obchod is None:
            return 0
        return (self.cena - od_ceny.nákup) * self.velikost

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
        
        self.obchody = {HORE: Seznam_býků(),  DOLE: Seznam_Medvědů()}
        self.uzavřené_obchody = []
        self.uložený_zisk = 0
        self.znamení_setby = None
        self.znamení_sklizně = None
        
#         při otevření svíce potřebuji profit pouze z obchodů, které byly otevřeny nejpopzději na předchozí svíci
#          při exportu s evšak k takové hodnotě nemohu dostat, neboť získávám až data s nově otevřenými obchody
#       proto si ten profit spočtu a uložím při započetí průchoud
        self.profit_při_otevření = None
        self.__swapovací_den = None
        
        self.počáteční_čas = None
        self.konečný_čas = None
        self.samoj_bolšoj_profit = [None,  None]
        self.samoj_bolšoj_zisk = [None,  None]
        self.samaja_bolšaja_velikost = {HORE: None,  DOLE: None}
        self.samoj_bolšoj_býk = None
        self.samoj_bolšoj_medvěd = None
        self.počet_svíček = None
        
    
    def __call__(self,  csv_soubor,  parametry = None):
        
        self.info = info_z_csv(csv_soubor)
        třída_ceny = davaj_cenu(spred = self.info['SPRED'],  přesnost = self.info['DIGITS'],  point = self.info['POINT'])
        
        if parametry is not None:
            if isinstance(parametry,  dict):
                self.info.update(parametry)
            else:
                raise ValueError('Parametry musí být slovníkem a nikolivěk {}'. format(type(parametry)))
        
        for data in data_z_csv(csv_soubor):
            
            upravím_data_ceny_na_int(data,  třída_ceny)
            
            if data['OPEN'] is None:
                print('Přeskakuji svíčku {} koja nemá ceny'.format(data['BAR']))
                continue
                
#            print(data['OPEN'])
                
#            print('-' * 44)
#            print('BAR {} {}'.format(data['BAR'],  data['OPEN TIME']))

            if self.počáteční_čas is None:
                self.počáteční_čas = data['OPEN TIME']
                
            if self.počet_svíček is None:
                self.počet_svíček = data['BAR']
                
            self.konečný_čas = data['OPEN TIME']
            
            self.data = data
            self.profit_při_otevření = self.profit(self.data['OPEN'])
            self.__přepočítám_swap()
            
            self.samoj_bolšoj_profit = [max(self.samoj_bolšoj_profit[0] or 0,  self.profit_při_otevření),  min(self.samoj_bolšoj_profit[1] or 0,  self.profit_při_otevření)]
            self.samoj_bolšoj_zisk = [max(self.samoj_bolšoj_zisk[0] or 0,  self.profit_při_otevření + self.uložený_zisk + self.swap),  min(self.samoj_bolšoj_zisk[1] or 0,  self.profit_při_otevření + self.uložený_zisk + self.swap)]
            
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
                self.medvědiště = generátor_medvědů(start = data[OPEN],  odstup = odstup,  rozestup = rozestup)
                self.býčiště = generátor_býků(start = data[OPEN],  odstup = odstup, rozestup = rozestup)
                
            for čekaná,  směr,  klíč in (self.býčiště,  HORE,  HIGHT),  (self.medvědiště,  DOLE,  LOW):
                if čekaná is not None:
                    k_ceně = data[klíč]
                    for nová_cena in čekaná(k_ceně):
                        #                    GAP
#                        if (nová_cena - data[OPEN]) * ZNAMÉNKO_SMÉRU[směr] < 0:
                        if čekaná < data[OPEN]:
                            if směr == HORE:
                                třída = Býk
                            if směr == DOLE:
                                třída = Medvěd
                                
                            obchod = třída(velikost = self.info['sázím loty'],  čas_otevření = Datum(0),  cena = 0)
                            obchod.zavřu(čas = self.data['OPEN TIME'],  cena = nová_cena)
#                            obchod = {SMÉR: směr, 
#                                      VELIKOST: self.info['sázím loty'], 
#                                      ČAS_OTEVŘENÍ: Datum(0), 
#                                      OTEVÍRACÍ_CENA: 0, 
#                                      ČAS_ZAVŘENÍ: self.data['OPEN TIME'], 
#                                      ZAVÍRACÍ_CENA: nová_cena
#                                      }
                            self.uzavřené_obchody.append(obchod)
                
                        else:
                            self.obchody[směr](cena = nová_cena,  velikost = self.info['sázím loty'],  čas = self.data['OPEN TIME'])
#                        print('nový obchod z ' + směr,  nová_cena,  čekaná)
            
            
            self.samoj_bolšoj_býk = max(self.samoj_bolšoj_býk or 0, self.obchody[HORE].velikost )
            self.samoj_bolšoj_medvěd = max(self.samoj_bolšoj_medvěd or 0,  self.obchody[DOLE].velikost)
            
            pozice = self.obchody[HORE].velikost - self.obchody[DOLE].velikost
            self.samaja_bolšaja_velikost[HORE] = max(self.samaja_bolšaja_velikost[HORE] or 0,  pozice)
            self.samaja_bolšaja_velikost[DOLE] = min(self.samaja_bolšaja_velikost[DOLE] or 0,  pozice)
            
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
                swap = násobek * self.info[info_klíč]
                self.obchody[hore_dole].swapuji(swap)

            self.__swapovací_den = vcilkajsi_den
            
    @property
    def swap(self):
        return self.obchody[HORE].swap + self.obchody[DOLE].swap


    def profit(self,  při_ceně):
        profit_býků = self.obchody[HORE].profit(při_ceně)
        profit_medvědů = self.obchody[DOLE].profit(při_ceně)
        
        return (profit_býků + profit_medvědů) * self.info['TICKVALUE'] 

    def __zavřu_vše_při_otevření_svíce(self):
        
        self.uložený_zisk = self.uložený_zisk + self.profit(self.data['OPEN'])
        
        for hore_dole in HORE,  DOLE:
            čas = self.data['OPEN TIME']
            cena = self.data['OPEN']
            if hore_dole == HORE:
                na_ceně = cena.prodej
            if hore_dole == DOLE:
                na_ceně = cena.nákup
            zavřelo_se = self.obchody[hore_dole].zavři_vše(čas,  na_ceně,  filtr = None)
            self.uzavřené_obchody.extend(zavřelo_se)
            
        self.medvědiště = None
        self.býčiště = None
        
        
    def __str__(self):
        import io
        import sys
        import datetime
        
        stdout = sys.stdout
        output_buffer = io.StringIO("")
        # přesměrování
        sys.stdout = output_buffer
        
        print("TALASNICA")
        
        print('symbol {}'.format(self.info['SYMBOL']))
        print('svíčky {} - {}'.format(self.počet_svíček,  self.data['BAR']))
        print('graf {}'.format(JMÉNO_GRAFU[self.info['časový rámec']]))
        
        print('započato {}'.format(self.počáteční_čas))
        print('ukončeno {}'.format(self.konečný_čas))
        print('doba {}'.format(self.konečný_čas.datum - self.počáteční_čas.datum))
        
        print('-'*20)
        
        print('největší býk {:,.2f}'.format(self.samoj_bolšoj_býk).replace(",", " ").replace(".", ","))
        print('největší medvěd {:,.2f}'.format(self.samoj_bolšoj_býk).replace(",", " ").replace(".", ","))
        
        print('největší pozice {:,.2f} a {:,.2f}'.format(self.samaja_bolšaja_velikost[HORE],  self.samaja_bolšaja_velikost[DOLE]).replace(",", " ").replace(".", ","))
        
        print('-'*20)
        
        print('otevřený zisk {1:,.2f} {0} a {2:,.2f} {0}'.format(self.info['měna účtu'],  *self.samoj_bolšoj_profit).replace(",", " ").replace(".", ","))
        print('celkový zisk {1:,.2f} {0} a {2:,.2f} {0}'.format(self.info['měna účtu'],  *self.samoj_bolšoj_zisk).replace(",", " ").replace(".", ","))

        print('-'*20)
        
        print('{:<25}{:>18,.2f}'.format('uložený zisk ',  self.uložený_zisk).replace(",", " ").replace(".", ","))
        print('{:<25}{:>18,.2f}'.format('+ swap',  self.swap).replace(",", " ").replace(".", ","))
        print('{:>25}{:>18,.2f}'.format('= ',  self.uložený_zisk + self.swap).replace(",", " ").replace(".", ","))
        print('{:<25}{:>18,.2f}'.format('+ otevřené pozice ', self.profit_při_otevření).replace(",", " ").replace(".", ","))
        print('{:>25}{:>18,.2f}'.format('= ',  self.uložený_zisk + self.swap + self.profit_při_otevření).replace(",", " ").replace(".", ","))
        
        
        # obnovíme standartní výstup
        sys.stdout = stdout
        return(output_buffer.getvalue())

if __name__ == '__main__':
    from talasnica.testuji_talasnicu import csv_soubor
    talasnica = Talasnica()
    for data in talasnica(csv_soubor):
        continue
