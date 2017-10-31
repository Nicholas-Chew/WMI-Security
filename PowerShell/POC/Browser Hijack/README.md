# Browser Hijack
## What is Browser Hijack?
The browser hijack is a script that uses WSMan (Remote Power Shell) or DCOM(enabled by default) for communication. Although WSMan is not enabled by default, many system administrators have enabled it to manage their infrastructure. Browser Hijack leverages on permanent WMI event subscription which is very hard to find and remove. It listens on Cim_DirectoryContainsFile for any changes every 30 seconds and invokes the Hijack script(VBScript) if there are changes.

## What Browser Hijack do?
As the name says, it hijacks “all” the browser's shortcut and put an argument to the shortcut, currently goog1e.com (not an active webpage). This forces the browser to start with goog1e.com as the default webpage.

## How to use Browser Hijack?
Browser Hijack is purposely made hard to successfully execute in case of any accident execution. To execute the script, please change the highlighted fields in the *BrowserHijack.ps1* file.
```
$Secpasswd = ConvertTo-SecureString "password" -AsPlainText -Force
$Creds = New-Object System.Management.Automation.PSCredential ("username", $secpasswd)
$CimSession = New-CimSession -ComputerName computername/ipaddress -Credential $Creds 
```

To use DCOM communication protocol, please uncomment this two line under *BrowserHijack.ps1*.
```
#$sOpt = New-CimSessionOption –Protocol DCOM
#$CimSession = New-CimSession –ComputerName computername/ipaddress –SessionOption $sOpt  -Credential $Creds 
```
