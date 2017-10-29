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


## Ways to create WMI Event Binding
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

Lastly on this list, the ```Registry*``` classes are **extrinsic events** which cannot be linked directly to the WMI model. Regardless, you can use thisQ to receive a notification if a part of the registry that has already been defined has been modified of.

### Avoid settig a short *within* value
When creating a WMI event query, make sure that the *within* value is not less than 30 (seconds) when going into production. It is common in testing, to set value to 5 (seconds); However, for production, never go less than 30 (seconds).


## WMI Consumer 
### Event Consumer Type
* [Script](https://msdn.microsoft.com/en-us/library/aa384749(v=vs.85).aspx) 
	* Allows you to run VBScript code in response to an event
	* Embed VBscript code in the consumer or reference a script file
* [Command Line](https://msdn.microsoft.com/en-us/library/aa389231(v=vs.85).aspx)
	* Run abitary comands in response to events
	* Pass event details as parameters to the command 
* [SMTP](https://msdn.microsoft.com/en-us/library/aa393629(v=vs.85).aspx)
	* Send an e-mail in response to an event (requites an open SMTP server)
	* Cannot use SMTP credentials with this consumer
* [NT Event Log](https://msdn.microsoft.com/en-us/library/aa392715(v=vs.85).aspx)
	* Log an event to the application event log in response to an event
	* Use WMI standtad string templates to pass event infomation to log entry
*[Log File Event](https://msdn.microsoft.com/en-us/library/aa392277(v=vs.85).aspx)
	* Writes customized strings to a text log file


