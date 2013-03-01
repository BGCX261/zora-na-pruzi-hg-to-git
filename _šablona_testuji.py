#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

import py.test

from zora_na_pruzi.vidimir import F

def test_0001_připojení_databáze ():
    '''
    testuji
    '''
    x = 45
        
    assert isinstance(x,  int)
    print('v pořádku' | F.TEST.OK)
    
    with py.test.raises(AttributeError):
        x.a
        
if __name__ == '__main__':
    from zora_na_pruzi.iskušitel  import spustím_test
    from zora_na_pruzi.iskušitel.zobrazím_v_prohlížeči import zobrazím_v_prohlížeči

    spustím_test(__file__)
        
    zobrazím_v_prohlížeči()
