using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WMIIDS.WMI_Detection.Alert_Trigger
{
    //Currently only using these two Event Type.
    //There are also LogFileEventConsumer, NTEventLogEventConsumer, SMTPEventConsumer
    public class EventConsumerType
    {
        public static readonly string ActiveScriptEventConsumer = "ActiveScriptEventConsumer";
        public static readonly string CommandLineEventConsumer = "CommandLineEventConsumer";
    }
}
