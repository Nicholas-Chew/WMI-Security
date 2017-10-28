function New-WMIEventFilter
{
    [CmdletBinding()]
    Param(
        
        #WMI Event Filter Parameter

        [Parameter(
            Mandatory = $false,
            HelpMessage = "Name of event filter."
            )]
        [ValidateNotNullOrEmpty()]
        [string]
        $Name,

        [Parameter(
            Mandatory = $false,
            HelpMessage = "Namespace for event query to be executed on"
            )]
        [ValidateNotNullOrEmpty()]
        $EventNamespace = 'root\cimv2',


        [Parameter(
            Mandatory = $true,
            HelpMessage = "WQL event query to be used for this event filter."
            )]
        [string]
        $Query,

        #End of WMI Event Filter Parameter


        #Common Parameter

         [Parameter(
            Mandatory = $false,
            HelpMessage = "Computer Name/IP Address for this event filter."
            )]
        [string[]]
        $ComputerName = '.',

        [Parameter(
            Mandatory = $false,
            HelpMessage = "Credentials for specified computers."
            )]
        [Management.Automation.PSCredential]
        [Management.Automation.CredentialAttribute()]
        $Credential = [Management.Automation.PSCredential]::Empty,

        [Parameter(
            Mandatory = $false,
            HelpMessage = "CimSessionDcom for this event filter."
            )]
        [Management.Automation.PSCredential]
        [Management.Automation.CredentialAttribute()]
        $CimSession

        #End of Common Parameter      
    )

    begin
    {
        #If CimSession is passed us CimSession
        if((!$CimSession) -and ($ComputerName))
        {
            #Else use Computer Name and Credential
            if($Credential)
            {
                $CimSession = New-CimSessionDcom -ComputerName $ComputerName -Credential $Credential
            }
            else
            {
                $CimSession = New-CimSessionDcom -ComputerName $ComputerName
            }
        }

        #Check if Event filter with the same name already exists
        if ($Name)
		{
			${ExistingFilter} = Get-CimInstance -Namespace ${Namespace} -ComputerName ${ComputerName} -Class __EventFilter -Filter "Name = '${Name}'"
			if (${ExistingFilter})
			{
				Write-Warning -Message "${CmdletName}: __EventFilter instance already exists with name ${Name}"
				#Write-Output -InputObject ${ExistingFilter}
			}
}
    }

}