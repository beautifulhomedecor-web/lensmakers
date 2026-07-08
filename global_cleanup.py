import os, re

directory = r'c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\screens'
glitch_pattern = r"'\s*param\(\$m\)\s*\$opacity = \$m\.Groups\[1\]\.Value\s*\"rgba\(11,31,28,0\.\$opacity\)\"\s*'"

for filename in os.listdir(directory):
    if filename.endswith(".js"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'param($m)' in content:
            new_content = re.sub(glitch_pattern, "'var(--color-text-secondary)'", content)
            
            # Since the prompt might be replacing #0B1F1C as well, I'll let future steps handle tokenization for other files.
            # I just want to remove the syntax breaking powershell glitch.
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"Fixed glitch in {filename}")

print("Global cleanup done.")
