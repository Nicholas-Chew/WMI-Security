using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using WMIIDS.WMI_Detection.Alert_Trigger;

namespace WMIIDS_UnitTest
{
    [TestClass]
    public class Alert_Test
    {
        [TestMethod]
        public void ActiveScriptEventConsumer_Event_Fired()
        {
            Alert ASEC = new EventComsumerAlert("my", new System.TimeSpan(0, 0, 1),
                     EventConsumerType.ActiveScriptEventConsumer, TriggerType.Creation);
            ASEC.EventArrived += new System.Management.EventArrivedEventHandler((sender, e) => { Assert.IsTrue(true, "Recieved Event. Success"); });

            Alert ASEC2 = new EventComsumerAlert("asd", new System.TimeSpan(0, 0, 1),
                    EventConsumerType.ActiveScriptEventConsumer, TriggerType.Creation);
        }
    }
}
