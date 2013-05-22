#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který ...
'''

from sqlalchemy import create_engine
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
    
engine = create_engine('postgresql+pypostgresql://golf:marihuana@localhost:5432/zemjemjerka',  echo=True)
metadata = MetaData(bind=engine,  schema='osm')

Session = sessionmaker(bind = engine)
session = Session()

def main():
    '''
    zahájí běh programu
    '''
    
#    připojovací_řetězec = 'postgresql+pypostgresql://golf:marihuana@localhost:5432/zemjemjerka'
#    engine = create_engine('sqlite:///:memory:', echo=True)
#    engine = create_engine(připojovací_řetězec, echo=True)
#    pitanje = engine.execute("select * FROM osm.users")
#    .scalar()
#    print(pitanje)
#    
#    for x in pitanje:
#        print(x)



    from sqlalchemy.schema import Table

#    from sqlalchemy import types

#    tabulka_uživatelů = Table('users', metadata,
#            Column('id', types.BigInteger, primary_key=True),
#            Column('name', types.Text)
#        )
    
#    tabulka_uživatelů =  Table('users',  metadata,  autoload = True)
    metadata.reflect(bind = engine)
    tabulka_uživatelů = metadata.tables['users']
    
    print('SELECT',  type(tabulka_uživatelů.select()))

#    from sqlalchemy.orm import mapper

#    mapper(Users, tabulka_uživatelů)

#    pitanje = session.query(Users).order_by(Users.id)
#    print(pitanje)

#    for instance in session.query(Users).order_by(Users.id): 
    for instance in session.query(tabulka_uživatelů).order_by(tabulka_uživatelů.id): 
        print(instance.id,  instance.name)
#        break
    
    
#    print(Nodes.__table__)
#    Base.metadata.create_all(engine) 

def info():
    for jméno_tabulky in engine.table_names(schema = 'osm'): 
#        schema=None, connection=None
        print(jméno_tabulky)
        
        
def inspektor():
    from sqlalchemy.engine.reflection import Inspector
    inspektor = Inspector.from_engine(engine)
    
    for index in inspektor.get_indexes('nodes', schema='osm'):
        print(index)
 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,  BigInteger,  Text
    
Base = declarative_base()
class Users(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    name = Column('name', Text)
    schema = 'osm'
    
#    def __init__(self, name):
#        self.name = name
#
#    def __repr__(self):
#        return "<User(’%s’)>" % (self.name)

def ako_rade_filter():
    from sqlalchemy import select, func
    metadata = MetaData(bind=engine,  schema='osm')
    
    tabulka_uživatelů = Table('users', metadata, autoload=True)
    print('tabulka_uživatelů',  tabulka_uživatelů,  type(tabulka_uživatelů))
    pitanje = tabulka_uživatelů.select()

    sloupec = tabulka_uživatelů.c.id
    print('sloupec',  sloupec,  type(sloupec))
    
    where = sloupec==5
    print('where',  where,  type(where))
    where = sloupec > 25
    
#    print('pitanje',  pitanje,  type(pitanje))
#    for řádek in pitanje():
#        print(řádek)

def select():
    from sqlalchemy import select, func
    metadata = {}
    metadata['osm'] = MetaData(bind=engine,  schema='osm')
    metadata['zemjemjerka'] = MetaData(bind=engine,  schema='zemjemjerka')
#    tabulka_relací = metadata.tables['relations']
#    tabulka_uživatelů = Table('users', metadata, autoload=True)
    tabulka_bodů_v_cestách = Table('way_nodes', metadata['osm'], autoload=True)
    pohled_body_s_utm = Table('osm_nodes_s_utm_souřadnicemi', metadata['zemjemjerka'], autoload=True)
#    pitanje = pohled_body_s_utm.select()

    
    propojeni =  tabulka_bodů_v_cestách.join(pohled_body_s_utm,  tabulka_bodů_v_cestách.c.node_id == pohled_body_s_utm.c.id)
#    pitanje = pitanje.limit(5, 5)
    pitanje = tabulka_bodů_v_cestách.select(propojeni)
    pitanje = pitanje.limit(5)
    print(pitanje)
    for řádek in pitanje():
        print(řádek)
    
    
    
#    dotaz = select([b.c.published_year, func.count('*').label('n')], from_obj=[b], group_by=[b.c.published_year])
#    dotaz = select([func.count('*').label('počet')], from_obj=[tabulka_uživatelů])
#    dotaz = select([tabulka_uživatelů]).execute()
#    for řádek in dotaz:
#        print(řádek['id'],  řádek['name'])
#        for sloupec in řádek:
#            print(sloupec)


if __name__ == '__main__':

    print(__doc__)

#    main()
#    select()
    ako_rade_filter()


