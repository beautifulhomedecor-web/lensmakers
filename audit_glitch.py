import os

directory = r'c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\screens'
glitch_files = []

for filename in os.listdir(directory):
    if filename.endswith(".js"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            if 'param($m)' in content:
                glitch_files.append(filename)

print("Files with glitch:", glitch_files)
