import sys, os
sys.stdout.reconfigure(encoding='utf-8')

files = [
    'src/components/AuthModal.js',
    'src/components/Onboarding.js',
    'src/components/UIPrimitives.js',
    'src/components/PromoCard.js',
    'src/components/PremiumPicks.js',
    'src/components/TryOnBanner.js',
    'src/components/TrendingSunglasses.js',
    'src/components/EyeglassesSection.js',
    'src/App.js',
]

replacements = [
    ("background: '#070A13'", "background: '#FFFFFF'"),
    ("background: '#FFF5EC'", "background: '#FFF6DA'"),
    ("background: '#FFFDF5'", "background: '#FFFFFF'"),
    ("background: '#FFF8E7'", "background: '#FFF6DA'"),
    ("background: '#FFF0D4'", "background: '#FFF6DA'"),
    ("background: '#FAFAF9'", "background: '#FFFFFF'"),
    ("background: '#F4F3EF'", "background: '#FFF6DA'"),
    ("background: '#ECEAE3'", "background: '#FFF6DA'"),
    ("background: '#1C1917'", "background: '#FFFFFF'"),
    ("color: '#1C1917'", "color: '#013E37'"),
    ("color: '#FFFFFF'", "color: '#013E37'"),
    ("color: '#84CC16'", "color: '#013E37'"),
    ("color: '#9CCC65'", "color: '#013E37'"),
    ("background: '#84CC16'", "background: '#013E37'"),
    ("background: '#9CCC65'", "background: '#013E37'"),
    ("color: '#00BADB'", "color: '#013E37'"),
    ("background: '#00BADB'", "background: '#013E37'"),
    ("color: '#64748B'", "color: 'rgba(1, 62, 55, 0.5)'"),
    ("color: '#94A3B8'", "color: 'rgba(1, 62, 55, 0.5)'"),
    ("color: '#475569'", "color: 'rgba(1, 62, 55, 0.4)'"),
    ("background: '#EF5350'", "background: '#A94A4A'"),
    ("color: '#EF5350'", "color: '#A94A4A'"),
    ("background: '#8140DC'", "background: '#013E37'"),
    ("background: '#0B2A6B'", "background: '#FFFFFF'"),
    ("background: '#1B3A73'", "background: '#FFFFFF'"),
    ("background: '#2B4C8C'", "background: '#FFF6DA'"),
]

for fpath in files:
    if not os.path.exists(fpath):
        print('[SKIP] ' + fpath)
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    changed = 0
    for old, new in replacements:
        cnt = c.count(old)
        if cnt:
            c = c.replace(old, new)
            changed += cnt
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print('[OK] ' + fpath + ': ' + str(changed) + ' replacements')

print('\nDone.')
