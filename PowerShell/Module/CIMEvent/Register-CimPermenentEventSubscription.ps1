function New-CimActiveScriptEventConsumer
{
    [CmdletBinding()]
    Param(
        
        #Cim Event Filter Parameter

        [Parameter(
            Mandatory = $false,
            HelpMessage = "Namespace for event query to be executed on. Default:root\subscription"
            )]
        [ValidateNotNullOrEmpty()]
        $Namespace = 'root\subscription',


        [Parameter(
            Mandatory = $true,
            HelpMessage = "Path for Cim Event Consumer"
            )]
        [ciminstance]
        $Consumer,

        [Parameter(
            Mandatory = $true,
            HelpMessage = "Path for Cim Event Consumer"
            )]
        [ciminstance]
        $Filter,


        #Cim of WMI Event Filter Parameter


        #Common Parameter

         [Parameter(
            Mandatory = $false,
            ValueFromPipeline=$True,
            HelpMessage = "Computer Name/IP Address for this event filter."
            )]
        [string]
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

        #Use CimSession if it is passed
        if(!$PSBoundParameters.ContainsKey('CimSession'))
        {
            Write-Verbose "$CmdletName : No CimSession paseed, using Computer Name to create a CimSession"
            #Else use Computer Name and Credential
            $SessionParams = @{}

            $SessionParams.ComputerName = $ComputerName

            #If no Credential is passed, use local Credential
            if($PSBoundParameters.ContainsKey('Credential'))
            {
                Write-Verbose "$CmdletName : Credential passed, using Credential to build CimSession"
                $SessionParams.Credential = $Credential
            }
            else
            {
                Write-Verbose "$CmdletName : No Credential passed, requesting Credential"
                $SessionParams.Credential = Get-Credential
            }

            if($SessionParams.Credential -eq $null)
            {
                Write-Error "No credential found, Stopping" -ErrorAction:Stop
            }

            #Test is Remote PowerShell is Enabled
            Write-Verbose "$CmdletName : Using WS-Man protocol to create CimSession"
            $CimSession = New-CimSession @SessionParams
 
            if ($CimSession -eq $null) 
            {
                Write-Warning "$CmdletName : Failed using WS-Man protocol, using DCOM as the protocol now"
                $SessionParams.SessionOption = (New-CimSessionOption -Protocol Dcom)
                $CimSession = New-CimSession @SessionParams
            }

            rv SessionParams
        }

    }

    process
    {      
        $bindingParam = @{
            Filter = [ref]$Filter
            Consumer = [ref]$Consumer
         }

         New-CimInstance -ClassName __FilterToConsumerBinding -Namespace root/subscription -CimSession $CimSession -Property $bindingParam | out-null


    }

    end
    {

        if($PSBoundParameters.ContainsKey('ComputerName'))
        {
            # Clean up the CimSessions we created to support the ComputerName parameter
            $CimSession | Remove-CimSession
        }

        return $filter
    }
}