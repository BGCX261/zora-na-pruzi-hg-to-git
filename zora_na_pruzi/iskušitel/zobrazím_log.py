#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který zobrazí log jako html stránku
'''

import os

LOGUJ_DO_SOUBORU = os.path.join(os.path.dirname(__file__), 'log.html')

def zobrazím_log_jako_html_stránku():
    '''
    zahájí běh programu
    '''
    
    if not os.path.isfile(LOGUJ_DO_SOUBORU):
        raise IOError('Nejestvuje soubor "{}", nemožu jej zobrazit.'.format(LOGUJ_DO_SOUBORU))
    
    import sys
#    from PyQt4.QtCore import QUrl
    from PyQt4.QtGui import QApplication
    from PyQt4.QtWebKit import QWebView

    app = QApplication(sys.argv)

    web = QWebView()

    with open(file = LOGUJ_DO_SOUBORU,  mode = 'r', encoding = 'utf8') as soubor:
        obsah = soubor.read()
        
        
    css = '''
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
    hlavička = '''
    <!DOCTYPE html>
<html lang="cs-cz" dir="ltr">
  <head>
      <meta charset="utf-8" />
      <title>Зора на прузи {soubor}</title>
      <style type="text/css">
        {css}
        </style>
  </head>
  <body>
    '''.format(soubor = LOGUJ_DO_SOUBORU,  css = css)
    
    patička = '''
    </body>
</html>
    '''
    obsah = '\n'.join((hlavička,  obsah,  patička))
    
    with open(file = LOGUJ_DO_SOUBORU,  mode = 'w', encoding = 'utf8') as soubor:
        soubor.write(obsah)

    web.setHtml(obsah)
    web.show()

    sys.exit(app.exec_())


if __name__ == '__main__':

#    print(__doc__)

    try:
        zobrazím_log_jako_html_stránku()
    except IOError as e:
        print(e)



