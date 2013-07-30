def davaj_jména_databází():
    '''
    spouštím funkci main()
    '''
    import os
    
    hen_adresář = os.path.dirname(__file__)
    
    for adresář in os.listdir(hen_adresář):
        if adresář.startswith('_'):
            continue
            
        if os.path.isdir(os.path.join(hen_adresář,  adresář)):
            yield adresář
 
#def davaj_seznam_databází():
#    return tuple(davaj_jména_databází())

def jestvuje_databáze(jméno_databáze):
    import os
    cesta_k_databázi = os.path.join(os.path.dirname(__file__),  jméno_databáze)
    return os.path.isdir(cesta_k_databázi)

def davaj_server(jméno_databáze):
    modul = '{}.{}'.format(__name__,  jméno_databáze)
    modul =  __import__(modul, globals(), locals(), [jméno_databáze])
    return modul
    
