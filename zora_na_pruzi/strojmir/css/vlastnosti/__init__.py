

class VLASTNOSTI(dict):
    
    def fill(self,  barva):
        self['fill'] = '#{:06X}'.format(barva)
        return self
        
    def stroke(self,  barva):
        self['stroke'] = '#{:06X}'.format(barva)
        return self
        
    def stroke_width(self,  velikost,  jednotka):
        self['stroke-width'] = '{}{}'.format(velikost,  jednotka)
        return self


    
#    def __str__(self):
#        
#        return '{}: {};'.format(self.vlastnost,  self.hodnota)
