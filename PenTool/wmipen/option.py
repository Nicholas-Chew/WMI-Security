# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 2018

@author: Chew Zhi Jie
"""


class Option(object):
    def __init__(self, name, value, required, description):
        self.name = name
        self.value = value
        self.description = description
        self.required = required

    def setValue(self, value):
        self.value = value


class Options(object):
    def __init__(self):
        self.options = []

    def add(self, name, value, required, description):
        name = name.upper()
        self.options.append(Option(name, value, required, description))

    def get(self, name):
        name = name.upper()
        for option in self.options:
            if option.name == name:
                return option.value

    def set(self, name, value):
        name = name.upper()
        for option in self.options:
            if option.name == name:
                option.setValue(value)
                return True
        return False
