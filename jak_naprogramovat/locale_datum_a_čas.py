#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import locale
locale.setlocale(locale.LC_ALL, '')



if __name__ == '__main__':
    
    from datetime import datetime

    jazyk = 'NENASTAVENO'
    print("locale %s\n\tdatum %s " % (jazyk, datetime.strftime(datetime.now(), "%A, %d.%B %Y, %H:%M:%S")))


    for jazyk in ('', 'cs', 'cs_CZ', 'czech', 'hu', 'pl', 'sk_SK'):
        try:
            locale.setlocale(locale.LC_ALL, jazyk)
        except locale.Error as e:
            print("locale {} nelze nastavit, není podporováno: {}".format(jazyk, e))
        else:
            print("locale %s\n\tdatum %s " % (jazyk or 'PRÁZDNÝ ŘETĚZEC', datetime.strftime(datetime.now(), "%A, %d.%B %Y, %H:%M:%S")))

       

    
