#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

from talasnica.csv_data import data_z_csv,  najdu_info_csv

BUY = 0
SELL = 1

velikost_obchodu_loty =  0.1

class Talasnica(object):
    
    def __init__(self,  csv_soubor):
        self._csv_soubor = csv_soubor
        self._info = najdu_info_csv(csv_soubor)
        
        self.cena = [0.0,  0.0]
        self.velikost = [0.0,  0.0]
        self.ohrada = [0.0,  0.0]
        self.čekaná = [0.0,  0.0]
        self.hranice = [0.0,  0.0]
        self.směr = (1,  -1)
        
    @property
    def point(self):
        return self._info['MODE_POINT']
        
    def prepocitam_obchody(self,  data,  směrem):

        if (self.hranice[směrem] - self.čekaná[směrem]) * self.směr[směrem] > 0:
#          double citatel_nove_ceny = cena_medvedu * velikost_medvedu;
            citatel_nove_ceny = self.cena[směrem] * self.velikost[směrem]
            jmenovatel_nove_ceny = self.velikost[směrem]
            cas_svicky = data['OPEN TIME']

            while (self.hranice[směrem] - self.čekaná[směrem]) * self.směr[směrem] > 0:


#             if(cena_ocekavaneho_medveda > Open[pos]){
                if (self.čekaná[směrem] - data['OPEN']) * self.směr[směrem] < 0:
#                    GAP
                    pass
                else:
                    citatel_nove_ceny = citatel_nove_ceny + velikost_obchodu_loty * self.čekaná[směrem]
                    jmenovatel_nove_ceny = jmenovatel_nove_ceny + velikost_obchodu_loty

#             // a idu o kus dál
                self.čekaná[směrem] = self.čekaná[směrem] + self.směr[směrem] * data['rozestup'] * data['point']

            self.čekaná[směrem] = self._info.cena(self.čekaná[směrem])
            
            self.cena[směrem]  = self._info.cena(citatel_nove_ceny/jmenovatel_nove_ceny)
#            float(int(citatel_nove_ceny/jmenovatel_nove_ceny*PRESNOST))/PRESNOST
            self.velikost[směrem]  = self._info.velikost(jmenovatel_nove_ceny)
            print(jmenovatel_nove_ceny)
#            if směrem == BUY: 
#                assert self.velikost[směrem] == data['velikost byku']
#            else:
#                assert self.velikost[směrem] == data['velikost medvedu']
            return True

        return False
    
    
    def start(self):
    #    while(pos > 0)
    #   {
        for data in data_z_csv(self._csv_soubor):
            
            if data['BAR'] == 18607:
                print('DEBUGUJU')
            
    #      //Print("while pos > 0, pos = " + pos);
    #      dHigh = High[pos] + MarketInfo(Symbol(),MODE_SPREAD) * Point;
    #      dLow = Low[pos];
    #      
    #      da_li_seju = treba_zaset(pos);
            da_li_seju = data['da li seju']
    #      
    #      if (da_li_seju) {
            if da_li_seju:
    #            print(data)
    #         //Print(pos + " treba_zaset");
    #         medvedi_ohrada = Open[pos] - odstup * Point;
    #            medvedi_ohrada = data['OPEN'] - data['odstup'] * data['point']
    #            assert medvedi_ohrada == data['medvedi ohrada']
    ##         byci_ohrada  = Open[pos] + odstup*Point + SPREAD_V_POINTECH;
    #            byci_ohrada = data['OPEN'] + (data['odstup']  + data['spred']) * data['point']
    #            assert byci_ohrada == data['byci ohrada']
                
                self.ohrada[BUY] = data['OPEN'] + (data['odstup']  + data['spred']) * data['point']
                self.ohrada[SELL] = data['OPEN'] - data['odstup'] * data['point']
                assert self.ohrada[SELL]  == data['medvedi ohrada']
                assert self.ohrada[BUY] == data['byci ohrada']
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
                self.hranice[BUY] = data['HIGHT']
                self.hranice[SELL] = data['LOW']
    #            assert byci_maximum == data['byci max']
                assert self.hranice[BUY] == data['byci max']
    #         medvedi_minimum = dLow;
    #            medvedi_minimum = data['LOW']
    #            assert medvedi_minimum == data['medvedi min']
                assert self.hranice[SELL] == data['medvedi min']
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
                self.hranice[BUY] = data['HIGHT']
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
        
            yield data


if __name__ == '__main__':

    csv_soubor = './experts/files/profitmetr/ladenka/EURJPY._60_2013-04-16-10-59-16.csv'
   
    talasnica = Talasnica(csv_soubor)
    
    for data in talasnica.start():
       
#        ExtMapBuffer_medvedi_ohrada[pos] = medvedi_ohrada;
        assert talasnica.ohrada[SELL] == data['medvedi ohrada']
#        ExtMapBuffer_byci_ohrada[pos] = byci_ohrada;
        assert talasnica.ohrada[BUY] == data['byci ohrada']
#        ExtMapBuffer_velikost_medvedu[pos] = velikost_medvedu;
        if not talasnica.velikost[SELL] == data['velikost medvedu']:
            print(data)
        assert talasnica.velikost[SELL] == data['velikost medvedu']
#        ExtMapBuffer_velikost_byku[pos] = velikost_byku;
        if not talasnica.velikost[BUY] == data['velikost byku']:
            print(data)
        assert talasnica.velikost[BUY] == data['velikost byku']
#        ExtMapBuffer_cena_medvedu[pos] = cena_medvedu;
        assert talasnica.cena[SELL] == data['cena medvedu']
#        ExtMapBuffer_cena_byku[pos] = cena_byku;
        assert talasnica.cena[BUY] == data['cena byku']
#        ExtMapBuffer_cekajici_medved[pos] = cena_ocekavaneho_medveda;
        assert talasnica.čekaná[SELL] == data['cena oc. medveda']
#        ExtMapBuffer_cekajici_byk[pos] = cena_ocekavaneho_byka;
        assert talasnica.čekaná[BUY] == data['cena oc. byka']
    
    
