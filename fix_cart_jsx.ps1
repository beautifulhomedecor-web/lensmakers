$cartPath = "c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\screens\CartScreen.js"
$cart = [System.IO.File]::ReadAllText($cartPath, [System.Text.Encoding]::UTF8)

$cart = $cart -replace "style=\{\{ boxShadow: '0 8px 32px var\(--color-shadow\)',\s*style=\{\{", "style={{ boxShadow: '0 8px 32px var(--color-shadow)',"

[System.IO.File]::WriteAllText($cartPath, $cart, [System.Text.Encoding]::UTF8)
Write-Host "Fixed JSX style glitch."
