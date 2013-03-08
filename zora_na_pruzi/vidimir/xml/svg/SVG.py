#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

from zora_na_pruzi.vidimir.__SOUBOR import __SOUBOR

class SVG(__SOUBOR):
       
    def __call__(self):
        
        import lxml.etree
        
        xml_stylesheet = lxml.etree.PI('xml-stylesheet', "href='{}' type='text/css'")
        xml_stylesheet = lxml.etree.tounicode(xml_stylesheet,  pretty_print=True)
        
        print(self.obsah.xml_deklarace)
        print(xml_stylesheet)
        
        from zora_na_pruzi import __version__,  __author__
        from datetime import date
            
        def rok():
            letos = date.today().timetuple()[0]
            if letos > 2012:
                return '2012 - {}'.format(letos)
            else:
                return '2012'
         
        obsah = self.obsah
      
        obsah.insert(0, lxml.etree.Comment('Изготовила Зора на прузи {verze} ©Домоглед {autor} {rok} on {datum}'.format(verze = __version__, datum = date.today().isoformat(),  autor = __author__,  rok = rok())))
        obsah.insert(1, lxml.etree.Comment('http://domogled.eu'))
        obsah.insert(2, lxml.etree.Comment('http://code.google.com/p/zora-na-pruzi/'))
        
        print(obsah)
