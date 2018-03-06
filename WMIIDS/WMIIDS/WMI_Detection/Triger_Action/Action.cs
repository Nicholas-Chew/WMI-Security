using System;
using System.Management;

namespace WMIIDS.WMI_Detection.Triger_Action
{
    public abstract class Action
    {
        public void Log(object sender, EventArrivedEventArgs e)
        {
            try
            {
                DoLog((ManagementBaseObject)e.NewEvent["TargetInstance"]);
            }
            catch(Exception)
            {
                throw;
            }
        }

        public abstract void DoLog(ManagementBaseObject obj);
    }
}
