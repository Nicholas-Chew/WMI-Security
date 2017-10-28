# WMI Events & Consumer Binding
## WMI Permanent Event Consumer Flow
1. Filters
	* Capture object creation, deletion, change events - Intrinsic Event
	* Monitor "what's going on" insude a Windows OS
	
2. Consumers
	* Respond to event occurences
	* Take action based on certain conditions

3. Binding
	* Bind a consumer and filter together
	* Initiates the flow of the events through the WMI eventing subsystem


## Ways to create WMI Binding
* Manually develop and compile MOF files
	* Ugly syntax - lots of ` \\\\\\\\\\\'s`

* Write VBscript code to create the objects
	* Boring
    
* Manually create objects with wbemtest or CIM studio
	* Slow & unmanageable

## WMI Events

### Types of WMI Events
* Intrinsic (WMI Objects)
	* Changes to actual WMI objects detected by querying system event classes
	* Example: __InstanceCreationEvent
	* Example: __InstanceDeletionEvent
	* Example: __InstanceModificationEvent

* Extrinsic (provider-specific)
	* Events reported by a WMI provider Implementation
	* Example: Win32_ProcessStartTrace
	* Example: Win32_ComputerSystemEvent
	* Example: RegistryEvent

**Useful Classes To Know**

Working with WMI Events means that you need to know what kind of classes are available to initiate the subscriptions. The following classes are the ones that I have used or read about and will prove useful when registering for the WMI Events:

| Class | URL |
| :---- | :-- |
| Win32_ProcessStartTrace | http://msdn.microsoft.com/en-us/library/windows/desktop/aa394374(v=vs.85).aspx |
| Win32_ProcessStopTrace | http://msdn.microsoft.com/en-us/library/windows/desktop/aa394376(v=vs.85).aspx |
| __InstanceModificationEvent | http://msdn.microsoft.com/en-us/library/windows/desktop/aa394651(v=vs.85).aspx |
| __InstanceCreationEvent | http://msdn.microsoft.com/en-us/library/windows/desktop/aa394649(v=vs.85).aspx |
| __InstanceDeletionEvent | http://msdn.microsoft.com/en-us/library/windows/desktop/aa394650(v=vs.85).aspx |
| RegistryTreeChangeEvent | http://msdn.microsoft.com/en-us/library/windows/desktop/aa393041(v=vs.85).aspx |
| RegistryKeyChangeEvent | http://msdn.microsoft.com/en-us/library/windows/desktop/aa393040(v=vs.85).aspx |
| RegistryValueChangeEvent | http://msdn.microsoft.com/en-us/library/windows/desktop/aa393042(v=vs.85).aspx |

Working down the line of classes, the ProcessTrace classes are used to report when a process has started or stopped.

The ```__Instance*``` classes are **intrinsic event** classes which reports a change to the WMI repository, such as a creation or modification. An example of this would be to use one of the ```__Instance*``` classes with ```Win32_Service``` to track when a service starts or stops. More on this with examples later.

Lastly on this list, the ```Registry*``` classes are **extrinsic events** which cannot be linked directly to the WMI model. Regardless, you can use this to receive a notification if a part of the registry that has already been defined has been modified of deleted.

### WMI Event Query Structure
##### Basic Example
`Select <fields> from <EventClass> WITHIN <Seconds> WHERE <criteria>`

###### A Realistic Example
`Select <fields> from <EventClass> WITHIN <Seconds> WHERE TargetInstance ISA '<TargetClass>'`

Note: *"TargetInstance"* is a property on intrisic event classes which refers to the object that generated the event (Eg. Win32_Process)

Example:
```
"select * from __instanceModificationEvent within 5 where targetInstance isa 'win32_Service'"
```
Breaking it down, I will show you what is happening with this filter.

| Query | Description |
| :---- | :---------- |
| “select * from __instanceModificationEvent” | Specify properties which are returned from query. |
| “within 5” | Poll every 5 seconds for event (this doesn’t mean something will be missed, it just means that it may take 5 seconds to acknowledge the event).|
| “where targetInstance isa ‘win32_Service'” | Where filters the scope down and isa applies a query to the subclasses of a specified class |

For more information regarding WMI queries, check out the following article on more keywords related to WQL: http://msdn.microsoft.com/en-us/library/windows/desktop/aa394606(v=vs.85).aspx

### Examples using VBscript
###### New Process
```
instance of __EventFilter as $FILTER
{
    Name = "NewProcesses";
    Query = "SELECT * FROM __InstanceCreationEvent within 2 where TargetInstance ISA 'Win32_Process'";
    QueryLanguage = "WQL";
    EventNamespace = "\root\cimv2";

    // this is the Administrators SID in array of bytes format
    CreatorSID = {1,2,0,0,0,0,0,5,32,0,0,0,32,2,0,0}; 
};
```
**Note: Can add more in the future**

## WMI Consumer 
### Event Consumer Type
* Script 
	* Allows you to run VBScript code in response to an event
	* Embed VBscript code in the consumer or reference a script file
* Command Line
	* Run abitary comands in response to events
	* Pass event details as parameters to the command 
* SMTP
	* Send an e-mail in response to an event (requites an open SMTP server)
	* Cannot use SMTP credentials with this consumer
* NT Event Log
	* Log an event to the application event log in response to an event
	* Use WMI standtad string templates to pass event infomation to log entry

### Examples using VBscript
```
#pragma namespace("\\\\.\\root\\subscription")

instance of ActiveScriptEventConsumer as $CONSUMER
{
    Name = "MyConsumerName";
    ScriptingEngine = "VBScript";
    ScriptText = 

        "Set objFS = CreateObject(\"Scripting.FileSystemObject\")\n"
        "Set objFile = objFS.OpenTextFile(\"C:\\\\ASEC.log\", 8, true);\n"
        "objFile.WriteLine \"Time: \" + new Date() + \";\n"
        "objFile.WriteLine \"Entry made by: \\\"ActiveScript\\\"\";\n"
        "objFile.Close\n";
    
    // this is the Administrators SID in array of bytes format
    CreatorSID = {1,2,0,0,0,0,0,5,32,0,0,0,32,2,0,0}; 
};
```

## WMI Event Bindings
* The "glue" between filters & Consumers
* Two main properties" Filter & Consumers
* Does not have a name propery

````
instance of __FilterToConsumerBinding
{
    Filter = $FILTER;
    Consumer = $CONSUMER;
    DeliverSynchronously=FALSE;

    // this is the Administrators SID in array of bytes format
    CreatorSID = {1,2,0,0,0,0,0,5,32,0,0,0,32,2,0,0}; 
};
````
