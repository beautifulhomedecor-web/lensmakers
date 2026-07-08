$path = "c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\screens\HomeScreen.js"
$content = [System.IO.File]::ReadAllText($path)

$glitch = @"
    param(`$m)
    `$opacity = `$m.Groups[1].Value
    `"rgba(11,31,28,0.`$opacity)`"
"@

$content = $content.Replace($glitch, "")
$content = $content.Replace(" : ''", "")
$content = $content.Replace(" : ' '", "")
$content = $content.Replace("color:  ,", "color: 'var(--color-text-secondary)',")

[System.IO.File]::WriteAllText($path, $content)
Write-Host "Cleaned up HomeScreen.js Glitch"
