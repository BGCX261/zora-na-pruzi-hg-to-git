#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

def pomocí_import():

    
    _temp = __import__('zora_na_pruzi.system', globals(), locals(), ['html_prohlížeč', 'spustím_příkaz',  'TEMP_DIR'], 0)
    print(_temp)
    print(type(_temp))
    modul = getattr(_temp,  'html_prohlížeč')
    print(modul)
    temp_dir = getattr(_temp,  'TEMP_DIR')
    print(temp_dir)
    print(type(temp_dir))
#    eggs = _temp.eggs
#    saus = _temp.sausage
    
if __name__ == '__main__':
    
    pomocí_import()
