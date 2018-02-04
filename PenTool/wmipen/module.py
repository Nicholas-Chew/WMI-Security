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
        for root, dirs, filenames in os.walk("module"):
            for filename in filenames:
                if filename.endswith(".py") and not filename == "__init__.py":
                    file = os.path.join(root,filename)
                    modules.append((file[7:])[:-3])
                    
        return modules


    

    
        

        

        