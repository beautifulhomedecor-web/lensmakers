$path = "c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\screens\ShopScreen.js"
$content = [System.IO.File]::ReadAllText($path)

# Fix glitch
$glitch = @"
    param(`$m)
    `$opacity = `$m.Groups[1].Value
    `"rgba(11,31,28,0.`$opacity)`"
"@
$content = $content.Replace($glitch, "")
$content = $content.Replace(" : ''", "")
$content = $content.Replace(" : ' '", "")
$content = $content.Replace("color:  ,", "color: 'var(--color-text-secondary)',")
$content = $content.Replace("color: isSel ? '#FFFFFF' : '", "color: isSel ? 'var(--color-bg-primary)' : 'var(--color-text-secondary)'")
$content = $content.Replace("color: checked ? '#FFFFFF' : '", "color: checked ? 'var(--color-bg-primary)' : 'var(--color-text-secondary)'")

# Border colors
$content = $content -replace "#FFF6DA", "var(--color-glass-border)"
$content = $content -replace "rgba\(255,255,255,0\.15\)", "var(--color-glass-border)"
$content = $content -replace "rgba\(255,255,255,0\.1\)", "var(--color-glass-border)"

# Backgrounds
$content = $content -replace "#FFFFFF", "var(--color-bg-primary)"
$content = $content -replace "'white'", "'var(--color-bg-primary)'"
$content = $content -replace "rgba\(255,\s*255,\s*255,\s*0\.[9]\d*\)", "var(--color-glass-surface)"
$content = $content -replace "rgba\(255,\s*246,\s*218,\s*0\.\d+\)", "var(--color-glass-surface)"
$content = $content -replace "rgba\(255,245,236,0\.95\)", "var(--color-glass-surface)"
$content = $content -replace "rgba\(255,240,224,0\.8\)", "var(--color-glass-surface)"

# Text
$content = $content -replace "#0B1F1C", "var(--color-text-primary)"
$content = $content -replace "rgba\(11,\s*31,\s*28,\s*0\.6\)", "var(--color-text-secondary)"

# Shadows 
$content = $content -replace "rgba\(11,\s*31,\s*28,\s*0\.0[6-9]\)", "var(--color-shadow)"
$content = $content -replace "rgba\(11,\s*31,\s*28,\s*0\.1[0-5]\)", "var(--color-shadow)"
$content = $content -replace "rgba\(0,\s*0,\s*0,\s*0\.\d+\)", "var(--color-shadow)"

# Accents
$content = $content -replace "#A94A4A", "var(--color-accent-primary)"
$content = $content -replace "rgba\(169,\s*74,\s*74,\s*0\.\d+\)", "var(--color-accent-tint)"
$content = $content -replace "#013E37", "var(--color-accent-primary)"

# Success
$content = $content -replace "#66BB6A", "var(--color-success)"
$content = $content -replace "#22C55E", "var(--color-success)"

# Unselected Chip text (using Accent primary per prompt)
# Since the prompt said "Accent tint token for the unselected chip label color, at full opacity for legibility" which equals Accent primary
$content = $content -replace "'#706C68'", "'var(--color-accent-primary)'"

[System.IO.File]::WriteAllText($path, $content)
Write-Host "Replaced tokens in ShopScreen.js"
