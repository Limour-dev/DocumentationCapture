# set-executionpolicy remotesigned
Set-Location $PSScriptRoot
$scriptPath = Resolve-Path '.\start.ps1'
$wd = Resolve-Path '.'
Start-Process -verb runas "powershell.exe" -ArgumentList "-NoProfile -ExecutionPolicy Bypass -file $scriptPath", $wd