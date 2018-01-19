#On Client side
#Get Host Name
nbtstat -A %ipaddress%	 

#Make srure WinRM is runnig
WinRM quickconfig
#Add remote server to trusted Host 
Set-Item WSMan:\localhost\Client\TrustedHosts -Value '%ipaddress%'

#Connect to Remote PS
Enter-PSSession -ComputerName %ipaddress% -Credential %login-user%
