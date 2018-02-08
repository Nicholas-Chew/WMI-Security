# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 2018

@author: Chew Zhi Jie
"""
import wmipen.core
from wmipen.inclass import inclass

import sys
sys.path.append('../')


@inclass(wmipen.core.Core)
def do_info(self, s):
    if hasattr(self, 'module'):
        self.module.help()
    else:
        print("No active module. Please use ""use [module_name]"" to start interacting with the module.")


@inclass(wmipen.core.Core)
def help_info(self):
    print ("Display the infomation for current active module.")   
