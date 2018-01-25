# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 2018

@author: Chew Zhi Jie
"""
import abc
class Module(abc.ABC):
    NAME = ""
    DESCRIPTION = ""
    AUTHOR = ""
    options = []
        
    @abc.abstractmethod      
    def run(self):
        pass
    @abc.abstractmethod
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
    

    
        

        

        