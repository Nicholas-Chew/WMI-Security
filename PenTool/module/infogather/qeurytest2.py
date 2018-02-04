# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 2018

@author: Chew Zhi Jie
"""
import sys
sys.path.append('../')
import wmipen.module
import protocol.wmic as wmic

class QeuryTest2(wmipen.module.Module):
    
    NAME = "Query Test 2"
    DESCRIPTION = "A simple wmic get Win32_Process"
    AUTHOR = ['Chew Zhi Jie']
        
    def help(self):
        print(self.DESCRIPTION)
        
    def run(self, options):  
        query = wmic.WMIC(options)
        query.gwmi("select * from Win32_Bus")
    
    
    
    