#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

import py.test
import os

import postgresql

def db():
        from zora_na_pruzi.danimir.připojení.postgresql import pruga_test
        from zora_na_pruzi.danimir.připojení.připojím_postgresql import postgresql_připojím_se_k_databázi
    
        from zora_na_pruzi.danimir.db import db
        return db(postgresql_připojím_se_k_databázi(pruga_test))
        
db = db()
db.execute('DELETE FROM "pruga"."uzly"')
db.execute('DELETE FROM "pruga"."klíče"')
#db.execute('SELECT setval(\'"pruga"."klíče_id_seq"\', 0)')
db.execute('ALTER SEQUENCE "pruga"."klíče_id_seq" RESTART WITH 1')
db.execute('ALTER SEQUENCE "pruga"."uzly_id_seq" RESTART WITH 1')


        
def test_připojení():
    assert isinstance(db,  postgresql.driver.pq3.Connection)

def test_nový_klíč():
    from zora_na_pruzi.danimir.najdu_či_vytvořím_klíč import najdu_či_vytvořím_klíč
    
    id_klíče = najdu_či_vytvořím_klíč('firma')
    assert id_klíče == 1
    
    id_klíče = najdu_či_vytvořím_klíč('firma')
    assert id_klíče == 1
    
    id_klíče = najdu_či_vytvořím_klíč('účet')
    assert id_klíče == 2
    

def test_nový_uzel():
    from zora_na_pruzi.danimir.nový_uzel import nový_uzel
    
    firma = nový_uzel('firma')
    
    from zora_na_pruzi.danimir.Uzel import Uzel
    assert isinstance(firma,  Uzel)
    
    assert firma._Uzel__id == 1
    
    with py.test.raises(postgresql.exceptions.NotNullError):
        uzel = nový_uzel('nejestvující_klíč')


#def test_0001_tvořím_elementy():
#    
#    html_třída = E['HTML']
#    
#    assert issubclass(html_třída,  HTML)
#    assert html_třída ==  HTML
#    
#    html_builder = E.HTML
#    html_builder_2 = E('HTML')
#    assert html_builder.__class__.__name__ == html_builder_2.__class__.__name__
#    assert str(html_builder) == str(html_builder_2)
#    
#    html = html_builder(id = 11)
#    html_2 = html_builder_2(id = 11)
#    assert str(html) == str(html_2)
#    
#    html_builder = E.HTML
#    html_builder['id'] = 245
#    html_builder_2 = E('HTML',  id = 245)
#    assert str(html_builder) == str(html_builder_2)
#    
#    html_builder = E.HTML
#    html_builder['q'] = None
#    html_builder_2 = E('HTML',  q = None)
#    assert str(html_builder) == str(html_builder_2)
#    
#    assert str(html_builder()) == str(html_builder_2())
#    
#    
