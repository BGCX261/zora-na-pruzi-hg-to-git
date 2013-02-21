#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který vytvoří odkazy na adresář zora_na_pruzi v systému
'''

PYTHON_DIR = '/usr/local/lib/python3.2/dist-packages/'
ZORA_NA_PRUZI = 'zora_na_pruzi'

def nastavím_odkazy():
    '''
    spouštím funkci main()
    '''
    import os
    
    hen = os.path.dirname(__file__)
    vývojový_adresář = os.path.realpath(os.path.join(hen,  '../',  ZORA_NA_PRUZI))
    build_dir = os.path.abspath(os.path.join(hen,  '../build/lib.linux-x86_64-3.2',  ZORA_NA_PRUZI))
    python_dir = os.path.join(PYTHON_DIR,  ZORA_NA_PRUZI)
    
    def vytvořím_odkaz(zdroj,  cíl):

        if os.path.exists(cíl) and os.path.samefile(zdroj,  cíl):
            print('Odkaz {} -> {} je v pořádku'.format(zdroj,  cíl))
            return True
        
        if os.path.islink(cíl):
            print('Jestvuje odkaz {}'.format(build_dir))
            if input('Zda-li mám smazat odkaz {} -> {}?\n da - ne >>  '.format(cíl,  os.path.realpath(cíl))) in ('da'):
                os.unlink(cíl)
                print('\tsmazáno')
            else:
                print('Tož dobrá, ale nebude to správně nastavené.')
                return False
                
        if os.path.isdir(cíl):
            raise NotImplementedError('Odkaz {} jestvuje jako adresář, ale to zatím neumím řešit. Zkus jej ručně smazat, nebo přesunout.'.format(cíl))
            
        if os.path.isfile(cíl):
            raise NotImplementedError('Odkaz {} jestvuje jako soubor, ale to zatím neumím řešit. Zkus jej ručně smazat, nebo přesunout.'.format(cíl))
        
        
        příkaz = 'ln -s {} {}'.format(zdroj,  cíl)
        print('spouštím',  příkaz)
        os.system(příkaz)
            
    vytvořím_odkaz(vývojový_adresář,  build_dir)
    vytvořím_odkaz(build_dir,  python_dir)

if __name__ == '__main__':

    print(__doc__)

    nastavím_odkazy()
