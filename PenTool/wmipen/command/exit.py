# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 2018

@author: Chew Zhi Jie
"""
import sys
sys.path.append('../')
import wmipen.core
from wmipen.inclass import inclass

@inclass(wmipen.core.Core)    
def do_exit(self, s):
    return True
 
@inclass(wmipen.core.Core) 
def help_exit(self):
    print("Exit the interpreter")
