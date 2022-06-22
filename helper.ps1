$Src = "Twisted Wire Pair"
$Zipped = "Twisted Wire Pair.zip"
$Addon = "C:\Users\marco\AppData\Roaming\Blender Foundation\Blender\3.1\scripts\addons\Twisted Wire Pair"

Set-Location -Path "C:\Users\marco\blender-twisted-wire-pair"

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