using System;
using System.Collections.ObjectModel;
using System.Management;
using System.Windows;
using WMIIDS.Model;
using WMIIDS.UtilityClasses;

namespace WMIIDS.ViewModel
{
    public class WMIIDSViewModel : BaseViewModel
    {
        #region Property

        private ObservableCollection<LogData> logDatas;

        #endregion

        #region Constructors

        public WMIIDSViewModel()
        {
            this.Initialize();
        }

        #endregion

        #region Data Properties
        
        public ObservableCollection<LogData> LogDatas
        {
            get { return this.logDatas; }
            set
            {
                this.logDatas = value;
                this.RaisePropertyChangedEvent("LogDatas");
            }
        }


        #endregion

        public void EventArrived(object sender, EventArrivedEventArgs e)
        {
            var mbo = (ManagementBaseObject)e.NewEvent["TargetInstance"];
            Application.Current.Dispatcher.Invoke(new Action(() =>
            {
                this.LogDatas.Insert(0, new LogData(mbo));
            }));

        }

        private void Initialize()
        {
            logDatas = new ObservableCollection<LogData>();
        }
    }
}
