using System;
using System.Management;

namespace WMIIDS.WMI_Detection.Triger_Action
{
    public abstract class Action
    {
        /// <summary>
        /// Callback function to bind to Alert Class. Alert.EventArrived += (new Action()).Log
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
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

        protected abstract void DoLog(ManagementBaseObject mbo);
    }
}
