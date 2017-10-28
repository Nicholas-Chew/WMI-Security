function Copy-FileByCim 
{
    [CmdletBinding()]
    param (
        [Parameter(
            Mandatory = $true,
            HelpMessage = "Destination CIMSession for this file transfer.",
            ValueFromPipeline=$true
            )]
        [Microsoft.Management.Infrastructure.CimSession[]]
        $CimSession,

        [Parameter(
            Mandatory = $true,
            HelpMessage = "Absolute file path for source this of transfer."
            )]
        [string] $LocalFilePath,

        [Parameter(
            Mandatory = $true,
            HelpMessage = "Absolute file path for destination of this transfer."
            )]
        [string] $RemoteFilePath
    )

    $Process = Get-CimInstance -Namespace root\cimv2 -ClassName Win32_Process

    $Base64File = [System.Convert]::ToBase64String((Get-Content -Path $LocalFilePath -Encoding Byte -Raw))
    $Arguments = @{
        CommandLine = 'powershell.exe -Command "Set-Content -Path ''{0}'' -Value ([System.Convert]::FromBase64String(''{1}'')) -Encoding Byte; sleep 3"' -f $RemoteFilePath, $Base64File
    }

    Write-Verbose -Message $Arguments.CommandLine
    
    $Result = Invoke-CimMethod -CimSession $CimSession -ClassName Win32_Process -MethodName Create -Arguments $Arguments
    Write-Output -InputObject $Result
}