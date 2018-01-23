# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 13:24:56 2018

@author: Chew Zhi Jie
"""

_version = "0.1"
_author = "chewzhijie"

if __name__ == "__main__":
    
    import WMIPen.core

    banner = open("Data/banner.txt", "rb").read().decode("unicode_escape")
    
    helllo = "hello"
    coreLoop = WMIPen.core.Core(banner,_version)
    coreLoop.cmdloop()

