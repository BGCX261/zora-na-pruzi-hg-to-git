

class __VLASTNOST(object):
    
    def __init__(self,  hodnota):
        self.__hodnota = hodnota
    
    def __str__(self):
        import io
        
        output_buffer = io.StringIO('')
        
        print(self._formát.format(self._vlastnost,  self.__hodnota),  file=output_buffer,  end='')
            
        obsah = output_buffer.getvalue()
        output_buffer.close()
        return obsah

class __BARVA(__VLASTNOST):
    _formát = '{}: #{:06X};'
    
class __VELIKOST(__VLASTNOST):
    _formát = '{0}: {1[hodnota]}{1[jednotka]};'
    
    def __init__(self,  hodnota):
        if not isinstance(hodnota,  (dict,  )):
            hodnota = {'hodnota': hodnota,  'jednotka': 'px'}
            
        if not 'hodnota' in hodnota or not 'jednotka' in hodnota:
            raise TypeError("Vlastnost VELIKOST vyžaduje zadat hodnotu a jednotku jako slovník {'hodnota': hodnota,  'jednotka': ''}")
            
        super().__init__(hodnota)

class fill(__BARVA):
    _vlastnost = 'fill'
    
class stroke(__BARVA):
    _vlastnost = 'stroke'
    
class stroke_width(__VELIKOST):
    _vlastnost = 'stroke-width'
    
