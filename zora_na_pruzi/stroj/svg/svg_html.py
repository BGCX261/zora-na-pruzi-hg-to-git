#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

if __name__ == '__main__':
    from vytvořím_svg_příklad import davaj_svg
    from zora_na_pruzi.stroj.html5 import index_html
    
    svg = davaj_svg()
    html = index_html.stránka()
    
    html.tělo.append(svg)
    
    print(html)
    
    from lxml.html import open_in_browser
    open_in_browser(html)
    
#    uložím_do_souboru = 'testuji.html'
#    import os
#    svg.CSS >> '{}.{}'.format(os.path.splitext(uložím_do_souboru)[0],  'css')
#    html >> uložím_do_souboru
#
#    import webbrowser
#    webbrowser.open(uložím_do_souboru)
