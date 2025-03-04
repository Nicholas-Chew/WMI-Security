# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 2018

@author: Chew Zhi Jie
"""
import wmipen.core
from wmipen.inclass import inclass

import sys
sys.path.append('../')


@inclass(wmipen.core.Core)
def do_use(self, s):
    import importlib
    import inspect
    import wmipen.module

    if s == "":
        print("No module name")
        self.help_use()
        return

# Clear up the previous module if exists
    if hasattr(self, 'module'):
        del self.module

# Import and initialize module
    try:
        mod = s.replace('/', '.')
        env = importlib.import_module("module." + mod)
        for name, obj in inspect.getmembers(env):
            if inspect.isclass(obj) and issubclass(obj, wmipen.module.Module):
                self.module = obj()
        self.prompt = 'WMIPen(' + s + ') > '
    except ImportError:
        print("ImportError: Failed to load module: "+s)
    except RuntimeError:
        print("RuntimeError: Failed to load module: "+s)


# TODO: FIX the / bug here. cmd module take / as a new string
@inclass(wmipen.core.Core)
def complete_use(self, text, line, begidx, endidx):
    MODULE = self.modules

    if not text:
        completions = MODULE[:]
    else:
        completions = [i
                       for i in MODULE
                       if i.startswith(text)
                       ]

    print(completions)
    return completions


@inclass(wmipen.core.Core)
def help_use(self):
    print("Usage use [module_name]")
    print("\nThe use command is for interacting with module.")
