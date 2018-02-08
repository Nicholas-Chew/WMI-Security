# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 13:48:11 2018

@author: Chew Zhi Jie
"""
import wmipen.core
from wmipen.inclass import inclass

import sys
sys.path.append('../')


@inclass(wmipen.core.Core)
def do_set(self, s):
    arg = s.split()

    if len(arg) < 2:
        print ("Unknown variable")
        self.help_set()
        return

    if self.options.set(arg[0], arg[1]):
        print (arg[0] + " => " + arg[1])
    else:
        print ("Unknown variable " + arg[0])


@inclass(wmipen.core.Core)
def help_set(self):
    print ("Usage set [option] [value]")
    print ("\nSet the given option to value. If value is omitted, print the current value.")
