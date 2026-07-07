import re

PATH = 'src/components/Header.js'
with open(PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Header background
content = re.sub(
    r"background: activeTab === 'home' \? '#070A13' : 'linear-gradient[^']+'",
    "background: 'rgba(255, 255, 255, 0.85)', backdropFilter: 'blur(20px)'",
    content
)

# Search Bar background and border
content = re.sub(
    r"background: '#FFF5EC',[^}]*border: '1px solid #FFEDD5'",
    "background: 'rgba(255, 246, 218, 0.5)', border: '1px solid #FFF6DA'",
    content
)

# Hamburger icon (it was white)
content = re.sub(
    r'<Menu size=\{24\} color="var\(--text-white\)" strokeWidth=\{2\.5\} />',
    '<Menu size={24} color="#013E37" strokeWidth={2.5} />',
    content
)
# Wait, if it was overridden in styles.css, let's just make sure
content = re.sub(
    r'<Menu size=\{24\}[^>]*/>',
    '<Menu size={24} color="#013E37" strokeWidth={2.5} />',
    content
)

# Logo (lens and makers)
content = re.sub(
    r'<span style=\{\{ color: \'#FFFFFF\'.*?>lens</span>',
    '<span style={{ color: \'#013E37\', fontWeight: \'800\' }}>lens</span>',
    content
)
content = re.sub(
    r'<span style=\{\{ color: \'#84CC16\'.*?>makers</span>',
    '<span style={{ color: \'#013E37\', fontWeight: \'800\' }}>makers</span>',
    content
)

# Bell icon
content = re.sub(
    r'<Bell size=\{24\} color="var\(--text-white\)"[^>]*/>',
    '<Bell size={24} color="#013E37" strokeWidth={2.5} />',
    content
)
content = re.sub(
    r'<Bell size=\{24\}[^>]*/>',
    '<Bell size={24} color="#013E37" strokeWidth={2.5} />',
    content
)

# Location Dropdown Text
content = re.sub(
    r"color: '#FFFFFF'",
    "color: 'rgba(1, 62, 55, 0.8)'",
    content
)
# Fix other instances in Header.js where text was white or brand colors
content = re.sub(
    r"color: 'var\(--text-white\)'",
    "color: '#013E37'",
    content
)

# Search icons
content = re.sub(
    r'<Search size=\{20\} color="[^"]+"',
    '<Search size={20} color="#013E37"',
    content
)
content = re.sub(
    r'<Mic size=\{20\} color="[^"]+"',
    '<Mic size={20} color="#013E37"',
    content
)

# Placeholder color (requires a CSS class or inline style hack, but standard input placeholder is styled via CSS)
# Let's add a class to the input
content = re.sub(
    r'(<input[^>]+className=")([^"]*)(")',
    r'\1\2 custom-search-input\3',
    content
)

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print("Header.js refactored.")
