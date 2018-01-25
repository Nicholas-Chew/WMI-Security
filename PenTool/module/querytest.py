# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 2018

@author: Chew Zhi Jie
"""
import wmipen.module

class QueryTest(wmipen.module.Module):
    
    NAME = "Query Test"
    DESCRIPTION = "A simple wmic get Win32_Process"
    AUTHOR = ['Chew Zhi Jie']
        
    def help(self):
        print(self.DESCRIPTION)
        
    def run(self):
        print(self.NAME)
        
