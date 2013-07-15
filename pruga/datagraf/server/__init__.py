def davaj_seznam_databází():
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
        
def jestvuje_databáze(jméno_databáze):
    import os
    cesta_k_databázi = os.path.join(os.path.dirname(__file__),  jméno_databáze)
    return os.path.isdir(cesta_k_databázi)

def davaj_server(jméno_databáze):
    from .Neo4j import Neo4j
    return Neo4j(jméno_databáze)
    
