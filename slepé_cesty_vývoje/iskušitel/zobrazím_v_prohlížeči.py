#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který zobrazí log jako html stránku
'''

   
def zobrazím_v_prohlížeči(html_soubor = None):
    
    if html_soubor is None:
        from zora_na_pruzi.iskušitel.html_výstup import VÝSLEDKY_TESTŮ_DO_SOUBORU
        html_soubor = VÝSLEDKY_TESTŮ_DO_SOUBORU
    
#    PYTHON_BIN = 'python3'
#    import subprocess
    from zora_na_pruzi.system import html_prohlížeč
    from zora_na_pruzi.system.spustím_příkaz import spustím_příkaz

    příkaz = [html_prohlížeč.__file__,  html_soubor]
    spustím_příkaz(příkaz)
    #    subprocess.call(['./zobrazím_log.py'])
        
        
if __name__ == '__main__':
    
    zobrazím_v_prohlížeči()



    
