#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

import py.test

def test_0001_připojení_databáze ():
    '''
    testuji
    '''
    x = 45
        
    assert isinstance(x,  int)
    
    with py.test.raises(AttributeError):
        x.a
        
if __name__ == '__main__':
    from zora_na_pruzi.iskušitel  import spustím_test,  zobrazím_log_jako_html_stránku

    spustím_test(__file__)
        
    zobrazím_log_jako_html_stránku()
