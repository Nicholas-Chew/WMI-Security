# CIM vs WMI - Microsoft
## Content
1. CIM vs WMI
2. Why is CIM Cmdlets created
3. Key goals for new CIM Cmdlets
4. Basic Usage Of CIM Cmdlets

## Basic Termology
| Short-Form | Description |
| :-- | :----- |
| CIM | Common Information Model (CIM) is the DMTF standard [DSP0004] for describing the structure and behavior of managed resources such as storage, network, or software components. |
| WMI | Windows Management Instrumentation (WMI) is a CIM server that implements the CIM standard on Windows. |
| [WS-Man] (https://en.wikipedia.org/wiki/WS-Management) | WS-Management (WS-Man) protocol is a SOAP-based, firewall-friendly protocol for management clients to communicate with CIM servers. |
| [WinRM] (https://msdn.microsoft.com/en-us/library/windows/desktop/aa384426%28v=vs.85%29.aspx) | Windows Remote Management (WinRM) is the Microsoft implementation of the WS-Man protocol on Windows. |


## CIM vs WMI

CIM = WMI. CIM is an open standard from the Distributed Management Task Force (DMTF), with the latest version introduced in January 2016. 
CIM provides a common definition of management information for systems, networks, applications, and services, and it allows for vendor extensions. 
WMI is the Microsoft implementation of CIM for the Windows platform.

Get-WmiObject is one of the original PowerShell cmdlets. 
It was enhanced in PowerShell 2.0 when the other WMI cmdlets were introduced. 
In PowerShell 1.0, Get-WmiObject was the only cmdlet with the option to access another system. 

The big drawback to the WMI cmdlets is that they use DCOM to access remote machines. 
DCOM isn’t firewall friendly, can be blocked by networking equipment, and gives some arcane errors when things go wrong. 

The CIM cmdlets appeared in PowerShell 3.0 as part of the new API for working with CIM classes, which is more standards based. 
The CIM cmdlets were overshadowed by PowerShell workflows, but they are (to my mind) the most important thing to come out of that release. 

The other major CIM-related advance was the introduction of CDXML, which enables a CIM class to be wrapped in some simple XML and published as a PowerShell module. 
This is how over 60% of the cmdlets in Windows 8 and later are produced.

The big difference between the WMI cmdlets and the CIM cmdlets is that the CIM cmdlets use WSMAN (WinRM) to connect to remote machines.


## Why is CIM Cmdlets Created
We had two set of Cmdlets to manage Windows and Non-Windows. WMI Cmdlets were primarily used to manage Windows and WsMan Cmdlets were targeted at non-Windows that implemented WsMan standard.
##### WMI Cmdlets:
> Pros: Provid better task abstraction compare to WS-Man Cmdlet, output is a .Net Object

> Cons: Use of non-standrad DCOM protocol. Does not work for non-Windows Platform

##### WinRM Cmdlets:
> Pros: Works with Windows and non-Windows using standard protocol

> Cons: Poor task abstraction. Output is XML

Problem:
1. Major obstacle in PS scriptiong for WMI is lack of discoverabiity. 
2. WMI Cmdlets don't pprovide first class PS experience.
3. Issue with serializing a WMI objec
4. No concept of session reuse
5. WMI object has weir looking property name (like __Server)
6. Poor formatting for most of the commonly used WMI classes

## Key goals for new CIM Cmdlets
> **Rich PowerShell experience**. Make CIM a first class citizen of PS, addressing usability concerns and user feedback for WMI and WsMan Cmdlets. 

> **Standard compliance**. With so much focus on standards, our goal is to make PowerShell the best platform for managing Windows and Non-Windows. New CIM Cmdlets should be able to manage any CIM + WsMan compliant endpoint, including Windows.

> **Support for down-level machines**. We understand that there are more down-level servers in a datacenter than there would be Windows Server 2012 for some time to come. We want to make sure same set of Cmdlets can be used to manage down-level Windows as well.

## Basic Usage Of CIM Cmdlets
### Goal 1 - Rich PowerShell Experiene
#### 1. Discovery of classes and namespaces
Key Improvement:
1. Tab completion for classname and namespace parameters. 
2. Get-CimClass Cmdlets

```
# Using tab completion for CIM cmdlet parameters ( Tab+Space in ISE shows a drop down)

Get-CimInstance –Namespace <Tab> #Finding top-level namespaces
```

```
# Tab completion for class names
# If namespace is not specified, shows classes from default root/cimv2 namespace

Get-CimInstance -ClassName *Bios<Tab>

Get-CimInstance –Namespace root/Microsoft/Windows/smb –ClassName <tab>

# Note: Tab completion only works for local machine.
```

```
# Using Get-CimClass for advanced class search
# All classes in root/cimv2

Get-CimClass
```

```
#Classes named like disk

Get-CimClass -ClassName *disk*
```

```
# The Cmdlet makes querying much easier (what would require scripting before)
# Get all classes starting with "Win32" that have method starting with "Term"

Get-CimClass Win32* -MethodName Term*
```

```
# Get classes starting with "Win32" that have a property named "Handle"

Get-CimClass Win32* -PropertyName Handle
```

```
# Get classes starting with "Win32" that have the "Association" qualifier

Get-CimClass Win32* -QualifierName Association
```

```
#Find classes used for events

Get-CimClass -Namespace root/Microsoft/Windows/smb -class *Smb* -QualifierName Indication
```
Tab Completion described above only works for local machine.

#### 2. Getting Instances
Key Improvement:
1. ```Get-CimInstance``` returns one or more instances of CimInstance. Ciminstance is different from the object returned by ```Get-WmiObject```
2. ```__Properties``` are no longer mixed with properties of an instance
3. Reduce memory and on-the-wire footprint by allowing retrival of a subset of properties
4. Allow retrieval of key properties
5. Allow creation of in-memory instance to reduce round trips
6. Allow retrieval of speciffic instances using in-memory instance or actual instance
7. ```DateTime``` value s are returned as objects of ```System.DateTime.type``` . Old Cmdlets treat them as strings

```
# Get-CimInstance was designed to be similar to the Get-WmiObject
# WMI Cmdlet : Get-WmiObject -class Win32_Process
# WsMan Cmdlet : get-wsmaninstance wmicimv2/win32_process -Enumerate
# The default value of -Namespace is root/cimv2, and the default value of -ComputerName is local computer

Get-CimInstance -Class Win32_Process
```

```
# Filtering using WQL

Get-CimInstance -Query "SELECT * FROM Win32_Process WHERE Name Like ‘power%’"
```

```
# use the -Filter parameter with -classname

Get-CimInstance -Class Win32_Process -Filter "Name Like ‘power%’"
```

```
#Retrieving a subset of properties : To reduce memory and on-the-wire footprint

Get-CimInstance -Class Win32_Process -Property Name, Handle
```

```
#Only get the key properties

Get-CimInstance -Class Win32_Process -KeyOnly
```

```
########################## Looking into CimInstance #########################

$x, $y = Get-CimInstance Win32_Process

$x | gm


# The object contains the full CIM class derivation hierarchy

$x.pstypenames


# The object also has a reference to its class declaration

$x.CimClass | gm
```

```
# DateTime values are returned as strings

Get-WmiObject Win32_OperatingSystem | Select *Time*


# DateTime values are returned as System.DateTime

Get-CimInstance Win32_OperatingSystem | Select *Time*#
```

#### 3. Working with associations
Working with associations was not straight foward in the old WMI cmdlets. To resolve this, the new cmdlets called ```Get-CimAssociatedInstance``` was built.

```
# Get instance of Win32_LogicalDisk class with DriveType = 3 (hard drives)

$disk1, $diskn = Get-CimInstance -class Win32_LogicalDisk -Filter ‘DriveType = 3’

$disk1


# Get the all instances associated with this disk

Get-CimAssociatedInstance -CimInstance $disk1


# Get instances of a specific type

Get-CimAssociatedInstance -CimInstance $disk1 -ResultClassName Win32_DiskPartition


# Finding associated instances through a specific CIM relationship

Get-CimAssociatedInstance -CimInstance $diskn -Association Win32_LogicalDiskRootDirectory
```

#### 4. Working with methods
Large number of task in WMI are achieved by invoking methods.

Key Improvement for ```Invoke-CimMethod```:
1. Discovery of method and method paramters
2. Execution of methods with parameters

```
$class = Get-CimClass Win32_Process

$class.CimClassMethods


# Get the parameters of the Create method

$class.CimClassMethods["Create"].Parameters


# Invoke the static Create method on the Win32_Process class to create an instance of the Notepad application. Notice that the method parameters are given in a hash table since CIM method arguments are unordered by definition.

Invoke-CimMethod -Class win32_process -MethodName Create -Argument @{CommandLine=’notepad.exe’;
CurrentDirectory = "c:\windows\system32"}


# Get the owners of the running Notepad instances

$result = Invoke-CimMethod -Query ‘SELECT * FROM Win32_Process WHERE name like "notepad%"’ -MethodName GetOwner


# The result has the returned value and out parameters of the method

$result
```

#### 5. CliXML Serialization
CimInstance supports full fidelity serialization and deserialization. This is an important feature for those who wish to save state of an instance or result of a cmdlet and then want to use it later. The WMI cmdlets do not support full-fidelity serialization/deserialization.

```
# CimInstances are serialized and deserialized with full fidelity

$x = Get-CimInstance Win32_Service

$x

$x[0].pstypenames

$x | Export-CliXml t1.xml
```

```
$y = Import-CliXml .\t1.xml

$y

$y[0].pstypenames

# The deserialized objects are identical to the ones obtained from the server

diff ($y) (Get-CimInstance win32_service )
```

#### 6. Remote Management
Managing remote machines with the new cmdlets is also pretty simple and straight forward. The two parameters that can be used to manage remote machines are:
> a.ComputerName

> b.CimSession

```
$props = @{v_Key = [UInt64] 8;}

# If ComputerName parameter is used, the cmdlets create an implicit session during the execution.

$inst = New-CimInstance -ClassName TestClass -Namespace root\test -Key v_Key -Property $props -ComputerName SecondWin8Server
```

```
# Create a session

$session = New-CimSession –ComputerName SecondWin8Server
```

```
# Use the session

$inst = New-CimInstance -ClassName TestClass -Namespace root\test -Key v_Key -Property $props –CimSession $session
```

### WMI vs CIM
| WMI Cmdlets | CIM Cmdlets |
| :---------- | :---------- |
| Get-WmiObject | Get-CimInstance |
| Get-WmiObject -list | Get-CimClass |
| Set-WmiInstance | Set-CimInstance |
| Set-WmiInstance -PutTypeCreateOnly | New-CimInstance |
|Remove-WmiObject | Remove-CimInstance |
| Invoke-WmiMethod | Invoke-CimMethod |

```
# OLD:

Invoke-WMIMethod -class Win32_Process -Name create -ArgumentList ‘calc.exe’


# NEW:

Invoke-CimMethod Win32_Process -MethodName create -Arguments @{CommandLine=’calc.exe’}

New Cmdlet takes a hash table or ordered dictionary as input not an Object.
```

### Goal 2 - Standrad Compliance
· CIM cmdlets are modeled on generic CIM operations

· Work over WsMan for remote management, making it possible to manage any server or device that implements WsMan and CIM standard.

· Removes the need to build custom agents and/or protocol to manage complex heterogeneous environments

· CIM cmdlets will work seamlessly with the new Open Management Infrastructure. http://blogs.technet.com/b/windowsserver/archive/2012/06/28/open-management-infrastructure.aspx

```
# Save credentials in an object

$cred = Get-Credential -UserName admin


# Create a session with Intel AMT machine.

$s = New-CimSession -ComputerName $serverAMT -Port 16992 -Authentication Digest -Credential $cred


# Use classname to get instances from an Intel AMT machine.

Get-CimInstance -class CIM_ComputerSystem -Namespace interop -CimSession $s


# Use resourceURI to get instances from an Intel AMT machine.

$resourceURI = “http://intel.com/wbem/wscim/1/amt-schema/1/AMT_GeneralSettings”

Get-CimInstance -ResourceUri $resourceURI -Namespace interop -CimSession $s
```

### Goal 3 - Support for down-level OS or non-windows machines
CIM Cmdlets can used to manage any machine that has a CIM standrads compliant CIMOM.

To manage these machines, a CimSession to the machine is required. Once a CimSession is created, the machine can be managed irrespective of the OS.

WinRM support on down-level windows machinesis limited. The latest WMF-V1 release will enable the latest version of WinRM on the down-level machine.

WinRM can always use DCOM protocol if WMF-V1 is not installed.

```
# If ComputerName is specified, WinRM protocol is used

PS:> $serverwin8 = New-CimSession –ComputerName "ServerWin8"

PS:> $serverwin2k8r2 = New-CimSession –ComputerName “Serverwin2k8r2 "
```

```
# For a remote machine, if you wish to go over DCOM, you need to explicitly specify

PS:> $sOpt = New-CimSessionOption –Protocol DCOM

PS:> $sessionWin2k8r2Dcom = New-CimSession –ComputerName “Serverwin2k8r2 " –SessionOption $sOpt
```

```
# User Experience remains same irrespective of the target machine.

PS:> $instanceServerWin8 = Get-CimInstance –CimSession $ serverwin8

PS:> $instanceServerWin2k8r2 = Get-CimInstance –CimSession $ serverwin2k8r2

PS:> $instanceServerWin2k8r2DCOM = Get-CimInstance –CimSession $ sessionWin2k8r2Dcom

#Note: The results in $instanceServerWin2k8r2 and $instanceServerWin2k8r2DCOM are identical in all aspects.

# Only the protocol used to get them is different.
```