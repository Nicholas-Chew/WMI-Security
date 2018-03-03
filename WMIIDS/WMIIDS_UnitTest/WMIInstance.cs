using System;
using System.Collections.Generic;
using System.Linq;
using System.Management;

namespace WMIIDS_UnitTest
{
    class WMIInstance
    {
        ManagementClass cls;
        ManagementObject obj;

        public WMIInstance(String nameSpace, String cls)
        {
            try
            {
                var managementPath = new ManagementPath();
                managementPath.ClassName = cls;
                managementPath.NamespacePath = nameSpace;

                this.cls = new ManagementClass(managementPath, null);
                this.obj = this.cls.CreateInstance();
            }
            catch(ManagementException e)
            {
                throw e;
            }
        }

        public void AddPropertyValue(String propertyName, object propertyValue)
        {
            this.obj.SetPropertyValue(propertyName, propertyValue);
        }

        public void Add()
        {
            try
            {
                var p = new PutOptions();
                p.Type = PutType.UpdateOrCreate;
                ManagementPath result = obj.Put(p);

                Console.WriteLine("result=" + result.ToString());
            }
            catch (ManagementException e)
            {
                throw e;
            }
        }

        public void Remove()
        {
            try
            {
                this.obj.Delete();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }
    }
}
