$cartPath = "c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\screens\CartScreen.js"
$cart = [System.IO.File]::ReadAllText($cartPath, [System.Text.Encoding]::UTF8)

$glitchRegex = [regex]::new('\r?\n\s*param\(\$m\)\r?\n\s*\$opacity = \$m\.Groups\[1\]\.Value\r?\n\s*"rgba\(11,31,28,0\.\$opacity\)"\r?\n\s*', [System.Text.RegularExpressions.RegexOptions]::Singleline)

$cart = $glitchRegex.Replace($cart, 'var(--color-text-secondary)')

[System.IO.File]::WriteAllText($cartPath, $cart, [System.Text.Encoding]::UTF8)

Write-Host "Cleaned up CartScreen corruption."
