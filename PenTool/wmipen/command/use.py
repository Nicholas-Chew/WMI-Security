# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 2018

@author: Chew Zhi Jie
"""
import sys
sys.path.append('../')
import wmipen.core
from wmipen.inclass import inclass

@inclass(wmipen.core.Core)    
def do_use(self, s):
    import importlib
    import inspect
    import wmipen.module
    
    #Clear up the previous module if exists
    if hasattr(self,'module'):
        del self.module
    
    #Import and initialize module
    try:
        mod = s.replace('/','.')
        env = importlib.import_module("module."+ mod)
        for name, obj in inspect.getmembers(env):
            if inspect.isclass(obj) and issubclass(obj, wmipen.module.Module):
                self.module = obj()
        self.prompt = 'WMIPen('+ s +') > '
    except ImportError:
        print("ImportError: Failed to load module: "+s)
    except RuntimeError:
        print("RuntimeError: Failed to load module: "+s)

@inclass(wmipen.core.Core)
def complete_use(self, text, line, begidx, endidx):
    return [i for i in self.modules if i.startswith(text)]

@inclass(wmipen.core.Core) 
def help_use(self):
    print("Usage use [module_name]")
    print("\nThe use command is for interacting with module.")