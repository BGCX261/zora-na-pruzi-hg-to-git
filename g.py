#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je program, který ...
'''

__version__ = '0.0.1'
__author__ = 'Петр Болф <petr.bolf@domogled.eu>'

import sys
from PySide import QtGui
 
app = QtGui.QApplication(sys.argv)
 
win = QtGui.QWidget()
 
win.resize(320, 240)  
win.setWindowTitle("Hello, World!") 
win.show()  
 
sys.exit(app.exec_())
