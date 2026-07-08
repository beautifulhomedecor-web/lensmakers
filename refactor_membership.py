import re

path = r'c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\screens\MembershipScreen.js'

with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix the powershell glitch:
glitch_pattern = r"'\s*param\(\$m\)\s*\$opacity = \$m\.Groups\[1\]\.Value\s*\"rgba\(11,31,28,0\.\$opacity\)\"\s*'"
text = re.sub(glitch_pattern, "'var(--color-text-secondary)'", text)

# 2. Refactor colors for Prompt 8
# The prompt says: "Glass surface token for the price card, with a slightly stronger opacity" -> "rgba(255, 246, 218, 0.95)" or "var(--color-glass-surface)"
# Let's map standard tokens globally first
text = text.replace("'#0B1F1C'", "'var(--color-text-primary)'")
text = text.replace("'#A94A4A'", "'var(--color-accent-primary)'")
text = text.replace("linear-gradient(135deg, #013E37 0%, #A94A4A 100%)", "var(--color-accent-primary)")
text = text.replace("linear-gradient(135deg, #013E37, #A94A4A)", "var(--color-accent-primary)")
text = text.replace("'#FFFFFF'", "'var(--color-bg-primary)'")

# Price Card specific updates:
# Left: Monthly Plan
text = re.sub(r"className=\"glass-card-standard\" style=\{\{ padding: '18px 14px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', border: selectedPlan === 'monthly' \? '2px solid var\(--color-accent-primary\)' : '1px solid rgba\(255,255,255,0\.15\)'", r"className=\"\" style={{ background: 'rgba(255, 246, 218, 0.95)', boxShadow: '0 12px 48px var(--color-shadow)', padding: '18px 14px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', border: selectedPlan === 'monthly' ? '2px solid var(--color-accent-primary)' : '1px solid var(--color-glass-border)'", text)

# Right: Annual Plan
text = re.sub(r"className=\"glass-card-glow-pink\" style=\{\{ padding: '18px 14px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', border: '2px solid var\(--color-accent-primary\)'", r"className=\"\" style={{ background: 'rgba(255, 246, 218, 0.95)', boxShadow: '0 12px 48px var(--color-shadow)', padding: '18px 14px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', border: '2px solid var(--color-accent-primary)'", text)

# Benefit List (Checkmarks)
# "color: '#0B1F1C', fontSize: '18px', fontWeight: '900' }}>✓</div>"
text = re.sub(r"color: 'var\(--color-text-primary\)', fontSize: '18px', fontWeight: '900' \}\}>✓", r"color: 'var(--color-success)', fontSize: '18px', fontWeight: '900' }}>✓", text)

# "Join Club" Button
text = text.replace("borderColor: 'var(--color-accent-primary)', color: 'var(--color-accent-primary)'", "background: 'var(--color-accent-primary)', color: 'var(--color-bg-primary)', border: 'none'")

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Membership screen refactored.")
