# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 13:24:56 2018

@author: Chew Zhi Jie
"""
import os
import cmd

import WMIPen.option

class Core(cmd.Cmd, object):
    def __init__(self, banner, version):
        self.banner = banner
        self.version = version
        
        self._import_command_()
        
        self._init_option_()
        super(Core,self).__init__()
        
    def _init_option_(self):
        self.options = WMIPen.option.Options()
        
        self.options.add("RHOST","0.0.0.0", True, "The target address")
        self.options.add("RDOMAIN",".", True, "The target domain")
        self.options.add("RUSER","Administrator", True, "The target username")
        self.options.add("RPASS","", True, "The target password")
    
    def preloop(self):
        self._print_banner_()
        super(Core,self).preloop()
        
    def postloop(self):
        print ("Goodbye")
        super(Core,self).postloop()
        
    def _print_banner_(self):
        os.system("clear")
        print(self.banner % (self.version))
        
    def _import_command_(self):
        for file in os.listdir("WMIPen/Command/"):
            if file.endswith(".py"):
                exec(open("WMIPen/Command/"+file).read())
    

