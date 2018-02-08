# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 2018

@author: Chew Zhi Jie
"""
import cmd
import os
import sys

import wmipen.module
import wmipen.option


class Core(cmd.Cmd, object):
    def __init__(self, banner, version):
        self.banner = banner
        self.version = version

        self._import_command_()
        self._import_module_()

        self._init_option_()
        super(Core, self).__init__()

    def _init_option_(self):
        self.options = wmipen.option.Options()

        self.options.add("RHOST", "10.0.75.2", True, "The target address")
        self.options.add("RDOMAIN", "", True, "The target domain")
        self.options.add("RUSER", "Administrator", True, "The target username")
        self.options.add("RPASS", "P@ssw0rd!", True, "The target username")

        if "linux" in sys.platform:
            self.options.add("PROTOCOL", "WinRM", True, "Protocol Use: WinRM(default) or DCOM")
        else:
            self.options.add("PROTOCOL", "WinRM", True, "Protocol Use: WinRM")

        self._print_banner_()

    def postcmd(self, stop, line):
        print("")
        return cmd.Cmd.postcmd(self, stop, line)

    def _print_banner_(self):
        os.system("clear")
        print(self.banner % (self.version))

    def _import_command_(self):
        for file in os.listdir("wmipen/command/"):
            if file.endswith(".py"):
                exec(open("wmipen/command/"+file).read())

    def _import_module_(self):
        self.modules = wmipen.module.Modules.avaliableModule()
