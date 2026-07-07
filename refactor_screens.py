import re, sys
sys.stdout.reconfigure(encoding='utf-8')

files = [
    'src/screens/ShopScreen.js',
    'src/screens/CartScreen.js',
    'src/screens/ProfileScreen.js',
    'src/screens/MembershipScreen.js',
    'src/screens/TryOnScreen.js',
    'src/screens/EyeCheckupScreen.js',
    'src/screens/StoreLocatorScreen.js',
    'src/screens/PrescriptionScreen.js',
]

replacements = [
    # Dark navy blues -> white/cornsilk
    ("background: '#070A13'", "background: '#FFFFFF'"),
    ("background: '#0A112A'", "background: '#FFFFFF'"),
    ("background: '#0F1535'", "background: '#FFFFFF'"),
    ("background: '#1C2240'", "background: '#FFFFFF'"),
    ("background: '#2D3A6B'", "background: '#FFF6DA'"),
    ("background: '#1A1A2E'", "background: '#FFFFFF'"),
    ("background: '#16213E'", "background: '#FFFFFF'"),
    ("background: '#0D1B2A'", "background: '#FFFFFF'"),
    ("background: '#0B2A6B'", "background: '#FFFFFF'"),
    ("background: '#1B3A73'", "background: '#FFFFFF'"),
    ("background: '#2B4C8C'", "background: '#FFF6DA'"),
    # Lime green -> dark green (color)
    ("color: '#84CC16'", "color: '#013E37'"),
    ("color: '#9CCC65'", "color: '#013E37'"),
    ("color: '#A8FF00'", "color: '#013E37'"),
    ("color: '#7DCE4A'", "color: '#013E37'"),
    # Lime green -> dark green (background)
    ("background: '#84CC16'", "background: '#013E37'"),
    ("background: '#9CCC65'", "background: '#013E37'"),
    ("background: '#A8FF00'", "background: '#013E37'"),
    ("background: '#7DCE4A'", "background: '#013E37'"),
    # White text -> dark green
    ("color: '#FFFFFF'", "color: '#013E37'"),
    # Translucent white text -> dark green at opacity
    ("color: 'rgba(255, 255, 255, 0.9)'", "color: '#013E37'"),
    ("color: 'rgba(255, 255, 255, 0.8)'", "color: 'rgba(1, 62, 55, 0.8)'"),
    ("color: 'rgba(255, 255, 255, 0.7)'", "color: 'rgba(1, 62, 55, 0.7)'"),
    ("color: 'rgba(255, 255, 255, 0.6)'", "color: 'rgba(1, 62, 55, 0.6)'"),
    ("color: 'rgba(255, 255, 255, 0.5)'", "color: 'rgba(1, 62, 55, 0.5)'"),
    ("color: 'rgba(255, 255, 255, 0.4)'", "color: 'rgba(1, 62, 55, 0.4)'"),
    # White glass surfaces -> cornsilk
    ("background: 'rgba(255, 255, 255, 0.08)'", "background: '#FFF6DA'"),
    ("background: 'rgba(255, 255, 255, 0.1)'", "background: '#FFF6DA'"),
    ("background: 'rgba(255, 255, 255, 0.12)'", "background: '#FFF6DA'"),
    ("background: 'rgba(255, 255, 255, 0.15)'", "background: '#FFF6DA'"),
    ("background: 'rgba(255, 255, 255, 0.05)'", "background: 'rgba(255, 246, 218, 0.4)'"),
    ("background: 'rgba(255, 255, 255, 0.03)'", "background: 'rgba(255, 246, 218, 0.3)'"),
    # White borders -> cornsilk
    ("border: '1px solid rgba(255, 255, 255, 0.1)'", "border: '1px solid #FFF6DA'"),
    ("border: '1px solid rgba(255, 255, 255, 0.12)'", "border: '1px solid #FFF6DA'"),
    ("border: '1px solid rgba(255, 255, 255, 0.15)'", "border: '1px solid #FFF6DA'"),
    ("border: '1px solid rgba(255, 255, 255, 0.2)'", "border: '1px solid #FFF6DA'"),
    ("borderColor: 'rgba(255, 255, 255, 0.1)'", "borderColor: '#FFF6DA'"),
    ("borderColor: 'rgba(255, 255, 255, 0.15)'", "borderColor: '#FFF6DA'"),
    # Accent red -> rose vale
    ("background: '#EF5350'", "background: '#A94A4A'"),
    ("background: '#FF6B6B'", "background: '#A94A4A'"),
    ("background: '#FF7873'", "background: '#A94A4A'"),
    ("background: '#E53935'", "background: '#A94A4A'"),
    ("color: '#EF5350'", "color: '#A94A4A'"),
    ("color: '#FF6B6B'", "color: '#A94A4A'"),
    ("color: '#FF7873'", "color: '#A94A4A'"),
    # Teal/cyan accents -> dark green
    ("color: '#00BADB'", "color: '#013E37'"),
    ("background: '#00BADB'", "background: '#013E37'"),
    ("color: '#00E5FF'", "color: '#013E37'"),
    ("background: '#00E5FF'", "background: '#013E37'"),
    # Purple -> dark green
    ("color: '#8140DC'", "color: '#013E37'"),
    ("background: '#8140DC'", "background: '#013E37'"),
    # Background text muted blues -> dark green at opacity
    ("color: '#0B2A6B'", "color: '#013E37'"),
    ("color: '#1B3A73'", "color: '#013E37'"),
    ("color: '#2B4C8C'", "color: 'rgba(1, 62, 55, 0.6)'"),
    ("color: '#3D5A99'", "color: 'rgba(1, 62, 55, 0.5)'"),
    # Generic grays -> dark green at opacity
    ("color: '#64748B'", "color: 'rgba(1, 62, 55, 0.5)'"),
    ("color: '#94A3B8'", "color: 'rgba(1, 62, 55, 0.5)'"),
    ("color: '#475569'", "color: 'rgba(1, 62, 55, 0.4)'"),
    # Product card bg
    ("background: '#F8F6FF'", "background: '#FFFFFF'"),
    ("background: '#F0F9FF'", "background: '#FFF6DA'"),
    ("background: '#FDF2F8'", "background: '#FFF6DA'"),
    ("background: '#F4F3EF'", "background: '#FFF6DA'"),
    ("background: '#FAFAF9'", "background: '#FFFFFF'"),
    ("background: '#F4F3F4'", "background: '#FFFFFF'"),
    # Cart / modal sheets
    ("background: '#1C1917'", "background: '#FFFFFF'"),
    ("color: '#1C1917'", "color: '#013E37'"),
    # Logout button
    ("background: '#EF5350'", "background: '#A94A4A'"),
]

for fpath in files:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        changed = 0
        for old, new in replacements:
            count = content.count(old)
            if count > 0:
                content = content.replace(old, new)
                changed += count

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] {fpath}: {changed} replacements")
    except FileNotFoundError:
        print(f"[SKIP] {fpath}: not found")

print("\nAll screens refactored.")
