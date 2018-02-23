# Tracing WMI Activity
WMI can be used from applications & scripts. It provides an infrastructure that makes it easy to both discover and perform management tasks.
In addition, it is possible to add to the set of possibe management tasks by creating own WMI providers.

Following are ways to trace WMI activity:

### Obtaining WMI Events Through Event Viewer
The WMITracing.log file contains the events that WMI traces. However, this is a binary file. To see these events in a format readable by humans, use **Event Viewer**.
It will be under Applications and Service Logs | Mivrosoft | Windows | WMI Acticity.

The Event ID field displays a value that contains the following information.

#### Event 1
Start of the event sequence for a specific operation. One occurrence for each sequence.

The event fields for an Event 1 are:
- **GroupOperationID** is a unique identifier that is used for all events reported for a specific client.
- **OperationId** indicates the operation sequence.
- **Operation** specifies the connection or request to WMI.
- **User** indicates the account that makes a request to WMI by running a script or through CIM Studio.
- **Namespace** shows the WMI namespace to which the connection is made.
For example, a script may request all the instances of a WMI class, such as Win32_Service. The first operation may be a connection to WMI.

#### Event 2
Events that make up the operation. One or more occurrences in the sequence.

The event fields for an Event 2 are:

- **GroupOperationID** indicates the sequence in which the event occurs.
- **GroupOperationID** indicates the sequence in which the event occurs.
- **ProviderName** indicates the name of the provider which supplies the data.
- Path is the WMI path to the object.
For example, the operation may be an enumeration of Win32_Service.

#### Event 3
End of the event sequence for a specific operation. One occurrence for each sequence.

Only the **GroupOperationID** is shown.
 
 
### Obtaining WMI Events Through Event Viewer
Enable WMI event tracing through the Wevtutil command-line tool. Use the following command: Wevtutil.exe sl Microsoft-Windows-WMI-Activity/Trace /e:true. The WMI event source is Microsoft-Windows-WMI.

### Using WPP-based WMI Tracing
WMI creates an active trace channel during the boot process. The name of the channel is WMI_Trace_Session. Only errors are logged to the channel.