$path = "c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\screens\HomeScreen.js"
$content = [System.IO.File]::ReadAllText($path)

# Fix scriptblock glitch text
$content = $content -replace "\s*param\(\$m\)\s*\$opacity = \$m.Groups\[1\].Value\s*`"rgba\(11,31,28,0.\$opacity\)`"\s*", " "

# Remaining raw colors
$content = $content -replace "#2196F3", "var(--color-accent-primary)"
$content = $content -replace "rgba\(59, 130, 246, 0.12\)", "var(--color-accent-tint)"
$content = $content -replace "#3B82F6", "var(--color-accent-primary)"
$content = $content -replace "rgba\(156, 204, 101, 0.12\)", "var(--color-accent-tint)"
$content = $content -replace "#EAEAEA", "var(--color-glass-border)"
$content = $content -replace "#1C1917", "var(--color-text-primary)"
$content = $content -replace "#64748B", "var(--color-text-secondary)"
$content = $content -replace "rgba\(102,187,106,0.2\)", "var(--color-accent-tint)"
$content = $content -replace "#0288D1", "var(--color-accent-primary)"
$content = $content -replace "rgba\(255,122,48,0.18\)", "var(--color-accent-tint)"
$content = $content -replace "rgba\(255,122,48,0.4\)", "var(--color-glass-border)"
$content = $content -replace "#F0F0F5", "var(--color-text-secondary)"
$content = $content -replace "rgba\(255,255,255,0.06\)", "var(--color-shadow)"

[System.IO.File]::WriteAllText($path, $content)
Write-Host "Cleaned up HomeScreen.js"
