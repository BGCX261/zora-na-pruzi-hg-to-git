from pruga.vidimir.stroj.konzole.dekorátory import obarvi,  orámuj,  odsaď
from pruga.vidimir.stroj.konzole.barvy import *




#NADPIS = Obarvi(ČERNÁ,  NA_SIVÉ,  nadtržítko = '=',  podtržítko = '=',  formát = '*** {} ***',  odsazení = 10)

@obarvi(ČERNÁ,  NA_SIVÉ)
@odsaď(10)
@orámuj(hore = '=',  dole = '=')
def NADPIS(text):
    return '*** {} ***'.format(text)
H1 = NADPIS
#H2 = Obarvi(ČERNÁ,  NA_SIVÉ,  formát = '| {} |',  nadtržítko = '_',  podtržítko = '-',  odsazení = 10)
#H3 = Obarvi(ČERNÁ,  NA_SIVÉ,   nadtržítko = '-.',  podtržítko = '-.',  odsazení = 10)

#INFO  = Obarvi(BÍLÁ,  NA_TMAVĚ_ČERVENÉ)
@obarvi(BÍLÁ,  NA_TMAVĚ_ČERVENÉ)
def INFO(text):
    return text


#CHYBA  = Obarvi(ŽLUTÁ,  NA_TMAVĚ_ČERVENÉ)
@obarvi(ŽLUTÁ,  NA_TMAVĚ_ČERVENÉ)
def CHYBA(text):
    return text

#PŘÍKAZ = Obarvi(PROHOĎ_BARVU_A_POZADÍ)
@obarvi(PROHOĎ_BARVU_A_POZADÍ)
def PŘÍKAZ(text):
    return text
#BÍLÁ,  NA_TMAVĚ_ČERVENÉ,  PROHOĎ_BARVU_A_POZADÍ
#SOUBOR = Obarvi(PROHOĎ_BARVU_A_POZADÍ)
@obarvi(PROHOĎ_BARVU_A_POZADÍ)
def SOUBOR(text):
    return text
#Obarvi(BÍLÁ,  TUČNĚ,  NA_TMAVĚ_SIVÉ)
#OBJEKT = Obarvi(SIVÁ,  TUČNĚ,  NA_ČERNÉ)

@obarvi(BÍLÁ,  NA_TMAVĚ_SIVÉ)
def VÝPIS_PROGRAMU(text):
    return text  
