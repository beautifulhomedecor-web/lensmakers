import re

path = r'c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\screens\ProfileScreen.js'

with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix the powershell glitch:
glitch_pattern = r"'\s*param\(\$m\)\s*\$opacity = \$m\.Groups\[1\]\.Value\s*\"rgba\(11,31,28,0\.\$opacity\)\"\s*'"
text = re.sub(glitch_pattern, "'var(--color-text-secondary)'", text)

# 2. General Token Replacements
text = text.replace("'#0B1F1C'", "'var(--color-text-primary)'")
text = text.replace("'#A94A4A'", "'var(--color-accent-primary)'")
text = text.replace("'#FFFFFF'", "'var(--color-bg-primary)'")

# 3. Avatar ring outline (it's already #A94A4A which became var(--color-accent-primary))
# 4. Membership pill (ACTIVE MEMBER / Join Club)
text = re.sub(r"className=\"badge-pill badge-green\"(\s*style=\{\{[^\}]*\}\})", r"className=\"\"\1", text)
text = re.sub(r"padding: '6px 16px', fontSize: '11px', fontWeight: '800', cursor: 'pointer', boxShadow: '0 0 16px rgba\(67,160,71,0\.4\)', display: 'flex', alignItems: 'center', gap: '6px'", r"background: 'var(--color-accent-primary)', color: 'var(--color-bg-primary)', padding: '6px 16px', borderRadius: '999px', fontSize: '11px', fontWeight: '800', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '6px'", text)
# The "Join Club" pill when not a member
text = re.sub(r"background: 'rgba\(1,62,55,0\.15\)', border: '1\.5px solid #013E37', color: 'var\(--color-text-primary\)'", r"background: 'var(--color-accent-primary)', border: 'none', color: 'var(--color-bg-primary)'", text)
# Arrow on join club
text = re.sub(r"<span style=\{\{ color: 'var\(--color-text-primary\)' \}\}>→</span>", r"<span style={{ color: 'var(--color-bg-primary)' }}>→</span>", text)

# 5. Chevrons on every navigable list row -> accent token
text = re.sub(r"color: 'var\(--color-text-secondary\)', fontWeight: '800' \}\}>→</span>", r"color: 'var(--color-accent-primary)', fontWeight: '800' }}>→</span>", text)

# 6. Log out of account row (Line 528+)
# Should use accent token for its icon and label (Wait, the row around 210 also has Log Out)
text = re.sub(r"color: 'var\(--color-accent-primary\)', fontSize: '12px', fontWeight: '800'", r"color: 'var(--color-accent-primary)', fontSize: '12px', fontWeight: '800'", text) # already accent
text = re.sub(r"border: '1\.5px solid rgba\(239,83,80,0\.3\)',\s*background: 'rgba\(239,83,80,0\.08\)'", r"border: '1.5px solid var(--color-accent-primary)', background: 'transparent'", text)
# The text and icon for the main log out is already '#A94A4A' which is now 'var(--color-accent-primary)'

# 7. Shadows beneath identity header card and stats row container
text = re.sub(r"className=\"glass-card-elevated(.*?)\"(\s*)style=\{\{ padding", r"className=\"glass-card-elevated\1\"\2style={{ boxShadow: '0 12px 48px var(--color-shadow)', padding", text)
text = re.sub(r"className=\"glass-card-standard(.*?)style=\{\{ display: 'grid'", r"className=\"glass-card-standard\1style={{ boxShadow: '0 12px 48px var(--color-shadow)', display: 'grid'", text)

# 8. In-transit/delivered badge should be var(--color-success). It is using "badge-green".
# Let's ensure "1 IN TRANSIT" has var(--color-success) inline instead of relying on badge-green just in case.
text = re.sub(r"className=\"badge-pill badge-green\" style=\{\{ fontSize: '9px' \}\}>1 IN TRANSIT", r"className=\"\" style={{ background: 'rgba(122, 142, 110, 0.2)', color: 'var(--color-success)', padding: '2px 8px', borderRadius: '999px', fontSize: '9px', fontWeight: '900' }}>1 IN TRANSIT", text)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Profile screen refactored.")
