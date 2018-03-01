using System;
using System.Management;

namespace WMIIDS.WMI_Detection.Alert_Trigger
{
    class EventComsumerAlert : Alert
    {
        private String EventConsumerType { get; set; }
        private String TriggerType { get; set; }

        public EventComsumerAlert(String TriggerName, int PollingInterval, String EventConsumerType, String TriggerType) :
            base(TriggerName, PollingInterval)
        {
            this.EventConsumerType = EventConsumerType;
            this.TriggerType = TriggerType;
        }

        public override void generateTriggerTable()
        {
            WqlEventQuery query =
               new WqlEventQuery(this.TriggerType,
                               new TimeSpan(0, 0, this.PollingInterval),
                             String.Format("TargetInstance isa '{0}'",this.EventConsumerType));

            // Initialize an event watcher and subscribe to events 
            // that match this query
            ManagementEventWatcher watcher = new ManagementEventWatcher(query);

            // Block until the next event occurs 
            // Note: this can be done in a loop if waiting for 
            //        more than one occurrence
            ManagementBaseObject e = watcher.WaitForNextEvent();

            //Display information from the event
            Console.WriteLine(
               "Service {0} has changed, State is {1}",
                ((ManagementBaseObject)e["TargetInstance"])["Name"],
                ((ManagementBaseObject)e["TargetInstance"])["State"]);

            //Cancel the subscription
            watcher.Stop();

        }
    }
}
