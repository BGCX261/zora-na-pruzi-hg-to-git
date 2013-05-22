#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je test správného tvoření SQL dotazů Danimírem
'''

import unittest

from danimir import databáze
from danimir.příkazy import SELECT,  INSERT,  UPDATE
from danimir.připojení import testovací_databáze

db = databáze(testovací_databáze)
tabulka = db.první_tabulka

class Vytváříš_správné_SQL(unittest.TestCase):
    
    def test_0000_SELECT_ (self):
        def příkaz():
            return str(SELECT().FROM(tabulka))
        má_být = '''
    SELECT * FROM "první_tabulka"
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))


    def test_0001_SELECT_ (self):
        def příkaz():
            return str(SELECT(None).FROM(tabulka))
        self.assertRaises(TypeError, příkaz)


    def test_0002_SELECT_ (self):
        def příkaz():
            return str(SELECT(tabulka).FROM(tabulka))
        má_být = '''
    SELECT "první_tabulka".* FROM "první_tabulka"
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))


    def test_0003_SELECT_ (self):
        def příkaz():
            return str(SELECT(tabulka.sloupec1).FROM(tabulka))
        má_být = '''
    SELECT "první_tabulka"."sloupec1" FROM "první_tabulka"
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))


    def test_0004_SELECT_ (self):
        def příkaz():
            return str(SELECT(tabulka.sloupec1,  tabulka.sloupec2).FROM(tabulka))
        má_být = '''
    SELECT "první_tabulka"."sloupec1", "první_tabulka"."sloupec2" FROM "první_tabulka"
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))


    def test_0005_SELECT_ (self):
        def příkaz():
            return str(SELECT('*').FROM(tabulka))
        má_být = '''
    SELECT * FROM "první_tabulka"
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))


    def test_0006_SELECT_ (self):
        def příkaz():
            return str(SELECT(tabulka.sloupec1.AS('medved')).FROM(tabulka))
        má_být = '''
    SELECT "první_tabulka"."sloupec1" AS "medved" FROM "první_tabulka"
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))


    def test_0007_SELECT_ (self):
        def příkaz():
            return str(SELECT('sloupec1',  'sloupec2').FROM(tabulka))
        má_být = '''
    SELECT "první_tabulka"."sloupec1", "první_tabulka"."sloupec2" FROM "první_tabulka"
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))


    def test_0008_SELECT_ (self):
        def příkaz():
            return str(SELECT(tabulka.sloupec1.AS('medved')).FROM('jméno_tabulky'))
        self.assertRaises(TypeError, příkaz)


    def test_0009_INSERT_ (self):
        def příkaz():
            return str(INSERT(tabulka).VALUES(sloupec1 = 25,  sloupec2 = 'řetězec'))
        má_být = '''
    INSERT INTO
    "první_tabulka"
    ("sloupec1","sloupec2")
    VALUES
        (25,'řetězec')
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))


    def test_0010_INSERT_ (self):
        def příkaz():
            return str(INSERT(tabulka).VALUES(sloupec1 = 25,  sloupec2 = 'řetězec').VALUES(sloupec1 = 45,  sloupec2 = 'řetězec dva'))
        má_být = '''
    INSERT INTO
    "první_tabulka"
    ("sloupec1","sloupec2")
    VALUES
        (25,'řetězec'),
        (45,'řetězec dva')
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))


    def test_0011_INSERT_ (self):
        def příkaz():
            return str(INSERT(tabulka).VALUES(sloupec1 = 25,  sloupec2 = 'řetězec').VALUES( 45,  'řetězec dva'))
        self.assertRaises(ValueError, příkaz)


    def test_0012_INSERT_ (self):
        def příkaz():
            return str(INSERT(tabulka).INTO(tabulka.sloupec1,  'sloupec2').VALUES(sloupec1 = 25,  sloupec2 = 'řetězec').VALUES( 45,  'řetězec dva').VALUES('třetí', sloupec1 = 100))
        má_být = '''
    INSERT INTO
    "první_tabulka"
    ("sloupec1","sloupec2")
    VALUES
        (25,'řetězec'),
        (45,'řetězec dva'),
        (100,'třetí')
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))


    def test_0013_INSERT_ (self):
        def příkaz():
            return str(INSERT(tabulka).VALUES(sloupec1 = 25,  sloupec2 = 'řetězec').VALUES(sloupec2 = 'řetězec dva',  sloupec1 = 12))
        má_být = '''
    INSERT INTO
    "první_tabulka"
    ("sloupec1","sloupec2")
    VALUES
        (25,'řetězec'),
        (12,'řetězec dva')
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))


    def test_0014_INSERT_ (self):
        def příkaz():
            return str(INSERT(tabulka).VALUES(sloupec1 = 25,  sloupec2 = 'řetězec').VALUES(sloupec2 = 'řetězec dva'))
        self.assertRaises(ValueError, příkaz)


    def test_0015_INSERT_ (self):
        def příkaz():
            return str(INSERT(tabulka).INTO(tabulka.sloupec1,  'sloupec2').VALUES(sloupec1 = 25,  sloupec100 = 'řetězec'))
        self.assertRaises(ValueError, příkaz)


    def test_0016_INSERT_ (self):
        def příkaz():
            return str(INSERT(tabulka).INTO(tabulka.sloupec1,  'sloupec2').VALUES(25, 'řetězec').VALUES(11,  'druhý',  'přebývající'))
        self.assertRaises(ValueError, příkaz)


    def test_0017_INSERT_ (self):
        def příkaz():
            return str(INSERT(tabulka).VALUES(sloupec2 = 'řetězec',  sloupec1 = 25).VALUES(12,  'dva').VALUES('tři',  3))
        self.assertRaises(ValueError, příkaz)


    def test_0018_INSERT_ (self):
        def příkaz():
            return str(INSERT(tabulka).VALUES(sloupec1 = 25,  sloupec2 = 'řetězec').VALUES(12,  'dva').VALUES('tři',  3))
        self.assertRaises(ValueError, příkaz)


    def test_0019_INSERT_ (self):
        def příkaz():
            return str(INSERT(tabulka).INTO(tabulka.sloupec1,  tabulka.sloupec2.AS('alias názvu')).VALUES(sloupec1 = 25,  sloupec2 = 'řetězec').VALUES( 45,  'řetězec dva').VALUES('třetí', sloupec1 = 100))
        má_být = '''
    INSERT INTO
    "první_tabulka"
    ("sloupec1","sloupec2")
    VALUES
        (25,'řetězec'),
        (45,'řetězec dva'),
        (100,'třetí')
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))


    def test_0020_UPDATE_ (self):
        def příkaz():
            return str(UPDATE(tabulka))
        self.assertRaises(ValueError, příkaz)


    def test_0021_UPDATE_ (self):
        def příkaz():
            return str(UPDATE(tabulka).SET(sloupec1 = 25,  sloupec2 = 'gora'))
        má_být = '''
    UPDATE
    "první_tabulka"
    SET
    "sloupec1"=25,"sloupec2"='gora'
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))


    def test_0022_UPDATE_ (self):
        def příkaz():
            return str(UPDATE(tabulka).SET(sloupec1 = 25,  sloupec2 = 'gora').WHERE(1))
        má_být = '''
    UPDATE
    "první_tabulka"
    SET
    "sloupec1"=25,"sloupec2"='gora'
    WHERE
    1
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))


    def test_0023_UPDATE_ (self):
        def příkaz():
            return str(UPDATE(tabulka).SET(sloupec1 = 25,  sloupec2 = 'gora').WHERE(1 == 1))
        má_být = '''
    UPDATE
    "první_tabulka"
    SET
    "sloupec1"=25,"sloupec2"='gora'
    WHERE
    True
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))


    def test_0024_UPDATE_ (self):
        def příkaz():
            x = 2
            return str(UPDATE(tabulka).SET(sloupec1 = 25,  sloupec2 = 'gora').WHERE(x == 1))
        má_být = '''
    UPDATE
    "první_tabulka"
    SET
    "sloupec1"=25,"sloupec2"='gora'
    WHERE
    False
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))


    def test_0025_UPDATE_ (self):
        def příkaz():
            x = 2
            return str(UPDATE(tabulka).SET(sloupec1 = 25,  sloupec2 = 'gora').WHERE(x == 2))
        má_být = '''
    UPDATE
    "první_tabulka"
    SET
    "sloupec1"=25,"sloupec2"='gora'
    WHERE
    True
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))


    def test_0026_UPDATE_ (self):
        def příkaz():
            return str(UPDATE(tabulka).SET(sloupec1 = 25,  sloupec2 = 'gora').WHERE(tabulka.sloupec == 2))
        má_být = '''
    UPDATE
    "první_tabulka"
    SET
    "sloupec1"=25,"sloupec2"='gora'
    WHERE
    "první_tabulka"."sloupec"=2
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))


    def test_0027_UPDATE_ (self):
        def příkaz():
            return str(UPDATE(tabulka).SET(sloupec1 = 25,  sloupec2 = 'gora').WHERE(tabulka.sloupec == db.jiná_tabulka.její_sloupec))
        má_být = '''
    UPDATE
    "první_tabulka"
    SET
    "sloupec1"=25,"sloupec2"='gora'
    WHERE
    "první_tabulka"."sloupec"="jiná_tabulka"."její_sloupec"
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))


    def test_0028_UPDATE_ (self):
        def příkaz():
            return str(UPDATE(tabulka).SET(sloupec1 = 25,  sloupec2 = 'gora').WHERE(tabulka.sloupec >= db.jiná_tabulka.její_sloupec))
        má_být = '''
    UPDATE
    "první_tabulka"
    SET
    "sloupec1"=25,"sloupec2"='gora'
    WHERE
    "první_tabulka"."sloupec">="jiná_tabulka"."její_sloupec"
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))


    def test_0029_UPDATE_ (self):
        def příkaz():
            return str(UPDATE(tabulka).SET(sloupec1 = 25,  sloupec2 = 'gora').WHERE((tabulka.sloupec > db.jiná_tabulka.její_sloupec).AND (tabulka.sloupec > 5)))
        má_být = '''
    UPDATE
    "první_tabulka"
    SET
    "sloupec1"=25,"sloupec2"='gora'
    WHERE
    ("první_tabulka"."sloupec">"jiná_tabulka"."její_sloupec")  AND  ("první_tabulka"."sloupec">5)
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))


    def test_0030_UPDATE_ (self):
        def příkaz():
            return str(UPDATE(tabulka).SET(sloupec1 = 25,  sloupec2 = 'gora').WHERE((tabulka.sloupec > db.jiná_tabulka.její_sloupec).OR(tabulka.sloupec > 5)))
        má_být = '''
    UPDATE
    "první_tabulka"
    SET
    "sloupec1"=25,"sloupec2"='gora'
    WHERE
    ("první_tabulka"."sloupec">"jiná_tabulka"."její_sloupec")  OR  ("první_tabulka"."sloupec">5)
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))

    def test_0031_SELECT_hstore (self):
        def příkaz():
            return str(SELECT(tabulka.sl_hstore).FROM(tabulka))
        má_být = '''
    SELECT "první_tabulka"."sl_hstore" FROM "první_tabulka"
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))


    def test_0032_SELECT_hstore (self):
        def příkaz():
            return str(SELECT(tabulka.sl_hstore['qwert']).FROM(tabulka))
        má_být = '''
    SELECT "první_tabulka"."sl_hstore"->'qwert' FROM "první_tabulka"
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))


    def test_0033_SELECT_hstore (self):
        def příkaz():
            return str(SELECT(tabulka.sl_hstore['qwert',  'klíč2',  'klíč3']).FROM(tabulka))
        má_být = '''
    SELECT "první_tabulka"."sl_hstore"->ARRAY['qwert','klíč2','klíč3'] FROM "první_tabulka"
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))

    def test_0034_SELECT_hstore (self):
        def příkaz():
            return str(SELECT(tabulka.sl_hstore['qwert',  'klíč2',  'klíč3'].AS('klíče')).FROM(tabulka))
        má_být = '''
        SELECT "první_tabulka"."sl_hstore"->ARRAY['qwert','klíč2','klíč3'] AS "klíče" FROM "první_tabulka"
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))

    def test_0035_SELECT_schéma (self):
        def příkaz():
            tabulka = db['moje_schéma'].první_tabulka
            return str(SELECT(tabulka.sloupec1,  tabulka.sloupec2).FROM(tabulka))
        má_být = '''
    SELECT "moje_schéma"."první_tabulka"."sloupec1", "moje_schéma"."první_tabulka"."sloupec2" FROM "moje_schéma"."první_tabulka"
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))
        
    def test_0036_SELECT_hstore (self):
        def příkaz():
            return str(SELECT(tabulka.sloupec1,  tabulka.sloupec2).FROM(tabulka).WHERE(tabulka.sloupec2['klíč'] == 'hodnota'))
        má_být = '''
    SELECT "první_tabulka"."sloupec1", "první_tabulka"."sloupec2" FROM "první_tabulka" WHERE "sloupec2"@>'"klíč"=>"hodnota"'
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))

    def test_0037_SELECT_ORDER_BY (self):
        def příkaz():
            return str(SELECT(tabulka).FROM(tabulka).ORDER_BY(tabulka.sloupec_řazení))
        má_být = '''
    SELECT "první_tabulka".* FROM "první_tabulka" ORDER BY "první_tabulka"."sloupec_řazení"
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))
        
    def test_0038_SELECT_ORDER_BY (self):
        def příkaz():
            return str(SELECT(tabulka).FROM(tabulka).ORDER_BY(tabulka.sloupec_řazení,  tabulka.jiný_sloupec))
        má_být = '''
    SELECT "první_tabulka".* FROM "první_tabulka" ORDER BY "první_tabulka"."sloupec_řazení","první_tabulka"."jiný_sloupec"
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))
        
    def test_0039_SELECT_ORDER_BY (self):
        def příkaz():
            return str(SELECT(tabulka).FROM(tabulka).ORDER_BY('nějaký_sloupec',  tabulka.jiný_sloupec))
        má_být = '''
    SELECT "první_tabulka".* FROM "první_tabulka" ORDER BY "první_tabulka"."nějaký_sloupec","první_tabulka"."jiný_sloupec"
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))
        
    def test_0039_SELECT_ORDER_BY (self):
        def příkaz():
            return str(SELECT(tabulka).FROM(tabulka).ORDER_BY(tabulka.sloupec_řazení.ASC(),  tabulka.jiný_sloupec.DESC()))
        má_být = '''
    SELECT "první_tabulka".* FROM "první_tabulka" ORDER BY "první_tabulka"."sloupec_řazení" ASC,"první_tabulka"."jiný_sloupec" DESC
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))
        
    def test_0040_SELECT_WHERE (self):
        def příkaz():
            return str(SELECT(tabulka.sloupec1,  tabulka.sloupec2).FROM(tabulka).WHERE(tabulka.sloupec2['klíč'] .LIKE('hodnota')))
        má_být = '''
    SELECT "první_tabulka"."sloupec1", "první_tabulka"."sloupec2" FROM "první_tabulka" WHERE "první_tabulka"."sloupec2"->'klíč' LIKE 'hodnota'
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))
        
    def test_0041_SELECT_JOIN (self):
        def příkaz():
            return str(SELECT().FROM(tabulka).JOIN(tabulka,  db.druhá_tabulka))
        má_být = '''
    SELECT * FROM "první_tabulka" JOIN "druhá_tabulka"  ON "první_tabulka"."id_druhá_tabulka" = "druhá_tabulka"."id"
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))
        
    def test_0042_SELECT_JOIN (self):
        def příkaz():
            return str(SELECT().FROM(tabulka).JOIN(tabulka.sloupec1,  db.druhá_tabulka.sloupec2))
        má_být = '''
    SELECT * FROM "první_tabulka" JOIN "druhá_tabulka"  ON "první_tabulka"."sloupec1" = "druhá_tabulka"."sloupec2"
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))
        
    def test_0043_SELECT_funkce (self):
        def příkaz():
            return str(SELECT(db.max(tabulka.sloupec1),  db.moja_funkce('řetězec',  1,  tabulka.sloupec2)).FROM(tabulka))
        má_být = '''
    SELECT "max"("první_tabulka"."sloupec1"), "moja_funkce"(řetězec,1,"první_tabulka"."sloupec2") FROM "první_tabulka"
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))
        
    def test_0044_SELECT_funkce (self):
        def příkaz():
            return str(SELECT(db.max(tabulka.sloupec1).AS('největší'),  db.moja_funkce('řetězec',  1,  tabulka.sloupec2)).FROM(tabulka))
        má_být = '''
    SELECT "max"("první_tabulka"."sloupec1") AS "největší", "moja_funkce"(řetězec,1,"první_tabulka"."sloupec2") FROM "první_tabulka"
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))
        
    def test_0044_WHERE (self):
        def příkaz():
            where = db.max(tabulka.sloupec1) == 5
            where.AND(db.tabulka.sloupec2 <= db.tabulka.sloupec3)
            where.OR(db.tabulka.medved.LIKE('BRUM BRUM BRUM'))
            return str(where)
        má_být = '''
    (("max"("první_tabulka"."sloupec1")=5) AND ("tabulka"."sloupec2"<="tabulka"."sloupec3")) OR ("tabulka"."medved" LIKE 'BRUM BRUM BRUM')
    '''
        vrátilo_sa = příkaz()
        self.assertEqual(" ".join(má_být.split()), " ".join(vrátilo_sa.split()))
        
if __name__ == '__main__':
    unittest.main()
