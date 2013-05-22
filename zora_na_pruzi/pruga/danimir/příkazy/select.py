#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je třída pro tvorbu SQL příkazu SELECT
'''

#from ..prvky_databáze.formát import formát_názvu,  formát_hodnoty
from ..prvky_databáze.tabulka_databáze import tabulka_databáze
from ..prvky_databáze.sloupec_tabulky import sloupec_tabulky
from ..prvky_databáze.spojení import spojení

from ._příkaz import _příkaz

class SELECT(_příkaz):
    
    '''
    Tato třída umožní snadno sestavit SQl příkaz SELECT
    
    '''
    
    def __init__(self,  *args): # ,  **kwargs
        for sloupec in args:
            povolené_typy = (sloupec_tabulky,  str,  tabulka_databáze)
            if not isinstance(sloupec,  povolené_typy):
                raise TypeError('Sloupec tabulky musí být jedním z datového typu {}, ale je typu {}'.format('\n'.join(map(str,  povolené_typy)),  type(sloupec)))
          
        self.__sloupce = tuple(args)
        self.__tabulka =  None
        self.__where = None
        self.__order_by = None
        self.__group_by = None
        self.__join = None
        
#        for alias,  sloupec in kwargs.items():
#            if not isinstance(sloupec,  sloupec_tabulky):
#                raise TypeError('Sloupec tabulky musí být typu sloupec_tabulky, ale je typu {}'.format(type(sloupec)))
#     
  
    def FROM(self,  tabulka):
#        print(type(tabulka))
#        print(tabulka_databáze)
#        print(isinstance(tabulka,  tabulka_databáze))
        if not isinstance(tabulka,  tabulka_databáze):
            raise TypeError('Databázová tabulka musí být typu tabulka_databáze, ale je typu {}'.format(type(tabulka)))
            
        self.__tabulka = tabulka
        return self

    def WHERE(self,  where):
        self.__where = where
        return self

    def ORDER_BY(self,  *args):
        
        order_by = []
        
        for sloupec in args:
            
            if isinstance(sloupec,  str):
                sloupec = sloupec_tabulky(jméno = sloupec,  tabulka = self.__tabulka)
                
            if not isinstance(sloupec,  sloupec_tabulky):
                raise TypeError('Sloupec pro řazení dat musí být řetězec, nebo sloupec tabulky, ale je typu {}'.format(type(sloupec)))

            order_by.append(sloupec)
            
        self.__order_by = order_by
        
        return self
        
    def GROUP_BY(self,  *args):
        
        group_by = []
        
        for sloupec in args:
            
            if isinstance(sloupec,  str):
                sloupec = sloupec_tabulky(jméno = sloupec,  tabulka = self.__tabulka)
                
            if not isinstance(sloupec,  sloupec_tabulky):
                raise TypeError('Sloupec pro seskupení dat musí být řetězec, nebo sloupec tabulky, ale je typu {}'.format(type(sloupec)))

            group_by.append(sloupec)
            
        self.__group_by = group_by
        
        return self

    def JOIN(self,  první_tabulka,  druhá_tabulka):
        join = spojení(první_tabulka,  druhá_tabulka)
        
        if self.__join is None:
            self.__join = []

        self.__join.append(join)
        
        return self

    def __str__(self):
        tabulka = self.__tabulka
        if not len(self.__sloupce):
            sloupce = '*'
        else:
            sloupce = ', '.join(map(self.__formát_sloupce, self.__sloupce))
        
        sql = []
        sql.append('SELECT {sloupce} FROM {tabulka}'.format(sloupce = sloupce,  tabulka = tabulka))
        
        if self.__join is not None:
            for join in self.__join:
                sql.append(str(join))
        
        if self.__where is not None:
            sql.append('WHERE')
            sql.append(str(self.__where))
            
        if self.__order_by is not None:
            sql.append('ORDER BY')
            sql.append(','.join(map(str,  self.__order_by)))
            
        if self.__group_by is not None:
            sql.append('GROUP BY')
            sql.append(','.join(map(str,  self.__group_by)))
            
        return '\n'.join(sql)
        
    def __formát_sloupce(self,  sloupec):
        if isinstance(sloupec,  tabulka_databáze):
            return '{}.*'.format(str(sloupec))
        elif isinstance(sloupec,  str):
            if sloupec == '*':
                return sloupec
            else:
                sloupec = getattr(self.__tabulka,  sloupec)
 
        return str(sloupec)


    

if __name__ == '__main__':

    print(__doc__)
    
    import doctest
    doctest.testmod()
#    from pruga.pohunci.logování.termcolor.termcolor import cprint
#    x = cprint('TESTUJI SELECT', color='blue')
#    print(x,  type(x))

#    main()



