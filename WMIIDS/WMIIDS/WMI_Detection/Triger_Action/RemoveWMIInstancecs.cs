using System;
using System.Collections.Generic;
using System.Linq;
using System.Management;
using System.Text;
using System.Threading.Tasks;

namespace WMIIDS.WMI_Detection.Triger_Action
{
    class RemoveWMIInstancecs : Action
    {
        protected override void DoLog(ManagementBaseObject mbo)
        {
            var mo = (ManagementObject)mbo;
            mo.Delete();
        }
    }
}
