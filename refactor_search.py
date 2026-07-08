import re

header_path = r'c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\components\Header.js'
styles_path = r'c:\Users\NEW\OneDrive\Desktop\lensmakers-web\styles.css'

with open(header_path, 'r', encoding='utf-8') as f:
    header_content = f.read()

# 1. Add isSearchFocused state to Header
header_content = header_content.replace(
    "const [voiceTranscript, setVoiceTranscript] = useState('');",
    "const [voiceTranscript, setVoiceTranscript] = useState('');\n  const [isSearchFocused, setIsSearchFocused] = useState(false);"
)

# 2. Update standalone search input focus and shadow
# Original:
# border: isListening ? '1.5px solid var(--color-accent-primary)' : '1px solid var(--color-glass-border)',
# boxShadow: isListening ? '0 0 0 3px var(--color-accent-tint), inset 0 2px 4px var(--color-accent-tint)' : 'inset 0 2px 4px var(--color-accent-tint)',

header_content = re.sub(
    r"border: isListening \? '[^']+' : '[^']+',",
    "border: (isListening || isSearchFocused) ? '1.5px solid var(--color-accent-primary)' : '1px solid var(--color-glass-border)',",
    header_content
)

header_content = re.sub(
    r"boxShadow: isListening \? '[^']+' : '[^']+',",
    "boxShadow: (isListening || isSearchFocused) ? '0 0 0 3px var(--color-accent-tint), 0 16px 48px var(--color-shadow)' : 'inset 0 2px 4px var(--color-accent-tint)',",
    header_content
)

header_content = re.sub(
    r"<input\n\s*type=\"text\"",
    "<input\n              type=\"text\"\n              onFocus={() => setIsSearchFocused(true)}\n              onBlur={() => setTimeout(() => setIsSearchFocused(false), 200)}",
    header_content
)

# 3. Update search icon and clear button colors
header_content = re.sub(
    r'color: \'var\(--color-text-primary\)\', pointerEvents: \'none\', zIndex: 2',
    "color: 'var(--color-accent-primary)', pointerEvents: 'none', zIndex: 2",
    header_content
)

header_content = re.sub(
    r"color: 'var\(--color-text-primary\)', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center',\n\s*fontSize: '11px', zIndex: 3",
    "color: 'var(--color-accent-primary)', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center',\n              fontSize: '11px', zIndex: 3",
    header_content
)

# 4. Replace the autocomplete-dropdown content
new_dropdown_content = """        <div 
          className="autocomplete-dropdown"
          style={{
            position: 'absolute', top: '100%', left: 'var(--screen-padding)', right: 'var(--screen-padding)',
            background: 'var(--color-bg-primary)',
            border: '1px solid var(--color-glass-border)',
            borderRadius: '16px',
            marginTop: '8px',
            boxShadow: '0 12px 36px var(--color-shadow)',
            overflow: 'hidden',
            zIndex: 999999
          }}
        >
          {/* RECENT SEARCHES */}
          {debouncedQuery.length === 0 && (
            <div style={{ padding: '16px' }}>
              <div style={{ fontSize: '11px', color: 'var(--color-text-secondary)', fontWeight: '700', letterSpacing: '0.8px', marginBottom: '12px' }}>
                RECENT SEARCHES
              </div>
              <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
                {['Titanium', 'Aviator', 'VIP Club', 'Blue Light'].map((term) => (
                  <button
                    key={term}
                    className="recent-search-chip"
                    style={{
                      padding: '6px 14px', borderRadius: '999px', background: 'var(--color-glass-surface)',
                      border: '1px solid var(--color-glass-border)', color: 'var(--color-text-secondary)',
                      fontSize: '12px', fontWeight: '600', cursor: 'pointer', transition: 'all 200ms ease'
                    }}
                    onClick={() => setSearchQuery(term)}
                  >
                    {term}
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* SEARCH RESULTS GRID */}
          {debouncedQuery.length > 0 && (
            <div style={{ padding: '16px' }}>
              <div style={{ fontSize: '11px', color: 'var(--color-text-secondary)', fontWeight: '700', letterSpacing: '0.8px', marginBottom: '12px', borderBottom: '1px solid var(--color-glass-border)', paddingBottom: '8px' }}>
                SEARCH RESULTS FOR "{debouncedQuery.toUpperCase()}"
              </div>
              
              {matchedResults.length === 0 ? (
                <div style={{ padding: '24px 0', textAlign: 'center', color: 'var(--color-text-secondary)', fontSize: '13px' }}>
                  No exact matches found. Try searching for "Titanium", "VIP", or "Try-On".
                </div>
              ) : (
                <div className="product-grid-2col">
                  {matchedResults.map((item, index) => {
                    const price = item.sub.includes('₹') ? item.sub.split('₹')[1] : '3,499';
                    const category = item.sub.split(' • ')[0] || item.type;
                    
                    return (
                      <div key={index} className="product-card-glass" onClick={() => handleSelectResult(item)}>
                        <div className="white-surface-inset">
                          <div style={{ position: 'absolute', top: '8px', left: '8px', display: 'flex', flexDirection: 'column', gap: '4px', zIndex: 5 }}>
                            {item.type === 'product' && (
                              <span style={{ background: 'var(--color-accent-primary)', color: 'var(--color-text-primary)', padding: '2px 8px', borderRadius: '999px', fontSize: '10px', fontWeight: '900' }}>
                                BOGO FREE
                              </span>
                            )}
                          </div>
                          <div style={{ fontSize: '64px', filter: 'drop-shadow(0 8px 12px var(--color-shadow))', display: 'flex', alignItems: 'center', justifyContent: 'center', height: '100%' }}>
                            {item.thumb || (item.icon === 'camera' ? '📷' : '⭐')}
                          </div>
                        </div>
                        <div style={{ padding: '14px 14px 16px', display: 'flex', flexDirection: 'column', flex: 1, justifyContent: 'space-between' }}>
                          <div>
                            <div style={{ fontSize: '10px', fontWeight: '700', color: 'var(--color-text-secondary)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                              {category}
                            </div>
                            <h3 style={{ fontSize: '14px', fontWeight: '800', color: 'var(--color-text-primary)', margin: '4px 0 8px', lineHeight: '1.3' }}>
                              {item.name}
                            </h3>
                          </div>
                          <div className="flex-between" style={{ alignItems: 'flex-end', marginTop: '4px' }}>
                            <div>
                              <div style={{ display: 'flex', alignItems: 'baseline', gap: '6px' }}>
                                <span style={{ fontSize: '16px', fontWeight: '900', color: 'var(--color-text-primary)' }}>₹{price}</span>
                              </div>
                            </div>
                            <button
                              type="button"
                              style={{
                                width: '34px', height: '34px', borderRadius: '50%',
                                background: 'var(--color-accent-primary)', border: 'none', color: 'var(--color-text-primary)', 
                                display: 'flex', alignItems: 'center', justifyContent: 'center', cursor: 'pointer'
                              }}
                            >
                              →
                            </button>
                          </div>
                        </div>
                      </div>
                    );
                  })}
                </div>
              )}
            </div>
          )}
        </div>"""

# Replace the dropdown logic in Header.js
# It spans from <div className="autocomplete-dropdown" ... to its closing </div>
header_content = re.sub(
    r"\{\/\* LIVE AUTOCOMPLETE DROPDOWN \*\/}.*?className=\"autocomplete-dropdown\".*?</div>\s*\)\}\s*</div>\s*\)\}\s*<>\s*;\s*};\s*window\.Header = Header;",
    "<!-- ERROR IN REGEX -> use a robust split/replace -->",
    header_content, flags=re.DOTALL
)

# Better replacement method:
# Find {/* LIVE AUTOCOMPLETE DROPDOWN */} and replace until the end of the block.
start_idx = header_content.find('{/* LIVE AUTOCOMPLETE DROPDOWN */}')
if start_idx != -1:
    end_idx = header_content.find('      </div>\n      )}\n    </>\n  );\n};\n\nwindow.Header = Header;')
    if end_idx != -1:
        header_content = header_content[:start_idx] + "{/* EXPANDED DROPDOWN (Recent & Results) */}\n      {(debouncedQuery.length > 0 || isSearchFocused) && (\n" + new_dropdown_content + "\n      )}\n" + header_content[end_idx:]


with open(header_path, 'w', encoding='utf-8') as f:
    f.write(header_content)

# Clean up styles.css param($m) in search placeholder
with open(styles_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Lines 3415-3420:
css = re.sub(
    r"\.search-bar-wrapper input::placeholder,\n\.search-input-container input::placeholder \{\n\s*color:\s*param\(\$m\).*?rgba\(11,31,28,0\.\$opacity\)\"\s*!important;",
    ".search-bar-wrapper input::placeholder,\n.search-input-container input::placeholder {\n  color: var(--color-text-secondary) !important;",
    css, flags=re.DOTALL
)

with open(styles_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Search results refactored!")
