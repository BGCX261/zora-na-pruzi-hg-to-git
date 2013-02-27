#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který zobrazí log jako html stránku
'''

   
def zobrazím_v_prohlížeči(html_soubor):
    PYTHON_BIN = 'python3'
    import subprocess
    from zora_na_pruzi.system import html_prohlížeč

    příkaz = [PYTHON_BIN,  html_prohlížeč.__file__,  html_soubor]
    subprocess.Popen(příkaz)
    #    subprocess.call(['./zobrazím_log.py'])
        
        
if __name__ == '__main__':

    from html_výstup import VÝSLEDKY_TESTŮ_DO_SOUBORU
    zobrazím_v_prohlížeči(VÝSLEDKY_TESTŮ_DO_SOUBORU)



    
