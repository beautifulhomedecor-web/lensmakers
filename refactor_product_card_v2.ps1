$cssPath = "c:\Users\NEW\OneDrive\Desktop\lensmakers-web\styles.css"
$css = [System.IO.File]::ReadAllText($cssPath)

# Fix product card core CSS
$css = $css -replace "background: #FFFFFF !important;", "background: var(--color-glass-surface) !important;"
$css = $css -replace "border: 1px solid #FFF6DA !important;", "border: 1px solid var(--color-glass-border) !important;"
$css = $css -replace "box-shadow: 0 4px 20px rgba\(1, 62, 55, 0\.08\) !important;", "box-shadow: 0 4px 20px var(--color-shadow) !important;"

# Typography inside product card
$css = $css -replace ".product-card-glass \.product-price, \[class\*=`"product-card`"\] \.product-price \{\s*color: #0B1F1C !important;\s*\}", ".product-card-glass .product-price, [class*=`"product-card`"] .product-price { color: var(--color-accent-primary) !important; }"

# Add specific overrides at the end to ensure priority
$css += "`n.product-card-glass:active, [class*=`"product-card`"]:active { transform: scale3d(0.95, 0.95, 1) !important; background: linear-gradient(rgba(135, 59, 59, 0.08), rgba(135, 59, 59, 0.08)), var(--color-glass-surface) !important; border: 1px solid var(--color-glass-border) !important; transition: all 120ms var(--spring-snappy) !important; }"
$css += "`n.product-card-glass h3, [class*=`"product-card`"] h3 { color: var(--color-text-primary) !important; }"
$css += "`n.product-card-glass .product-brand, [class*=`"product-card`"] .product-brand { color: var(--color-text-secondary) !important; }"
$css += "`n.product-card-glass .product-price, [class*=`"product-card`"] .product-price { color: var(--color-accent-primary) !important; }"
$css += "`n.product-card-glass .star-rating { color: var(--color-accent-primary) !important; }"
$css += "`n.wishlist-circle-btn.saved .heart-icon { color: var(--color-accent-primary) !important; }"
$css += "`n.wishlist-circle-btn .heart-icon { color: var(--color-bg-primary) !important; }"

[System.IO.File]::WriteAllText($cssPath, $css)

# Fix ShopScreen.js and HomeScreen.js inline glitches & badges
$files = @(
    "c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\screens\ShopScreen.js",
    "c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\screens\HomeScreen.js",
    "c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\components\EyeglassesSection.js",
    "c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\components\PremiumPicks.js",
    "c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\components\TrendingSunglasses.js"
)

foreach ($f in $files) {
    if (-not (Test-Path $f)) { continue }
    $content = [System.IO.File]::ReadAllText($f)
    
    # Fix glitch newlines from previous replace
    $content = $content -replace "color: '\r?\n\r?\n  '", "color: 'var(--color-text-secondary)'"
    $content = $content -replace "color: '\n\n  '", "color: 'var(--color-text-secondary)'"
    
    # Badges Fix (Discount & BOGO)
    # BOGO
    $content = $content -replace "background: 'var\(--color-accent-primary\)', color: 'var\(--color-text-primary\)', padding: '2px 8px', borderRadius: '999px', fontSize: '10px', fontWeight: '900', boxShadow: '0 2px 6px var\(--color-shadow\)' \}>\s*BOGO FREE", "background: 'var(--color-success)', color: 'var(--color-bg-primary)', padding: '2px 8px', borderRadius: '999px', fontSize: '10px', fontWeight: '900', boxShadow: '0 2px 6px var(--color-shadow)' }>BOGO FREE"
    
    # Discount
    $content = $content -replace "background: 'var\(--color-accent-primary\)', color: 'var\(--color-text-primary\)', padding: '2px 8px', borderRadius: '999px', fontSize: '10px', fontWeight: '900', boxShadow: '0 2px 6px var\(--color-shadow\)' \}>\s*\{item\.discount\}", "background: 'var(--color-accent-tint)', color: 'var(--color-accent-primary)', padding: '2px 8px', borderRadius: '999px', fontSize: '10px', fontWeight: '900', boxShadow: 'none' }>{item.discount}"
    
    # Inline heart
    $content = $content -replace "isSaved \? 'var\(--color-accent-primary\)' : 'var\(--color-bg-primary\)'", "isSaved ? 'var(--color-accent-primary)' : 'var(--color-bg-primary)'" # already correct
    
    [System.IO.File]::WriteAllText($f, $content)
}

Write-Host "Product Card refactor complete."
