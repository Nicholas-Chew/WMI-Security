# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 2018

@author: Chew Zhi Jie
"""
from abc import abstractmethod
class Module(object):
    NAME = ""
    DESCRIPTION = ""
    AUTHOR = ""
    options = []
        
    @abstractmethod      
    def run(self):
        pass
    @abstractmethod
    def help(self):
        pass
    
import os
class Modules:
    @staticmethod
    def avaliableModule():
        modules = []
        for file in os.listdir("module/"):
            if file.endswith(".py"):
                modules.append(file[:-3])
        return modules
    

    
        

        

        