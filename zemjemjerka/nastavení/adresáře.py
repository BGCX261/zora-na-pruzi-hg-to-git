# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

"""
zde jsou nastavení balíčku zemjemjerka
"""

import os
    
ADRESÁŘ_GDE_ULOŽÍM_STAŽENÁ_DATA_OSM_PBF = "/home/pruga/data/osm/pbf" 
DOČASNÝ_ADRESÁŘ_PRO_IMPORT_PBF = "/home/pruga/tmp"
ADRESÁŘ_GDE_ULOŽÍM_DATA_PŘEVEDENÁ_Z_OSM_PBF_DO_PGSQL_DUMP = "/home/pruga/data/osm/pgsql_dump" 

SEZNAM_SOUBORÚ_KE_STAŽENÍ = os.path.join(os.path.dirname(__file__) or '.',  "seznamy_souborů_ke_stažení/geofabrik.txt")  

ADRESÁŘ_POSTGISU = '/usr/share/postgresql/9.1/contrib/postgis-1.5/'
ADRESÁŘ_OSMOSIS_SQL_DB_SCHEMA = '/usr/share/doc/osmosis/examples/pgsnapshot_schema_0.6.sql'
ADRESÁŘ_SQL_SKRIPTOV_ZEMJEMJERKY = '/home/pruga/sql/zemjemjerka'
    
#
#__JMÉNO_ADRESÁŘE_GDE_ULOŽÍM_DATA_Z_PBF = "data-dump"
#
#def davaj_adresář_gde_uložím_data_z_pbf(jméno_pbf_souboru):
#    ADRESÁŘ_GDE_ULOŽÍM_DATA_Z_PBF = os.path.realpath(os.path.join("../instalace",  __JMÉNO_ADRESÁŘE_GDE_ULOŽÍM_DATA_Z_PBF))
#    return os.path.join(ADRESÁŘ_GDE_ULOŽÍM_DATA_Z_PBF,  os.path.splitext(os.path.basename(jméno_pbf_souboru))[0])
