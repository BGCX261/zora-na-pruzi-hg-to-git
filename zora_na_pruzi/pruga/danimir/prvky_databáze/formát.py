#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen sú udělátka na formátování v SQL příkazu
'''

import datetime,  time

def formát_názvu(název):
    '''
    formát názvu sloupce, databáze atd.
    '''
    return '"{}"'.format(název)


def formát_hodnoty(hodnota):
#   nejdřív zjistíme,  zda ide o datum,  pokud ano,  převedem jej na řetězec a dále zpracujeme jako řetězec
    if isinstance(hodnota,  (datetime.datetime, datetime.date)):
#  print(type(hodnota))
        hodnota = str(hodnota)
            
    if hodnota is None:
        return 'NULL'
    elif isinstance(hodnota,  str):
        return ("'{}'".format(hodnota))
    else:
        return str(hodnota)

#if __name__ == '__main__':
#
#    print(__doc__)
#
#    main()



