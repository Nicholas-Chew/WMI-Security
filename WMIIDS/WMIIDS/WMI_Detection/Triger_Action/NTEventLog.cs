using System;
using System.Diagnostics;
using System.Globalization;
using System.Management;

using WMIIDS.Facade;
using WMIIDS.Model;

namespace WMIIDS.WMI_Detection.Triger_Action
{
    /// <summary>
    /// Log trigger into windows event log, will be log into Application with Source WMI Security Activity
    /// </summary>
    public class NTEventLog : Action
    {
        // The actual limit is higher than this, but different Microsoft operating systems actually have
        // different limits. So just use 30,000 to be safe.
        private const int MaxEventLogEntryLength = 30000;

        protected override void DoLog(ManagementBaseObject mbo)
        {
            try
            {
                if(!EventLog.SourceExists("WMI Security Activity"))
                    EventLog.CreateEventSource("WMI Security Activity", "Application");
                EventLog.WriteEntry("WMI Security Activity", EnsureLogMessageLimit((new LogData(mbo)).ToString()), EventLogEntryType.Warning);
            }
            catch(Exception)
            {
                throw;
            }
        }

        // Ensures that the log message entry text length does not exceed the event log viewer maximum length of 32766 characters.
        private static string EnsureLogMessageLimit(string logMessage)
        {
            if (logMessage.Length > MaxEventLogEntryLength)
            {
                string truncateWarningText = string.Format(CultureInfo.CurrentCulture, "... | Log Message Truncated [ Limit: {0} ]", MaxEventLogEntryLength);

                logMessage = logMessage.Substring(0, MaxEventLogEntryLength - truncateWarningText.Length);
                logMessage = string.Format(CultureInfo.CurrentCulture, "{0}{1}", logMessage, truncateWarningText);
            }

            return logMessage;
        }
    }
}
