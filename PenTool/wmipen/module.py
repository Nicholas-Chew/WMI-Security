# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 2018

@author: Chew Zhi Jie
"""

import protocol.wsman as wsman
import protocol.dcom as dcom

from abc import abstractmethod
import os
import sys
sys.path.append('../')


class Module(object):
    NAME = ""
    DESCRIPTION = ""
    AUTHOR = ""
    options = []

    def connect(self, options):
        if options.get('PROTOCOL') == "DCOM":
            self.session = dcom.DCOM(options)
        else:
            self.session = wsman.WSMan(options)

    def execute(self, options):
        self.connect(options)
        self.run(options)
        self.close()

    def close(self):
        try:
            self.session.close()
        except Exception:
            pass

    @abstractmethod
    def run(self, options):
        pass

    @abstractmethod
    def help(self):
        pass


class Modules:
    @staticmethod
    def avaliableModule():
        modules = []
        for root, dirs, filenames in os.walk("module"):
            for filename in filenames:
                if filename.endswith(".py") and not filename == "__init__.py":
                    file = os.path.join(root, filename)
                    modules.append((file[7:])[:-3])

        return modules
