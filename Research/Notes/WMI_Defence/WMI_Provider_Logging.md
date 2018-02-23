# WMI Logging
## WMI Provider Log Files
WMI Provider may also maintains logs. Different prividers output different logs.

The logs may be located in the following log directory:

### Wmiprov.log
This log contains the management data and events from WMI-enabled Windows Driver Model & WDM Provider.
It provide warning & error information primarily for troubleshooting and debugging things that use it.

It contains:
1. Errors from WDM provider or the device driver such as the binary MOF - Managed Object Format, language that is used to describe CIM, compile failing or failure to retrieve data.
2. The status of the MOF compile for each of the drivers which use MOF format.
3. Provider construction and deconstruction events.
4. Printout WNODE 

#### WDW Provier
The WDM (Windows Driver Model) provider grant access to the classes, instances, methods, and events of hardware drivers hat confrom to the WDM model. 
The classes for hardware drivers reside in the "root\wmi namespace"

WDM classes are primarily in Wmi.mof.

WDM is an OS interface through which hardware components provide infomation and event notification. The WDM provider is a class, instance, event, and method provider that allows management application to access tot data and events from WMI-for-WDM enabled device drivers.
The classes created by the WDM provider to represent device driver data reside only in the "Root\WMI" namespace. This namespace must already exist before the WDM provider will process the installed WDM drivers.

The WDM provider supports the WMIEvent extrinsic event, which notifies WMI regarding events from WDM-based drivers. You can register your event consumers for WMIEvent events as you would any other event.

### Ntevt.log
This log contains trace messages from the Event Log Provider.

#### Event Log Provider
This event log provider supplies Access to data from Event Log service and Notifications of events.

The Event log service writes events to one of the several log files.
The Event log provider uses the ```Win32_NTEventLogFile``` class to map data from the event logs to WMI objects.
It also uses the ```Win32_NTLogEvent``` class to represent events. 
These two ```_Win32Provider``` instance names are MS_NT_EVENTLOG_PROVIDER & MS_NT_EVENTLOG_EVENT_PROVIDER

As an instance, method, and event provider the Event Log provider implements standrad ```IWbemProviderInit``` interface, as well as the following ```IWBemServices``` methods:
 - CreateInstanceEnumAsync
 - ExecMethodAcync
 - ExecNotificationQueryAsync
 - ExecQueryAsync
 - GetObjectAsync
 - PutInstanceAsync
 
Event Log Provider supports the following classes:
 - Win32_NTEventLogFile
 - Win32_NTLogEvent
 - Win32_NTLogEventLog
 - Win32_NTLogEventUser
 - Win32_NTLogEventComputer
 
### Ntevt.log
This log contains trace infomation and error messages for Active Diretory Provider
 
 
 
 