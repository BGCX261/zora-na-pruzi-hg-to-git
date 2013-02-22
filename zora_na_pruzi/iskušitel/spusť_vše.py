#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

MASKA_TESTOVACÍCH_SOUBORŮ = 'testuji_*.py'

if __name__ == '__main__':

    __version__ = 0.1

    from zora_na_pruzi.iskušitel import spustím_test,  zobrazím_log_jako_html_stránku
    import argparse
    import os
#    import glob
#    import sys
    import fnmatch


    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser()

#   a pak mu nastavím jaké příkazy a parametry má přijímat
    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, искушител {}'.format(__version__))
    
    parser.add_argument('cesta')
#    parser.add_argument('maska_souborů')
    parser.add_argument('-l', '--log',  action='store_false',  help = 'vypne zobrazení html logu')
    
    #    a včíl to možu rozparsovat
    args = parser.parse_args()

    def projdi_a_najdi(cesta):
        if os.path.isdir(cesta):

            print('SPOUŠTÍM TESTY {} z adresáře "{}"'.format(MASKA_TESTOVACÍCH_SOUBORŮ,  cesta))

            for cesta_do_adresáře, nalezené_adresáře, nalezené_soubory in os.walk(cesta):
                for jméno_nalezeného_souboru in nalezené_soubory:
                    if fnmatch.fnmatch(jméno_nalezeného_souboru, MASKA_TESTOVACÍCH_SOUBORŮ):
#                    if jméno_nalezeného_souboru.endswith('.py')  and not  jméno_nalezeného_souboru.startswith('__init__'):
                        cesta_k_nalezenému_souboru = os.path.join(cesta_do_adresáře, jméno_nalezeného_souboru)
                        yield cesta_k_nalezenému_souboru
        else:
            yield cesta
         
    počet_testů = -1
    for počet_testů,  soubor_testu in enumerate(projdi_a_najdi(args.cesta)):
#        print(počet_testů, soubor_testu)
        print('{} spouštím {}'.format(počet_testů + 1, soubor_testu))
        spustím_test(soubor_testu)

    if počet_testů == -1:
        print('Nenašel jsem žádný testovací soubor vyhovující jménem {}, žádný test nemohl být proveden.'.format(MASKA_TESTOVACÍCH_SOUBORŮ))
    else:
        print('Dotestováno. Počet nalezených testovacích souborů je {}'.format(počet_testů + 1))

        if args.log:
            zobrazím_log_jako_html_stránku()



