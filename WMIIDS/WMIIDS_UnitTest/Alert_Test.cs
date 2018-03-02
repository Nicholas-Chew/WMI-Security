using System.Management;
using Microsoft.VisualStudio.TestTools.UnitTesting;

using WMIIDS.WMI_Detection.Alert_Trigger;

namespace WMIIDS_UnitTest
{
    [TestClass]
    public class Alert_Test
    {
        bool eventRaised;
        [TestMethod]
        public void ActiveScriptEventConsumer_Event_Fired()
        {
            eventRaised = false;

            Alert ASEC = new EventComsumerAlert("my", new System.TimeSpan(0, 0, 1),
                     EventConsumerType.ActiveScriptEventConsumer, TriggerType.Creation);
            ASEC.EventArrived += new System.Management.EventArrivedEventHandler(RevieceEventSucces);
            ASEC.Start();

            var wmiInstance = new WMIInstance("root/subscription", "ActiveScriptEventConsumer");
            wmiInstance.AddPropertyValue("Name", "UnitTesting");
            wmiInstance.AddPropertyValue("ScriptText", "UnitTesting");
            wmiInstance.AddPropertyValue("ScriptingEngine", "VBScript");
            wmiInstance.Add();

            System.Threading.Thread.Sleep(1000);

            if (eventRaised)
                Assert.IsTrue(true,"Event Raised");
            else
                Assert.Fail("Event Not Recieved");

            wmiInstance.Remove();
        }

        private void RevieceEventSucces(object sender, EventArrivedEventArgs e)
        {
            eventRaised = true;
        }      
    }
}
