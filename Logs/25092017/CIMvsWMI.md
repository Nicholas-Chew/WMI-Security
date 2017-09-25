## CIM vs WMI - Microsoft
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

**Only Studied the difference between CIM and WMI. Didn't look into differences in cmdlet**