#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který zobrazí log jako html stránku
'''

import os

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
    body {
    margin: 0 0 2em;
    padding: 0;
}
#stranka{
    background: none repeat scroll 0 0 white;
    color: #333333;
    font: 12pt/1.5 Verdana,sans-serif;
    left: 0;
    position: absolute;
    text-align: left;
    top: 0;
    width: 100%;
    z-index: 23178;
}
* {
    background: none repeat scroll 0 0 transparent;
    border: medium none;
    color: inherit;
    font: inherit;
    margin: 0;
    padding: 0;
    text-align: inherit;
    text-indent: 0;
}
b {
    font-weight: bold;
}
i {
    font-style: italic;
}
#netteBluescreenIcon {
    background: none repeat scroll 0 0 #CD1818;
    padding: 3px;
    position: absolute;
    right: 0.5em;
    text-decoration: none;
    top: 0.5em;
    z-index: 23179;
}

h1 {
    font-size: 18pt;
    font-weight: normal;
    margin: 0.7em 0;
    text-shadow: 1px 1px 0 rgba(0, 0, 0, 0.4);
}
h2 {
    color: #888888;
    font: 14pt/1.5 sans-serif !important;
    margin: 0.6em 0;
}
a {
    color: #328ADC;
    margin: -2px -4px;
    padding: 2px 4px;
    text-decoration: none;
}
a abbr {
    color: #BBBBBB;
    font-family: sans-serif;
}
h3 {
    font: bold 10pt/1.5 Verdana,sans-serif !important;
    margin: 1em 0;
    padding: 0;
}
p, pre {
    margin: 0.8em 0;
}
pre, code, table {
    font: 9pt/1.5 Consolas,monospace !important;
}
pre, table {
    background: none repeat scroll 0 0 #FDF5CE;
    border: 1px dotted silver;
    overflow: auto;
    padding: 0.4em 0.7em;
}
table pre {
    border: medium none;
    margin: 0;
    padding: 0;
}
pre.nette-dump span {
    color: #CC2222;
}
pre.nette-dump a {
    color: #333333;
}
div.panel {
    padding: 1px 25px;
}
div.inner {
    background: none repeat scroll 0 0 #F4F3F1;
    border-radius: 8px 8px 8px 8px;
    padding: 0.1em 1em 1em;
}
table {
    border-collapse: collapse;
    width: 100%;
}
.outer {
    overflow: auto;
}
td, th {
    border: 1px solid #E6DFBF;
    padding: 2px 6px;
    text-align: left;
    vertical-align: top;
}
th {
    font-weight: bold;
    width: 10%;
}
tr:nth-child(2n), tr:nth-child(2n) pre {
    background-color: #F7F0CB;
}
ol {
    margin: 1em 0;
    padding-left: 2.5em;
}
ul {
    background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFEAAAAjCAMAAADbuxbOAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAADBQTFRF/fz24d7Y7Onj5uLd9vPu3drUzMvG09LN39zW8e7o2NbQ3NnT29jS0M7J1tXQAAAApvmsFgAAABB0Uk5T////////////////////AOAjXRkAAAKlSURBVHja7FbbsqQgDAwENEgc//9vN+SCWDtbtXPmZR/Wc6o02mlC58LA9ckFAOszvMV8xNgyUjyXhojfMVKvRL0ZHavxXYy5JrmchMdzou8YlTClxajtK8ZGGpWRoBr1+gFjKfHkJPbizabLgzE3pH7Iu4K980xgFvlrVzMZoVBWhtvouCDdcTDmTgMCJdVxJ9MKO6XxnliM7hxi5lbj2ZVM4l8DqYyKoNLYcfqBB1/LpHYxEcfVG6ZpMDgyFUVWY/Q1sSYPpIdSAKWqLWL0XqWiMWc4hpH0OQOMOAgdycY4N9Sb7wWANQs3rsDSdLAYiuxi5siVfOhBWIrtH0G3kNaF/8Q4kCPE1kMucG/ZMUBUCOgiKJkPuWWTLGVgLGpwns1DraUayCtoBqERyaYtVsm85NActRooezvSLO/sKZP/nq8n4+xcyjNsRu8zW6KWpdb7wjiQd4WrtFZYFiKHENSmWp6xshh96c2RQ+c7Lt+qbijyEjHWUJ/pZsy8MGIUuzNiPySK2Gqoh6ZTRF6ko6q3nVTkaA//itIrDpW6l3SLo8juOmqMXkYknu5FdQxWbhCfKHEGDhxxyTVaXJF3ZjSl3jMksjSOOKmne9pI+mcG5QvaUJhI9HpkmRo2NpCrDJvsktRhRE2MM6F2n7dt4OaMUq8bCctk0+PoMRzL+1l5PZ2eyM/Owr86gf8z/tOM53lom5+nVcFuB+eJVzlXwAYy9TZ9s537tfqcsJWbEU4nBngZo6FfO9T9CdhfBtmk2dLiAy8uS4zwOpMx2HqYbTC+amNeAYTpsP4SIgvWfUBWXxn3CMHW3ffd7k3+YIkx7w0t/CVGvcPejoeOlzOWzeGbawOHqXQGUTMZRcfj4XPCgW9y/fuvVn8zD9P1QHzv80uAAQA0i3Jer7Jr7gAAAABJRU5ErkJggg==") no-repeat scroll 99% 10px #F6F5F3;
    border-top: 1px solid #DDDDDD;
    color: #777777;
    font: 7pt/1.5 Verdana,sans-serif !important;
    margin: 1em 0 0;
    padding: 2em 4em;
}
.highlight {
    background: none repeat scroll 0 0 #CD1818;
    color: white;
    display: block;
    font-style: normal;
    font-weight: bold;
    margin: 0 -0.4em;
    padding: 0 0.4em;
}
.line {
    color: #9F9C7F;
    font-style: normal;
    font-weight: normal;
}
a[href^="editor:"] {
    border-bottom: 1px dotted #328ADC;
    color: inherit;
}

.TEST {
    background-color: silver;
}

.SOUBOR {
    font-style: italic;
}

.PŘÍKAZ {
    color: LimeGreen;
    background-color: black;
}

.CHYBA {
    background: none repeat scroll 0 0 #CD1818;
    color: white;
}

.INFO {
    background-color: OrangeRed;
    color: darksilver;
}
    
    '''
    
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
    
#    if soubor == VÝSLEDKY_TESTŮ_DO_SOUBORU:
#        css =  '<link type="text/css" href="styl.css" rel="stylesheet">'
#    else:
    css = '<style type="text/css">\n{css}\n</style>'.format(css = css_styly())
    
    return '''
    <!DOCTYPE html>
<html lang="cs-cz" dir="ltr">
  <head>
      <meta charset="utf-8" />
      <title>Зора на прузи TESTUJI {soubor}</title>
      
        {css}
        
  </head>
  <body>
  <div id="stranka">
    '''.format(soubor = soubor ,  css = css)

def patička():
    return '''
    </div>
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



    
