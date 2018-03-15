using System;
using System.Management;
using WMIIDS.UtilityClasses;
using WMIIDS.Facade;

namespace WMIIDS.Model
{
    public class LogData : ObservarableObject
    {
        #region Property

        private DateTime dateTime;
        private String nameSpace;
        private String className;
        private String infomation;

        #endregion
        
        #region Getter Setter

        public DateTime DateTime
        {
            get
            {
                return this.dateTime;
            }
            set
            {
                this.dateTime = value;
                base.RaisePropertyChangedEvent("DateTime");
            }
        }
        public string NameSpace
        {
            get
            {
                return this.nameSpace;
            }
            set
            {
                this.nameSpace = value;
                base.RaisePropertyChangedEvent("NameSpace");
            }
        }

        public string ClassName
        {
            get
            {
                return this.className;
            }
            set
            {
                this.className = value;
                base.RaisePropertyChangedEvent("ClassName");
            }
        }

        public string Infomation
        {
            get
            {
                return this.infomation;
            }
            set
            {
                this.infomation = value;
                base.RaisePropertyChangedEvent("Infomation");
            }
        }

        #endregion

        public LogData(ManagementBaseObject mbo)
        {
            this.DateTime = DateTime.Now;
            this.NameSpace = mbo.GetNameSpace();
            this.ClassName = mbo.GetClassName();
            this.Infomation = mbo.AllPropertyToString();
        }

        public override string ToString()
        {
            return String.Format("Date: {0} \nNameSpace: {1} \nClassName: {2} \nInfomation:\n{3}", 
                this.DateTime, this.NameSpace, this.ClassName, this.Infomation);
        }
    }
}
