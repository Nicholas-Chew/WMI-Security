$Secpasswd = ConvertTo-SecureString "Secret" -AsPlainText -Force
$Creds = New-Object System.Management.Automation.PSCredential ("Administration", $secpasswd)
$CimSession = New-CimSession -ComputerName 0.0.0.0 -Credential $Creds
