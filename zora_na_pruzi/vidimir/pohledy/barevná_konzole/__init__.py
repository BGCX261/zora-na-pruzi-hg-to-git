from zora_na_pruzi.vidimir.stroj.konzole.obarvi import OBARVI
from zora_na_pruzi.vidimir.stroj.konzole.barvy import *

NADPIS = OBARVI(ČERNÁ,  NA_SIVÉ,  nadtržítko = '=',  podtržítko = '=',  formát = '*** {} ***',  odsazení = 10)
H1 = NADPIS
H2 = OBARVI(ČERNÁ,  NA_SIVÉ,  formát = '| {} |',  nadtržítko = '_',  podtržítko = '-',  odsazení = 10)
H3 = OBARVI(ČERNÁ,  NA_SIVÉ,   nadtržítko = '-.',  podtržítko = '-.',  odsazení = 10)

INFO  = OBARVI(BÍLÁ,  NA_TMAVĚ_ČERVENÉ)
CHYBA  = OBARVI(ŽLUTÁ,  NA_TMAVĚ_ČERVENÉ)

PŘÍKAZ = OBARVI(PROHOĎ_BARVU_A_POZADÍ)
#BÍLÁ,  NA_TMAVĚ_ČERVENÉ,  PROHOĎ_BARVU_A_POZADÍ
SOUBOR = OBARVI(PROHOĎ_BARVU_A_POZADÍ)
#OBARVI(BÍLÁ,  TUČNĚ,  NA_TMAVĚ_SIVÉ)
OBJEKT = OBARVI(SIVÁ,  TUČNĚ,  NA_ČERNÉ)
