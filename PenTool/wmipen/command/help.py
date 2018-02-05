# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 14:57:23 2018

@author: root
"""
import sys
sys.path.append('../')
import wmipen.core
from wmipen.inclass import inclass

@inclass(wmipen.core.Core)    
def do_help(self, s):
    print """
    Core Commands
    =============
    
        Command        Description
        -------        -----------
        options        Display the WMI connection parameter for the current session
        search         Searches module name
        set            Set WMI connection parameter
        use            Set module by name
    
    Module Commands
    ===============
         
        Command        Description
        -------        -----------
        info           Display all WMI connection parameter
        run            Execute the current active module
    """
 
