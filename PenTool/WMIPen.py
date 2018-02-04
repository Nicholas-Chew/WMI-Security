#!/usr/bin/env python
"""
Created on Tue Jan 23 2018

@author: Chew Zhi Jie
"""

__author__ = "chewzhijie"

__version__ = "0.1"


if __name__ == "__main__":
    import wmipen.core

    banner = open("data/banner.txt", "rb").read().decode("utf-8")
    
    coreLoop = wmipen.core.Core(banner,__version__)
    coreLoop.prompt = 'WMIPen > '
    coreLoop.cmdloop()

