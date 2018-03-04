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
        public void ActiveScriptEventConsumerAlert_Event_Fired()
        {
            eventRaised = false;

            Alert ASEC = new EventComsumerAlert("unittest", new System.TimeSpan(0, 0, 1),
                     EventConsumerType.ActiveScriptEventConsumer, TriggerType.Creation);
            ASEC.EventArrived += new EventArrivedEventHandler(RevieceEventSucces);
            ASEC.Start();

            var wmiInstance = new WMIInstance("root/subscription", "ActiveScriptEventConsumer");
            wmiInstance.AddPropertyValue("Name", "UnitTesting");
            wmiInstance.AddPropertyValue("ScriptText", "UnitTesting");
            wmiInstance.AddPropertyValue("ScriptingEngine", "VBScript");
            wmiInstance.Add();

            System.Threading.Thread.Sleep(10);

            if (eventRaised)
                Assert.IsTrue(true,"Event Raised");
            else
                Assert.Fail("Event Not Recieved");

            wmiInstance.Remove();
        }

        [TestMethod]
        public void CommandLineEventConsumerAlert_Event_Fired()
        {
            eventRaised = false;

            Alert CLE = new EventComsumerAlert("unittest", new System.TimeSpan(0, 0, 1),
                     EventConsumerType.CommandLineEventConsumer, TriggerType.Creation);
            CLE.EventArrived += new EventArrivedEventHandler(RevieceEventSucces);
            CLE.Start();

            var wmiInstance = new WMIInstance("root/subscription", "CommandLineEventConsumer");
            wmiInstance.AddPropertyValue("Name", "UnitTesting");
            wmiInstance.AddPropertyValue("CommandLineTemplate", "dir");
            wmiInstance.AddPropertyValue("RunInteractively", true);
            wmiInstance.AddPropertyValue("WorkingDirectory", "c:\\");
            wmiInstance.Add();

            System.Threading.Thread.Sleep(10);

            if (eventRaised)
                Assert.IsTrue(true, "Event Raised");
            else
                Assert.Fail("Event Not Recieved");

            wmiInstance.Remove();
        }

        // TODO: To test this, the test must be run as Admin which could be disasterous. Find another way to test this Alert
        [TestMethod]
        public void StartupCommandEventAlert_Event_Fired()
        {
            eventRaised = false;

            Alert SCE = new StartupCommandEventAlert("unittest", new System.TimeSpan(0, 0, 1),
                      TriggerType.Creation);
            SCE.EventArrived += new EventArrivedEventHandler(RevieceEventSucces);
            SCE.Start();


           Assert.IsTrue(true, "Event Raised");

            //wmiInstance.Remove();
        }

        // TODO: To test this, the test must be run as Admin which could be disasterous. Find another way to test this Alert
        [TestMethod]
        public void RegisteryChangeEvent_Event_Fired()
        {
            eventRaised = false;

            Alert RCE = new RegistryChangeEvent("unittest", new System.TimeSpan(0, 0, 1), RegistryChangeType.RegistryTreeChangeEvent ,"HKEY_USERS", "","");
            RCE.EventArrived += new EventArrivedEventHandler(RevieceEventSucces);
            RCE.Start();

            System.Threading.Thread.Sleep(10);

            Assert.IsTrue(true, "Event Raised");

        }

        private void RevieceEventSucces(object sender, EventArrivedEventArgs e)
        {
            eventRaised = true;
        }      
    }
}
