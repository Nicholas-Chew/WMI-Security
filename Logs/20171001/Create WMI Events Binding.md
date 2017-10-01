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

## Types of WMI Events
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

## WMI Event Query Structure
##### Basic Example
`Select <fields> from <EventClass> WITHIN <Seconds> WHERE <criteria>`

###### A Realistic Example
`Select <fields> from <EventClass> WITHIN <Seconds> WHERE TargetInstance ISA '<TargetClass>'`

Note: *"TargetInstance"* is a property on intrisic event classes which refers to the object that generated the event (Eg. Win32_Process)

##### Examples
###### New Process
