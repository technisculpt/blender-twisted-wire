$Src = "Twisted Wire"
$Zipped = "Twisted Wire.zip"
$Addon = "C:\Users\marco\AppData\Roaming\Blender Foundation\Blender\3.1\scripts\addons\Twisted Wire"

Set-Location -Path "C:\Users\marco\blender-twisted-wire"

if (Test-Path $Zipped) 
{
  Remove-Item $Zipped
  Compress-Archive -Path $Src -DestinationPath $Zipped
}
else
{
	Compress-Archive -Path $Src -DestinationPath $Zipped
}

if (Test-Path $Addon)
{
  Remove-Item -Recurse $Addon
}