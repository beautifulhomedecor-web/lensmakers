import re

# 1. Update Splash Screen in styles.css
styles_path = r'c:\Users\NEW\OneDrive\Desktop\lensmakers-web\styles.css'
with open(styles_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Splash Container Bg
css = re.sub(
    r'\.splash-container\s*\{[^}]*background:[^;]+;',
    '.splash-container { background: var(--color-bg-primary);',
    css
)

# Splash Tagline Text Color
css = re.sub(
    r'\.splash-tagline\s*\{[^}]*color:\s*[^;]+;',
    lambda m: m.group(0).replace('var(--text-lavender-gray)', 'var(--color-text-primary)'),
    css
)

# Onboarding Container
css = re.sub(
    r'\.onboarding-container\s*\{[^}]*background:[^;]+;',
    '.onboarding-container { background: var(--color-bg-primary);',
    css
)

# Onboarding Heading
css = re.sub(
    r'\.onboarding-heading\s*\{[^}]*color:\s*[^;]+;',
    lambda m: m.group(0).replace('var(--text-white)', 'var(--color-text-primary)'),
    css
)

# Onboarding Subtext
css = re.sub(
    r'\.onboarding-subtext\s*\{[^}]*color:\s*[^;]+;',
    lambda m: m.group(0).replace('var(--text-lavender-gray)', 'var(--color-text-secondary)'),
    css
)

# Auth Container
css = re.sub(
    r'\.auth-container\s*\{[^}]*background:[^;]+;',
    '.auth-container { background: var(--color-bg-primary);',
    css
)

# Auth Card Wrapper
css = re.sub(
    r'\.auth-card-wrapper\s*\{([^}]+)\}',
    r'.auth-card-wrapper {\1  background: var(--color-glass-surface);\n  box-shadow: 0 16px 48px var(--color-shadow);\n  border: 1px solid var(--color-glass-border);\n  border-radius: 24px;\n}',
    css
)

# Glass Input Focus
css = re.sub(
    r'\.glass-input:focus\s*\{[^}]*\}',
    '.glass-input:focus {\n  border-color: var(--color-accent-primary);\n  outline: none;\n  box-shadow: 0 0 0 3px rgba(169,74,74,0.15);\n  background: var(--color-glass-surface);\n}',
    css
)

# Glass Input Default
css = re.sub(
    r'\.glass-input\s*\{([^}]+)\}',
    lambda m: m.group(0).replace('background: rgba(255, 246, 218, 0.8);', 'background: var(--color-glass-surface);').replace('border: 1.5px solid #FFF6DA;', 'border: 1.5px solid var(--color-glass-border);'),
    css
)

# Page Dots
page_dot_css = """
.page-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--color-text-secondary);
  transition: all 300ms ease;
  opacity: 0.5;
}
.page-dot.active {
  width: 8px;
  height: 8px;
  background: var(--color-accent-primary);
  opacity: 1;
}
"""
css += page_dot_css

with open(styles_path, 'w', encoding='utf-8') as f:
    f.write(css)


# 2. Update Logo.js
logo_path = r'c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\components\Logo.js'
with open(logo_path, 'r', encoding='utf-8') as f:
    logo = f.read()

logo = logo.replace("stroke=\"#013E37\"", "stroke=\"var(--color-accent-primary)\"")
logo = logo.replace("fill=\"rgba(1,62,55, 0.15)\"", "fill=\"transparent\"")
logo = logo.replace("fill=\"rgba(156, 204, 101, 0.15)\"", "fill=\"transparent\"")
logo = logo.replace("color: '#FFFFFF'", "color: 'var(--color-text-primary)'")

with open(logo_path, 'w', encoding='utf-8') as f:
    f.write(logo)


# 3. Update AuthModal.js
auth_path = r'c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\components\AuthModal.js'
with open(auth_path, 'r', encoding='utf-8') as f:
    auth = f.read()

# Fix glitch at line 87: 'rgba(11,31,28,0.5)' is what the other script did, but here it's broken over lines.
auth = re.sub(r'strengthColors = \[\'#A94A4A\', \'#A94A4A\', \'#013E37\', \'[\s\S]*?\', \'#013E37\'\];', "strengthColors = ['#A94A4A', '#A94A4A', 'var(--color-text-secondary)', 'var(--color-text-primary)', 'var(--color-accent-primary)'];", auth)
auth = auth.replace("color: 'var(--text-white)'", "color: 'var(--color-text-primary)'")
auth = auth.replace("color: 'var(--text-lavender-gray)'", "color: 'var(--color-text-secondary)'")

# Buttons using accent primary
auth = re.sub(
    r"background: 'linear-gradient\([^)]+\)'",
    "background: 'var(--color-accent-primary)'",
    auth
)
auth = auth.replace("color: '#0B1F1C'", "color: 'var(--color-text-primary)'")
auth = auth.replace("background: 'var(--color-text-primary)'", "background: 'var(--color-accent-primary)'")
auth = auth.replace("background: 'var(--text-white)'", "background: 'var(--color-accent-primary)'")
auth = auth.replace("background: '#0B1F1C'", "background: 'var(--color-accent-primary)'")

with open(auth_path, 'w', encoding='utf-8') as f:
    f.write(auth)


# 4. Update Onboarding.js
onboarding_path = r'c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\components\Onboarding.js'
with open(onboarding_path, 'r', encoding='utf-8') as f:
    onb = f.read()

onb = onb.replace("color: '#A94A4A'", "color: 'var(--color-accent-primary)'")
onb = onb.replace("background: '#0B1F1C'", "background: 'var(--color-accent-primary)'")
onb = onb.replace("color: '#0B1F1C'", "color: 'var(--color-bg-primary)'")
# Next Button specifically:
onb = re.sub(
    r"background: 'var\(--color-bg-primary\)',\s*color: 'var\(--color-accent-primary\)'",
    "background: 'var(--color-accent-primary)', color: 'var(--color-bg-primary)'",
    onb
)

with open(onboarding_path, 'w', encoding='utf-8') as f:
    f.write(onb)

print("Refactored Prompt 15 successfully.")
