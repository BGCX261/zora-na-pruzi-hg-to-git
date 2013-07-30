def jakoby_instaluji(jméno_databáze = 'NENE'):
    return 'Chtěl bych nainstalovat {}'.format(jméno_databáze)

def instaluji_neo4j(jméno_databáze,  instalační_soubor):
    import os
    if not os.path.isfile(instalační_soubor):
        _instalační_soubor = instalační_soubor
        instalační_soubor = os.path.join(os.path.dirname(__file__),  instalační_soubor)
        if not os.path.isfile(instalační_soubor):
            raise IOError('Nenašel jsem instalační soubor "{}", ani hen "{}".'.format(_instalační_soubor,  instalační_soubor)) 
            
    from .. import server

    if server.jestvuje_databáze(jméno_databáze):
        raise AttributeError('Databáze jména "{}" již jestvuje'.format(jméno_databáze))
       
    import tarfile
       
    tar = tarfile.open(instalační_soubor, 'r')
    
    jméno_rozbaleného_tar = tar.members[0].name
    print('tar src',  jméno_rozbaleného_tar)
    
    import shutil
    TEMP_ADRESÁŘ = os.path.join(os.path.dirname(__file__),  '__TEMP__')
    if os.path.isdir(TEMP_ADRESÁŘ):
        print('mažu',  TEMP_ADRESÁŘ)
        shutil.rmtree(TEMP_ADRESÁŘ)
        print('vytvářím',  TEMP_ADRESÁŘ)
        os.mkdir(TEMP_ADRESÁŘ)
      
    print('rozbaluji {} do {}'.format(instalační_soubor,  TEMP_ADRESÁŘ))
    tar.extractall(TEMP_ADRESÁŘ)
        
    cesta_k_nové_databázi = os.path.join(os.path.dirname(server.__file__),  jméno_databáze)
    print(cesta_k_nové_databázi)
    
    cesta_rozbaleného_tar = os.path.join(TEMP_ADRESÁŘ,  jméno_rozbaleného_tar)
    print('přesouvám {} do {}'.format(cesta_rozbaleného_tar,  cesta_k_nové_databázi))
    shutil.move(cesta_rozbaleného_tar,  cesta_k_nové_databázi)
    
    print('mažu',  TEMP_ADRESÁŘ)
    shutil.rmtree(TEMP_ADRESÁŘ)
    
    
    zdroj_init_py = os.path.join(os.path.dirname(__file__),  '__init__.py.pruga')
    cíl_init_py = os.path.join(cesta_k_nové_databázi,  '__init__.py')
    print('přidávám __init__.py do {} ==> {}'.format(zdroj_init_py,  cíl_init_py))
    shutil.copy(zdroj_init_py, cíl_init_py)
               
