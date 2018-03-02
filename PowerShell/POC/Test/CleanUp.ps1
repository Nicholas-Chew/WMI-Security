﻿Get-CimInstance -Namespace root/subscription -ClassName __EventFilter -Filter "Name='BrowserHijackFilter'" | Remove-CimInstance
Get-CimInstance -Namespace root/subscription -ClassName ActiveScriptEventConsumer -Filter "Name='BrowserHijackConsumer'" | Remove-CimInstance
Get-CimInstance -Namespace root/subscription -ClassName __FilterToConsumerBinding -Filter "__PATH like '%BrowserHijackFilter%'" | Remove-CimInstance