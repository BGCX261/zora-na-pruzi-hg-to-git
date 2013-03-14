#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

from . import __ELEMENT_GRAFU,  E

class __PRVEK_GRAFU(__ELEMENT_GRAFU):
    @property
    def jméno(self):
        return self.attrib['id']

    @property
    def data(self):
        return self.findall(E.DATA.TAG_NAME)
