#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import datetime,  pytz

from talasnica.konstanty import BUY,  SELL,  PROFIT_OPEN,  PROFIT_HORE, PROFIT_DOLE, PROFIT_CLOSE,  SWAP,  ULOŽENÝ_ZISK

from talasnica.csv_data import data_z_csv,  info_z_csv,  Numero


#class Zaokrouhluji():

class Cena(dict):

    def __init__(self,  přesnost):
        self._přesnost = přesnost
        self[BUY] = 0.0
        self[SELL] = 0.0

    def __setitem__(self,  klíč,  hodnota):

#        print('cena {} => '.format(hodnota),  end = ' ')

#       kvůli zaokrouhlování v pythonu přičtu maličkou hodnotičku aby se vždy X.0005 zaokrouhlilo hore
        hodnota = hodnota + 10**(-1 * self._přesnost * self._přesnost)
        hodnota = round(hodnota,  self._přesnost)

#        print(hodnota)

        super().__setitem__(klíč,  hodnota)

class Profit(Cena):

    def __init__(self,  přesnost):
        self._přesnost = přesnost
        self[PROFIT_OPEN] = 0.0
        self[PROFIT_HORE] = 0.0
        self[PROFIT_DOLE] = 0.0
        self[PROFIT_CLOSE] = 0.0


class Zisk(Cena):

    def __init__(self,  přesnost):
        self._přesnost = přesnost
        self[SWAP] = 0.0
        self[ULOŽENÝ_ZISK] = 0.0

#    def __setitem__(self,  klíč,  hodnota):
#
#        print('cena {} => '.format(hodnota),  end = ' ')
#
##       kvůli zaokrouhlování v pythonu přičtu maličkou hodnotičku aby se vždy X.0005 zaokrouhlilo hore
#        hodnota = hodnota + 10**(-1 * self._přesnost * self._přesnost)
#        hodnota = round(hodnota,  self._přesnost)
#
#        print(hodnota)
#
#        super().__setitem__(klíč,  hodnota)

class Měna(object):

    def __init__(self,  symbol):
        self.__symbol = symbol

    def __call__(self,  částka):
        return '{:n} {}'.format(round(částka,  0),  self.__symbol)

class Talasnica(object):

    def __init__(self,  csv_soubor):
        self._csv_soubor = csv_soubor
        self._info = info_z_csv(self._csv_soubor)
        self.odstup_v_pointech = self._info['odstup'] * self._info['POINT']
        self.rozestup_v_pointech = self._info['rozestup'] * self._info['POINT']
        self.spred_v_pointech = self._info['SPRED'] * self._info['POINT']

        self.data = None

        self.směr = {BUY:1,  SELL: -1}
        self.da_li_seju = None
        self.znamení_sklizně = None

        self.zisk = Zisk(přesnost = 4)
        self.vynuluji_počítadla()
        self.profit = Profit(přesnost = 4)

        self.__swapovací_den = None
        self.__pointy_na_peníze = None


    @property
    def pointy_na_peníze(self):
        if self.__pointy_na_peníze is None:
            self.__pointy_na_peníze = self._info['TICKVALUE'] / self._info['POINT']

        return self.__pointy_na_peníze


    def start(self):
        
#      int pos = Bars - counted_bars;
#      double MinMax_Svice[2];
        MinMax_Svíce = Cena(přesnost = self._info['DIGITS'])
        
        
    #    while(pos > 0)
    #   {
        for data in data_z_csv(self._csv_soubor):
            
            self.data = data
            
#            print('BAR {} {}'.format(data['BAR'],  data['OPEN TIME']))
            
#            if data['BAR'] == 18686:
#                print('DEBUGUJU')

            MinMax_Svíce[BUY] = data['HIGHT'] + self.spred_v_pointech
            MinMax_Svíce[SELL] = data['LOW']

            self._přepočítám_profit_při_otevření()

            self.znamení_sklizně = self.imam_znameni_ke_sklizni()
#            assert self.znamení_sklizně == data['znamení sklizně']
            
#            sklizeň
            if self.znamení_sklizně:
                if self.imam_profit():
                    self.zavru_vse_pri_otevreni_svice()
                    

            self.da_li_seju = self._da_li_třeba_zaset()
            assert self.da_li_seju == data['da li seju']
   
#            setba
            if self.da_li_seju:
                #print('TOZ SEJU')
                self.ohrada[BUY] = data['OPEN'] + self.odstup_v_pointech + self.spred_v_pointech
                self.ohrada[SELL] = data['OPEN'] - self.odstup_v_pointech
                assert self.ohrada[SELL]  == data['medvědí ohrada']
                assert self.ohrada[BUY] == data['býčí ohrada']
    
                self.čekaná[BUY] = self.ohrada[BUY]
                self.čekaná[SELL] = self.ohrada[SELL]
    
                self.hranice[BUY] = MinMax_Svíce[BUY] 
                self.hranice[SELL] = MinMax_Svíce[SELL] 
                assert self.hranice[BUY] == data['hranice býka']
                assert self.hranice[SELL] == data['hranice medvěda']
    
                self.prepocitam_obchody(směrem = BUY)
                self.prepocitam_obchody(směrem = SELL)
    
#            růst
            for směrem in BUY,  SELL:
                
                if self.hranice[směrem] > 0 and (self.hranice[směrem] - MinMax_Svíce[směrem] ) * self.směr[směrem] < 0:
                    self.hranice[směrem] = MinMax_Svíce[směrem]
                    self.prepocitam_obchody(směrem)


#        // včíl máme zjištěné koliko obchodů s eběhem svíce otevře
#      // nevíme sice v jakém pořadí, ale nejméně příznivý scénář beru takto
#      // hore počítám, že s eotevřely aj všechny protipozice, takže zisk je o to nižší
#      // a dole naopak počítám s otevřenými všemi horními pozicemi
#      // při zavření je to jasné, tam budou jistě otevřeny horní i dolní pozice
#      prepocitam_profit_na_svici(pos);
            self._přepočítám_profit_na_svíci()

            yield data


    def _da_li_třeba_zaset(self):

        if self.data['OPEN TIME'] < datetime.datetime(
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

        if self.čekaná[BUY] == 0 and self.čekaná[SELL]  == 0:
            #print('seju bo {} + {} == 0'.format(self.čekaná[BUY],  self.čekaná[SELL]))
            return True
            
        #print('neseju bo {} + {} != 0'.format(self.čekaná[BUY],  self.čekaná[SELL]))
        return False


    def _přepočítám_profit_při_otevření(self):
        self.profit[PROFIT_OPEN] = (self.data['OPEN'] - self.cena[BUY]) * self.velikost[BUY] + (self.cena[SELL] - self.data['OPEN'] - self.spred_v_pointech) * self.velikost[SELL]

    def _přepočítám_profit_na_svíci(self):
#        double bid_Open = Open[pos];
#       double ask_Open = bid_Open + SPREAD_V_POINTECH;
#
#       double bid_High = High[pos];
#       double ask_High = bid_High + SPREAD_V_POINTECH;
#
#       double bid_Low = Low[pos];
#       double ask_Low = bid_Low + SPREAD_V_POINTECH;
#
#       double bid_Close = Close[pos];
#       double ask_Close = bid_Close + SPREAD_V_POINTECH;
#
#       profit_pri_otevreni = (bid_Open - cena_byku) * velikost_byku + (cena_medvedu - ask_Open) * velikost_medvedu;
#       profit_hore = (bid_High - cena_byku) * velikost_byku + (cena_medvedu - ask_High) * velikost_medvedu;
#       profit_dole = (bid_Low - cena_byku) * velikost_byku + (cena_medvedu - ask_Low) * velikost_medvedu;
#       profit_pri_zavreni = (bid_Close - cena_byku) * velikost_byku + (cena_medvedu - ask_Close) * velikost_medvedu;
        for klíč_tal,  klíč_data in {PROFIT_HORE: 'HIGHT',  PROFIT_DOLE:'LOW',  PROFIT_CLOSE: 'CLOSE'}.items():
            self.profit[klíč_tal] = (self.data[klíč_data] - self.cena[BUY]) * self.velikost[BUY] + (self.cena[SELL] - self.data[klíč_data] - self.spred_v_pointech) * self.velikost[SELL]
#
#       int vcilkajsi_den = TimeDay(Time[pos]);
        vcilkajsi_den = self.data['OPEN TIME'].day
#
#       if(swapovaci_den != vcilkajsi_den){
        if not self.__swapovací_den == vcilkajsi_den:

#          double swap = velikost_byku * MarketInfo(Symbol(), MODE_SWAPLONG) + velikost_medvedu * MarketInfo(Symbol(), MODE_SWAPSHORT);
            swap = self.velikost[BUY] * self._info['býčí swap'] + self.velikost[SELL] * self._info['medvědí swap']
#          if(TimeDayOfWeek(Time[pos]) == 3){
            if self.data['OPEN TIME'].isoweekday() == 3:
#             swap = swap * 3;
                swap = swap * 3
#          }
#          celkovy_swap = celkovy_swap + swap;
            self.zisk[SWAP] = self.zisk[SWAP] + swap
#          swapovaci_den = vcilkajsi_den;
            self.__swapovací_den = vcilkajsi_den
#       }

    def imam_znameni_ke_sklizni(self):
        return True

#    bool imam_profit(int pos) {
    def imam_profit(self):
#
#       double zisk = profit_pri_otevreni * POINTY_NA_PENIZE + celkovy_swap;
#       if(zisk > sklizim_pri_zisku) {
        if self.profit[PROFIT_OPEN] * self.pointy_na_peníze + self.zisk[SWAP] > self._info['sklízím při zisku']:
#          return(true);
            return True
#       }
#       return(false);
        return False
#    }
#
#    void zavru_vse_pri_otevreni_svice() {
    def zavru_vse_pri_otevreni_svice(self):
#       ulozene_zisky = ulozene_zisky + profit_pri_otevreni * POINTY_NA_PENIZE + celkovy_swap;
        self.zisk[ULOŽENÝ_ZISK] = self.zisk[ULOŽENÝ_ZISK] + self.profit[PROFIT_OPEN] * self.pointy_na_peníze + self.zisk[SWAP]

        self.vynuluji_počítadla()

#       // tento si ponecha puvodni hodnotu, na ktere se zavíralo
#       //profit_pri_otevreni = 0;
#       profit_hore = 0;
#       profit_dole = 0;
#       profit_pri_zavreni = 0;
        for profit_při in PROFIT_HORE,  PROFIT_DOLE,  PROFIT_CLOSE:
            self.profit[profit_při] = 0.0

#       celkovy_swap = 0;

        self.zisk[SWAP] = 0.0

#    }

    def vynuluji_počítadla(self):
        přesnost = self._info['DIGITS']
        self.cena = Cena(přesnost)
        self.velikost = Cena(přesnost = 2)
        self.ohrada = Cena(přesnost)
        self.čekaná = Cena(přesnost)
        self.hranice = Cena(přesnost)
        
    def prepocitam_obchody(self,  směrem):
        #print('prepocitam_obchody směrem ',  směrem)
        if (self.hranice[směrem] - self.čekaná[směrem]) * self.směr[směrem] > 0:
            #print('if {} > 0'.format(self.hranice[směrem] - self.čekaná[směrem]) * self.směr[směrem])
#          double citatel_nove_ceny = cena_medvědů * velikost_medvědů;
            citatel_nove_ceny = 0
            jmenovatel_nove_ceny = 0

            while (self.hranice[směrem] - self.čekaná[směrem]) * self.směr[směrem] > 0:
                #print('while pro ',  směrem)

#             if(cena_ocekavaneho_medveda > Open[pos]){
                if (self.čekaná[směrem] - self.data['OPEN']) * self.směr[směrem] < 0:
#                    GAP
                    #print('GAP')
                    pass
                else:
                    citatel_nove_ceny = citatel_nove_ceny + self._info['sázím loty'] * self.čekaná[směrem]
                    jmenovatel_nove_ceny = jmenovatel_nove_ceny + self._info['sázím loty']
                    #print('jmenovatel_nove_ceny = ',  jmenovatel_nove_ceny)
                    #print('citatel_nove_ceny = ',  citatel_nove_ceny)

#             // a idu o kus dál
                self.čekaná[směrem] = self.čekaná[směrem] + self.směr[směrem] * self.rozestup_v_pointech
                #print('self.čekaná[{}] '.format(směrem),  self.čekaná[směrem])

#            self.čekaná[směrem] = self.čekaná[směrem]

            if jmenovatel_nove_ceny > 0:
                citatel_nove_ceny = citatel_nove_ceny + self.cena[směrem] * self.velikost[směrem]
                jmenovatel_nove_ceny = jmenovatel_nove_ceny + self.velikost[směrem]
                self.cena[směrem]  = citatel_nove_ceny/jmenovatel_nove_ceny
                self.velikost[směrem]  = jmenovatel_nove_ceny
                #print('HOTOVO jmenovatel_nove_ceny = ',  jmenovatel_nove_ceny)
                #print('HOTOVO self.čekaná[{}] '.format(směrem),  self.čekaná[směrem])
                return True

        return False

        
    def report(self):

        print('REPORT TALASNICE')
        print('soubor {}'.format(self._csv_soubor))
        print('ZISK')

        měna = Měna(self._info['měna účtu'])

        for klíč,  hodnota in self.zisk.items():
            print('{} {}'.format(klíč,  měna(hodnota)))
        print('PROFIT')
        for klíč,  hodnota in self.profit.items():
            print('{} {} pipsů'.format(klíč,  hodnota))
            v_penězách = hodnota * self.pointy_na_peníze
            print('{} {}'.format(klíč,  měna(v_penězách)))

if __name__ == '__main__':
    from talasnica.testuji_talasnicu import csv_soubor
    talasnica = Talasnica(csv_soubor)
    for data in talasnica.start():
        continue
