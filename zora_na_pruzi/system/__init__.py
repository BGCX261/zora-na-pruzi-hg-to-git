
import os

TEMP_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '../../.temp'))
if not os.path.isdir(TEMP_DIR):
    print('nejestvuje dočasný adresář "{}", idu da ho vytvořím.'.format(TEMP_DIR))
    os.mkdir(TEMP_DIR)
    import stat
    os.chmod(TEMP_DIR,  stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)

if not os.access(TEMP_DIR, os.W_OK | os.R_OK):
    print('dočasný adresář "{}" nemá dostatek práv pro zápis a čtení , idu da ich nastavím.'.format(TEMP_DIR))
    import stat
    os.chmod(TEMP_DIR,  stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
    if not os.access(TEMP_DIR, os.W_OK | os.R_OK):
        import sys
        print( 'Do dočasného adresáře "{}" nelze zapisovat. UKONČÍM PROGRAM {}'.format(TEMP_DIR,  sys.argv[0]))
        sys.exit()
