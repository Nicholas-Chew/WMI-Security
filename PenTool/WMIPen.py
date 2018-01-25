# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 2018

@author: Chew Zhi Jie
"""

_version = "0.1"
_author = "chewzhijie"

if __name__ == "__main__":
    
    import wmipen.core

    banner = open("Data/banner.txt", "rb").read().decode("unicode_escape")
    
    coreLoop = wmipen.core.Core(banner,_version)
    coreLoop.prompt = 'WMIPen > '
    coreLoop.cmdloop()

