# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 11:23:57 2018

@author: Chew Zhi Jie
"""
from impacket.dcerpc.v5.dtypes import NULL
from impacket.dcerpc.v5.dcom import wmi
from impacket.dcerpc.v5.dcomrt import DCOMConnection


class DCOM(object):

    def __init__(self, options):
        namespace = '//./root/cimv2'

        try:
            self.dcom = DCOMConnection(options.get('RHOST'), options.get('RUSER'),
                                       options.get('RPASS'), options.get('RDOMAIN'),
                                       '', '', None, oxidResolver=True, doKerberos=False)

            wmiInterface = self.dcom.CoCreateInstanceEx(wmi.CLSID_WbemLevel1Login,
                                                        wmi.IID_IWbemLevel1Login)
            wmiLogin = wmi.IWbemLevel1Login(wmiInterface)
            self.wmiServices = wmiLogin.NTLMLogin(namespace, NULL,  NULL)
            wmiLogin.RemRelease()
        except Exception as e:
            try:
                if wmiLogin is not None:
                    wmiLogin.RemRelease()
                if self.wmiServices is not None:
                    self.wmiServices.RemRelease()
                if self.dcom is not None:
                    self.dcom.disconnect()
            except Exception:
                pass
            raise e

    def gwmi(self, wql):
        try:
            wmiQueryObject = self.wmiServices.ExecQuery(wql.strip('\n'))
            self._printReply_(wmiQueryObject)
            wmiQueryObject.RemRelease()
        except Exception as e:
            try:
                if wmiQueryObject is not None:
                    wmiQueryObject.RemRelease()
                if self.wmiServices is not None:
                    self.wmiServices.RemRelease()
                if self.dcom is not None:
                    self.dcom.disconnect()
            except Exception:
                pass
            raise e

    def _printReply_(self, QeuryObject):
        printHeader = True

        while True:
            try:
                pEnum = QeuryObject.Next(0xffffffff, 1)[0]
                record = pEnum.getProperties()
                if printHeader is True:
                    print '|',
                    for col in record:
                        print '%s |' % col,
                    print
                    printHeader = False

                print '|',
                for key in record:
                    if type(record[key]['value']) is list:
                        for item in record[key]['value']:
                            print item,
                        print '|',
                    else:
                        print '%s |' % record[key]['value'],
                print
            except Exception as e:
                if str(e).find('S_FAKSE') < 0:
                    raise e
                else:
                    break
        QeuryObject.RemRelease()

    def close(self):
        try:
            self.wmiServices.RemRelease()
            self.dcom.disconnect()
        except Exception:
            pass


if __name__ == "__main__":
    import wmipen.option
    options = wmipen.option.Options()

    options.add("RHOST", "10.0.75.2", True, "The target address")
    options.add("RDOMAIN", "", True, "The target domain")
    options.add("RUSER", "Administrator", True, "The target username")
    options.add("RPASS", "P@ssw0rd!", True, "The target password")

    query = DCOM(options)
    query.gwmi("select name from Win32_Process")
    query.close()
