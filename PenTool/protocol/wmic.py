# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 11:23:57 2018

@author: Chew Zhi Jie
"""
from impacket.dcerpc.v5.dtypes import NULL
from impacket.dcerpc.v5.dcom import wmi
from impacket.dcerpc.v5.dcomrt import DCOMConnection

class WMIC(object):
    
    def __init__(self,options):
        self.options = options
    
    def gwmi(self, wql):
        namespace = '//./root/cimv2'

        try:
            dcom = DCOMConnection(self.options.get('RHOST'), self.options.get('RUSER'), self.options.get('RPASS'), self.options.get('RDOMAIN'),
                                  '', '', None, oxidResolver=True, doKerberos=False) 
            
            wmiInterface = dcom.CoCreateInstanceEx(wmi.CLSID_WbemLevel1Login, wmi.IID_IWbemLevel1Login)
            wmiLogin = wmi.IWbemLevel1Login(wmiInterface)
            wmiServices = wmiLogin.NTLMLogin(namespace, NULL,  NULL)
            wmiLogin.RemRelease()
            
            '''
            DO STUFF HERE - query
            '''
            
            wmiQueryObject = wmiServices.ExecQuery(wql.strip('\n'))
            self._printReply_(wmiQueryObject)
            wmiQueryObject.RemRelease()
            
            wmiServices.RemRelease()    
            dcom.disconnect()                            
        except Exception as e:
            print(str(e))
            try:
                if wmiLogin is not None:
                    wmiLogin.RemRelease()
                if wmiServices is not None:
                    wmiServices.RemRelease()
                if dcom is not None:
                    dcom.disconnect()
            except Exception:
                pass

    def _printReply_(self, QeuryObject):
        printHeader = True
        
        while True:
            try:
                pEnum = QeuryObject.Next(0xffffffff,1)[0]
                record = pEnum.getProperties()
                if printHeader is True:
                    print('|')
                    for col in record:
                        print ('%s |' % col)
                    print('')
                    printHeader = False
                
                for key in record:
                    if type(record[key]['value']) is list:
                        for item in record[key]['value']:
                            print(item)
                        print('|')
                    else:
                        print('%s |' % record[key]['value'])
                print('')
            except Exception as e:
                if str(e).find('S_FAKSE') < 0:
                    raise
                else:
                    break
        QeuryObject.RemRelease()
            

if __name__ == "__main__":
    import wmipen.option
    options = wmipen.option.Options()
        
    options.add("RHOST","10.0.75.2", True, "The target address")
    options.add("RDOMAIN","", True, "The target domain")
    options.add("RUSER","Administrator", True, "The target username")
    options.add("RPASS","P@ssw0rd!", True, "The target password")
    
    query = WMIC(options)
    query.gwmi("select * from Win32_Bus")