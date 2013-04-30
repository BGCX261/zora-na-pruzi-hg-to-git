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
        self.čas_zavření = None
        self.swap = 0
        
        
    def zavřu(self,  čas_zavření,  cena_zavření):
        if not isinstance(cena_zavření,  int):
            raise TypeError('Cena je {}'.format(type(cena_zavření)))
        self.cena_zavření = cena_zavření
        self.čas_zavření = čas_zavření
            
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
        
    def zavřu_vše(self, čas_zavření,  cena_zavření,  *filtry):
        
        smazané_obchody = []
        smazané_klíče = []
        
        for klíč,  obchod in self.obchody.items():
            for filtr in filtry:
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


class Celkové_obchodní_postavení(object):
    
    def __init__(self,  info):
        self.info = info
        
        self.__swapovací_den = None
        
        self.býci = Seznam_býků()
        self.medvědi = Seznam_Medvědů()
        self.uzavřené = []
        
        self.uložený_zisk = 0
 
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

    def zavřu_obchody(self,  čas_zavření,  cena_zavření,  *filtry):
        
        self.uložený_zisk = self.uložený_zisk + self.profit(cena_zavření)
        
        zavření_býci = self.býci.zavřu_vše(čas_zavření = čas_zavření,  cena_zavření = cena_zavření.prodej,  *filtry)
        zavření_medvědi = self.medvědi.zavřu_vše(čas_zavření = čas_zavření,  cena_zavření = cena_zavření.nákup,  *filtry)
        
        self.uzavřené.extend(zavření_býci)
        self.uzavřené.extend(zavření_medvědi)
        
        
    @property
    def velikost(self):
        return self.býci.velikost - self.medvědi.velikost
        
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
            
    def profit(self,  při_ceně):
        profit_býků = self.býci.profit(při_ceně)
        profit_medvědů = self.medvědi.profit(při_ceně)
        return (profit_býků + profit_medvědů) * self.info['TICKVALUE'] 

class Talasnica(object):
    
    obchody = {}
#    maximum = None
#    minimum = None
#    ohrada = None
    
    def __init__(self,  zdrojové_csv,  parametry = None):
        
        self.zdrojové_csv = zdrojové_csv
        self.info = info_z_csv(zdrojové_csv)
        
        self.Třída_ceny = davaj_cenu(spred = self.info['SPRED'],  přesnost = self.info['DIGITS'],  point = self.info['POINT'])
        
        self.obchody = Celkové_obchodní_postavení(info = self.info)
        
        if parametry is not None:
            if isinstance(parametry,  dict):
                self.info.update(parametry)
            else:
                raise ValueError('Parametry musí být slovníkem a nikolivěk {}'. format(type(parametry)))
                
        self.data = None
        
#        generátory nových pozic
        self.býčiště = None
        self.medvědiště = None
        
        self.znamení_setby = None
        self.znamení_sklizně = None
        
#         při otevření svíce potřebuji profit pouze z obchodů, které byly otevřeny nejpopzději na předchozí svíci
#          při exportu s evšak k takové hodnotě nemohu dostat, neboť získávám až data s nově otevřenými obchody
#       proto si ten profit spočtu a uložím při započetí průchoud
        self.profit_při_otevření = None
        
        self.počáteční_čas = None
        self.konečný_čas = None
        self.samoj_bolšoj_profit = [None,  None]
        self.samoj_bolšoj_zisk = [None,  None]
        self.samaja_bolšaja_velikost = {HORE: None,  DOLE: None}
        self.samoj_bolšoj_býk = None
        self.samoj_bolšoj_medvěd = None
        self.počet_svíček = None
        
    
    def __iter__(self):
        
        for data in data_z_csv(self.zdrojové_csv):
            
            upravím_data_ceny_na_int(data,  self.Třída_ceny)
            
            if data['OPEN'] is None:
                print('Přeskakuji svíčku {} koja nemá ceny'.format(data['BAR']))
                continue
                
            self.data = data
                
#            print(data['OPEN'])
                
#            print('-' * 44)
#            print('BAR {} {}'.format(data['BAR'],  data['OPEN TIME']))

            if self.počáteční_čas is None:
                self.počáteční_čas = data['OPEN TIME']
                
            if self.počet_svíček is None:
                self.počet_svíček = data['BAR']
                
            self.konečný_čas = data['OPEN TIME']
            
            self.profit_při_otevření = self.obchody.profit(data['OPEN'])
            self.obchody.swapuji(data['OPEN TIME'])
            
            self.samoj_bolšoj_profit = [max(self.samoj_bolšoj_profit[0] or 0,  self.profit_při_otevření),  min(self.samoj_bolšoj_profit[1] or 0,  self.profit_při_otevření)]
            self.samoj_bolšoj_zisk = [max(self.samoj_bolšoj_zisk[0] or 0,  self.profit_při_otevření + self.obchody.uložený_zisk + self.obchody.swap),  min(self.samoj_bolšoj_zisk[1] or 0,  self.profit_při_otevření + self.obchody.uložený_zisk + self.obchody.swap)]
            
            self.znamení_sklizně = self.__imam_znameni_ke_sklizni()
#            assert self.znamení_sklizně == data['znamení sklizně']
            
#            sklizeň
            if self.znamení_sklizně is True:
                if self.profit_při_otevření  + self.obchody.swap > self.info['sklízím při zisku']:
                    self.obchody.zavřu_obchody(cena_zavření = data['OPEN'],  čas_zavření = data['OPEN TIME'])
                    self.medvědiště = None
                    self.býčiště = None
            
            
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
                
            for čekaná,  klíč in (self.býčiště,  HIGHT),  (self.medvědiště,  LOW):
                if čekaná is not None:
                    k_ceně = data[klíč]
                    for nová_cena in čekaná(k_ceně):
                        #                    GAP
#                        if (nová_cena - data[OPEN]) * ZNAMÉNKO_SMÉRU[směr] < 0:
                        if čekaná < data[OPEN]:
                            self.obchody.zruším_obchod_gapem(směrem = čekaná.směrem,  čas = data['OPEN TIME'],  cena = nová_cena,  velikost = self.info['sázím loty'])
#                            if směr == HORE:
#                                třída = Býk
#                            if směr == DOLE:
#                                třída = Medvěd
#                                
#                            obchod = třída(velikost = self.info['sázím loty'],  čas_otevření = Datum(0),  cena = nová_cena)
#                            obchod.zavřu(čas = data['OPEN TIME'],  cena = nová_cena)
##                            obchod = {SMÉR: směr, 
##                                      VELIKOST: self.info['sázím loty'], 
##                                      ČAS_OTEVŘENÍ: Datum(0), 
##                                      OTEVÍRACÍ_CENA: 0, 
##                                      ČAS_ZAVŘENÍ: data['OPEN TIME'], 
##                                      ZAVÍRACÍ_CENA: nová_cena
##                                      }
#                            self.uzavřené_obchody.append(obchod)
                
                        else:
                            self.obchody.otevřu_nový_obchod(směrem = čekaná.směrem,  cena = nová_cena,  velikost = self.info['sázím loty'],  čas = data['OPEN TIME'])
#                        print('nový obchod z ' + směr,  nová_cena,  čekaná)
            
            
            self.samoj_bolšoj_býk = max(self.samoj_bolšoj_býk or 0, self.obchody.býci.velikost )
            self.samoj_bolšoj_medvěd = max(self.samoj_bolšoj_medvěd or 0,  self.obchody.medvědi.velikost)
            
            velikost_postavení = self.obchody.velikost
            self.samaja_bolšaja_velikost[HORE] = max(self.samaja_bolšaja_velikost[HORE] or 0,  velikost_postavení)
            self.samaja_bolšaja_velikost[DOLE] = min(self.samaja_bolšaja_velikost[DOLE] or 0,  velikost_postavení)
            
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
        print('největší medvěd {:,.2f}'.format(self.samoj_bolšoj_medvěd).replace(",", " ").replace(".", ","))
        
        print('největší pozice {:,.2f} a {:,.2f}'.format(self.samaja_bolšaja_velikost[HORE],  self.samaja_bolšaja_velikost[DOLE]).replace(",", " ").replace(".", ","))
        
        print('-'*20)
        
        print('otevřený zisk {1:,.2f} {0} a {2:,.2f} {0}'.format(self.info['měna účtu'],  *self.samoj_bolšoj_profit).replace(",", " ").replace(".", ","))
        print('celkový zisk {1:,.2f} {0} a {2:,.2f} {0}'.format(self.info['měna účtu'],  *self.samoj_bolšoj_zisk).replace(",", " ").replace(".", ","))

        print('-'*20)
        
        uložený_zisk = self.obchody.uložený_zisk
        swap = self.obchody.swap
        profit_při_otevření = self.profit_při_otevření
        print('{:<25}{:>18,.2f}'.format('uložený zisk ',  uložený_zisk).replace(",", " ").replace(".", ","))
        print('{:<25}{:>18,.2f}'.format('+ swap',  swap).replace(",", " ").replace(".", ","))
        print('{:>25}{:>18,.2f}'.format('= ',  uložený_zisk + swap).replace(",", " ").replace(".", ","))
        print('{:<25}{:>18,.2f}'.format('+ otevřené pozice ', profit_při_otevření).replace(",", " ").replace(".", ","))
        print('{:>25}{:>18,.2f}'.format('= ',  uložený_zisk + swap + profit_při_otevření).replace(",", " ").replace(".", ","))
        
        
        # obnovíme standartní výstup
        sys.stdout = stdout
        return(output_buffer.getvalue())

if __name__ == '__main__':
    from talasnica.testuji_talasnicu import csv_soubor
    talasnica = Talasnica()
    for data in talasnica(csv_soubor):
        continue
