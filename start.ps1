 param (
    [string]$wd
 )
Set-Location $wd
$myE = Resolve-Path '.'
$myE = $myE.Path + '\DocumentationCapture.exe'
Copy-Item -Path $myE -Destination C:\DocumentationCapture.exe -Force
$conf = Resolve-Path '.\conf.json'
& "C:\DocumentationCapture.exe" $conf
Write-Host 'Press Any Key!' -NoNewline
$null = [Console]::ReadKey('?')