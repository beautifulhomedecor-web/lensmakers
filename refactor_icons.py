import re

styles_path = r'c:\Users\NEW\OneDrive\Desktop\lensmakers-web\styles.css'
with open(styles_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update .icon-btn-circle
css = re.sub(
    r"\.icon-btn-circle \{\s*width: 36px; height: 36px; border-radius: 50%;\s*background: linear-gradient[^\n]+\n[^\n]+\n[^\n]+\n[^\n]+\n[^\n]+",
    r".icon-btn-circle {\n  width: 36px; height: 36px; border-radius: 50%;\n  background: var(--color-glass-surface);\n  border: 1px solid var(--color-glass-border);\n  box-shadow: 0 12px 48px var(--color-shadow);\n  display: flex; align-items: center; justify-content: center;\n  color: var(--color-accent-primary); cursor: pointer;\n}",
    css
)
css = re.sub(
    r"\.icon-btn-circle:hover \{[^\}]+\}",
    r".icon-btn-circle:hover { background: var(--color-glass-surface); border-color: var(--color-accent-primary); color: var(--color-accent-primary); transform: scale(1.05); }",
    css
)
css = re.sub(
    r"\.icon-btn-circle:active \{[^\}]+\}",
    r".icon-btn-circle:active { background: var(--color-accent-pressed); color: var(--color-bg-primary); transform: scale3d(0.92, 0.88, 1); }",
    css
)

# 2. Add active states to .icon-btn-circle
css = css + "\n.icon-btn-circle.active, .icon-btn-circle.selected {\n  background: var(--color-accent-primary);\n  color: var(--color-bg-primary);\n  border-color: var(--color-accent-primary);\n}\n"

# 3. Fix nav-item and nav-icon glitches and apply palette
css = re.sub(
    r"\.nav-item:not\(\.active\):hover \.nav-icon,\s*\n*\.nav-item:not\(\.active\):hover \.nav-item-pill svg \{[^}]+param\(\$m\)[^}]+\}",
    r".nav-item:not(.active):hover .nav-icon,\n.nav-item:not(.active):hover .nav-item-pill svg {\n  color: var(--color-accent-primary);\n}",
    css, flags=re.MULTILINE
)

# Fix .nav-item.active .nav-icon
css = re.sub(
    r"\.nav-item\.active \.nav-icon,\s*\n*\.nav-item\.active \.nav-item-pill svg \{[^}]+\}",
    r".nav-item.active .nav-icon,\n.nav-item.active .nav-item-pill svg {\n  color: var(--color-bg-primary) !important;\n  filter: none;\n  animation: navIconSpring 450ms var(--spring-bezier) forwards;\n  will-change: transform;\n}",
    css, flags=re.MULTILINE
)

# Fix .nav-item.active .nav-item-pill
css = re.sub(
    r"\.nav-item\.active \.nav-item-pill \{[^}]+\}",
    r".nav-item.active .nav-item-pill {\n  background: var(--color-accent-primary) !important;\n  border: 1px solid var(--color-accent-primary) !important;\n  box-shadow: 0 12px 48px var(--color-shadow) !important;\n  color: var(--color-bg-primary) !important;\n  animation: liquidPillMorph 480ms var(--spring-bezier) forwards;\n}",
    css, flags=re.MULTILINE
)

# 4. Fix nav.bottom-nav .tab-item glitches at the bottom of the file
css = re.sub(
    r"nav\.bottom-nav \.tab-item \{ color:[^}]+param\(\$m\)[^}]+\}",
    r"nav.bottom-nav .tab-item { color: var(--color-accent-primary) !important; }",
    css, flags=re.MULTILINE
)
css = re.sub(
    r"nav\.bottom-nav \.tab-item i, nav\.bottom-nav \.tab-item svg \{ color:[^}]+param\(\$m\)[^}]+\}",
    r"nav.bottom-nav .tab-item i, nav.bottom-nav .tab-item svg { color: var(--color-accent-primary) !important; stroke: var(--color-accent-primary) !important; }",
    css, flags=re.MULTILINE
)
css = re.sub(
    r"nav\.bottom-nav \.tab-item\.active, nav\.bottom-nav \.tab-active \{ color: #0B1F1C !important; \}",
    r"nav.bottom-nav .tab-item.active, nav.bottom-nav .tab-active { color: var(--color-bg-primary) !important; }",
    css
)
css = re.sub(
    r"nav\.bottom-nav \.tab-item\.active i, nav\.bottom-nav \.tab-item\.active svg,\s*\n*nav\.bottom-nav \.tab-active i, nav\.bottom-nav \.tab-active svg \{ color: #0B1F1C !important; stroke:[^}]+!important; \}",
    r"nav.bottom-nav .tab-item.active i, nav.bottom-nav .tab-item.active svg,\nnav.bottom-nav .tab-active i, nav.bottom-nav .tab-active svg { color: var(--color-bg-primary) !important; stroke: var(--color-bg-primary) !important; }",
    css, flags=re.MULTILINE
)

# 5. Fix nav-icon color generally
css = re.sub(
    r"\.nav-icon \{\s*transition:",
    r".nav-icon {\n  color: var(--color-accent-primary);\n  transition:",
    css
)

# Add glass surface to nav-item-pill in default state if it has none, or keep it transparent?
# "Glass surface token for the icon button's container fill." 
# For .nav-item-pill, it might be transparent. We should apply glass surface to it.
css = re.sub(
    r"\.nav-item-pill \{\s*position: relative;\s*display: inline-flex;\s*align-items: center;\s*justify-content: center;\s*gap: 6px;\s*height: 44px; padding: 0 16px; border-radius: 999px;\s*background: transparent;",
    r".nav-item-pill {\n  position: relative;\n  display: inline-flex;\n  align-items: center;\n  justify-content: center;\n  gap: 6px;\n  height: 44px; padding: 0 16px; border-radius: 999px;\n  background: var(--color-glass-surface);\n  border: 1px solid var(--color-glass-border);\n  box-shadow: 0 12px 48px var(--color-shadow);",
    css
)

with open(styles_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated glassmorphic icon buttons for Prompt 12")
