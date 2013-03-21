#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

#v systému
import webbrowser

webbrowser.open(url)

#nebo v lxml,  který to výše uvedené používá

from lxml.html import open_in_browser
open_in_browser(element)
