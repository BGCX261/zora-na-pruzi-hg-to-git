

from pruga.neomodel.properties import Property

class META_Uzel(type):
    
    def __new__(metatřída,  jméno_třídy,  předci,  slovník):
#        print('Izgotoviem {} si {}'.format(jméno_třídy,  slovník))
        
        slovník['__vlastnosti__'] = []
        instance = super().__new__(metatřída,  jméno_třídy,  předci,  slovník)
        
#        má předky,  není tedy třídou Uzel,  která je abstraktní
        if len(předci) > 0:
            if Uzel in předci:
#                print('SJE UZELEM')
                
                vlastnosti = slovník['__vlastnosti__'] 
                
                for klíč,  hodnota in slovník.items():
#                    print(klíč,  hodnota)
                    if issubclass(hodnota.__class__, Property):
                        hodnota.name = klíč
                        hodnota.owner = instance
                        vlastnosti.append(klíč)
                        
            else:
                raise TypeError('Ta to mosí být potomkem Uzlu, inač to nende.')
                
        return instance

class Uzel(metaclass = META_Uzel):
    
    def __init__(self,  **kwargs):
        for klíč,  hodnota in kwargs.items():
            if klíč in self.__vlastnosti__:
                setattr(self,  klíč,  hodnota)
            else:
                raise AttributeError('Třída {} nemá vlastnost {}'.format(self.__name__,  klíč))
    
    def __str__(self):
        
        vlastnosti = {klíč: getattr(self,  klíč) for klíč in self.__vlastnosti__}
        
        return '{}:{} {}'.format(self.__class__.__name__,  ':'.join(self.__labels__),  vlastnosti)


class META_VAZBA(type):
    
    def __new__(metatřída,  jméno_třídy,  předci,  slovník):
#        print('Izgotoviem {} si {}'.format(jméno_třídy,  slovník))
        
        slovník['__vlastnosti__'] = []
        slovník['__uzly__'] = ()
        instance = super().__new__(metatřída,  jméno_třídy,  předci,  slovník)
        
#        má předky,  není tedy třídou Uzel,  která je abstraktní
        if len(předci) > 0:
            if VAZBA in předci:
                
                vlastnosti = slovník['__vlastnosti__'] 
                
                for klíč,  hodnota in slovník.items():
#                    print(klíč,  hodnota)
                    if issubclass(hodnota.__class__, Property):
                        hodnota.name = klíč
                        hodnota.owner = instance
                        vlastnosti.append(klíč)
                        
            else:
                raise TypeError('Ta to mosí být potomkem Vazby, inač to nende.')
                
        return instance

class VAZBA(metaclass = META_VAZBA):
    
    def __init__(self,  počátek,  konec,  **kwargs):
        
        self.__uzly__ = počátek,  konec
#        self.__jméno__ = jméno
        
        if not isinstance(počátek,  self.__počátek__):
            raise TypeError('Počátek vazby {} musí být uzel typu {}'.format(self.__jméno__,  self.__počátek__))
            
        if not isinstance(konec,  self.__konec__):
            raise TypeError('Konec vazby {} musí být uzel typu {} a nikolivěk {}'.format(self.__jméno__,  self.__konec__,  type(konec)))
        
        for klíč,  hodnota in kwargs.items():
            if klíč in self.__vlastnosti__:
                setattr(self,  klíč,  hodnota)
            else:
                raise AttributeError('Třída {} nemá vlastnost {}'.format(self.__name__,  klíč))
    
    def __str__(self):
        
        vlastnosti = {klíč: getattr(self,  klíč) for klíč in self.__vlastnosti__}
        
        počátek,  konec = self.__uzly__
        return '({})-[:`{}`]->({}),'.format(počátek,  self.__jméno__,  konec)

