import re

styles_path = r'c:\Users\NEW\OneDrive\Desktop\lensmakers-web\styles.css'
with open(styles_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Update tracking dots
css = re.sub(
    r"\.tracking-timeline-line \{\s*position: absolute; left: 13px; top: 20px; bottom: 20px;\s*width: 3px; background: #FFF6DA;",
    r".tracking-timeline-line {\n  position: absolute; left: 13px; top: 20px; bottom: 20px;\n  width: 3px; background: var(--color-glass-border);",
    css
)
css = re.sub(
    r"\.tracking-timeline-progress \{\s*position: absolute; left: 13px; top: 20px; width: 3px;\s*background: #013E37;",
    r".tracking-timeline-progress {\n  position: absolute; left: 13px; top: 20px; width: 3px;\n  background: var(--color-accent-primary);",
    css
)
css = re.sub(
    r"\.tracking-dot\.completed \{ background: #013E37; color: #FFFFFF; box-shadow: 0 0 10px rgba\(1,62,55,0\.3\); \}",
    r".tracking-dot.completed { background: var(--color-accent-primary); color: var(--color-bg-primary); border: none; box-shadow: none; }",
    css
)
css = re.sub(
    r"\.tracking-dot\.current \{\s*background: #A94A4A; color: #FFFFFF;\s*box-shadow: 0 0 16px rgba\(169,74,74,0\.5\);",
    r".tracking-dot.current {\n  background: var(--color-accent-primary); color: var(--color-bg-primary);\n  box-shadow: 0 0 16px var(--color-accent-primary);",
    css
)
css = re.sub(
    r"\.tracking-dot\.upcoming \{\s*background: #FFF6DA; border: 2px solid rgba\(1,62,55,0\.15\);",
    r".tracking-dot.upcoming {\n  background: transparent; border: 2px solid var(--color-glass-border);\n  color: transparent;",
    css
)
# Note: Since the glitch `color: param($m)` was already globally removed, the regex for `.tracking-dot.upcoming` might not match the color line, so replacing just the background and border is safer. Wait, if it was replaced by `color: 'var(--color-text-secondary)'`, the above regex for upcoming only replaces the first line of the block. I will just do a simpler replace.

# Actually, let's just forcefully replace the blocks:
css = re.sub(
    r"\.tracking-dot\.completed \{.*?\}",
    r".tracking-dot.completed { background: var(--color-accent-primary); color: var(--color-bg-primary); border: none; }",
    css, flags=re.DOTALL
)
css = re.sub(
    r"\.tracking-dot\.current \{.*?\}",
    r".tracking-dot.current {\n  background: var(--color-accent-primary); color: var(--color-bg-primary);\n  box-shadow: 0 0 16px var(--color-accent-primary);\n  animation: pulseGlowAnim 1.5s infinite ease-in-out;\n}",
    css, flags=re.DOTALL
)
css = re.sub(
    r"\.tracking-dot\.upcoming \{.*?\}",
    r".tracking-dot.upcoming {\n  background: transparent; border: 2px solid var(--color-glass-border);\n  color: transparent;\n}",
    css, flags=re.DOTALL
)

with open(styles_path, 'w', encoding='utf-8') as f:
    f.write(css)


track_path = r'c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\screens\EyeCheckupScreen.js'
with open(track_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Replace colors
js = js.replace("'#0B1F1C'", "'var(--color-text-primary)'")
js = js.replace("'#A94A4A'", "'var(--color-accent-primary)'")
js = js.replace("'#013E37'", "'var(--color-accent-primary)'")
js = js.replace("'#FFFFFF'", "'var(--color-bg-primary)'")

# Status Badge
js = js.replace(
    'className="badge-pill badge-pink"',
    'className="" style={{ background: \'var(--color-success)\', color: \'var(--color-bg-primary)\', padding: \'4px 12px\', borderRadius: \'999px\', fontSize: \'10px\', fontWeight: \'900\', letterSpacing: \'0.5px\' }}'
)

# Shadows for order cards
js = js.replace(
    'className="glass-card-elevated mb-4" style={{ padding: \'16px\'',
    'className="glass-card-elevated mb-4" style={{ padding: \'16px\', boxShadow: \'0 12px 48px var(--color-shadow)\''
)
js = js.replace(
    'className="glass-card-standard mb-4" style={{ padding: \'24px 20px\'',
    'className="glass-card-standard mb-4" style={{ padding: \'24px 20px\', boxShadow: \'0 12px 48px var(--color-shadow)\''
)

# Courier Info Sub-Card
js = js.replace(
    "background: 'rgba(255,240,224,0.8)'",
    "background: 'var(--color-glass-surface)'"
)
js = js.replace(
    "border: '1px solid rgba(255,255,255,0.15)'",
    "border: '1px solid var(--color-glass-border)'"
)
js = js.replace(
    "border: '1px solid rgba(255,255,255,0.2)'",
    "border: '1px solid var(--color-glass-border)'"
)
js = js.replace(
    "background: 'rgba(255,255,255,0.1)'",
    "background: 'var(--color-glass-surface)'"
)

# Text token for timestamp
js = js.replace("'#0B1F1C'", "'var(--color-text-primary)'")
js = js.replace("color: '#0B1F1C'", "color: 'var(--color-text-primary)'")

with open(track_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated Order Tracking for Prompt 11")
