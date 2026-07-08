$shopPath = "c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\screens\ShopScreen.js"
$shop = [System.IO.File]::ReadAllText($shopPath, [System.Text.Encoding]::UTF8)

$correctBlock = @"
          {/* LENS CUSTOMIZATION SECTION (Radio List) */}
          <div className="glass-card-elevated" style={{ margin: '0 var(--screen-padding) 24px', padding: '22px 18px' }}>
            <div className="flex-between" style={{ marginBottom: '14px' }}>
              <h3 style={{ fontSize: '16px', fontWeight: '800', color: 'var(--color-text-primary)' }}>Choose Your Lenses</h3>
              <span 
                style={{ fontSize: '12px', color: 'var(--color-accent-primary)', fontWeight: '700', cursor: 'pointer', textDecoration: 'underline' }}
                onClick={() => showToast('🔬 Lens Guide: Blue Light filters screen glare!')}
              >
                What's the difference?
              </span>
            </div>

            {LENS_OPTIONS.map((lens, idx) => {
              const isSel = pdpSelectedLensIdx === idx;
              return (
                <div
                  key={idx}
                  className={`lens-radio-row `$\{isSel ? 'selected' : ''\}`}
                  onClick={() => setPdpSelectedLensIdx(idx)}
                >
                  <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                    <div style={{ width: '20px', height: '20px', borderRadius: '50%', border: '2px solid var(--color-accent-primary)', display: 'flex', alignItems: 'center', justifyContent: 'center', background: isSel ? 'var(--color-accent-primary)' : 'transparent' }}>
                      {isSel && <div style={{ width: '8px', height: '8px', borderRadius: '50%', background: 'var(--color-bg-primary)' }} />}
                    </div>

                    <div>
                      <div style={{ fontSize: '14px', fontWeight: '800', color: 'var(--color-text-primary)' }}>{lens.name}</div>
                      <div style={{ fontSize: '12px', color: 'var(--color-text-secondary)', marginTop: '2px' }}>{lens.desc}</div>
                    </div>
                  </div>
                  <div style={{ fontSize: '14px', fontWeight: '800', color: isSel ? 'var(--color-accent-primary)' : 'var(--color-text-secondary)', whiteSpace: 'nowrap' }}>
                    {lens.price === 0 ? '+₹0' : `+₹`$\{lens.price\}`}
                  </div>
                </div>
              );
            })}
          </div>
"@

$regex = [regex]::new("\{\/\* LENS CUSTOMIZATION SECTION \(Radio List\) \*\/\}.*?(?=\{\/\* DESCRIPTION & ACCORDIONS \*\/\})", [System.Text.RegularExpressions.RegexOptions]::Singleline)

$shop = $regex.Replace($shop, $correctBlock + "`r`n`r`n          ")

[System.IO.File]::WriteAllText($shopPath, $shop, [System.Text.Encoding]::UTF8)

Write-Host "Forced utf8 repair."
