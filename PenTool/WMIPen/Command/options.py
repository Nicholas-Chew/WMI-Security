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
def do_options(self, s):
    formats = '\t{0:<12}{1:<20}{2:<8}{3:<16}'
    print (formats.format("NAME", "VALUE", "REQ", "DESCRIPTION"))
    print (formats.format("-----","------------", "----", "-------------"))
    
    for option in self.options.options:
        require = "yes" if option.required else "no"
        print (formats.format(option.name, option.value, require, option.description))
 
@inclass(WMIPen.core.Core)
def help_options(self):
    print ("Qurries the options for the current Session")
