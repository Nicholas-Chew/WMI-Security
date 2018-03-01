using System;
using System.Management;

namespace WMIIDS.WMI_Detection.Alert_Trigger
{
    abstract class Alert
    {
        protected String TriggerName { get; set; }
        protected int PollingInterval { get; set; }
        protected ManagementEventWatcher watcher { get; set; }

        public Alert(String TriggerName, int PollingInterval)
        {
            this.TriggerName = TriggerName;
            this.PollingInterval = PollingInterval;
        }

        public abstract void generateTriggerTable();
    }
}
