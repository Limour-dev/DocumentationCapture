# set-executionpolicy remotesigned
$scriptPath = Resolve-Path '.\start.ps1'
$wd = Resolve-Path '.'
Start-Process -verb runas "powershell.exe" -ArgumentList "-file $scriptPath", $wd