# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 2018

@author: Chew Zhi Jie
"""
from library.impacket.dcerpc.v5.dtypes import NULL
from library.impacket.dcerpc.v5.dcom import wmi
from library.impacket.dcerpc.v5.dcomrt import DCOMConnection

import wmipen.module

class QueryTest(wmipen.module.Module):
    
    NAME = "Query Test"
    DESCRIPTION = "A simple wmic get Win32_Process"
    AUTHOR = ['Chew Zhi Jie']
        
    def help(self):
        print(self.DESCRIPTION)
        
    def run(self, options):
        namespace = '//./root/cimv2'
        delimiter = '|'
        conn = None
        classObject = None
        wmiService = None
        wmiLogin = None

        try:
            conn = DCOMConnection(options.get("RHOST"), options.get("RUSER"), options.get("RPASS"), options.get("RDOMAIN"), '', '',
                                  None, oxidResolver=True, doKerberos=False)
            wmiInterface = conn.CoCreateInstanceEx(wmi.CLSID_WbemLevel1Login, wmi.IID_IWbemLevel1Login)
            wmiLogin = wmi.IWbemLevel1Login(wmiInterface)
            wmiService = wmiLogin.NTLMLogin(namespace, NULL, NULL)
            wmiLogin.RemRelease()
            wql = "SELECT * FROM Win32_Process"
            queryObject = wmiService.ExecQuery(wql.strip('\n'),
                                               wmi.WBEM_FLAG_RETURN_IMMEDIATELY | wmi.WBEM_FLAG_ENSURE_LOCATABLE)
            self.print_results(queryObject, delimiter)
            queryObject.RemRelease()

            wmiService.RemRelease()
            conn.disconnect()
        except Exception as e:
            if classObject is not None:
                classObject.RemRelease()
            if wmiLogin is not None:
                wmiLogin.RemRelease()
            if wmiService is not None:
                wmiService.RemRelease()
            if conn is not None:
                conn.disconnect()
            raise Exception("Could not connect to %s: %s" % (self.host, e.message))
        
    def print_results(self, queryObject, delimiter):
        """
        Prints the results in the classObject as wmic.c would
        :param queryObject: IEnumWbemClassObject
        :param delimiter: string
        :return:
        """
        while True:
            try:
                classObject = queryObject.Next(0xffffffff, 1)[0]
                print('CLASS: %s' % classObject.getClassName())
                record = classObject.getProperties()
                keys = []
                for name in record:
                    keys.append(name.strip())
                keys = natsorted(keys, alg=ns.IGNORECASE)
                print (delimiter.join(keys))
                tmp = []
                for key in keys:
                    if key == 'MUILanguages':
                        vals = []
                        for v in record[key]['value']:
                            vals.append(self.get_language(v))
                        record[key]['value'] = vals

                    if isinstance(record[key]['value'], list):
                        values = []
                        for v in record[key]['value']:
                            values.append(
                                self.format_value(v, record[key]['qualifiers']['CIMTYPE'], record[key]['type']))
                        tmp.append('(%s)' % ','.join(values))
                    else:
                        tmp.append('%s' % self.format_value(record[key]['value'], record[key]['qualifiers']['CIMTYPE'],
                                                            record[key]['type']))
                print (delimiter.join(tmp))
            except Exception as e:
                if e.get_error_code() != wmi.WBEMSTATUS.WBEM_S_FALSE:
                    raise
                else:
                    break
                
if __name__ == "__main__":
    query = QueryTest()
    import wmipen.option
    options = wmipen.option.Options()
        
    options.add("RHOST","35.197.141.62", True, "The target address")
    options.add("RDOMAIN","", True, "The target domain")
    options.add("RUSER","chewzhijie0426", True, "The target username")
    options.add("RPASS","w6;I@Ryq=Wo&>P3", True, "The target password")
    
    query.run(options)
    
    
    