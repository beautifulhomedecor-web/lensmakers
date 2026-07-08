$shopPath = "c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\screens\ShopScreen.js"
$shop = [System.IO.File]::ReadAllText($shopPath)

$missingBlock = @"
                    <div>
                      <div style={{ fontSize: '14px', fontWeight: '800', color: 'var(--color-text-primary)' }}>{lens.name}</div>
                      <div style={{ fontSize: '12px', color: 'var(--color-text-secondary)', marginTop: '2px' }}>{lens.desc}</div>
                    </div>
                  </div>
                  <div style={{ fontSize: '14px', fontWeight: '800', color: isSel ? 'var(--color-accent-primary)' : 'var(--color-text-secondary)', whiteSpace: 'nowrap' }}>
                    {lens.price === 0 ? '+₹0' : `+₹${lens.price}`}
                  </div>
                </div>
              );
            })}
          </div>

          {/* DESCRIPTION & ACCORDIONS */}
"@

$shop = $shop -replace "(\s*\{isSel && <div style=\{\{ width: '8px', height: '8px', borderRadius: '50%', background: 'var\(--color-bg-primary\)' \}\} />\}\s*</div>\s*)\{/\* DESCRIPTION & ACCORDIONS \*/\}", "`$1$missingBlock"

[System.IO.File]::WriteAllText($shopPath, $shop)

Write-Host "Restored deleted block."
