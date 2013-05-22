#!/usr/bin/env python
# Copyright 2011 медвед медведович медведев

"""
nainstaluji data ze zálohy do databáze
"""

if __name__ == "__main__":
    
    import os
    import sys
    import argparse
    
    from zora_na_pruzi.pomocnik.spousteni_programu import spúšťám_program
    
    from zora_na_pruzi.danimir.databaze import nastavení_připojení_k_databázi
    from zora_na_pruzi.zemjemjerka.nastaveni import JMÉNO_DATABÁZE
        
    from zora_na_pruzi.zora_na_pruzi import Zora_na_pruzi
    
    app = Zora_na_pruzi(sys.argv)
    
    print(__doc__)
    
    parser = argparse.ArgumentParser()
    parser.add_argument('adresář_zálohy', metavar='adresář_zálohy', type=str,  help='cesta do adresáře, kde je umístěna záloha databáze')
    args = parser.parse_args()
        
    OSM_LOAD_SQL_SKRIPT = '/opt/osmosis-0.40.1/script/pgsnapshot_load_0.6.sql'
    ADRESÁŘ_ZÁLOHY = args.adresář_zálohy
    UPRAVENÝ_OSM_LOAD_SQL_SKRIPT = 'upraveny_pgsnapshot_load_0.6.sql'
    
    if os.path.isfile(args.adresář_zálohy):
        print("{} je soubor, zkusím najít adresář, kam byl naimportován".format(args.adresář_zálohy))
        from zora_na_pruzi.zemjemjerka.nastaveni import davaj_adresář_gde_uložím_data_z_pbf
        ADRESÁŘ_ZÁLOHY = davaj_adresář_gde_uložím_data_z_pbf(args.adresář_zálohy)
    
    if not os.path.isdir(ADRESÁŘ_ZÁLOHY):
        print("Ni adresář, ni soubor '{}' nejestvuje".format(args.adresář_zálohy))
        raise IOError("'{}' není adresářem zálohy, ani pbf souborem, který byl zálohován".format(args.adresář_zálohy))
#    app = QtGui.QApplication(sys.argv)
    
    print("měním pracovní adresář do {}".format(ADRESÁŘ_ZÁLOHY))
    adresář_odkud_byl_tento_program_spuštěn = os.getcwd()
    os.chdir(ADRESÁŘ_ZÁLOHY)
    
    print("kopíruji '{}' do '{}'".format(OSM_LOAD_SQL_SKRIPT,  os.path.join(ADRESÁŘ_ZÁLOHY,  UPRAVENÝ_OSM_LOAD_SQL_SKRIPT)))
    with open(UPRAVENÝ_OSM_LOAD_SQL_SKRIPT,  "w",  encoding='utf-8') as výstup,  open(OSM_LOAD_SQL_SKRIPT,  'r') as vstup:
        výstup.write("SET search_path TO osm, postgis;\n")
        výstup.write("DROP INDEX idx_nodes_tags;\n")
        výstup.write("DROP INDEX idx_ways_tags;\n")
        výstup.write("DROP INDEX idx_relations_tags;\n")
        výstup.write(vstup.read())
        výstup.write("CREATE INDEX idx_nodes_tags ON osm.nodes USING GIST(tags);\n")
        výstup.write("CREATE INDEX idx_ways_tags ON osm.ways USING GIST(tags);\n")
        výstup.write("CREATE INDEX idx_relations_tags ON osm.relations USING GIST(tags);\n")
        
        
#############################################################    
#          spuštění jako sql příkaz nefunguje, kvůli příkazu \copy ve skriptu, takže použijeme spuštění psql'''
##################################################################

    #db = vytvořím_databázi(JMÉNO_DATABÁZE)
    nastavení_připojení =  nastavení_připojení_k_databázi(JMÉNO_DATABÁZE)
    
    if not nastavení_připojení:
        raise Chyba_pripojeni_k_databazi("V systému nejestvuje nastavení pro připojení '{}'".format(JMÉNO_DATABÁZE))
    
#    nastavení_připojení['heslo_uživatele']
 

    
#    nastavím_schema_search_path('osm, postgis')
#    spustím_příkazy_ze_souboru(jména_souborů = ['pgsnapshot_load_0.6.sql'],  cesta = '/opt/osmosis-0.40.1/script/')
    
#    zavřu_databázové_připojení()
    
    spúšťám_program(['psql',  '-V'])
    příkaz_pro_import = ['psql', 
                        '-U', 
                        nastavení_připojení['jméno_uživatele'], 
                        '-h',  nastavení_připojení['adresa_serveru'], 
#                            '-W',  pripojeni_k_databazi_zemjemjerka['heslo'], 
#                        '-W', 
                            "-d", 
                            nastavení_připojení['jméno_databáze'], 
                            '-f', 
                            UPRAVENÝ_OSM_LOAD_SQL_SKRIPT
                            ]
    # pro etstovací účely zkusíme když bude nastaven i port    
    # nastavení_připojení['port'] = 5432
    if nastavení_připojení.get("port",  None):
        kam_přidat_port = příkaz_pro_import.index('<')
        příkaz_pro_import.insert(kam_přidat_port,  "--port={}".format(nastavení_připojení['port']))
      
    print("spustím\n", " ".join(příkaz_pro_import))
#spúšťám_program(příkaz_pro_import)
#    os.system(" ".join(příkaz_pro_import))
#    print(os.wait())
#    sys.exit()
    
    import subprocess
    
#    psql_env = dict()
    psql_env = dict(os.environ)
#    psql_env['PGPASSFILE'] = settings.DB_PASSFILE
    psql_env['PGPASSWORD'] = nastavení_připojení['heslo_uživatele']
    
    proc = subprocess.Popen(příkaz_pro_import, env=psql_env, shell = False) # ,  stderr=subprocess.PIPE, stdout=subprocess.PIPE
    proc.wait()
    
#    c = proc.communicate()
##    err = proc.communicate()[1]
#    print("*****************com\n",  c)
#    if c[1] != None:
#        print("chybička importu",  c[1])
#        
#    if c[0] != None:
#        print("výstup importu",  c[0])

    # Try reading it's data.
#    data = proc.stdout.read()

    # Check for errors.
#    err = proc.stderr.read()
#    if err:
#        raise Exception(err)
    
    print("vracím zpět pracovní adresář do '{}'".format(adresář_odkud_byl_tento_program_spuštěn))
    os.chdir(adresář_odkud_byl_tento_program_spuštěn)
    
