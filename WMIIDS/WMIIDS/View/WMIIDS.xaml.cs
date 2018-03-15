using System.Collections.ObjectModel;
using System.Management;
using System.Windows;
using WMIIDS.Model;
using WMIIDS.ViewModel;
using WMIIDS.WMI_Detection.Alert_Trigger;
using WMIIDS.WMI_Detection.Triger_Action;

namespace WMIIDS.View
{
    /// <summary>
    /// Interaction logic for WMIIDS.xaml
    /// </summary>
    public partial class WMIIDS : Window
    {
        private WMIIDSViewModel wMIIDSViewModel;

        public WMIIDS()
        {
            InitializeComponent();

            wMIIDSViewModel = new WMIIDSViewModel();
            this.DataContext = wMIIDSViewModel;

            Alert ASEC = new EventComsumer("unittest", new System.TimeSpan(0, 0, 1),
                     EventConsumerType.ActiveScriptEventConsumer, TriggerType.Creation);
            ASEC.EventArrived += (new NTEventLog()).Log;
            ASEC.EventArrived += wMIIDSViewModel.EventArrived;
            ASEC.EventArrived += ASEC_EventArrived;
            ASEC.EventArrived += (new RemoveWMIInstancecs()).Log;
            ASEC.Start();
        }

        private void ASEC_EventArrived(object sender, EventArrivedEventArgs e)
        {
            ((App)Application.Current).NotifyBallonTip("Warning", "WMI Event Detected", System.Windows.Forms.ToolTipIcon.Warning, 1000);
        }
    }
}
