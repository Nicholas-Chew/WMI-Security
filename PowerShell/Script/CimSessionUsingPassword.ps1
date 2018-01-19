$Secpasswd = ConvertTo-SecureString "P@ssw0rd!" -AsPlainText -Force
$Creds = New-Object System.Management.Automation.PSCredential ("wmiserver\dministrator", $secpasswd)
$CimSession = New-CimSession -ComputerName ComputerName -Credential $Creds