#!/usr/bin/env python3
'''
Toto je elegantní přesměrování za pomocí streamu
zachytávání do proměnné je myslím bezpečné.
Pro zachytávání do souboru je asi lepší použít příklad z Dive into Python
který najdu zde v jiném souboru

Created on 30.4.2011

@author: golf
'''

if __name__ == '__main__':
    
    import time
    start = time.time()
    
    import io
    import sys
    
    print('Testy\n**************')
    
    
    # záloha abych mohl zase obnovit vypisování na standartní výstup
    stdout = sys.stdout
    print("standartní výstup je object:", sys.stdout)
    output_buffer = io.StringIO("some initial text data")
    print("záchytný výstup je object:", output_buffer)
    
    #přímý zápis do záchytného výstupu, dvě možnosti
    output_buffer.write('Přímý zápis pomocí output_buffer.write(text).\n')
    print('Přímý zápis pomocí print(text, ..., file=output_buffer)', file=output_buffer)
    
    # přesměrování
    sys.stdout = output_buffer
    
    print('standartní výstup je přesměrován')
    x = 45
    testovací_kód = "print('Tento text se vyhodnotí pomocí exec() a i s proměnou %i' % x)"
    #eval(testovací_kód)
    exec(testovací_kód)
    
    # obnovíme standartní výstup
    sys.stdout = stdout
    
    # načteme zachycený výstup
    obsah = output_buffer.getvalue()
    print("zachycený výstup\n------------------\n%s-------------------" % obsah)
    
    # slušně zavřeme zachytávací výstup
    output_buffer.close()
    
    print("čas běhu testu {čas:.3f} ms".format(čas = 1000*(time.time() - start)))
