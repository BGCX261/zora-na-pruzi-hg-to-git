#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

def main():
    '''
    spouštím funkci main()
    '''
    print(main.__doc__)

if __name__ == '__main__':

    from zora_na_pruzi.system.spustím_příkaz import spustím_příkaz
    
    import argparse  
    #  nejdříve si parser vytvořím
    parser = argparse.ArgumentParser()
    parser.add_argument('slovo')
#    parser.add_argument('maska_souborů')
    #    a včíl to možu rozparsovat
    args = parser.parse_args()
    
    příkaz = 'grep -R "{}" *'.format(args.slovo)

    spustím_příkaz(příkaz)
