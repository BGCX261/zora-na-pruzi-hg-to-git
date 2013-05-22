#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je třída, která reprezentuje datový typ pro číslo účtu, aby se to pěkně parsovalo do SQL řetězce
'''

class ROW():
    
    def __init__(self,  syntetický,  analytický):
        self.syntetický = syntetický
        self.analytický = analytický
        
    def __str__(self):
        return 'ROW({},{})'.format(self.syntetický,  self.analytický)
        
    def __repr__(self):
        return 'ROW({},{})'.format(self.syntetický,  self.analytický)

