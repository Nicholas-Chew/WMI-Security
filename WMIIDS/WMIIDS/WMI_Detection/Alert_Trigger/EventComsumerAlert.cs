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

        protected override string NameSpace => "ROOT/SUBSCRIPTION";

        public EventComsumerAlert(String TriggerName, TimeSpan PollingInterval, String EventConsumerType, String TriggerType) :
            base(TriggerName, PollingInterval)
        {
            this.EventConsumerType = EventConsumerType;
            this.TriggerType = TriggerType;
        }
    }

    //Currently only using these two Event Type.
    //There are also LogFileEventConsumer, NTEventLogEventConsumer, SMTPEventConsumer
    public class EventConsumerType
    {
        public static readonly string ActiveScriptEventConsumer = "ActiveScriptEventConsumer";
        public static readonly string CommandLineEventConsumer = "CommandLineEventConsumer";
    }
}
