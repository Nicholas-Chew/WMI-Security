using System.Management;

namespace WMIIDS.WMI_Detection.Triger_Action
{
    public abstract class Action
    {
        public void Log(object sender, EventArrivedEventArgs e)
        {
            DoLog((ManagementBaseObject)e.NewEvent["TargetInstance"]);
        }

        public abstract void DoLog(ManagementBaseObject obj);
    }
}
