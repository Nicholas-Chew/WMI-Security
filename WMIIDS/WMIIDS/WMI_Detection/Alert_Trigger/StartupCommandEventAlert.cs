using System;
using System.Management;

namespace WMIIDS.WMI_Detection.Alert_Trigger
{
    public class StartupCommandEventAlert : Alert
    {
        private String TriggerType { get; set; }
        protected override WqlEventQuery Query => new WqlEventQuery(this.TriggerType,
                         this.PollingInterval,
                         String.Format("TargetInstance isa 'Win32_StartupCommand'"));

        protected override string NameSpace => "ROOT/CIMV2";

        public StartupCommandEventAlert(String TriggerName, TimeSpan PollingInterval, String TriggerType) :
            base(TriggerName, PollingInterval)
        {
            this.TriggerType = TriggerType;
        }
    }
}
