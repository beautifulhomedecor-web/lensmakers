import os
import re

STYLES_PATH = 'styles.css'

with open(STYLES_PATH, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update :root palette
root_replacement = """  /* NEW LUXURIOUS PALETTE */
  --color-white: #FFFFFF;
  --color-cornsilk: #FFF6DA;
  --color-dark-green: #013E37;
  --color-rose-vale: #A94A4A;
  
  --bg-primary: var(--color-white);
  --bg-secondary: var(--color-cornsilk);
  --bg-tertiary: var(--color-cornsilk);
  --brand-blue: var(--color-dark-green);
  --brand-green: var(--color-dark-green);
  --accent-pink: var(--color-rose-vale);
  --accent-purple: var(--color-dark-green);
  --accent-orange: var(--color-rose-vale);
  --accent-yellow: var(--color-rose-vale);
  --accent-cyan: var(--color-dark-green);
  --accent-red: var(--color-rose-vale);
  --accent-light-green: var(--color-dark-green);
  --accent-amber: var(--color-rose-vale);
  
  /* TEXT COLORS */
  --text-white: var(--color-dark-green);
  --text-off-white: var(--color-dark-green);
  --text-lavender-gray: rgba(1, 62, 55, 0.6);
  --text-muted: rgba(1, 62, 55, 0.6);
  
  /* BORDERS & SHADOWS */
  --border-subtle: var(--color-cornsilk);
  --border-glow: var(--color-cornsilk);
  --shadow-pink: rgba(1, 62, 55, 0.1);
  --shadow-dark: rgba(1, 62, 55, 0.15);
"""
css = re.sub(
    r'/\*\s*COLOUR PALETTE.*?--shadow-dark:[^;]+;', 
    root_replacement, 
    css, 
    flags=re.DOTALL
)

# Global body bg
css = re.sub(r'body\s*\{[^}]*background:[^;]+;', lambda m: m.group(0).replace(m.group(0).split('background:')[-1], ' var(--color-white);'), css)

# Hover and button micro-animations
css = re.sub(r'\.product-card-glass:hover\s*\{[^}]*transform:\s*translateY\([^)]+\)', 
             lambda m: m.group(0).replace(re.search(r'translateY\([^)]+\)', m.group(0)).group(0), 'translateY(-2px)'), css)

css = re.sub(r'\.btn-[a-zA-Z0-9-]+:active\s*\{[^}]*transform:\s*scale\([^)]+\)', 
             lambda m: m.group(0).replace(re.search(r'scale\([^)]+\)', m.group(0)).group(0), 'scale(0.95)'), css)

# Fix outline colors
css = re.sub(r':focus-visible\s*\{[^}]*outline:\s*[^;]+;', 
             lambda m: m.group(0).replace(re.search(r'outline:\s*[^;]+', m.group(0)).group(0), 'outline: 2px solid var(--color-dark-green)'), css)
css = re.sub(r':focus-visible\s*\{[^}]*outline-offset:\s*[^;]+;', 
             lambda m: m.group(0).replace(re.search(r'outline-offset:\s*[^;]+', m.group(0)).group(0), 'outline-offset: 2px'), css)


with open(STYLES_PATH, 'w', encoding='utf-8') as f:
    f.write(css)

print("styles.css updated successfully.")
