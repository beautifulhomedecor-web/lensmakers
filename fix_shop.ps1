$path = "c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\screens\ShopScreen.js"
$content = [System.IO.File]::ReadAllText($path)

$glitchStr = "var(--color-accent-primary)' : '`r`n`r`n  '"
$content = $content.Replace($glitchStr, "var(--color-accent-primary)' : 'var(--color-text-secondary)'")

$glitchStr2 = "var(--color-accent-primary)' : '`n`n  '"
$content = $content.Replace($glitchStr2, "var(--color-accent-primary)' : 'var(--color-text-secondary)'")

$glitchStr3 = "isSel ? 'var(--color-bg-primary)' : '`n`n  '"
$content = $content.Replace($glitchStr3, "isSel ? 'var(--color-bg-primary)' : 'var(--color-text-secondary)'")

$glitchStr4 = "isSel ? 'var(--color-bg-primary)' : '`r`n`r`n  '"
$content = $content.Replace($glitchStr4, "isSel ? 'var(--color-bg-primary)' : 'var(--color-text-secondary)'")

$glitchStr5 = "color: checked ? 'var(--color-bg-primary)' : '`n`n  '"
$content = $content.Replace($glitchStr5, "color: checked ? 'var(--color-bg-primary)' : 'var(--color-text-secondary)'")

$glitchStr6 = "color: checked ? 'var(--color-bg-primary)' : '`r`n`r`n  '"
$content = $content.Replace($glitchStr6, "color: checked ? 'var(--color-bg-primary)' : 'var(--color-text-secondary)'")

[System.IO.File]::WriteAllText($path, $content)
Write-Host "Fixed newlines."
