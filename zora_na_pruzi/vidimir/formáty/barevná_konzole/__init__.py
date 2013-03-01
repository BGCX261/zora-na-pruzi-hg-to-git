from zora_na_pruzi.vidimir.stroj.konzole.Obarvi import Obarvi
from zora_na_pruzi.vidimir.stroj.konzole.barvy import *

NADPIS = Obarvi(ČERNÁ,  NA_SIVÉ,  nadtržítko = '=',  podtržítko = '=',  formát = '*** {} ***',  odsazení = 10)
H1 = NADPIS
H2 = Obarvi(ČERNÁ,  NA_SIVÉ,  formát = '| {} |',  nadtržítko = '_',  podtržítko = '-',  odsazení = 10)
H3 = Obarvi(ČERNÁ,  NA_SIVÉ,   nadtržítko = '-.',  podtržítko = '-.',  odsazení = 10)

INFO  = Obarvi(BÍLÁ,  NA_TMAVĚ_ČERVENÉ)
CHYBA  = Obarvi(ŽLUTÁ,  NA_TMAVĚ_ČERVENÉ)

PŘÍKAZ = Obarvi(PROHOĎ_BARVU_A_POZADÍ)
#BÍLÁ,  NA_TMAVĚ_ČERVENÉ,  PROHOĎ_BARVU_A_POZADÍ
SOUBOR = Obarvi(PROHOĎ_BARVU_A_POZADÍ)
#Obarvi(BÍLÁ,  TUČNĚ,  NA_TMAVĚ_SIVÉ)
OBJEKT = Obarvi(SIVÁ,  TUČNĚ,  NA_ČERNÉ)
