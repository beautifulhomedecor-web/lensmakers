$shopPath = "c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\screens\ShopScreen.js"
$shop = [System.IO.File]::ReadAllText($shopPath)

# Back/Share/Wishlist header background
$shop = $shop -replace "background: 'rgba\(255,245,236,0\.8\)'", "background: 'var(--color-glass-surface)'"

# Back & Share buttons background
$shop = $shop -replace "background: 'var\(--color-glass-border\)', border: '1px solid rgba\(255,255,255,0\.2\)'", "background: 'var(--color-glass-surface)', border: '1px solid var(--color-glass-border)'"

# Try in 3D Button
$shop = $shop -replace "background: 'rgba\(1,62,55, 0\.2\)'", "background: 'var(--color-glass-surface)'"

# Color variant swatch ring
$shop = $shop -replace "border: ``2px solid `$\{isSel \? 'var\(--color-bg-primary\)' : 'rgba\(255,255,255,0\.3\)'\}``", "border: ``2px solid `$\{isSel ? 'var(--color-accent-primary)' : 'var(--color-glass-border)'\}``"

# Price Block styling
$shop = $shop -replace "background: 'rgba\(255,240,224,0\.6\)'", "background: 'var(--color-glass-surface)'"
$shop = $shop -replace "color: 'var\(--color-text-primary\)'\}>₹\{Math\.round\(pdpItem\.price \* 0\.75\)\}", "color: 'var(--color-accent-primary)'}>₹{Math.round(pdpItem.price * 0.75)}"
$shop = $shop -replace "color: 'var\(--color-text-primary\)'\}>₹\{pdpItem\.price\}", "color: 'var(--color-accent-primary)'}>₹{pdpItem.price}"

# Fit size selector
$shop = $shop -replace "background: isSel \? 'linear-gradient\(135deg, var\(--color-accent-primary\) 0%, var\(--color-accent-primary\) 100%\)' : 'rgba\(255,240,224,0\.6\)'", "background: isSel ? 'var(--color-accent-primary)' : 'var(--color-glass-surface)'"
$shop = $shop -replace "border: isSel \? 'none' : '1px solid rgba\(255,255,255,0\.2\)'", "border: isSel ? '1px solid var(--color-accent-primary)' : '1px solid var(--color-glass-border)'"

# Fix newlines in ShopScreen.js (Fit/Lens size glitches)
$shop = $shop -replace "color: isSel \? 'var\(--color-bg-primary\)' : 'var\(--color-text-secondary\)'\r?\n\r?\n  ',", "color: isSel ? 'var(--color-bg-primary)' : 'var(--color-text-secondary)',"
$shop = $shop -replace "color: isSel \? 'var\(--color-bg-primary\)' : 'var\(--color-text-secondary\)'\r?\n\r?\n  '", "color: isSel ? 'var(--color-bg-primary)' : 'var(--color-text-secondary)'"
$shop = $shop -replace "boxShadow: isSel \? '0 4px 12px \r?\n\r?\n  ' : 'none',", "boxShadow: isSel ? '0 4px 12px var(--color-shadow)' : 'none',"

# Sticky Action Row Buttons
$shop = $shop -replace "border: '1\.5px solid var\(--color-accent-primary\)', color: 'var\(--color-text-primary\)', background: 'var\(--color-glass-surface\)'", "border: '1.5px solid var(--color-accent-primary)', color: 'var(--color-accent-primary)', background: 'var(--color-glass-surface)'"

[System.IO.File]::WriteAllText($shopPath, $shop)


# Update btn-primary-pill in styles.css to use Accent token per Prompt 5
$cssPath = "c:\Users\NEW\OneDrive\Desktop\lensmakers-web\styles.css"
$css = [System.IO.File]::ReadAllText($cssPath)
$css = $css -replace "\.btn-primary-pill, \[class\*=`"btn-primary`"\] \{\r?\n  background: #013E37 !important;", ".btn-primary-pill, [class*=`"btn-primary`"] {`n  background: var(--color-accent-primary) !important;"
$css = $css -replace "outline: 2px solid #013E37 !important;", "outline: 2px solid var(--color-accent-primary) !important;"
[System.IO.File]::WriteAllText($cssPath, $css)

Write-Host "PDP refactor complete."
