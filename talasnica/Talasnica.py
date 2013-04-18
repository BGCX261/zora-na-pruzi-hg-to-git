#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import datetime,  pytz

BUY = 0
SELL = 1
OPEN = 0
#HORE = 1
#DOLE = 2
#CLOSE = 3

from talasnica.csv_data import INFO,  SVÍCA

class Talasnica(object):
    
    def __init__(self,  csv_soubor):
        self._csv_soubor = csv_soubor
        self._info = self._nactu_info()
        self.odstup_v_pointech = self._info['odstup'] * self._info['POINT']
        self.rozestup_v_pointech = self._info['rozestup'] * self._info['POINT']
        self.spred_v_pointech = self._info['SPRED'] * self._info['POINT']
        
        self.čas_otevření_svíčky = None
        self.cena = [0.0,  0.0]
        self.velikost = [0.0,  0.0]
        self.ohrada = [0.0,  0.0]
        self.čekaná = [0.0,  0.0]
        self.hranice = [0.0,  0.0]
        self.směr = (1,  -1)
        self.da_li_seju = None
        
        self.profit = [None,  None,  None,  None]
        self.swap = None
        self.uložený_zisk = 0
        
#    def porovnám_cenu(self,  první,  druhá):
#        if první == druhá:
#            return True
#            
#        rozdíl = abs(první-druhá)
#        přesnost = self._info['MODE_DIGITS']
#        rozdíl = round(rozdíl,  přesnost)
#        if rozdíl == self._info['MODE_POINT']:
#            return True
#            
#        print("NEROVNO",  první,  druhá,  rozdíl,  self._info['MODE_POINT'])
#        return False
        
    def prepocitam_obchody(self,  data,  směrem):

        if (self.hranice[směrem] - self.čekaná[směrem]) * self.směr[směrem] > 0:
#          double citatel_nove_ceny = cena_medvědů * velikost_medvědů;
            citatel_nove_ceny = self.cena[směrem] * self.velikost[směrem]
            jmenovatel_nove_ceny = self.velikost[směrem]
            cas_svicky = data['OPEN TIME']

            while (self.hranice[směrem] - self.čekaná[směrem]) * self.směr[směrem] > 0:


#             if(cena_ocekavaneho_medveda > Open[pos]){
                if (self.čekaná[směrem] - data['OPEN']) * self.směr[směrem] < 0:
#                    GAP
                    pass
                else:
                    citatel_nove_ceny = citatel_nove_ceny + self._info['sázím loty'] * self.čekaná[směrem]
                    jmenovatel_nove_ceny = jmenovatel_nove_ceny + self._info['sázím loty']

#             // a idu o kus dál
                self.čekaná[směrem] = self.čekaná[směrem] + self.směr[směrem] * self.rozestup_v_pointech

            self.čekaná[směrem] = self._info.cena(self.čekaná[směrem])
            
            self.cena[směrem]  = self._info.cena(citatel_nove_ceny/jmenovatel_nove_ceny)
#            float(int(citatel_nove_ceny/jmenovatel_nove_ceny*PRESNOST))/PRESNOST
            self.velikost[směrem]  = self._info.velikost(jmenovatel_nove_ceny)
            
#            if směrem == BUY: 
#                assert self.velikost[směrem] == data['velikost býků']
#            else:
#                assert self.velikost[směrem] == data['velikost medvědů']
            return True

        return False
    
    def _nactu_info(self):
        with open(self._csv_soubor,  mode = "r",  encoding = "windows-1250") as čtu_soubor:
            hlavička = čtu_soubor.readline()
            info = čtu_soubor.readline()
            return INFO(hlavička,  info)
        
    def _data_z_csv(self):
    
#        print('IMPORTUJI {}'.format(self._csv_soubor))
        
        with open(self._csv_soubor,  mode = "r",  encoding = "windows-1250") as čtu_soubor:
            
            čtu_soubor.readline()
            čtu_soubor.readline()
            
            hlavička = čtu_soubor.readline()
            
            for řádek in čtu_soubor:
                yield SVÍCA(hlavička,  řádek)
            
    def start(self):
    #    while(pos > 0)
    #   {
         
        for data in self._data_z_csv():
            
            self.čas_otevření_svíčky = data['OPEN TIME']
            
#            if data['BAR'] == 18686:
#                print('DEBUGUJU')
            
    #      //Print("while pos > 0, pos = " + pos);
    #      dHigh = High[pos] + MarketInfo(Symbol(),MODE_SPREAD) * Point;
    #      dLow = Low[pos];
    
#        // nejprve přepočítám profit při otevření, kterýžto se počítá z počtu pozic otevřených do předchozí svíce
#      // další profity se počítají jakoby už byly všechny obchody na této svíci otevřeny
#      // což dává nepřesný výsledek, ale měl by být horší, než skutečnost
#      // je to tedy scénář nejméně příznivého vývoje
#      prepocitam_profit_pri_otevreni(pos);
            self._přepočítám_profit_při_otevření(data)
#      
#      // zjistím, zda mohu zavřít a případně pozavírám vše při open
#      if(mozu_da_sklidim(pos)){
#         if(imam_profit(pos)){
#            zavru_vse_pri_otevreni_svice();
#            if(kresli){
#               ukoncim_obdelnik(OHRADA, Time[pos]);
#            }
#         }
#      }

    #      da_li_seju = treba_zaset(pos);
    
            self.da_li_seju = self._da_li_třeba_zaset()
            assert self.da_li_seju == data['da li seju']
    #      
    #      if (da_li_seju) {
            if self.da_li_seju:
#                print('SEJU',  data['BAR'] ,  self.čas_otevření_svíčky)
    #            print(data)
    #         //Print(pos + " treba_zaset");
    #         medvedi_ohrada = Open[pos] - odstup * Point;
    #            medvedi_ohrada = data['OPEN'] - data['odstup'] * data['point']
    #            assert medvedi_ohrada == data['medvedi ohrada']
    ##         byci_ohrada  = Open[pos] + odstup*Point + SPREAD_V_POINTECH;
    #            byci_ohrada = data['OPEN'] + (data['odstup']  + data['spred']) * data['point']
    #            assert byci_ohrada == data['býčí ohrada']
                
                self.ohrada[BUY] = data['OPEN'] + self.odstup_v_pointech + self.spred_v_pointech
                self.ohrada[SELL] = data['OPEN'] - self.odstup_v_pointech
                assert self.ohrada[SELL]  == data['medvědí ohrada']
                assert self.ohrada[BUY] == data['býčí ohrada']
    #         
    #         // na ohrade se take otevrou nejbližší obchody
    #         cena_ocekavaneho_medveda = medvedi_ohrada;
    #            cena_ocekavaneho_medveda = medvedi_ohrada
    #         cena_ocekavaneho_byka = byci_ohrada;
    #            cena_ocekavaneho_byka = byci_ohrada
                self.čekaná[BUY] = self.ohrada[BUY]
                self.čekaná[SELL] = self.ohrada[SELL] 
    #         
    #         // vychozi maximum a minimum
    #         byci_maximum = dHigh;
    #            byci_maximum
                self.hranice[BUY] = data['HIGHT'] + self.spred_v_pointech 
                self.hranice[SELL] = data['LOW']
    #            assert byci_maximum == data['býčí maximum']
                assert self.hranice[BUY] == data['býčí maximum']
    #         medvedi_minimum = dLow;
    #            medvedi_minimum = data['LOW']
    #            assert medvedi_minimum == data['medvědí minimum']
                assert self.hranice[SELL] == data['medvědí minimum']
    #         
    #         prepocitam_medvedy(pos);
    #            prepocitam_medvedy(data)
    #         prepocitam_byky(pos);
    #            prepocitam_byky(data)
                self.prepocitam_obchody(data,  směrem = BUY)
                self.prepocitam_obchody(data,  směrem = SELL)
    #      }
    #      
    #      // nové maximum a minimum
    #      if (byci_maximum < dHigh && byci_maximum > 0) {
            if self.hranice[BUY] < data['HIGHT'] and self.hranice[BUY] > 0:
    #         //Print(pos + " byci_maximum < dHigh && byci_maximum > 0, byci_maximum = " + byci_maximum + " dHigh = " + dHigh);
    #         byci_maximum = dHigh;
                self.hranice[BUY] = data['HIGHT'] + self.spred_v_pointech 
    #         prepocitam_byky(pos);
                self.prepocitam_obchody(data,  směrem = BUY)
    #      }
    #      
    #      if (medvedi_minimum > dLow  && medvedi_minimum > 0) {
            if self.hranice[SELL] > data['LOW'] and self.hranice[SELL] > 0:
    #         //Print(pos + " medvedi_minimum > dLow  && medvedi_minimum > 0, medvedi_minimum = " + medvedi_minimum + " dLow = " + dLow);
    #         medvedi_minimum = dLow;
                self.hranice[SELL] = data['LOW']
    #         prepocitam_medvedy(pos);
                self.prepocitam_obchody(data,  směrem = SELL)
    #      }
        
#        // včíl máme zjištěné koliko obchodů s eběhem svíce otevře
#      // nevíme sice v jakém pořadí, ale nejméně příznivý scénář beru takto
#      // hore počítám, že s eotevřely aj všechny protipozice, takže zisk je o to nižší
#      // a dole naopak počítám s otevřenými všemi horními pozicemi
#      // při zavření je to jasné, tam budou jistě otevřeny horní i dolní pozice
#      prepocitam_profit_na_svici(pos);
            self._přepočítám_profit_na_svíci(data)
            
            yield data


    def _da_li_třeba_zaset(self):
        
        if self.čas_otevření_svíčky < datetime.datetime(
                                                        year = 2010,
                                                        month = 4,
                                                        day = 9,
                                                        hour=10,
                                                        minute=0, 
                                                        tzinfo = pytz.UTC
                                                        ):
#            print(self.čas_otevření_svíčky)
            return False
       
        if self.velikost[BUY] == 0 and self.velikost[SELL]  == 0:
           return True

        return False
        
        
    def _přepočítám_profit_při_otevření(self,  data):
        self.profit[OPEN] = (data['OPEN'] - self.cena[BUY]) * self.velikost[BUY] + (self.cena[SELL] - data['OPEN'] - self.spred_v_pointech) * self.velikost[SELL]
        
    def _přepočítám_profit_na_svíci(self,  data):
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
        for číslo,  profit_v in enumerate(('HIGHT',  'LOW',  'CLOSE'),  start = 1):
            self.profit[číslo] = (data[profit_v] - self.cena[BUY]) * self.velikost[BUY] + (self.cena[SELL] - data[profit_v] - self.spred_v_pointech) * self.velikost[SELL]
#       
#       int vcilkajsi_den = TimeDay(Time[pos]);
#       
#       if(swapovaci_den != vcilkajsi_den){
#          double swap = velikost_byku * MarketInfo(Symbol(), MODE_SWAPLONG) + velikost_medvedu * MarketInfo(Symbol(), MODE_SWAPSHORT);
#          
#          if(TimeDayOfWeek(Time[pos]) == 3){
#             swap = swap * 3;
#          }
#          celkovy_swap = celkovy_swap + swap;
#          swapovaci_den = vcilkajsi_den;
#       }
