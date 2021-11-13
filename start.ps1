 param (
    [string]$wd=$PSScriptRoot
 )
Set-Location $wd

$myE = Resolve-Path '.'
$myE = $myE.Path + '\DocumentationCapture.exe'
Copy-Item -Path $myE -Destination C:\DocumentationCapture.exe -Force
$conf = Resolve-Path '.\conf.json'
Set-Location C:\
Start-Process -verb runas "C:\DocumentationCapture.exe" -ArgumentList $conf

Write-Host 'Press Any Key!' -NoNewline
$null = [Console]::ReadKey('?')

<#
   .NOTES
    ===========================================================================
     Created with:  SAPIEN Technologies, Inc., PowerShell Studio 2014 v4.1.58
     Created on:    2017/12/29 
     Created by:    hokis
    ===========================================================================
    .DESCRIPTION
        1、用于显示或隐藏指定程序主窗口
        2、FindWindow 函数，获取指定窗口句柄。第一参数为窗口的类名(可为空)，第二参数为窗口标题文本
        3、ShowWindow 函数，设置指定窗口的显示状态。第一参数为指定窗口的句柄，第二参数即为需要设置的状态(部分常用值：0-隐藏，1-正常显示，2-最小化，3-最大化，9-还原)
#>

$code = @'
[DllImport("user32.dll", EntryPoint = "FindWindow")] public extern static IntPtr FindWindow(string lpClassName, string lpWindowName);
[DllImport("user32.dll", EntryPoint = "ShowWindow", CharSet = CharSet.Auto)] public extern static bool ShowWindow(IntPtr hwnd, uint nCmdShow);
'@
#引入API
$myAPI = Add-Type -MemberDefinition $code -Name myAPI -PassThru
#测试CMD窗口（需先运行一个CMD窗口）
$cmdWin = "lqJnMCy7fOFsS4ZG"
#显示（1或9）或隐藏（0）
$myapi::ShowWindow($myAPI::FindWindow("ConsoleWindowClass", $cmdWin), 0)

Write-Host 'Press Any Key!' -NoNewline
$null = [Console]::ReadKey('?')