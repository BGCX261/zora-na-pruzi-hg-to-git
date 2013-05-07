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
                                 PŘESNOST_CENY, 
                                 PŘESNOST_LOTU, 
                                 PŘESNOST_PŘEPOČTU_PROFITU, 
                                 BB_MAIN,  BB_HORE,  BB_DOLE,  PSAR
                                 )


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
        print("přitáhnu býčí start", self.start,  "ku",  k_ceně.nákup)
        if k_ceně.nákup < self.start:
            while self.start > k_ceně.nákup:
                self.start = self.start - self.rozestup
                print(self.start)
            self.start = self.start + self.rozestup
            print("přitaženo na",  self.start)
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
        print("přitáhnu medvědí start", self.start,  "ku",  k_ceně.prodej)
        if k_ceně.prodej > self.start:
            while self.start < k_ceně.nákup:
                self.start = self.start + self.rozestup
                print(self.start)
            self.start = self.start - self.rozestup
            print("přitaženo na",  self.start)
            self.čekaná = self.start

    
def davaj_cenu(spred,  přesnost,  point):

    class Cena(object):
        
        def __init__(self,  prodej,  nákup = None,  cena_už_je_int = None):
            
            if cena_už_je_int is None:
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
        
        print("zavřel jsem ",  self.tiket,  " ",  čas_zavření,  cena_zavření,  " profit ",  self.profit(cena_zavření))
            
#    def __call__(self):
#        return 
        
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
                print(čas_zavření, "profit profitujících",  profit_profitujících,  ">", přetlačeno, "velikost",  velikost_profitujících, "ku",  velikost_býků, velikost_medvědů, "k zavření",  k_zavření)
                
                def filtr(obchod):
                    if obchod.tiket in k_zavření:
                        return True
                    return False
                
                self.zavřu_obchody(čas_zavření = čas_zavření,  cena_zavření = cena_zavření,   filtr = filtr)
                print("umenšeno jest")
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
    
    obchody = {}
#    maximum = None
#    minimum = None
#    ohrada = None
    
    def __init__(self,  zdrojové_csv,  parametry = None):
        
        self.zdrojové_csv = zdrojové_csv
        self.info = info_z_csv(zdrojové_csv)
        
        Třída_ceny = davaj_cenu(spred = self.info['SPRED'],  přesnost = self.info['DIGITS'],  point = self.info['POINT'])
        self.mapa_tříd = {}
        for klíč in OPEN,  HIGHT,  LOW,  CLOSE,  BB_MAIN,  BB_HORE,  BB_DOLE,  PSAR:
            self.mapa_tříd[klíč] = Třída_ceny
      
        
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
        
#         při otevření svíce potřebuji profit pouze z obchodů, které byly otevřeny nejpopzději na předchozí svíci
#          při exportu s evšak k takové hodnotě nemohu dostat, neboť získávám až data s nově otevřenými obchody
#       proto si ten profit spočtu a uložím při započetí průchoud
        self.profit_při_otevření = None
        
#        statistické informace
        self.počáteční_čas = None
        self.konečný_čas = None
        self.samoj_bolšoj_otevřený_zisk = {OPEN: None,  HIGHT: None,  LOW: None,  CLOSE: None}
        self.samaja_bolšaja_otevřená_ztráta = {OPEN: None,  HIGHT: None,  LOW: None,  CLOSE: None}
        self.samoj_bolšoj_celkový_zisk = {OPEN: None,  HIGHT: None,  LOW: None,  CLOSE: None}
        self.samaja_bolšaja_celková_ztráta = {OPEN: None,  HIGHT: None,  LOW: None,  CLOSE: None}
        self.samaja_bolšaja_velikost = {HORE: None,  DOLE: None}
        self.samoj_bolšoj_býk = None
        self.samoj_bolšoj_medvěd = None
        self.počet_svíček = None
        
        self.počítadlo_znamení_vstupů = 0
        
    
    def __iter__(self,  AOSy = []):
        
        for data in data_z_csv(self.zdrojové_csv,  self.mapa_tříd):
            
            if data[OPEN_TIME].timestamp == 0:
                print('Přeskakuji svíčku {} koja nemá ceny'.format(data[BAR]))
                continue
                
            self.data = data
            
#            for aos in AOSy:
#                funkce_události = aos.get('pří_otevření_svíčky',  None)
#                if callable(funkce_události):
#                    funkce_události(self)
                
#            print(data[OPEN])
                
#            print('-' * 44)
#            print('BAR {} {}'.format(data['BAR'],  data['OPEN TIME']))

            if self.počáteční_čas is None:
                self.počáteční_čas = data[OPEN_TIME]
                
            if self.počet_svíček is None:
                self.počet_svíček = data[BAR]
                
            self.konečný_čas = data[OPEN_TIME]
            
            self.zisk_při_otevření = self.obchody.zisk(data[OPEN])
            self.obchody.swapuji(data[OPEN_TIME])
            
            self.samoj_bolšoj_otevřený_zisk[OPEN] = max(self.samoj_bolšoj_otevřený_zisk[OPEN] or 0,  self.zisk_při_otevření)
            self.samaja_bolšaja_otevřená_ztráta[OPEN] = min(self.samaja_bolšaja_otevřená_ztráta[OPEN] or 0,  self.zisk_při_otevření)
            celkový_zisk = self.zisk_při_otevření + self.obchody.uložený_zisk + self.obchody.swap
            self.samoj_bolšoj_celkový_zisk[OPEN] = max(self.samoj_bolšoj_celkový_zisk[OPEN] or 0,  celkový_zisk)
            self.samaja_bolšaja_celková_ztráta[OPEN] = min(self.samaja_bolšaja_celková_ztráta[OPEN] or 0,  celkový_zisk)
            
            self.znamení_sklizně = self.__imam_znameni_ke_sklizni()
#            assert self.znamení_sklizně == data['znamení sklizně']
            
#            sklizeň
            if self.znamení_sklizně is True:
                if self.zisk_při_otevření  + self.obchody.swap > self.info['sklízím při zisku']:
                    self.obchody.zavřu_obchody(čas_zavření = data[OPEN_TIME],  cena_zavření = data[OPEN])
                    self.medvědiště = None
                    self.býčiště = None
                else:
                    umenšeno =  self.obchody.umenším_pozice(čas_zavření = data[OPEN_TIME],  cena_zavření = data[OPEN])
                    if umenšeno:
                        self.medvědiště.přitáhni_k_ceně(data[OPEN])
                        self.býčiště.přitáhni_k_ceně(data[OPEN])
                    
            
            
            self.znamení_setby = self.__da_li_třeba_zaset()
                
            if self.znamení_setby is True:
#                vytáhnu z info
                odstup = self.info['odstup']
                rozestup = self.info['rozestup']
#                dosadím a spočítám
#                self.ohrada = {HORE: data[OPEN] + odstup + spred,  DOLE: data[OPEN] - odstup}
                self.medvědiště = generátor_medvědů(start = data[OPEN],  odstup = odstup,  rozestup = rozestup)
                self.býčiště = generátor_býků(start = data[OPEN],  odstup = odstup, rozestup = rozestup)
                
            for čekaná,  klíč in (self.býčiště,  HIGHT),  (self.medvědiště,  LOW):
                if čekaná is not None:
                    k_ceně = data[klíč]
                    for nová_cena in čekaná(k_ceně):
                        #                    GAP
                        if čekaná < data[OPEN]:
                            if not čekaná < self.předchozí_data[CLOSE]:
                                self.obchody.zruším_obchod_gapem(směrem = čekaná.směrem,  čas = data[OPEN_TIME],  cena = nová_cena,  velikost = self.info['sázím loty'])
                        else:
                            self.obchody.otevřu_nový_obchod(směrem = čekaná.směrem,  cena = nová_cena,  velikost = self.info['sázím loty'],  čas = data[OPEN_TIME])
#                        print('nový obchod z ' + směr,  nová_cena,  čekaná)
            
            
            self.samoj_bolšoj_býk = max(self.samoj_bolšoj_býk or 0, self.obchody.býci.velikost )
            self.samoj_bolšoj_medvěd = max(self.samoj_bolšoj_medvěd or 0,  self.obchody.medvědi.velikost)
            
            velikost_postavení = self.obchody.velikost
            self.samaja_bolšaja_velikost[HORE] = max(self.samaja_bolšaja_velikost[HORE] or 0,  velikost_postavení)
            self.samaja_bolšaja_velikost[DOLE] = min(self.samaja_bolšaja_velikost[DOLE] or 0,  velikost_postavení)
            
            for KLÍČ_NA_CENĚ in HIGHT,  LOW,  CLOSE:
                zisk = self.obchody.zisk(data[KLÍČ_NA_CENĚ])
                self.samoj_bolšoj_otevřený_zisk[KLÍČ_NA_CENĚ] = max(self.samoj_bolšoj_otevřený_zisk[KLÍČ_NA_CENĚ] or 0,  zisk)
                self.samaja_bolšaja_otevřená_ztráta[KLÍČ_NA_CENĚ] = min(self.samaja_bolšaja_otevřená_ztráta[KLÍČ_NA_CENĚ] or 0, zisk)
                celkový_zisk = zisk + self.obchody.uložený_zisk + self.obchody.swap
                self.samoj_bolšoj_celkový_zisk[KLÍČ_NA_CENĚ] = max(self.samoj_bolšoj_celkový_zisk[KLÍČ_NA_CENĚ] or 0,  celkový_zisk)
                self.samaja_bolšaja_celková_ztráta[KLÍČ_NA_CENĚ] = min(self.samaja_bolšaja_celková_ztráta[KLÍČ_NA_CENĚ] or 0,  celkový_zisk)
            
            yield self
            self.předchozí_data = data
            

    def __imam_znameni_ke_sklizni(self):
        self.počítadlo_znamení_vstupů = self.počítadlo_znamení_vstupů + 1
        return True
        
        if self.předchozí_data is None:
            return False
        
        bb_main = self.předchozí_data[BB_MAIN].prodej
        
        if bb_main == 0:
            return False
        
        open = self.předchozí_data[OPEN].prodej
        close = self.předchozí_data[CLOSE].prodej
        
        hore = max(open,  close)
        dole = min(open,  close)
        
        if bb_main <= hore and bb_main >= dole:
            self.počítadlo_znamení_vstupů = self.počítadlo_znamení_vstupů + 1
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
        import io
        import sys
        
        stdout = sys.stdout
        output_buffer = io.StringIO("")
        # přesměrování
        sys.stdout = output_buffer
        
        ODDELOVAC = '='*40
        
        print("*********")
        print("TALASNICA")
        print("*********")
        print('závěrečná zpráva')
        print()
        print('symbol {}'.format(self.info['SYMBOL']))
        print('svíčky od {} do {}'.format(self.počet_svíček,  self.data[BAR]))
        print('graf {}'.format(JMÉNO_GRAFU[self.info['časový rámec']]))
        
        print('započato {}'.format(self.počáteční_čas))
        print('ukončeno {}'.format(self.konečný_čas))
        doba = self.konečný_čas.datum - self.počáteční_čas.datum
        print('doba {}'.format(doba))
        print()
        print('počet znamení vstupů ',  self.počítadlo_znamení_vstupů)
        print('v průměru každých ',  doba/self.počítadlo_znamení_vstupů)
        print(ODDELOVAC)
        print()
        print('největší býk {:,.2f}'.format(self.samoj_bolšoj_býk).replace(",", " ").replace(".", ","))
        print('největší medvěd {:,.2f}'.format(self.samoj_bolšoj_medvěd).replace(",", " ").replace(".", ","))
        
        print('největší pozice {:,.2f} a {:,.2f}'.format(self.samaja_bolšaja_velikost[HORE],  self.samaja_bolšaja_velikost[DOLE]).replace(",", " ").replace(".", ","))
        print()
        print(ODDELOVAC)
        print()
        for klíč,  popis in ((OPEN,  PROFIT_OPEN),  (HIGHT,  PROFIT_HORE),  (LOW,  PROFIT_DOLE),  (CLOSE,  PROFIT_CLOSE)):
            print(popis)
            print('-'*40)
            print('{1:,.2f}{0:4} | {2:,.2f}{0:4}'.format(self.info['měna účtu'],  self.samoj_bolšoj_otevřený_zisk[klíč],  self.samaja_bolšaja_otevřená_ztráta[klíč]).replace(",", " ").replace(".", ","))
            print('{1:,.2f}{0:4} | {2:,.2f}{0:4}'.format(self.info['měna účtu'],  self.samoj_bolšoj_celkový_zisk[klíč],  self.samaja_bolšaja_celková_ztráta[klíč]).replace(",", " ").replace(".", ","))
            print('-'*40)
            print()

        print()
        print(ODDELOVAC)
        print()
        
        print("na poslední svíci")
        print("cena open",  self.data[OPEN])
        print()
        print('velikost hore {:,.2f} dole {:,.2f} celkem {:,.2f}'.format(self.obchody.býci.velikost,  self.obchody.medvědi.velikost,  self.obchody.velikost).replace(",", " ").replace(".", ","))
        print()
        uložený_zisk = self.obchody.uložený_zisk
        swap = self.obchody.swap
        zisk_při_otevření = self.zisk_při_otevření
        print('{:<25}{:>18,.2f}'.format('uložený zisk ',  uložený_zisk).replace(",", " ").replace(".", ","))
        print('{:<25}{:>18,.2f}'.format('+ swap',  swap).replace(",", " ").replace(".", ","))
        print('-'*40)
        print('{:>25}{:>18,.2f}'.format('= ',  uložený_zisk + swap).replace(",", " ").replace(".", ","))
        print('{:<25}{:>18,.2f}'.format('+ otevřené pozice ', zisk_při_otevření).replace(",", " ").replace(".", ","))
        print('-'*40)
        print('{:>25}{:>18,.2f}'.format('= ',  uložený_zisk + swap + zisk_při_otevření).replace(",", " ").replace(".", ","))
        
        # obnovíme standartní výstup
        sys.stdout = stdout
        return(output_buffer.getvalue())

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
