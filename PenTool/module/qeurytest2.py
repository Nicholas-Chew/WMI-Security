# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 2018

@author: Chew Zhi Jie
"""
import sys
sys.path.append('../')
import wmipen.module
import winrm
from winrm.protocol import Protocol

class QueryTest(wmipen.module.Module):
    
    NAME = "Query Test"
    DESCRIPTION = "A simple wmic get Win32_Process"
    AUTHOR = ['Chew Zhi Jie']
        
    def help(self):
        print(self.DESCRIPTION)
        
    def run(self, options):
        
        session = winrm.Session(options.get('RHOST'), auth=(options.get('RUSER'), options.get('RPASS')), transport='ntlm')
        #session = winrm.Session('35.197.141.62', auth=("wmi-web\Administrator", "G0801346u!"))
        r = session.run_cmd('ipconfig',['/all'])
        print(r.status_code)
        print(r.std_out)
        print(r.std_err)
        '''
        p = Protocol(
                endpoint='https://35.197.141.62:5986/wsman',
                transport='ntlm',
                username=options.get('RUSER'),
                password=options.get('RPASS'),
                server_cert_validation='ignore')
        shell_id = p.open_shell()
        command_id = p.run_command(shell_id,'ipconfig',['/all'])
        '''
            
if __name__ == "__main__":
    query = QueryTest()
    import wmipen.option
    options = wmipen.option.Options()
        
    options.add("RHOST","10.0.75.2", True, "The target address")
    options.add("RDOMAIN","", True, "The target domain")
    options.add("RUSER","Administrator", True, "The target username")
    options.add("RPASS","P@ssw0rd!", True, "The target password")
    
    query.run(options)
    
    
    