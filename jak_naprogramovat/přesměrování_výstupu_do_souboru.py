#!/usr/bin/env python3
'''
Toto je složitější varianta přesměrování.
Příklad z knihy Dive into Python3
Přesměruje do souboru přes pomocnou třídu.

Jiné řešení je přesměrování za pomocí proudu
(to možná nefunguje pro soubory, ale do proměnné to dostat lze)
takový příklad najdu v jiném souboru - hledej podle názvu


Created on 30.4.2011

@author: golf
'''

'''
<?php

ob_start();

echo "Hello World";

$out = ob_get_clean();

var_dump($out);
?>

'''

import sys

class RedirectStdoutToOutputBuffer:
    '''
    přesměruje standartní výstup
    vytvořeno za účelem vyhodnocení testů
    nahrazuje ob_start() a ob_get_clean() z PHP
    '''
    
    def __init__(self, out_new):
        self.out_new = out_new


    def __enter__(self):
        self.out_old = sys.stdout
        sys.stdout = self.out_new  
        
    def __exit__(self, *args):
        sys.stdout = self.out_old

# nastavení locale kvůli výpisu data
import locale
locale.setlocale(locale.LC_ALL, '')

from datetime import datetime
       
with open('přesměrování_výstupu.log', encoding='utf-8', mode='a') as test_output, RedirectStdoutToOutputBuffer(test_output):
    print("%s přesměrovaný výstup" % datetime.strftime(datetime.now(), "%A, %d.%B %Y, %H:%M:%S"))
