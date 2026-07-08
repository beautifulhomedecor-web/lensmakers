$files = 'HomeScreen.js', 'Header.js', 'BottomNav.js', 'PromoCard.js', 'EyeglassesSection.js', 'PremiumPicks.js', 'TrendingSunglasses.js'

foreach ($f in $files) {
    $pathResult = Get-ChildItem -Path "c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src" -Recurse -Filter $f | Select-Object -First 1
    if (-not $pathResult) { continue }
    $path = $pathResult.FullName
    $content = [System.IO.File]::ReadAllText($path)

    # Fix syntax error in Header.js if present
    $content = $content -replace "'1px solid'1px solid #FFF6DA'", "'1px solid var(--color-glass-border)'"
    $content = $content -replace "'1px solid #FFF6DA'", "'1px solid var(--color-glass-border)'"

    # Border colors
    $content = $content -replace "#FFF6DA", "var(--color-glass-border)"

    # Backgrounds
    $content = $content -replace "#FFFFFF", "var(--color-bg-primary)"
    $content = $content -replace "'white'", "'var(--color-bg-primary)'"
    $content = $content -replace "`"white`"", "`"var(--color-bg-primary)`""
    $content = $content -replace "rgba\(255,\s*255,\s*255,\s*0\.\d+\)", "var(--color-glass-surface)"
    $content = $content -replace "rgba\(255,\s*246,\s*218,\s*0\.\d+\)", "var(--color-glass-surface)"
    
    # Text
    $content = $content -replace "#0B1F1C", "var(--color-text-primary)"
    $content = $content -replace "#2B2B2B", "var(--color-text-primary)"
    
    $content = $content -replace "rgba\(11,\s*31,\s*28,\s*0\.6\)", "var(--color-text-secondary)"
    $content = $content -replace "rgba\(11,31,28,0\.6\)", "var(--color-text-secondary)"
    $content = $content -replace "rgba\(11,\s*31,\s*28,\s*0\.[45]\)", "var(--color-text-secondary)"
    $content = $content -replace "rgba\(11,31,28,0\.[45]\)", "var(--color-text-secondary)"
    
    # Shadows (Opacity 0.05 to 0.15)
    $content = $content -replace "rgba\(11,\s*31,\s*28,\s*0\.0\d\)", "var(--color-shadow)"
    $content = $content -replace "rgba\(11,\s*31,\s*28,\s*0\.1[0-5]\)", "var(--color-shadow)"
    $content = $content -replace "rgba\(11,31,28,0\.0\d\)", "var(--color-shadow)"
    $content = $content -replace "rgba\(11,31,28,0\.1[0-5]\)", "var(--color-shadow)"
    
    # Accents
    $content = $content -replace "#A94A4A", "var(--color-accent-primary)"
    $content = $content -replace "rgba\(169,\s*74,\s*74,\s*0\.\d+\)", "var(--color-accent-tint)"
    $content = $content -replace "#013E37", "var(--color-accent-primary)"
    
    # Old Accent Tint (rgba(1,62,55, 0.x)) for non-shadow non-text
    $content = $content -replace "rgba\(1,\s*62,\s*55,\s*0\.\d+\)", "var(--color-accent-tint)"
    $content = $content -replace "rgba\(1,62,55,0\.\d+\)", "var(--color-accent-tint)"
    
    # Success
    $content = $content -replace "#66BB6A", "var(--color-success)"
    
    # Text secondary legacy
    $content = $content -replace "#706C68", "var(--color-text-secondary)"
    
    [System.IO.File]::WriteAllText($path, $content)
    Write-Host "Updated $f"
}
Write-Host "Replacement Complete."
