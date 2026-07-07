import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

# Final cleanup of stubborn legacy colors
fixes = {
    'src/App.js': [
        ('#9CCC65', '#013E37'),
    ],
    'src/components/AuthModal.js': [
        ('#8140DC', '#013E37'),
    ],
    'src/components/Logo.js': [
        ('#9CCC65', '#013E37'),
    ],
    'src/components/Onboarding.js': [
        ('#F4F3EF', '#FFF6DA'),
        ('#ECEAE3', '#FFF6DA'),
    ],
    'src/components/TryOnBanner.js': [
        ('#8140DC', '#013E37'),
        ('#0B2A6B', '#FFFFFF'),
    ],
    'src/components/UIPrimitives.js': [
        ('#8140DC', '#013E37'),
    ],
    'src/screens/CartScreen.js': [
        ('#8140DC', '#013E37'),
    ],
    'src/screens/HomeScreen.js': [
        ('#070A13', '#FFFFFF'),
        ('#9CCC65', '#013E37'),
        ('#8140DC', '#013E37'),
    ],
    'src/screens/MembershipScreen.js': [
        ('#8140DC', '#013E37'),
    ],
    'src/screens/PrescriptionScreen.js': [
        ('#8140DC', '#013E37'),
    ],
    'src/screens/ProfileScreen.js': [
        ('#8140DC', '#013E37'),
    ],
    'src/screens/ShopScreen.js': [
        ('#8140DC', '#013E37'),
    ],
    'src/screens/StoreLocatorScreen.js': [
        ('#8140DC', '#013E37'),
    ],
    'src/screens/TryOnScreen.js': [
        ('#F4F3EF', '#FFF6DA'),
    ],
    'src/utils/spring.js': [
        ('#8140DC', '#013E37'),
    ],
}

total = 0
for fpath, pairs in fixes.items():
    if not os.path.exists(fpath):
        print('[SKIP] ' + fpath)
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    changed = 0
    for old, new in pairs:
        cnt = c.count(old)
        if cnt:
            c = c.replace(old, new)
            changed += cnt
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    total += changed
    print('[OK] ' + fpath + ': ' + str(changed) + ' replacements')

print('\nTotal replacements: ' + str(total))
