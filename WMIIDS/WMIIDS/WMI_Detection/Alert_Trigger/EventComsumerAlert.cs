using System;
using System.Management;

namespace WMIIDS.WMI_Detection.Alert_Trigger
{
    public class EventComsumerAlert : Alert
    {
        private String EventConsumerType { get; set; }
        private String TriggerType { get; set; }

        protected override WqlEventQuery Query => new WqlEventQuery(this.TriggerType,
                         this.PollingInterval,
                         String.Format("TargetInstance isa '{0}'", this.EventConsumerType)); 

        protected override string NameSpace => "root/subscription";

        public EventComsumerAlert(String TriggerName, TimeSpan PollingInterval, String EventConsumerType, String TriggerType) :
            base(TriggerName, PollingInterval)
        {
            this.EventConsumerType = EventConsumerType;
            this.TriggerType = TriggerType;
        }
    }
}
