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
def do_run(self, s):
    if hasattr(self, 'module'):
        self.module.execute(self.options)
    else:
        print("No such command")


@inclass(wmipen.core.Core)
def help_run(self):
    if hasattr(self, 'module'):
        print("Lunch the module")
    else:
        print("No active module. Please use ""use [module_name]"" to start interacting with the module.")
