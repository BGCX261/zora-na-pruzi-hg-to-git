def davaj_seznam_databází():
    '''
    spouštím funkci main()
    '''
    import os
    
    for adresář in os.listdir(os.path.dirname(__file__)):
        if adresář.startswith('_'):
            continue
        yield adresář
        
def jestvuje_databáze(jméno_databáze):
    import os
    cesta_k_databázi = os.path.join(os.path.dirname(__file__),  jméno_databáze)
    return os.path.isdir(cesta_k_databázi)
