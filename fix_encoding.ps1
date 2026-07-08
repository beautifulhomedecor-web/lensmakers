$shopPath = "c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\screens\ShopScreen.js"
$shop = [System.IO.File]::ReadAllText($shopPath, [System.Text.Encoding]::UTF8)

# The corrupted line is: {lens.price === 0 ? '+?'0' : +?$\{lens.price\}} or similar.
# We will just replace the entire div block using a simpler regex.

$corruptedRegex = [regex]::new("\<div style=\{\{ fontSize: '14px', fontWeight: '800', color: isSel \? 'var\(--color-accent-primary\)' : 'var\(--color-text-secondary\)', whiteSpace: 'nowrap' \}\}\>.*?\<\/div\>", [System.Text.RegularExpressions.RegexOptions]::Singleline)

$cleanBlock = @"
<div style={{ fontSize: '14px', fontWeight: '800', color: isSel ? 'var(--color-accent-primary)' : 'var(--color-text-secondary)', whiteSpace: 'nowrap' }}>
                    {lens.price === 0 ? '+₹0' : `+₹`$\{lens.price\}}
                  </div>
"@

$shop = $corruptedRegex.Replace($shop, $cleanBlock)

[System.IO.File]::WriteAllText($shopPath, $shop, [System.Text.Encoding]::UTF8)

Write-Host "Fixed encoding."
