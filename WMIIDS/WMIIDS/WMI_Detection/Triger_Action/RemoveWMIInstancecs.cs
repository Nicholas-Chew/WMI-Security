using System.Management;

namespace WMIIDS.WMI_Detection.Triger_Action
{
    /// <summary>
    /// Remove the created instance once trigger
    /// </summary>
    class RemoveWMIInstancecs : Action
    {
        protected override void DoLog(ManagementBaseObject mbo)
        {
            var mo = (ManagementObject)mbo;
            mo.Delete();
        }
    }
}
