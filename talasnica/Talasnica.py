#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je třída, která ...
'''

from talasnica.csv_data import data_z_csv,  info_z_csv,  Datum
#import datetime,  pytz

from talasnica.konstanty import (
                                  __version__,  
                                 BAR, 
                                 OPEN_TIME, 
                                 OPEN,  HIGHT,  LOW,  CLOSE, 
                                 HORE,  DOLE, 
                                 JMÉNO_GRAFU, 
                                 PROFIT_OPEN,  PROFIT_HORE,  PROFIT_DOLE,  PROFIT_CLOSE, 
                                 BB_MAIN,  BB_HORE,  BB_DOLE,  PSAR
                                 )
from talasnica.funkce import ( 
                                PŘESNOST_CENY, 
                                 PŘESNOST_LOTU, 
                                 PŘESNOST_PŘEPOČTU_PROFITU, 
                                 max_nákupu,  min_prodeje
                                 )

from talasnica.AOS.Statistika import Statistika


class __generátor_obchodů(object):
    
    def __init__(self,  start,  rozestup):
        if self.start is None:
            raise ValueError('Nema start')
        self.čekaná = self.start
        self.rozestup = rozestup

class generátor_býků(__generátor_obchodů):
    směrem = HORE
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
        
    def přitáhni_k_ceně(self,  k_ceně):
#        print("přitáhnu býčí start", self.start,  "ku",  k_ceně.nákup)
        if k_ceně.nákup < self.start:
            while self.start > k_ceně.nákup:
                self.start = self.start - self.rozestup
#                print(self.start)
            self.start = self.start + self.rozestup
#            print("přitaženo na",  self.start)
            self.čekaná = self.start
            
class generátor_medvědů(__generátor_obchodů):
    směrem = DOLE
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
        
    def přitáhni_k_ceně(self,  k_ceně):
#        print("přitáhnu medvědí start", self.start,  "ku",  k_ceně.prodej)
        if k_ceně.prodej > self.start:
            while self.start < k_ceně.nákup:
                self.start = self.start + self.rozestup
#                print(self.start)
            self.start = self.start - self.rozestup
#            print("přitaženo na",  self.start)
            self.čekaná = self.start


def davaj_cenu_na_int(spred,  přesnost,  point):
    Třída_ceny = davaj_cenu(spred,  přesnost,  point)
    def cena_na_int(cena):
        cena = int(cena * 10 ** přesnost)
        return Třída_ceny(prodej = cena)
        
    return cena_na_int

def davaj_cenu(spred,  přesnost,  point):

    class Cena(object):
        
        def __init__(self,  prodej,  nákup = None):
            
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
                return Cena(nákup = self.nákup + posun_ceny,  prodej = self.prodej + posun_ceny)
                
                raise TypeError('TypeError: nepodporuji operátor sčítání {} + {}'.format(type(self),  type(posun_ceny)))
                
        def __sub__(self,  posun_ceny):
            if isinstance(posun_ceny,  int):
                return Cena(nákup = self.nákup - posun_ceny,  prodej = self.prodej - posun_ceny)
                
                raise TypeError('TypeError: nepodporuji operátor sčítání {} + {}'.format(type(self),  type(posun_ceny)))
                
            
    return Cena


class Obchod(object):
    
    __počítadlo = 0
    
    def __init__(self,  cena_otevření,  velikost,  čas_otevření = None):
        
        if not isinstance(cena_otevření,  int):
            raise TypeError('Cena je {}'.format(type(cena_otevření)))
        
        Obchod.__počítadlo = Obchod.__počítadlo + 1
        self.tiket = Obchod.__počítadlo
        
        self.cena_otevření = cena_otevření
        
        self.cena_zavření = None
        self.velikost = velikost
        self.čas_otevření = čas_otevření
        self.čas_zavření = Datum(0)
        self.swap = 0
        
        
    def zavřu(self,  čas_zavření,  cena_zavření):
        if not isinstance(cena_zavření,  int):
            raise TypeError('Cena je {}'.format(type(cena_zavření)))
        self.cena_zavření = cena_zavření
        self.čas_zavření = čas_zavření
            
#    def __call__(self):
#        return 
        
    def __str__(self):
        return "#{} směr {} cena otevření {} velikost {} čas otevření {} čas zavření {}".format(self.tiket, self.směr,  self.cena_otevření,  self.velikost,  self.čas_otevření,  self.čas_zavření)
        
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
                self.velikost = PŘESNOST_LOTU(jmenovatel)
                self.cena_otevření = int(cena)
                return self
                
            raise TypeError('TypeError: nepodporuji operátor sčítání {} + {}'.format(type(další_obchod),  type(self)))
        
    @property
    def otevřeno(self):
        return self.čas_otevření > 0 and self.čas_zavření == 0
        
    @property
    def uložený_profit(self):
        if self.otevřeno:
            return 0
            
        return self.profit(self.cena_zavření)
        
    def otevřený_profit(self,  k_ceně):
        if self.otevřeno:
            return self.profit(k_ceně)
            
        return 0

class Býk(Obchod):
    směr = HORE
    
    def profit(self, od_ceny):
        if self.cena_otevření > 0:
            if not isinstance(od_ceny,  (int,  float)):
                od_ceny = od_ceny.prodej
            return PŘESNOST_PŘEPOČTU_PROFITU((od_ceny - self.cena_otevření) * self.velikost)
            
        return 0
        
    
class Medvěd(Obchod):
    směr = DOLE

    def profit(self, od_ceny):
        if self.cena_otevření > 0:
            if not isinstance(od_ceny,  (int,  float)):
                od_ceny = od_ceny.nákup
            return PŘESNOST_PŘEPOČTU_PROFITU((self.cena_otevření - od_ceny) * self.velikost)
            
        return 0
        
        
class Seznam_obchodů(object):
    
    def __init__(self):
            
        self.obchod = None
        
        self.obchody = {}
        self._swap = None
        
#        self.cena = 0
#        self.velikost = 0
        
    def otevřu_nový_obchod(self,  čas_otevření,  cena_otevření,  velikost):
        if not cena_otevření in self.obchody:
            obchod = self.TŘÍDA_OBCHODŮ(cena_otevření = cena_otevření,  velikost = velikost,  čas_otevření = čas_otevření)
            
#            self.obchody[cena] = {SMÉR: self.směr,  VELIKOST: velikost,  ČAS_OTEVŘENÍ: čas,  OTEVÍRACÍ_CENA: cena}
            self.obchody[cena_otevření] = obchod
            
#            print(obchod)
            self.obchod = self.obchod + obchod
            
            print("otevřel jsem",  obchod)
                
#            čitatel = self.velikost * self.cena + velikost * cena
#            jmenovatel = self.velikost + velikost
#            cena = čitatel / jmenovatel
#            self.velikost = PŘESNOST_LOTU(jmenovatel)
#            self.cena = int(cena)
      
    def swapuji(self,  swap_za_lot):
        
        for obchod in self.obchody.values():
            
            if obchod.otevřeno is True:
                swap = swap_za_lot * obchod.velikost
                obchod.swap = PŘESNOST_CENY(obchod.swap + swap)
                self._swap = PŘESNOST_CENY(self._swap + swap)
      
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
        return "směr {} cena {} velikost {}".format(self.TŘÍDA_OBCHODŮ.směr,  self.cena,  self.velikost)
        
    def zavřu_vše(self, čas_zavření,  cena_zavření,  filtr = None):
        
        smazané_obchody = []
        smazané_klíče = []
        
        for klíč,  obchod in self.obchody.items():
            if callable(filtr):
                if not filtr(obchod):
                    continue
#            obchod[ČAS_ZAVŘENÍ] = čas
#            obchod[ZAVÍRACÍ_CENA] = cena
            obchod.zavřu(čas_zavření = čas_zavření,  cena_zavření = cena_zavření)
            smazané_obchody.append(obchod)
            smazané_klíče.append(klíč)
            print("zavřel jsem",  obchod)
        
        for klíč in smazané_klíče:
            del self.obchody[klíč]
        
#        self.cena = 0
#        self.velikost = 0
#        čitatel = 0
#        jmenovatel = 0
        self.obchod = None
        
        for zůstavší in self.obchody.values():
            self.obchod = self.obchod + zůstavší
#            čitatel = čitatel + zůstavší[VELIKOST] * zůstavší[OTEVÍRACÍ_CENA]
#            jmenovatel = jmenovatel + zůstavší[VELIKOST]
#            
#        if jmenovatel > 0:
#            cena = čitatel / jmenovatel
#            self.velikost = PŘESNOST_CENY(jmenovatel)
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


class Celkové_obchodní_postavení(object):
    
    def __init__(self,  info):
        self.info = info
        
        self.__swapovací_den = None
        
        self.býci = Seznam_býků()
        self.medvědi = Seznam_Medvědů()
        self.uzavřené = []
        
 
    def otevřu_nový_obchod(self,  směrem,  čas,  cena,  velikost):
        if směrem == HORE:
            seznam_obchodů = self.býci
        if směrem == DOLE:
            seznam_obchodů = self.medvědi
            
        seznam_obchodů.otevřu_nový_obchod(čas_otevření = čas,  cena_otevření = cena,  velikost = velikost)

    def zruším_obchod_gapem(self,  směrem,  čas,  cena,  velikost):
        
        if směrem == HORE:
            Třída = Býk
        if směrem == DOLE:
            Třída = Medvěd
                            
        obchod = Třída(velikost = velikost,  čas_otevření = Datum(0),  cena_otevření = 0)
        obchod.zavřu(čas_zavření = čas,  cena_zavření = cena)
        print("gap vyřadil",  obchod)
        self.uzavřené.append(obchod)

    def zavřu_obchody(self,  čas_zavření,  cena_zavření,   filtr = None):
        
        zavření_býci = self.býci.zavřu_vše(čas_zavření = čas_zavření,  cena_zavření = cena_zavření.prodej,  filtr = filtr)
        zavření_medvědi = self.medvědi.zavřu_vše(čas_zavření = čas_zavření,  cena_zavření = cena_zavření.nákup, filtr = filtr)
        
        self.uzavřené.extend(zavření_býci)
        self.uzavřené.extend(zavření_medvědi)
        

    def umenším_pozice(self,  čas_zavření,  cena_zavření):
        velikost_býků = self.býci.velikost
        velikost_medvědů = self.medvědi.velikost
        
        abs_velikosti = abs(self.velikost)
        profit_profitujících = 0
        velikost_profitujících = 0
        
        k_zavření = []
        
        if velikost_býků > 0 and velikost_medvědů > 0:
            
            if self.velikost > 0:
                převislé_ceny = sorted(self.býci.obchody.keys())
                převislé = self.býci
                brzdící = self.medvědi
                brzdící_ceny = sorted(self.medvědi.obchody.keys())
            else:
                převislé_ceny = sorted(self.medvědi.obchody.keys(),  reverse = True)
                převislé = self.medvědi
                brzdící = self.býci
                brzdící_ceny = sorted(self.býci.obchody.keys(),  reverse = True)
            
            for cena_převislého in převislé_ceny:
                obchod = převislé.obchody[cena_převislého]
                profit = obchod.profit(cena_zavření)
                if profit < self.info['rozestup'] * obchod.velikost:
                    break
                
                velikost_profitujících = PŘESNOST_LOTU(velikost_profitujících + obchod.velikost)
                
                if not velikost_profitujících < abs_velikosti:
                    break
                    
                profit_profitujících = PŘESNOST_CENY(profit_profitujících + profit)
                k_zavření.append(obchod.tiket)
               
            přetlačeno = profit_profitujících
            přetlačímos = False
            for cena_brzdící in  brzdící_ceny:
                obchod = brzdící.obchody[cena_brzdící]
                profit = obchod.profit(cena_zavření)
                přetlačeno = PŘESNOST_CENY(přetlačeno + profit)
                if not přetlačeno > self.info['rozestup'] * obchod.velikost:
                    break
                    
                k_zavření.append(obchod.tiket)
                přetlačímos = True
                    
            if přetlačímos:
#                print(čas_zavření, "profit profitujících",  profit_profitujících,  ">", přetlačeno, "velikost",  velikost_profitujících, "ku",  velikost_býků, velikost_medvědů, "k zavření",  k_zavření)
                print('-'*44)
                print('sklízím da umenším')
                print(čas_zavření, "profit profitujících",  profit_profitujících,  ">", přetlačeno, "velikost",  velikost_profitujících, "ku",  velikost_býků, velikost_medvědů, "k zavření",  k_zavření)
                
                def filtr(obchod):
                    if obchod.tiket in k_zavření:
                        return True
                    return False
                
                self.zavřu_obchody(čas_zavření = čas_zavření,  cena_zavření = cena_zavření,   filtr = filtr)
#                print("umenšeno jest")
                return True
                
        return False

    @property
    def velikost(self):
        return PŘESNOST_CENY(self.býci.velikost - self.medvědi.velikost)
        
    @property
    def cena(self):
        velikost = self.velikost
        if velikost == 0:
            return int((self.býci.cena + self.medvědi.cena) / 2)
        return int((self.býci.cena * self.býci.velikost - self.medvědi.cena * self.medvědi.velikost) / self.velikost)
        
    @property
    def swap(self):
        return self.býci.swap + self.medvědi.swap

    def swapuji(self,  čas_svíčky):

        vcilkajsi_den = čas_svíčky.datum

        if not self.__swapovací_den == vcilkajsi_den.day:
            
            if vcilkajsi_den.isoweekday() == 3:
                násobek = 3
            else:
                násobek = 1
                
            self.býci.swapuji(násobek * self.info['býčí swap'])
            self.medvědi.swapuji(násobek * self.info['medvědí swap'])

            self.__swapovací_den = vcilkajsi_den.day
            
    def zisk(self,  při_ceně):
        profit_býků = self.býci.profit(při_ceně)
        profit_medvědů = self.medvědi.profit(při_ceně)
        return PŘESNOST_CENY((profit_býků + profit_medvědů) * self.info['TICKVALUE'] )
       
    @property
    def uložený_zisk(self):
        zisk = 0
        for obchod in self.uzavřené:
            zisk = zisk + obchod.profit(obchod.cena_zavření)
            
        return PŘESNOST_CENY(zisk * self.info['TICKVALUE'] )

class Talasnica(object):
    
    __slots__ = ('zdrojové_csv',  'info',  'mapa_tříd',  'obchody',  'data',  'předchozí_data',  'býčiště',  'medvědiště',  'znamení_setby',  'znamení_sklizně',  'statistika')

    
    def __init__(self,  zdrojové_csv,  parametry = None):
        
        self.zdrojové_csv = zdrojové_csv
        self.info = info_z_csv(zdrojové_csv)
        
        dám_cenu_na_int = davaj_cenu_na_int(spred = self.info['SPRED'],  přesnost = self.info['DIGITS'],  point = self.info['POINT'])
        self.mapa_tříd = {}
        for klíč in OPEN,  HIGHT,  LOW,  CLOSE,  BB_MAIN,  BB_HORE,  BB_DOLE,  PSAR:
            self.mapa_tříd[klíč] = dám_cenu_na_int
      
        
        self.obchody = Celkové_obchodní_postavení(info = self.info)
        
        if parametry is not None:
            if isinstance(parametry,  dict):
                self.info.update(parametry)
            else:
                raise ValueError('Parametry musí být slovníkem a nikolivěk {}'. format(type(parametry)))
                
        self.data = None
        self.předchozí_data = None
        
#        generátory nových pozic
        self.býčiště = None
        self.medvědiště = None
        
        self.znamení_setby = None
        self.znamení_sklizně = None
        
        self.statistika = Statistika(talasnica = self)
        
    
    def __iter__(self,  AOSy = []):
        
        první_svíčka = True
        
        for data in data_z_csv(self.zdrojové_csv,  self.mapa_tříd):
            
            if data[OPEN_TIME].timestamp == 0:
                print('Přeskakuji svíčku {} koja nemá otevírací dobu'.format(data[BAR]))
                continue
                
            if data[OPEN].prodej == 0:
                print('Přeskakuji svíčku {} koja nemá ceny'.format(data[BAR]))
                continue
                
            if data[BB_MAIN].prodej == 0:
                print('Přeskakuji svíčku {} koja nemá bb indikátor'.format(data[BAR]))
                continue
                
            self.data = data
            
#            for aos in AOSy:
#                funkce_události = aos.get('pří_otevření_svíčky',  None)
#                if callable(funkce_události):
#                    funkce_události(self)
                
#            print(data[OPEN])
                
#            print('-' * 44)
#            print('BAR {} {}'.format(data['BAR'],  data['OPEN TIME']))

#            print('*'*44)
#            print(data[BAR],  data[OPEN_TIME],  data[OPEN])
#            print('-'*44)


            if první_svíčka is True:
                self.statistika.na_první_svíčce()
                první_svíčka = False
                
                
            self.obchody.swapuji(data[OPEN_TIME])
                
            self.statistika.pří_otevření_svíčky()
            zisk_při_otevření = self.statistika.zisk_při_otevření
            
            self.znamení_sklizně = self.__imam_znameni_ke_sklizni()
            
#            sklizeň
            if self.znamení_sklizně is True:
                if zisk_při_otevření  + self.obchody.swap > self.info['sklízím při zisku']:
                    print('-'*44)
                    print('sklízím při dosažení zisku')
                    self.obchody.zavřu_obchody(čas_zavření = data[OPEN_TIME],  cena_zavření = data[OPEN])
#                    self.medvědiště = None
#                    self.býčiště = None
                else:
                    umenšeno =  self.obchody.umenším_pozice(čas_zavření = data[OPEN_TIME],  cena_zavření = data[OPEN])
#                    if umenšeno:
#                        self.medvědiště.přitáhni_k_ceně(data[OPEN])
#                        self.býčiště.přitáhni_k_ceně(data[OPEN])
                    
            
            
            self.znamení_setby = self.__da_li_třeba_zaset()
                
#            if self.znamení_setby is True:
#                vytáhnu z info
            odstup = self.info['odstup']
            rozestup = self.info['rozestup']
            bb_hore = data[BB_HORE]
            bb_main = data[BB_MAIN]
            bb_dole = data[BB_DOLE]
            open = data[OPEN]
            
#            hen vrátím startování obchodů na horní či dolní bb,  vyžaduje indikaci změnu trendu
#                což řeším jako protnutí bb main 
            if open.prodej < bb_main.prodej:
                if self.býčiště is not None and self.býčiště.start < open.prodej:
                    self.býčiště = None
                    
            if open.prodej > bb_main.prodej:
                if self.medvědiště is not None and self.medvědiště.start > open.prodej:
                    self.medvědiště = None
                    
#            hen vytvořím objednávky obchodů ak nejestvují
            if self.býčiště is None:
                horní_cena = max_nákupu(open  + odstup,  bb_hore)
                self.býčiště = generátor_býků(start = horní_cena,  odstup = 0, rozestup = rozestup)
            else:
                if open.nákup < bb_hore.nákup:
                    self.býčiště.přitáhni_k_ceně(bb_hore)
                    
            if self.medvědiště is None:
                dolní_cena = min_prodeje(open - odstup,  bb_dole)
                self.medvědiště = generátor_medvědů(start = dolní_cena,  odstup = 0,  rozestup = rozestup)
            else:
                if open.prodej > bb_dole.prodej:
                    self.medvědiště.přitáhni_k_ceně(bb_dole)
                
               
#            pootvírám nové obchody
            for čekaná,  klíč in (self.býčiště,  HIGHT),  (self.medvědiště,  LOW):
                if čekaná is not None:
                    k_ceně = data[klíč]
                    for nová_cena in čekaná(k_ceně):
                        #                    GAP
                        if čekaná < data[OPEN]:
                            if not čekaná < self.předchozí_data[CLOSE]:
                                self.obchody.zruším_obchod_gapem(směrem = čekaná.směrem,  čas = data[OPEN_TIME],  cena = nová_cena,  velikost = self.info['sázím loty'])
                            else:
                                print("moram da prošetřím ovoj případ")
                        else:
                            self.obchody.otevřu_nový_obchod(směrem = čekaná.směrem,  cena = nová_cena,  velikost = self.info['sázím loty'],  čas = data[OPEN_TIME])
#                        print('nový obchod z ' + směr,  nová_cena,  čekaná)
            
            
            self.statistika.pří_zavření_svíčky()
            
            yield self
            self.předchozí_data = data
            

    def __imam_znameni_ke_sklizni(self):
        self.statistika.pří_znamení_ke_vstupu()
        return True
        
    def da_li_překračuji_bb(self,  bb_čára):
        if self.předchozí_data is None:
            return False
        
        bb_čára = self.předchozí_data[bb_čára].prodej
        
        if bb_čára == 0:
            return False
        
        open = self.předchozí_data[OPEN].prodej
        close = self.předchozí_data[CLOSE].prodej
        
        hore = max(open,  close)
        dole = min(open,  close)
        
        if bb_čára <= hore and bb_čára >= dole:
            return True 
        return False
        
    def __da_li_třeba_zaset(self):

#        if self.data[OPEN_TIME].datum < datetime.datetime(
#                                                        year = 2010,
#                                                        month = 4,
#                                                        day = 9,
#                                                        hour=10,
#                                                        minute=0,
#                                                        tzinfo = pytz.UTC
#                                                        ):
#            return False

        if self.medvědiště is None and self.býčiště is None:
            #print('seju bo {} + {} == 0'.format(self.čekaná[BUY],  self.čekaná[SELL]))
            return True
            
        #print('neseju bo {} + {} != 0'.format(self.čekaná[BUY],  self.čekaná[SELL]))
        return False
        
        
    def __str__(self):
        return str(self.statistika)

if __name__ == '__main__':
    import argparse
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser()

#   a pak mu nastavím jaké příkazy a parametry má přijímat
    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, {}'.format(__version__))

    parser.add_argument('zdrojový_adresář')
    parser.add_argument('--odstup',  '-o',  type=int)
    parser.add_argument('--rozestup',  '-r',  type=int)

    #    a včíl to možu rozparsovat
    args = parser.parse_args()

    print(args)

    
    zdrojový_adresář = args.zdrojový_adresář
#    zdrojové_csv = args.zdrojový_soubor
#    csv_soubor = args.soubor

    if zdrojový_adresář is None:
        print('Není zadán zdrojový adresář')
    else:
        print('Načtu data z adresáře {}'.format(zdrojový_adresář))


        parametry = {'sklízím při zisku': 1000,
                            'odstup':args.odstup or 200,
                            'rozestup': args.rozestup or 200,
                            'sázím loty': 0.1
                     }

        talasnica = Talasnica(zdrojové_csv = zdrojový_adresář,  parametry = parametry)
        for data in talasnica:
            continue
            
        print(talasnica)
