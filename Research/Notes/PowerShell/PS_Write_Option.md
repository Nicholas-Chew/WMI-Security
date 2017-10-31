# PowerShell Write Option
As of PowerShell v5, there are essentially six different kinds of streams: output, verbose, warning, error, debug, and information. 
Each of these streams is for various purposes and behaves a little bit differently. To aid in understanding this, you can think of a few of these streams as forming a hierarchy. 
These streams are debug, verbose, warning, and error in that order. Similar to how syslog represents severity in messages, PowerShell also adopts this concept of streams by severity.

### Write-Verbose
Send "nice to have" information to the console to let us know where it is in the process.

### Write-Error
Send a non-terminating error (error stream) to the console showing the read text. Normally for non-critical error. Use Throw if it is very critical

### Write-Warning
Send some text down the warning stream to warn the user this happened.

### Write-Debug
It isn't typical to use the debug stream. Other than returning output via the debug stream, it also serves a purpose in debugging.

