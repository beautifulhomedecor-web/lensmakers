$cssPath = "c:\Users\NEW\OneDrive\Desktop\lensmakers-web\styles.css"
$css = [System.IO.File]::ReadAllText($cssPath)

# Replace product-card-glass styles in styles.css
$css = $css -replace ".product-card-glass, \[class\*=`"product-card`"\], .product-card \{`r?`n  background: #FFFFFF !important;`r?`n  border: 1px solid #FFF6DA !important;`r?`n  box-shadow: 0 4px 20px rgba\(1, 62, 55, 0\.08\) !important;`r?`n\}", ".product-card-glass, [class*=`"product-card`"], .product-card {`n  background: var(--color-glass-surface) !important;`n  border: 1px solid var(--color-glass-border) !important;`n  box-shadow: 0 4px 20px var(--color-shadow) !important;`n}"

$css = $css -replace ".product-card-glass:active, \[class\*=`"product-card`"\]:active \{`r?`n  transform: translateY\(-2px\) !important;`r?`n\}", ".product-card-glass:active, [class*=`"product-card`"]:active {`n  transform: scale3d(0.95, 0.95, 1) !important;`n  transition: transform 120ms var(--spring-snappy) !important;`n  background: linear-gradient(rgba(135, 59, 59, 0.08), rgba(135, 59, 59, 0.08)), var(--color-glass-surface) !important;`n}"

# Wait, the hover and active states are a bit different in styles.css. Let's just append the active state to the bottom of the file to ensure it overrides.
$css += "`n.product-card-glass:active, [class*=`"product-card`"]:active { transform: scale3d(0.95, 0.95, 1) !important; background: linear-gradient(rgba(135, 59, 59, 0.08), rgba(135, 59, 59, 0.08)), var(--color-glass-surface) !important; border: 1px solid var(--color-glass-border) !important; transition: all 120ms var(--spring-snappy) !important; }"

[System.IO.File]::WriteAllText($cssPath, $css)

# Now fix the glitches in ShopScreen.js
$shopPath = "c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\screens\ShopScreen.js"
$shop = [System.IO.File]::ReadAllText($shopPath)
$shop = $shop -replace "color: '`r`n`r`n  '", "color: 'var(--color-text-secondary)'"
$shop = $shop -replace "color: '`n`n  '", "color: 'var(--color-text-secondary)'"
$shop = $shop -replace "background: 'rgba\(67,160,71,0\.15\)'", "background: 'var(--color-success)'"
$shop = $shop -replace "color: 'var\(--color-text-primary\)', padding: '2px 8px', borderRadius: '999px', fontSize: '10px', fontWeight: '900', boxShadow: '0 2px 6px var\(--color-shadow\)' \}>\s*BOGO FREE", "color: 'var(--color-bg-primary)', padding: '2px 8px', borderRadius: '999px', fontSize: '10px', fontWeight: '900', background: 'var(--color-success)', boxShadow: '0 2px 6px var(--color-shadow)' }>BOGO FREE"
$shop = $shop -replace "background: 'var\(--color-accent-primary\)', color: 'var\(--color-text-primary\)', padding: '2px 8px', borderRadius: '999px', fontSize: '10px', fontWeight: '900', boxShadow: '0 2px 6px var\(--color-shadow\)' \}>\s*\{item\.discount\}", "background: 'var(--color-accent-tint)', color: 'var(--color-accent-primary)', padding: '2px 8px', borderRadius: '999px', fontSize: '10px', fontWeight: '900', boxShadow: 'none' }>{item.discount}"
[System.IO.File]::WriteAllText($shopPath, $shop)

# HomeScreen.js badges
$homePath = "c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\screens\HomeScreen.js"
$home = [System.IO.File]::ReadAllText($homePath)
$home = $home -replace "background: 'var\(--color-accent-primary\)', color: 'var\(--color-text-primary\)', padding: '2px 8px', borderRadius: '999px', fontSize: '10px', fontWeight: '900', boxShadow: '0 2px 6px var\(--color-shadow\)' \}>\s*BOGO FREE", "color: 'var(--color-bg-primary)', padding: '2px 8px', borderRadius: '999px', fontSize: '10px', fontWeight: '900', background: 'var(--color-success)', boxShadow: '0 2px 6px var(--color-shadow)' }>BOGO FREE"
$home = $home -replace "background: 'var\(--color-accent-primary\)', color: 'var\(--color-text-primary\)', padding: '2px 8px', borderRadius: '999px', fontSize: '10px', fontWeight: '900', boxShadow: '0 2px 6px var\(--color-shadow\)' \}>\s*\{item\.discount\}", "background: 'var(--color-accent-tint)', color: 'var(--color-accent-primary)', padding: '2px 8px', borderRadius: '999px', fontSize: '10px', fontWeight: '900', boxShadow: 'none' }>{item.discount}"
[System.IO.File]::WriteAllText($homePath, $home)

Write-Host "Product Card refactor complete."
