using System;
using System.Management;

namespace WMIIDS.WMI_Detection.Alert_Trigger
{
    //There are 3 ChangeEvent for registery. https://msdn.microsoft.com/en-us/library/aa393041(v=vs.85).aspx
    //Using RegistryTreeChangeEvent as it detects subtrees
    public class RegistryChangeEvent : Alert
    {
        private String Hive { get; set; }
        private String Path { get; set; }
        private String ValueName { get; set; }
        private String RegistryChangeType { get; set; }

        protected override WqlEventQuery Query
        { get
            {
                // No idea why cannot use the normal way. If use normal way, unprasable query will occur
                string queryString = "";
                switch (this.RegistryChangeType)
                {

                    case "RegistryKeyChangeEvent":
                        queryString = String.Format("Select * from RegistryKeyChangeEvent WHERE Hive = '{0}' AND KeyPath = '{1}'", this.Hive, this.Path);
                        break;
                    case "RegistryTreeChangeEvent":
                        queryString = String.Format("Select * from RegistryTreeChangeEvent WHERE Hive = '{0}' AND RootPath = '{1}'", this.Hive, this.Path);
                        break;
                    case "RegistryValueChangeEvent":
                        queryString = String.Format("Select * from RegistryValueChangeEvent WHERE Hive = '{0}' AND KeyPath = '{1}' AND ValueName={2}", this.Hive, this.Path, this.ValueName);
                        break;
                }

                return new WqlEventQuery(queryString)
                {
                    WithinInterval = this.PollingInterval
                };
            }
        }

        protected override string NameSpace => "ROOT/DEFAULT";

        public RegistryChangeEvent(String TriggerName, TimeSpan PollingInterval, String RegistryChangeType, String Hive, String Path, String ValueName) :
            base(TriggerName, PollingInterval)
        {
            this.PollingInterval = PollingInterval;
            this.RegistryChangeType = RegistryChangeType;
            this.Hive = Hive;
            this.Path = Path;
            this.ValueName = ValueName;
        }
    }

    public class RegistryChangeType
    {
        public static readonly string RegistryKeyChangeEvent = "RegistryKeyChangeEvent";
        public static readonly string RegistryTreeChangeEvent = "RegistryTreeChangeEvent";
        public static readonly string RegistryValueChangeEvent = "RegistryValueChangeEvent"; 
    }
}
