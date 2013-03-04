#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který st8hne a spustí instalaci IDE Eric
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

import os

GDE_ULOŽÍM_SOUBORY = os.path.join(os.path.dirname(__file__ ),  'instalace/eric')


def stáhnu(verze):
    '''
    spouštím funkci main()
    '''
    
    print('Stáhnu Eric IDE verze {}'.format(verze))
#    verze = '5.3.1'

    import httplib2
    h = httplib2.Http(GDE_ULOŽÍM_SOUBORY)
    
    zdroj = 'http://sourceforge.net/projects/eric-ide/files/eric5/stable/{0}/eric5-{0}.tar.gz/download'.format(verze)
    zdroj_lokalizace = 'http://sourceforge.net/projects/eric-ide/files/eric5/stable/5.3.1/eric5-i18n-cs-{}.tar.gz/download'.format(verze)
    
    def vytvářím_adresář(cesta):
        if not os.path.isdir(cesta):
            rodičovský_adresář= os.path.dirname(cesta)
            if not os.path.isdir(rodičovský_adresář):
                vytvářím_adresář(rodičovský_adresář)
            print('Vytvářím adresář {}'.format(cesta))
            os.mkdir(cesta)
    
    vytvářím_adresář(GDE_ULOŽÍM_SOUBORY)
    
    def stahuji(zdroj):
    
        print('Stahuji {}'.format(zdroj))
        hlavička, obsah_souboru = h.request(zdroj)
        if not hlavička['status'] == '200':
#            print(response)
            raise ValueError('Selhalo hledání zdroje {}, vrátilo {}'.format(zdroj,  hlavička))
        else:
            jméno_souboru = os.path.basename(hlavička['content-location'])
            uložím_do_souboru = os.path.join(GDE_ULOŽÍM_SOUBORY,  jméno_souboru)
#            print(hlavička)
            print('soubor nalezen, uložím jej do {}'.format(uložím_do_souboru))
            if hlavička['content-type'] in ['image/jpeg',  'application/x-gzip']:
                with open(uložím_do_souboru, mode='wb') as proud:
                    proud.write(obsah_souboru)
                    if hlavička['content-type'] == 'application/x-gzip':
                        print('rozbalím tar.gz archív')
                        import tarfile
                        # tar file path to extract
                        rozbalím_do_adresáře = GDE_ULOŽÍM_SOUBORY
                         
                        # open the tar file
                        tar_soubor = tarfile.open(uložím_do_souboru)
                         
                        if tarfile.is_tarfile(uložím_do_souboru):
#                            # list all contents
#                            print "tar file contents:"
#                            print tfile.list(verbose=False)
#                            # extract all contents
                            tar_soubor.extractall(rozbalím_do_adresáře)
                        else:
                            print ("{} není archív typu .tar.".format(uložím_do_souboru))
                        
                        
                    
            else:
                with open(uložím_do_souboru, mode='w', encoding='utf-8') as proud:
                    proud.write(obsah_souboru.decode('utf-8'))
        
        
    stahuji(zdroj)
    stahuji(zdroj_lokalizace)
    

def nainstaluji(verze):
    adresář_instalace = os.path.join(GDE_ULOŽÍM_SOUBORY,  'eric5-{0}'.format(verze))
    if not os.path.isdir(adresář_instalace):
        raise ValueError('Instalční adresář {} nejestvuje'.format(adresář_instalace))

    hen = os.getcwd()
    os.chdir(adresář_instalace)
    for příkaz in 'python3 ./install.py',  'python3 ./install-i18n.py':
        print('spouštím příkaz {}'.format(příkaz))
        os.system(příkaz)
    
    os.chdir(hen)
    
    import shutil
    shutil.rmtree(GDE_ULOŽÍM_SOUBORY)
    
    
    
    
    

if __name__ == '__main__':

    print(__doc__)

    import argparse
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser()

#   a pak mu nastavím jaké příkazy a parametry má přijímat
    parser.add_argument('--version', '-v',  action='version', version='%(prog)s, искушител {}'.format(__version__))
    
    parser.add_argument('verze')
    parser.add_argument('--nestahuj',  action='store_true',  help = 'vynechám stahování')
    parser.add_argument('--neinstaluj',  action='store_true',  help = 'neprovedu instalaci')
    
    #    a včíl to možu rozparsovat
    args = parser.parse_args()

    print(args)

    if not args.nestahuj is True:
        stáhnu(args.verze)
    if not args.neinstaluj is True:
        nainstaluji(args.verze)
