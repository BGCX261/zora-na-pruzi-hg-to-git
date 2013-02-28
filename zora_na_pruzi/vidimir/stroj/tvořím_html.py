#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''


'''


if __name__ == '__main__':
    
    import lxml.html
    from lxml.html import builder as E

    
#    html = E.P('{}', E.CLASS('třída'), styl='styl')

html = E.P('{}', E.CLASS('třída'), styl='styl')
    
kód =  lxml.html.tostring(html,   pretty_print=False,    encoding='unicode')
#    .decode(encoding = 'UTF-8')

#    print(kód)
    
print("Formát(formát = '{}')".format(kód))
    
   
def třídu(html):
    kód =  lxml.html.tostring(html,   pretty_print=False,    encoding='unicode')
    return "Formát(formát = '{}')".format(kód)
  
#    lxml.html.html_to_xhtml(html)
#    kód =  lxml.html.tostring(html,   pretty_print=False).decode(encoding = 'UTF-8')
#    print(kód)

for číslo in range(1, 6):
    tag = 'H{}'.format(číslo)
#    print(tag)
    html = getattr(E,  tag)('{}')
    print("{} = {}".format(tag,  třídu(html)))
    
for tag in 'P',  'DIV',  'SPAN':
    html = getattr(E,  tag)('{}')
    print("{} = {}".format(tag,  třídu(html)))
    
for třída in 'INFO',  'CHYBA',  'SOUBOR',  'PŘÍKAZ',  'OBJEKT':
    html = E.SPAN('{}', E.CLASS(třída))
    print("{} = {}".format(třída,  třídu(html)))
