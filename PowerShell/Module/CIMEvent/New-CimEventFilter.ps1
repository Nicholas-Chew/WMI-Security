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
            ValueFromPipeline=$True,
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
        [Microsoft.Management.Infrastructure.CimSession[]]
        $CimSession

        #End of Common Parameter      
    )

    begin
    {
    	$CmdletName = $Pscmdlet.MyInvocation.MyCommand.Name

        #If CimSession is passed us CimSession
        if((!$PSBoundParameters.ContainsKey('CimSession')) -and ($PSBoundParameters.ContainsKey('$ComputerName')))
        {
            $SessionParams = @{}

            #Else use Computer Name and Credential
            $SessionParams.ComputerName = $ComputerName

            if($Credential)
            {
                $SessionParams.Credential = $Credential
            }
            else
            {
                $SessionParams.Credential = Get-Credential
            }

            #Test is Remote PowerShell is Enabled
            $WSMan = Test-WSMan -ComputerName $ComputerName -ErrorAction SilentlyContinue
 
            if (($WSMan -ne $null) -and ($WSMan.ProductVersion -match 'Stack: ([3-9]|[1-9][0-9]+)\.[0-9]+')) 
            {
                $CimSession = New-CimSession @SessionParams
            } 
 
            if ($Session -eq $null) 
            {
                $SessionParams.SessionOption = (New-CimSessionOption -Protocol Dcom)
                $CimSession = New-CimSession @SessionParams
            }

            rv $SessionParams
            rv $WSMan
        }
    }

    process
    {
        
    }

    end
    {
        Receive-Job -Job $Jobs -Wait
        $Jobs | Remove-Job

        if($PSBoundParameters.ContainsKey('ComputerName'))
        {
            # Clean up the CimSessions we created to support the ComputerName parameter
            $CimSession | Remove-CimSession
        }
    }
}