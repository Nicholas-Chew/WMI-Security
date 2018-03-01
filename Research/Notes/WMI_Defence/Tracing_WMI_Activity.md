# Tracing WMI Activity
WMI can be used from applications & scripts. It provides an infrastructure that makes it easy to both discover and perform management tasks.
In addition, it is possible to add to the set of possibe management tasks by creating own WMI providers.

Following are ways to trace WMI activity:

## Obtaining WMI Events Through Event Viewer
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
 
 
## Obtaining WMI Events Through Event Viewer
Enable WMI event tracing through the Wevtutil command-line tool. Use the following command: Wevtutil.exe sl Microsoft-Windows-WMI-Activity/Trace /e:true. The WMI event source is Microsoft-Windows-WMI.

## Using WPP-based WMI Tracing
WMI creates an active trace channel during the boot process. The name of the channel is WMI_Trace_Session. Only errors are logged to the channel.

The Windows software trace preprocessor (WPP) records infomation in a binary file. To read it, tool such as tracefmt.exe from the Windoes Driver Kit (WDK) is needed to do translation.
The tool requires information stored in some associated files. The files are located in the %SystemRoot%\System32\wbem\tmf directory and have a .tmf file name extension.
 
After installing the Windows Driver Kit (WDK) to get the tracelog.exe and tracefmt.exe command-line tools, perform the following steps to collect a WPP-based WMI trace.

#### To View a WPP-based trace
1. To create the single .tmf file, open an elevated Command Prompt window and navigate to the %SystemRoot%\System32\wbem\tmf directory.
2. Type ````copy /y %SystemRoot%\System32\wbem\tmf\*.tmf```` ````%SystemRoot%\System32\wbem\tmf\wmi.tmf````. This will create a file named wmi.tmf that includes the contents of all of the other .tmf files.
3. Type ````tracelog -flush WMI_Trace_Session````. This will flush the WPP buffers on the disk.
4. Type ````set TRACE_FORMAT_PREFIX = [%9!d!]%8!04X!.%3!04X!.%3!04X!::%4!s![%1!s!](%!COMPNAME!:%!FUNC !:%2!s!)````. The tracefmt tool adds some default information to each trace message. You can configure what information is included by setting the TRACE_FORMAT_PREFIX environment variable. 
5. Type ````tracefmt -tmf %systemroot%\system32\wbem\tmf\wmi.tmf -o OUTPUT.TXT %systemroot%\system32\wbem\logs\WMITracing.log````. This performs the translation from binary format to readable text format.
6. Type ````notepad %systemroot%\system32\wbem\tmf\OUTPUT.TXT````. This will open the trace file in Notepad.

Following are some other WPP-related tasks might be needed.
 - Stop WPP-based WMI tracing
     ````tracelog -stop WMI_Trace_Session````
- Start WPP-based WMI tracing
    ````tracelog -start WMI_Trace_Session -guid #1FF6B227-2CA7-40f9-9A66-980EADAA602E -rt -level 5 -flag 0x7 -f MYTRACE.BIN````
- List all WPP trace sessions
    ````tracelog -l````
- List info about the WMI WPP trace session
    ````tracelog -l | findstr /i "wmi_trace"````
-View the WMI WPP trace session parameters
    ````Type tracelog -q WMI_Trace_Session````