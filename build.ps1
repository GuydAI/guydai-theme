# Rebuilds GuydAI-Theme.jar from the files in src/.
# Usage:  ./build.ps1
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

$root = $PSScriptRoot
$src  = Join-Path $root 'src'
$jar  = Join-Path $root 'GuydAI-Theme.jar'

if (Test-Path $jar) { Remove-Item $jar -Force }
$zip = [System.IO.Compression.ZipFile]::Open($jar, 'Create')

function Add-Entry($zip, $file, $name) {
    # JAR entry names MUST use forward slashes or the IDE can't read the plugin.
    $entry = $zip.CreateEntry($name, [System.IO.Compression.CompressionLevel]::Optimal)
    $out   = $entry.Open()
    $bytes = [System.IO.File]::ReadAllBytes($file)
    $out.Write($bytes, 0, $bytes.Length)
    $out.Dispose()
}

Add-Entry $zip (Join-Path $src 'META-INF\plugin.xml')       'META-INF/plugin.xml'
Add-Entry $zip (Join-Path $src 'META-INF\pluginIcon.svg')   'META-INF/pluginIcon.svg'
Add-Entry $zip (Join-Path $src 'META-INF\pluginIcon_dark.svg') 'META-INF/pluginIcon_dark.svg'
Add-Entry $zip (Join-Path $src 'guydai.theme.json')         'guydai.theme.json'
Add-Entry $zip (Join-Path $src 'GuydAI.icls')               'GuydAI.icls'
$zip.Dispose()

Write-Host ("Built " + $jar + "  (" + (Get-Item $jar).Length + " bytes)") -ForegroundColor Green
