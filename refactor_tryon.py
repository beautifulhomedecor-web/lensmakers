import re

styles_path = r'c:\Users\NEW\OneDrive\Desktop\lensmakers-web\styles.css'
with open(styles_path, 'r', encoding='utf-8') as f:
    css = f.read()

# .tryon-circle-btn
css = re.sub(
    r"\.tryon-circle-btn \{\s*width: 44px; height: 44px; border-radius: 14px;\s*background: rgba\(255,245,236, 0\.75\);\s*border: 1\.5px solid rgba\(255, 255, 255, 0\.25\);\s*color: #FFFFFF;",
    r".tryon-circle-btn {\n  width: 44px; height: 44px; border-radius: 14px;\n  background: var(--color-glass-surface);\n  backdrop-filter: blur(24px);\n  -webkit-backdrop-filter: blur(24px);\n  border: 1.5px solid var(--color-glass-border);\n  color: var(--color-text-primary);\n  box-shadow: 0 12px 48px var(--color-shadow);",
    css
)
css = re.sub(
    r"\.tryon-circle-btn:hover \{\s*background: rgba\(1,62,55, 0\.25\);\s*border-color: #0B1F1C;\s*color: #FFFFFF;",
    r".tryon-circle-btn:hover {\n  background: rgba(255, 246, 218, 0.95);\n  border-color: var(--color-accent-primary);\n  color: var(--color-accent-primary);",
    css
)

# .tryon-bottom-panel
# Adding glass surface, blur(24px), and shadow to the bottom panel
css = re.sub(
    r"\.tryon-bottom-panel \{\s*position: absolute; bottom: 20px; left: 0; right: 0;\s*margin: 0 auto;\s*width: calc\(100% - 24px\);\s*max-width: 620px;\s*z-index: 20;",
    r".tryon-bottom-panel {\n  position: absolute; bottom: 20px; left: 0; right: 0;\n  margin: 0 auto;\n  width: calc(100% - 24px);\n  max-width: 620px;\n  z-index: 20;\n  background: var(--color-glass-surface);\n  backdrop-filter: blur(24px);\n  -webkit-backdrop-filter: blur(24px);\n  border: 1.5px solid var(--color-glass-border);\n  box-shadow: 0 12px 48px var(--color-shadow);",
    css
)

# .tryon-thumb-circle
css = re.sub(
    r"\.tryon-thumb-circle \{\s*width: 56px; height: 56px; border-radius: 50%;\s*background: #FFFFFF;\s*border: 2px solid #FFF6DA;",
    r".tryon-thumb-circle {\n  width: 56px; height: 56px; border-radius: 50%;\n  background: var(--color-glass-surface);\n  backdrop-filter: blur(24px);\n  -webkit-backdrop-filter: blur(24px);\n  border: 2px solid var(--color-glass-border);\n  box-shadow: 0 12px 48px var(--color-shadow);",
    css
)
css = re.sub(
    r"\.tryon-thumb-circle\.selected \{\s*border-color: #0B1F1C;",
    r".tryon-thumb-circle.selected {\n  border-color: var(--color-accent-primary);",
    css
)
css = re.sub(
    r"box-shadow: 0 0 16px rgba\(1,62,55,0\.25\);\s*background: #FFF6DA;",
    r"box-shadow: 0 0 16px var(--color-accent-primary);\n  background: var(--color-glass-surface);",
    css
)

# .tryon-capture-btn
css = re.sub(
    r"\.tryon-capture-btn \{\s*width: 64px; height: 64px; border-radius: 50%;\s*background: #013E37;\s*border: 3\.5px solid #FFF6DA;\s*box-shadow: 0 8px 24px rgba\(1,62,55,0\.35\);",
    r".tryon-capture-btn {\n  width: 64px; height: 64px; border-radius: 50%;\n  background: var(--color-accent-primary);\n  border: 3.5px solid var(--color-bg-primary);\n  box-shadow: 0 12px 48px var(--color-shadow);",
    css
)

# .tryon-mini-icon-btn (the upload photo button in demo mode)
css = re.sub(
    r"\.tryon-mini-icon-btn \{\s*display: flex; align-items: center; gap: 4px; padding: 6px 12px; border-radius: 999px;\s*background: rgba\(255,255,255,0\.15\);\s*border: 1px solid rgba\(255,255,255,0\.2\);\s*color: #FFFFFF;",
    r".tryon-mini-icon-btn {\n  display: flex; align-items: center; gap: 4px; padding: 6px 12px; border-radius: 999px;\n  background: var(--color-glass-surface);\n  backdrop-filter: blur(24px);\n  -webkit-backdrop-filter: blur(24px);\n  border: 1px solid var(--color-glass-border);\n  color: var(--color-text-primary);\n  box-shadow: 0 12px 48px var(--color-shadow);",
    css
)

# .tryon-mode-pill-mini
css = re.sub(
    r"\.tryon-mode-pill-mini \{\s*display: flex; align-items: center; background: rgba\(255,255,255,0\.15\);\s*border-radius: 999px; padding: 3px; border: 1px solid rgba\(255,255,255,0\.15\);",
    r".tryon-mode-pill-mini {\n  display: flex; align-items: center; background: var(--color-glass-surface);\n  backdrop-filter: blur(24px);\n  -webkit-backdrop-filter: blur(24px);\n  border-radius: 999px; padding: 3px; border: 1px solid var(--color-glass-border);\n  box-shadow: 0 12px 48px var(--color-shadow);",
    css
)
css = re.sub(
    r"\.tryon-mode-option-mini \{\s*border: none; background: transparent; color: #FFFFFF;",
    r".tryon-mode-option-mini {\n  border: none; background: transparent; color: var(--color-text-primary);",
    css
)
css = re.sub(
    r"\.tryon-mode-option-mini\.active \{\s*background: #013E37;\s*color: #FFF5EC;",
    r".tryon-mode-option-mini.active {\n  background: var(--color-accent-primary);\n  color: var(--color-bg-primary);",
    css
)

with open(styles_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Update TryOnScreen.js for inline styles (#0B1F1C -> var(--color-text-primary))
tryon_path = r'c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\screens\TryOnScreen.js'
with open(tryon_path, 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace("color: '#0B1F1C'", "color: 'var(--color-text-primary)'")

with open(tryon_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated TryOnScreen and styles.css for Prompt 10")
