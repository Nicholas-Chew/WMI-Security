# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 11:17:12 2018

@author: Chew Zhi Jie
"""
import winrm


class WSMan(object):

    def __init__(self, options):
        try:
            self.session = winrm.Session(options.get('RHOST'),
                                         auth=(options.get('RUSER'),
                                               options.get('RPASS')),
                                         transport='ntlm')

        except Exception as e:
            raise e

    def gwmi(self, wmiclass):
        try:
            r = self.session.run_ps('gwmi -Query "' + wmiclass + '"')
            print(r.status_code)
            print(r.std_out)
            print(r.std_err)
        except Exception as e:
            raise e

    def close(self):
        pass


if __name__ == "__main__":
    import wmipen.option
    options = wmipen.option.Options()

    options.add("RHOST", "10.0.75.2", True, "The target address")
    options.add("RDOMAIN", "", True, "The target domain")
    options.add("RUSER", "Administrator", True, "The target username")
    options.add("RPASS", "P@ssw0rd!", True, "The target password")

    query = WSMan(options)
    query.gwmi("select * from Win32_Bus")
    query.close
