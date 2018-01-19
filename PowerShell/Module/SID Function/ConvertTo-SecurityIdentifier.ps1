Function ConvertTo-SecurityIdentifier
{
    [CmdletBinding()]
    param(
        [Parameter(Mandatory=$true)]
        $SID
    )
    
    try
    {
        if( $SID -is [string] )
        {
            New-Object 'Security.Principal.SecurityIdentifier' $SID
        }
        elseif( $SID -is [byte[]] )
        {
            New-Object 'Security.Principal.SecurityIdentifier' $SID,0
        }
        elseif( $SID -is [Security.Principal.SecurityIdentifier] )
        {
            $SID
        }
        else
        {
            Write-Error ('Invalid SID.')
            return
        }
    }
    catch
    {
        Write-Error ('Exception converting SID')
        return
    }
}