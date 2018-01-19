Function Convert-SIDToByte
{
    [CmdletBinding()]
    Param(
        [Parameter(
            Mandatory = $true,
            HelpMessage = "SID."
            )]
        [ValidateNotNullOrEmpty()]
        [Security.Principal.SecurityIdentifier]
        $SID
    )

    try
    {
        $SIDByte = New-Object Byte[] ($SID.BinaryLength)
        $SID.GetBinaryForm($SIDByte,0)
        return $SIDByte
    }
    catch
    { 
        Write-Error ('Exception converting SID to byte')
        return
    }
}