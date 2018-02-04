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
def do_options(self, s):
    formats = '\t{0:<12}{1:<20}{2:<8}{3:<16}'
    print (formats.format("NAME", "VALUE", "REQ", "DESCRIPTION"))
    print (formats.format("-----","------------", "----", "-------------"))
    
    for option in self.options.options:
        require = "yes" if option.required else "no"
        print (formats.format(option.name, option.value, require, option.description))
 
@inclass(wmipen.core.Core)
def help_options(self):
    print ("Display the WMI connection parameter for the current session")
