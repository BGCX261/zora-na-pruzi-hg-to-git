#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Tento skript zobrazí html stránku v prohlížeči
'''
import os

def zobrazím_html_stránku(html_soubor):
    '''
    vytvoří prohlížeč pomocí PyQt a zobrazí v něm stránku
    '''
    
    if not os.path.isfile(html_soubor):
        raise IOError('Nejestvuje soubor "{}", nemožu jej zobrazit.'.format(html_soubor))
    
    import sys
#    from PyQt4.QtCore import QUrl
    from PyQt4.QtGui import QApplication
    from PyQt4.QtWebKit import QWebView

    with open(file = html_soubor,  mode = 'r', encoding = 'UTF-8') as soubor:
        obsah = soubor.read()
        
       
    #    prohlížeč = davaj_prohlížeč()
    app = QApplication(sys.argv)
    prohlížeč = QWebView()
    
    prohlížeč.setHtml(obsah)
    prohlížeč.show()

    sys.exit(app.exec_())


if __name__ == '__main__':

    import argparse
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('html_soubor')
    
    args = parser.parse_args()

    try:
        zobrazím_html_stránku(args.html_soubor)
    except IOError as e:
        print('Selhalo zobrazení html stránky {}'.format(args.html_soubor))
        print(e)



