$cartPath = "c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\screens\CartScreen.js"
$cart = [System.IO.File]::ReadAllText($cartPath, [System.Text.Encoding]::UTF8)

# 1. BOGO Banner updates
$cart = $cart -replace "background: 'linear-gradient\(135deg, rgba\(67,160,71,0\.15\), rgba\(255,240,224,0\.8\)\)'", "background: 'var(--color-glass-surface)'"
$cart = $cart -replace "border: '1\.5px solid #013E37'", "border: '1px solid var(--color-glass-border)'"
$cart = $cart -replace "boxShadow: '0 8px 32px var\(--color-shadow\)'", "" # remove if exists to avoid duplicates
$cart = $cart -replace "className=`"bogo-glow-banner(.*?)\`"", "className=`"bogo-glow-banner`$1`" style={{ boxShadow: '0 8px 32px var(--color-shadow)', "
$cart = $cart -replace "background: 'linear-gradient\(135deg, #A94A4A, #013E37\)'", "background: 'var(--color-accent-primary)'"

# 2. Cart Item Card
$cart = $cart -replace "background: 'rgba\(255,240,224, 0\.85\)'", "background: 'var(--color-glass-surface)'"
$cart = $cart -replace "color: '#0B1F1C'", "color: 'var(--color-text-primary)'"
$cart = $cart -replace "Part of your BOGO offer 🎁\r?\n\s*</div>", "Part of your BOGO offer 🎁`r`n                          </div>"
$cart = $cart -replace "<div style=\{\{ fontSize: '12px', color: 'var\(--color-text-primary\)', fontWeight: '700', marginTop: '4px' \}\}>\r?\n\s*Part of your BOGO offer", "<div style={{ fontSize: '12px', color: 'var(--color-success)', fontWeight: '700', marginTop: '4px' }}>`r`n                            Part of your BOGO offer"

# 3. Quantity Stepper
$cart = $cart -replace "background: 'rgba\(255,255,255,0\.06\)'", "background: 'var(--color-glass-surface)'"
$cart = $cart -replace "background: 'rgba\(255,255,255,0\.1\)'", "background: 'transparent'"
$cart = $cart -replace "color: '#A94A4A'", "color: 'var(--color-accent-primary)'"

# 4. Save for later & Move to cart links
$cart = $cart -replace "♡ Save for Later\r?\n\s*</button>", "♡ Save for Later`r`n                      </button>"
$cart = $cart -replace "onClick=\{\(\) => handleMoveToSaved\(item\.id\)\}\r?\n\s*>\r?\n\s*♡ Save for Later", "onClick={() => handleMoveToSaved(item.id)}`r`n                      >`r`n                        ♡ Save for Later"
# I'll use regex for these buttons
$cart = [regex]::Replace($cart, "color: 'var\(--color-text-primary\)', fontSize: '12px', fontWeight: '700', cursor: 'pointer' \}\}\s*onClick=\{\(\) => handleMoveToSaved", "color: 'var(--color-accent-primary)', fontSize: '12px', fontWeight: '700', cursor: 'pointer' }} onClick={() => handleMoveToSaved")
$cart = [regex]::Replace($cart, "bordercolor: 'var\(--color-text-primary\)', color: 'var\(--color-text-primary\)' \}\}\s*onClick=\{\(\) => handleMoveToCart", "borderColor: 'var(--color-accent-primary)', color: 'var(--color-accent-primary)' }} onClick={() => handleMoveToCart")

# Global remaining Raw Hex to Token replacements
$cart = $cart -replace "'#0B1F1C'", "'var(--color-text-primary)'"
$cart = $cart -replace "'#A94A4A'", "'var(--color-accent-primary)'"
$cart = $cart -replace "'linear-gradient\(135deg, #013E37, #A94A4A\)'", "'var(--color-accent-primary)'"
$cart = $cart -replace "'linear-gradient\(135deg, #013E37, var\(--color-accent-primary\)\)'", "'var(--color-accent-primary)'"
$cart = $cart -replace "background: 'rgba\(255,240,224,0\.6\)'", "background: 'var(--color-glass-surface)'"
$cart = $cart -replace "border: '1\.5px solid var\(--color-accent-primary\)'", "border: '1px solid var(--color-glass-border)'"
$cart = $cart -replace "'#FFFFFF'", "'var(--color-bg-primary)'"

# Saved Items background container fixing
$cart = $cart -replace "background: 'rgba\(255,255,255,0\.03\)'", "background: 'var(--color-glass-surface)'"
$cart = $cart -replace "border: '1px solid rgba\(255,255,255,0\.12\)'", "border: '1px solid var(--color-glass-border)'"
$cart = $cart -replace "border: '1px solid rgba\(255,255,255,0\.15\)'", "border: '1px solid var(--color-glass-border)'"

[System.IO.File]::WriteAllText($cartPath, $cart, [System.Text.Encoding]::UTF8)
Write-Host "Cart screen colors replaced."
