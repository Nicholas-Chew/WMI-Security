# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 2018

@author: Chew Zhi Jie
"""
import sys
sys.path.append('../')
import wmipen.core
from wmipen.inclass import inclass

@inclass(wmipen.core.Core)
def do_search(self, s):
    for module in self.modules:
        print (module)
    
@inclass(wmipen.core.Core)
def help_search(self):
    print ("Usage set [option] [value]")
    print ("\nSet the given option to value. If value is omitted, print the current value.")