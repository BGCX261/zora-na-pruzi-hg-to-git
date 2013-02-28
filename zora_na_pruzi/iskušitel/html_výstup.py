#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který zobrazí log jako html stránku
'''

import os,  sys

from zora_na_pruzi.system import  TEMP_DIR
VÝSLEDKY_TESTŮ_DO_SOUBORU = os.path.join(TEMP_DIR, 'výsledky_testování.html')
        
#class HTML_VÝSTUP():
#    
#    def __init__(self,  html_soubor = VÝSLEDKY_TESTŮ_DO_SOUBORU):
#        self.__html_soubor = html_soubor
##
##    def __getattr__(self,  jméno):
##        return getattr(self.__stream,  jméno)
##        
##    def close(self):
##        print(' KLOSE '*44)
##        self.__stream.close()
#        
#    def __enter__(self):
#        self.__stdout = sys.stdout
#        self.__stream = open(self.__html_soubor,  mode ='w',  encoding = 'UTF-8')
#        sys.stdout = self.__stream
#        print(self.__hlavička())
#        
#    def __exit__(self, *args):
#        print(self.__patička())
#        self.__stream.close()
#        sys.stdout = self.__stdout


def css_styly():
    
    return '''
    body {margin: 4px;}
    p {margin: 2px 2px;}
    h1, h2, h3, h4, h5, h6 {margin: 4px;}
        .DEBUG {
    background-color: green;
            }
            .INFO {
                background-color: white;
                border:
            }
            .WARNING {
                background-color: yellow;
            }
            .ERROR {
                background-color: orange;
            }
            .CRITICAL {
                background-color: red;
            }
            .ramecek {border-top: 1px solid navy; margin-top: .3em}
    '''
    
def hlavička(soubor = VÝSLEDKY_TESTŮ_DO_SOUBORU):
    
    return '''
    <!DOCTYPE html>
<html lang="cs-cz" dir="ltr">
  <head>
      <meta charset="utf-8" />
      <title>Зора на прузи TESTUJI {soubor}</title>
      <style type="text/css">
        {css}
        </style>
  </head>
  <body>
    '''.format(soubor = soubor ,  css = css_styly())

def patička():
    return '''
    </body>
</html>
    '''
    
#def zobrazím_v_prohlížeči():
#    PYTHON_BIN = 'python3'
#    import subprocess
#    from zora_na_pruzi.system import html_prohlížeč
#
#    příkaz = [PYTHON_BIN,  html_prohlížeč.__file__,  self.__html_soubor]
#    subprocess.Popen(příkaz)
    #    subprocess.call(['./zobrazím_log.py'])
    
    
#if __name__ == '__main__':
#
#    html = HTML_VÝSTUP()
#    html.zobrazím_v_prohlížeči()



    
