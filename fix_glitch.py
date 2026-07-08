import re

styles_path = r'c:\Users\NEW\OneDrive\Desktop\lensmakers-web\styles.css'
header_path = r'c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\components\Header.js'

with open(styles_path, 'r', encoding='utf-8') as f:
    css = f.read()

# The glitch pattern
glitch_pattern = r"\s*param\(\$m\)\s*\$opacity = \$m\.Groups\[1\]\.Value\s*\"rgba\(11,31,28,0\.\$opacity\)\""

# Replace globally in CSS
css = re.sub(glitch_pattern, " rgba(11,31,28,0.5)", css)

with open(styles_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Replace globally in Header.js
with open(header_path, 'r', encoding='utf-8') as f:
    header = f.read()

header = re.sub(glitch_pattern, "rgba(11,31,28,0.5)", header)

with open(header_path, 'w', encoding='utf-8') as f:
    f.write(header)

print("Glitch remediated globally.")
