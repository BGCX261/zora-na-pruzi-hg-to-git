import os
__HEN = os.path.dirname(__file__)
__PŔÍPONA = '.cql'

def cython(soubor):
    
    if not soubor.endswith(__PŔÍPONA):
        soubor = '{}.cql'.format(soubor,  __PŔÍPONA)
    
    with open(os.path.join(__HEN,  soubor),  mode = 'r',  encoding='UTF-8') as cql_soubor:
        return cql_soubor.read()
