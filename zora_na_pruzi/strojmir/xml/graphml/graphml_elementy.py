#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

import lxml.etree
from . import NS_GRAPHML

class __ELEMENT(lxml.etree.ElementBase):
    pass
    
class graphml(__ELEMENT):
    
    def __str__(self):
        return lxml.etree.tounicode(self,  pretty_print=True)
        
    @property
    def uzly(self):
        for uzel in self.getroottree().findall('//{}'.format(NS_GRAPHML.node)):
            yield uzel.attrib['id']
    
class key(__ELEMENT):
    __default = None
    @property
    def default(self):
        if self.__default is None:
            default=self.find(NS_GRAPHML.default)
            if default is not None:
                self.__default = default.text
        return self.__default
    
class graph(__ELEMENT):
    pass
    
class node(__ELEMENT):
    pass
    
class edge(__ELEMENT):
    pass
    
#class default(__ELEMENT):
#    pass

#class data(__ELEMENT):
#    pass
