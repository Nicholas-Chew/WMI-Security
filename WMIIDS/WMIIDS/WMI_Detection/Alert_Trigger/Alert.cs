using System;
using System.Management;

namespace WMIIDS.WMI_Detection.Alert_Trigger
{
    public abstract class Alert
    {
        #region Base variables

        protected String TriggerName { get; set; }
        protected TimeSpan PollingInterval { get; set; }
        protected ManagementEventWatcher Watcher { get; set; }

        #endregion

        #region WMI variables needed from child

        protected abstract WqlEventQuery Query { get; }
        protected abstract string NameSpace { get; }

        #endregion

        public event EventArrivedEventHandler EventArrived;

        public Alert(String TriggerName, TimeSpan PollingInterval)
        {
            this.TriggerName = TriggerName;
            this.PollingInterval = PollingInterval;
        }

        public void Start()
        {
            //Local for now only. Can use ManagementScope(NameSpace, Connection) to monitor network
            Watcher = new ManagementEventWatcher(new ManagementScope(NameSpace), Query);
            Watcher.EventArrived += new EventArrivedEventHandler(OnEventArrived);
            Watcher.Start();
        }

        private void OnEventArrived(object sender, EventArrivedEventArgs e)
        {
            OnEventArrived(e);
        }

        private void OnEventArrived(EventArrivedEventArgs e)
        {
            EventArrived?.Invoke(this, e);
        }
    }
}
