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
def do_exit(self, s):
    return True
 
@inclass(WMIPen.core.Core) 
def help_exit(self):
    print ("Exit the interpreter.")
    print ("You can also use the Ctrl-D shortcut.")