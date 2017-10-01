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

### WMI Event Query Structure
##### Basic Example
`Select <fields> from <EventClass> WITHIN <Seconds> WHERE <criteria>`

###### A Realistic Example
`Select <fields> from <EventClass> WITHIN <Seconds> WHERE TargetInstance ISA '<TargetClass>'`

Note: *"TargetInstance"* is a property on intrisic event classes which refers to the object that generated the event (Eg. Win32_Process)

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