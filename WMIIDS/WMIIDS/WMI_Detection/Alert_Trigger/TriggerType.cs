using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WMIIDS.WMI_Detection.Alert_Trigger
{
    class TriggerType
    {
        public static readonly string Creation = "__InstanceCreationEvent";
        public static readonly string Modification = "__InstanceModificationEvent";
        public static readonly string Deletion = "__InstanceDeletionEvent";
    }
}
