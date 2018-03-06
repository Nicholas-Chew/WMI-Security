using System.Windows;
using WMIIDS.WMI_Detection.Alert_Trigger;
using WMIIDS.WMI_Detection.Triger_Action;

namespace WMIIDS.View
{
    /// <summary>
    /// Interaction logic for WMIIDS.xaml
    /// </summary>
    public partial class WMIIDS : Window
    {
        public WMIIDS()
        {
            InitializeComponent();

            Alert ASEC = new EventComsumer("unittest", new System.TimeSpan(0, 0, 1),
                     EventConsumerType.ActiveScriptEventConsumer, TriggerType.Creation);
            ASEC.EventArrived += (new NTEventLog()).Log;
            ASEC.EventArrived += (new RemoveWMIInstancecs()).Log;
            ASEC.Start();
        }
    }
}
