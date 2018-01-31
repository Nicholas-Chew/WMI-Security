## WMI Protocol - How to remote WMI?
Windows Management Instrumentation can be access through 2 protocol:

### 1. WinRM(Windows Remote Management)
| | |
|:----|:----|
|Protocol used: | WS-Management Protocol|
|Port used: | tcp:5985 (default, HTTP) tcp:5986 (HTTPS,default)|

##### Setting up WinRM on remote server
`winrm quickconfig` starts winrm using the default template which only listens to HTTP.

`winrm quickconfig -transport:https` will listens to HTTPS.

For more configuration for WinRM click [here](https://msdn.microsoft.com/en-us/library/aa384372(v=vs.85).aspx).

##### Using WinRM to  interact with WMI
Since WinRM allows PSRemote to create by default. There are two ways to interact with WMI:
1. PSRemote to remote host and invoke WMI method
2. Using CIM method to interact with WMI, for more info type `help *cim*` in powershell.

**NOTE**: WinRM can be quite pickish on its [Auth type(depending on configuration)](https://msdn.microsoft.com/en-us/library/aa384295(v=vs.85).aspx). A quick workaround can be adding remote host to TrustedHost using `winrm s winrm/config/client '@{TrustedHosts="IP-ADDRESS"}'`.


### 2. DCOM(Distributed Component Object Model) **This only works on local	**
| | |
|:----|:----|
|Protocol used: | DPM control protocol|
|Port used: | tcp:135|

##### Setting up DCOM on remote server
DCOM is enabled by default in Windows. If it is not, it can be enable through `dcomcnfg.exe`.

Click [here](https://msdn.microsoft.com/en-us/library/aa822854(v=vs.85).aspx) for more infomation 

##### Using WinRM to  interact with WMI
There is two ways to interact with WMI using DCOM:
1. Using PowerShell's WMI command, for more info type `help *wmi*` in powershell.
2. Using `wmic` client

**NOTE**: DCOM is very not firewall friendly. Beisde opening port on network  firewall. You might also need toallow DCOM on the windows host using `netsh advfirewall firewall set rule group="windows management instrumentation (wmi)" new enable=yes`