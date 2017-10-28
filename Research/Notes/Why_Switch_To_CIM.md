# Why Switch to CIM Cmdlets?
## The CIM Session
Both WMI and CIM supports ```ComputerName``` parameter that allow you to connect to a remote computer to execute commands. However, CIM also supports ```CimSession``` parametes, that takes a Session Object.

CimSession allows you to use **different credentials** even **different authentication** methods:
```
$Cred = Get-Credential
$Session = New-CimSession -ComputerName CM01 -Credential $Cred

$BasicSession = New-CimSession -ComputerName CM01 -Credential $Cred -Authentication Basic

Get-CimInstance -CimSession $Session -ClassName Win32_OperatingSystem
```

Cim Cmdlets by default uses WS-Man (Web Service-Management), as WS-Man is an industry standrad, the CIM Cmdlets aren't restricted to only Windows.

They can be used for basically any OS that supports WS-Man

An example is[Managing Linux OMI](https://becomelotr.wordpress.com/2013/06/22/managing-linux-via-omi-configuration/)

In addition, If WinRM is not enabled, the CimCmdlets can still fall back to DCOM (WMI Protocol)
```
New-CimSession –ComputerName CM01 –SessionOption (New-CimSessionOption –Protocol DCOM)
```

Below is a small snippet that allow you to auto fallback on DCOM when WS-Man is not avaliable
```
$SessionParams = @{}
if ($PSBoundParameters['Credential']) {$SessionParams.Credential = $Credential}
      
$SessionParams.ComputerName = $ComputerName
$WSMan = Test-WSMan -ComputerName $ComputerName -ErrorAction SilentlyContinue
 
if (($WSMan -ne $null) -and ($WSMan.ProductVersion -match 'Stack: ([3-9]|[1-9][0-9]+)\.[0-9]+')) {
    $Session = New-CimSession @SessionParams
} 
 
if ($Session -eq $null) {
    $SessionParams.SessionOption = (New-CimSessionOption -Protocol Dcom)
    $Session = New-CimSession @SessionParams
}
```

## Parallel Execution - Fan Out
WMI Cmdlets process each ```ComputerName``` sequentially. The execution time just sums up. To be able to reduce total execution time, a custom methods must be implemented for parallal execution using ```Invoke-Async```, ```Background jobs```, ```PS Parallel ForEach```.

However, Cim Cmdlets built this function out of the box:
```
$AllSessions = New-CimSession -ComputerName $Servers -Credential $Cred

Get-CimInstance -CimSession $AllSessions -ClassName Win32_ComputerSystem


$Servers = New-CimSession -ComputerName $Servers -Credential $Cred | Get-CimInstance -ClassName Win32_ComputerSystem
```

## Invoke methods with named parameters
Calling WMI methods using VBScript was (and still is) a pain:
```
strComputer = "."
Set objWMIService = GetObject("winmgmts:" _
    & "{impersonationLevel=impersonate}!\\" & strComputer _
    & "\root\sms\Site_TST")

Set objClientOperation= objWMIService.Get("SMS_ClientOperation")

' Obtain an InParameters object 
Set objInParam = objClientOperation.Methods_("InitiateClientOperation").inParameters.SpawnInstance_()

' Add the input parameters. 
objInParam.Properties_.item("Type") = 1
objInParam.Properties_.item("TargetCollectionID") = "SMS00001
objInParam.Properties_.item("TargetResourceIDs") = Array(123456,234567)
objInParam.Properties_.item("RandomizationWindow") = NULL

Set objOutParams = objClientOperation.ExecMethod_("InitiateClientOperation", objInParam)
```

It gets a whole lot easier using ```Inoke-WMIMethod```:
```
Invoke-WMIMethod -Class SMS_ClientOperation ` 
-Name "InitiateClientOperation" ` 
-ArgumentList @($null, "SMS00001", @(123456,234567), 1) ` -Namespace root\sms\site_XYZ
```

As you can see while it’s definitely easier than VBScript, it still has the drawback, that you need to supply the method parameters in a certain order. And if you think that this would be the order as specified in the documentation, you might be wrong.

The second option would be to get a list of parameters first and then pass them as an object.
```
$WMIConnection = [WMICLASS]"\\.\root\sms\Site_TST:SMS_ClientOperation"

$ClientOperation= $WMIConnection.psbase.GetMethodParameters("InitiateClientOperation")
$ClientOperation.Type = 1 
$ClientOperation.TargetCollectionID = "SMS00001"
$ClientOperation.TargetResourceIDs = @(123456,234567)
$ClientOperation.RandomizationWindow = $null

$WMIConnection.psbase.InvokeMethod("InitiateClientOperation",$ClientOperation,$Null)
```

This is working as well. Now let's have a look on how ```Invoke-CimMethod``` handles the same call:
```
$Args= @{
    Type=1
    TargetCollectionID="SMS00001"
    TargetResourceIDs=@(123456,234567)
    RandomizationWindow=$null
}
Invoke-CimMethod -ClassName SMS_ClientOperation `
                 -MethodName "InitiateClientOperation" ` 
                 -Arguments $Args `
                 -Namespace root\sms\site_TST
```
Many IT Professionals perfer handling methods and passing in a hashtable that contains the name and values for the method parameters.

For sure there are other interesting aspects as well like the easy serialization/deserialization of objects via Export-CliXML and Import-CliXML, listing of classes using Get-CimClass, the automated conversion of e.g. the WMI DateTime format into the DateTime format used within .Net and PowerShell and a bunch of others.

## Drawbacks
1. Dosen't work well with embedded classes without key property
2. Dosen't work with classes that contain lazy properties

However, there are work arounds below:

http://maikkoster.com/powershell-cim-cmdlets-working-with-embedded-or-keyless-classes/


http://maikkoster.com/powershell-cim-cmdlets-working-with-lazy-properties/