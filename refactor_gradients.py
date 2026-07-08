import re

styles_path = r'c:\Users\NEW\OneDrive\Desktop\lensmakers-web\styles.css'
with open(styles_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Fix .tryon-bottom-panel overriding background
css = re.sub(
    r"\.tryon-bottom-panel \{[^}]+\}",
    lambda m: re.sub(r"background: linear-gradient[^\n]+\n", "", m.group(0)),
    css
)

# Same for .search-bar-expanded-wrapper
css = re.sub(
    r"\.search-bar-expanded-wrapper \{[^}]+\}",
    lambda m: re.sub(r"background: linear-gradient[^\n]+\n", "background: var(--color-glass-surface);\n", m.group(0)),
    css
)

with open(styles_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Cleaned up old gradients")
