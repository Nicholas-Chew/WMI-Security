# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 13:48:11 2018

@author: Chew Zhi Jie
"""
import sys
sys.path.append('../')
import WMIPen.core
from WMIPen.inclass import inclass

@inclass(WMIPen.core.Core)
def do_set(self, s):
    arg = s.split()
    
    if len(arg)<2:
        print ("Unknown variable")
        self.help_set()
        return
    
    if self.options.set(arg[0], arg[1]):
        print (arg[0] + " => " + arg[1])
    else:
        print ("Unknown variable " + arg[0])
    
@inclass(WMIPen.core.Core)
def help_set(self):
    print ("Usage set [option] [value]")
    print ("\nSet the given option to value. If value is omitted, print the current value.")

