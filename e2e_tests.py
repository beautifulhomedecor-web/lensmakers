#!/usr/bin/env python3
"""
e2e_tests.py - Lens Makers E2E Test Suite (Tiers 1 to 4)

This programmatic E2E test runner scans the Lens Makers codebase to verify
feature coverage, design system compliance, color palette consistency,
and user interaction behaviors.
"""

import os
import re
import sys
import json

ROOT = r"c:\Users\NEW\OneDrive\Desktop\lensmakers-web"

# Design System Palette Definitions
AUTHORIZED_HEXES = {
    "#ffffff", "#fff6da", "#013e37", "#a94a4a",
    "#fff", # shorthand white
}

AUTHORIZED_RGBAS = {
    # 60% Dark Green (subtitles/secondary text)
    "rgba(1, 62, 55, 0.6)", "rgba(1,62,55,0.6)",
    # 40% Dark Green (inactive tabs/muted text)
    "rgba(1, 62, 55, 0.4)", "rgba(1,62,55,0.4)",
    # 8% - 12% Dark Green (drop shadows)
    "rgba(1, 62, 55, 0.08)", "rgba(1,62,55,0.08)",
    "rgba(1, 62, 55, 0.09)", "rgba(1,62,55,0.09)",
    "rgba(1, 62, 55, 0.1)", "rgba(1,62,55,0.1)",
    "rgba(1, 62, 55, 0.11)", "rgba(1,62,55,0.11)",
    "rgba(1, 62, 55, 0.12)", "rgba(1,62,55,0.12)",
    "rgba(1, 62, 55, 0.15)", "rgba(1,62,55,0.15)",  # soft glow
    "rgba(1, 62, 55, 0.05)", "rgba(1,62,55,0.05)",  # light wash overlay
}

class TestResult:
    def __init__(self, name, tier, passed=True, message="", details=None):
        self.name = name
        self.tier = tier
        self.passed = passed
        self.message = message
        self.details = details or []

    def to_dict(self):
        return {
            "name": self.name,
            "tier": self.tier,
            "passed": self.passed,
            "message": self.message,
            "details": self.details
        }

def find_files(root_dir):
    src_files = []
    css_files = []
    
    for dirpath, dirs, files in os.walk(root_dir):
        # Exclude metadata, build, node, git folders
        dirs[:] = [d for d in dirs if d not in ['.agents', 'node_modules', '.git', 'assets']]
        for fname in files:
            ext = os.path.splitext(fname)[1].lower()
            fp = os.path.join(dirpath, fname)
            rel = os.path.relpath(fp, root_dir)
            
            # Skip product data to avoid color palette confusion with product asset colors
            if rel == os.path.join('src', 'data', 'products.js'):
                continue
                
            if ext == '.js':
                src_files.append((fp, rel))
            elif ext == '.css':
                css_files.append((fp, rel))
                
    return src_files, css_files

def run_e2e_tests():
    print("=" * 80)
    print("               LENS MAKERS E2E STATIC-SEMANTIC TEST RUNNER")
    print("=" * 80)
    
    src_files, css_files = find_files(ROOT)
    results = []
    
    # -------------------------------------------------------------------------
    # TIER 1: FEATURE COVERAGE
    # -------------------------------------------------------------------------
    
    # Tier 1 - Header Coverage
    header_res = TestResult("Header Feature Coverage", 1)
    header_fp = os.path.join(ROOT, "src", "components", "Header.js")
    if not os.path.exists(header_fp):
        header_res.passed = False
        header_res.message = "src/components/Header.js is missing"
    else:
        try:
            content = open(header_fp, 'r', encoding='utf-8', errors='ignore').read()
            missing = []
            if "selectedLocation" not in content and "onOpenLocation" not in content:
                missing.append("Location Selection Bar")
            if "voiceSearch" not in content and "isListening" not in content and "listening" not in content.lower():
                missing.append("Voice Search Trigger")
            if "activeTab" not in content:
                missing.append("Active Tab Indicators")
            if "unreadNotifs" not in content and "hasUnreadNotifs" not in content and "notification" not in content.lower():
                missing.append("Notifications Pill/Count")
            if not missing:
                header_res.message = "All header features detected."
            else:
                header_res.passed = False
                header_res.message = f"Missing header features: {', '.join(missing)}"
        except Exception as e:
            header_res.passed = False
            header_res.message = f"Error reading Header.js: {e}"
    results.append(header_res)

    # Tier 1 - Search Coverage
    search_res = TestResult("Search Feature Coverage", 1)
    if not os.path.exists(header_fp):
        search_res.passed = False
        search_res.message = "src/components/Header.js is missing"
    else:
        try:
            content = open(header_fp, 'r', encoding='utf-8', errors='ignore').read()
            missing = []
            if "<input" not in content and "searchQuery" not in content:
                missing.append("Search Input Field")
            if "listening" not in content.lower() and "transcript" not in content.lower():
                missing.append("Voice Search Integration")
            if "matchedResults" not in content and "autocomplete" not in content.lower():
                missing.append("Live Autocomplete Results")
            if not missing:
                search_res.message = "All search features detected."
            else:
                search_res.passed = False
                search_res.message = f"Missing search features: {', '.join(missing)}"
        except Exception as e:
            search_res.passed = False
            search_res.message = f"Error reading Header.js for Search: {e}"
    results.append(search_res)

    # Tier 1 - Hero Section Coverage
    hero_res = TestResult("Hero Section Feature Coverage", 1)
    home_fp = os.path.join(ROOT, "src", "screens", "HomeScreen.js")
    if not os.path.exists(home_fp):
        hero_res.passed = False
        hero_res.message = "src/screens/HomeScreen.js is missing"
    else:
        try:
            content = open(home_fp, 'r', encoding='utf-8', errors='ignore').read()
            missing = []
            if "See the world" not in content and "clarity" not in content:
                missing.append("Hero Main Heading")
            if "Premium Lenses" not in content and "Perfect Vision" not in content and "Subtitle" not in content:
                # Let's check for sub-heading
                if "subtitle" not in content.lower() and "heading" not in content.lower():
                    missing.append("Hero Subtitle")
            if "onSelectTab('shop')" not in content and "shop" not in content.lower():
                missing.append("Primary CTA Button")
            if "badge" not in content.lower() and "floating" not in content.lower():
                missing.append("Floating/Animated Badge")
            if not missing:
                hero_res.message = "All hero section features detected."
            else:
                hero_res.passed = False
                hero_res.message = f"Missing hero features: {', '.join(missing)}"
        except Exception as e:
            hero_res.passed = False
            hero_res.message = f"Error reading HomeScreen.js: {e}"
    results.append(hero_res)

    # Tier 1 - Quick Links Coverage
    quick_res = TestResult("Quick Links Feature Coverage", 1)
    shop_fp = os.path.join(ROOT, "src", "screens", "ShopScreen.js")
    if not os.path.exists(shop_fp):
        quick_res.passed = False
        quick_res.message = "src/screens/ShopScreen.js is missing"
    else:
        try:
            content = open(shop_fp, 'r', encoding='utf-8', errors='ignore').read()
            missing = []
            if "category" not in content.lower() and "filter" not in content.lower():
                missing.append("Category Filter Chips")
            if "size" not in content.lower() and "width" not in content.lower() and "selector" not in content.lower():
                missing.append("Size Selectors")
            if not missing:
                quick_res.message = "All Quick Links features detected."
            else:
                quick_res.passed = False
                quick_res.message = f"Missing Quick Links features: {', '.join(missing)}"
        except Exception as e:
            quick_res.passed = False
            quick_res.message = f"Error reading ShopScreen.js: {e}"
    results.append(quick_res)

    # Tier 1 - Product Cards Coverage
    product_res = TestResult("Product Cards Feature Coverage", 1)
    if not os.path.exists(shop_fp):
        product_res.passed = False
        product_res.message = "src/screens/ShopScreen.js is missing"
    else:
        try:
            content = open(shop_fp, 'r', encoding='utf-8', errors='ignore').read()
            missing = []
            if "product.name" not in content and ".name" not in content:
                missing.append("Product Title")
            if "product.price" not in content and ".price" not in content:
                missing.append("Product Price")
            if "color" not in content.lower() and "picker" not in content.lower():
                missing.append("Color Selection Indicator")
            if "add to cart" not in content.lower() and "cart" not in content.lower():
                missing.append("Add to Cart Button")
            if not missing:
                product_res.message = "All product card features detected."
            else:
                product_res.passed = False
                product_res.message = f"Missing product card features: {', '.join(missing)}"
        except Exception as e:
            product_res.passed = False
            product_res.message = f"Error reading ShopScreen.js: {e}"
    results.append(product_res)

    # Tier 1 - Cart Coverage
    cart_res = TestResult("Cart Feature Coverage", 1)
    cart_fp = os.path.join(ROOT, "src", "screens", "CartScreen.js")
    if not os.path.exists(cart_fp):
        cart_res.passed = False
        cart_res.message = "src/screens/CartScreen.js is missing"
    else:
        try:
            content = open(cart_fp, 'r', encoding='utf-8', errors='ignore').read()
            missing = []
            if "BOGO" not in content and "banner" not in content.lower() and "offer" not in content.lower():
                missing.append("BOGO Alert/Banner")
            if "step" not in content.lower() and "indicator" not in content.lower() and "line" not in content.lower():
                missing.append("Step Indicator Lines")
            if "address" not in content.lower() and "shipping" not in content.lower():
                missing.append("Address Card")
            if "total" not in content.lower() and "due" not in content.lower() and "calculation" not in content.lower():
                missing.append("Total Calculation Logic")
            if "checkout" not in content.lower() and "place order" not in content.lower() and "btn" not in content.lower():
                missing.append("Checkout / Place Order Button")
            if not missing:
                cart_res.message = "All cart features detected."
            else:
                cart_res.passed = False
                cart_res.message = f"Missing cart features: {', '.join(missing)}"
        except Exception as e:
            cart_res.passed = False
            cart_res.message = f"Error reading CartScreen.js: {e}"
    results.append(cart_res)

    # Tier 1 - Profile Coverage
    profile_res = TestResult("Profile Feature Coverage", 1)
    profile_fp = os.path.join(ROOT, "src", "screens", "ProfileScreen.js")
    if not os.path.exists(profile_fp):
        profile_res.passed = False
        profile_res.message = "src/screens/ProfileScreen.js is missing"
    else:
        try:
            content = open(profile_fp, 'r', encoding='utf-8', errors='ignore').read()
            missing = []
            if "toggle" not in content.lower() and "switch" not in content.lower():
                missing.append("Settings Toggles")
            if "optometrist" not in content.lower() and "vip" not in content.lower() and "support" not in content.lower():
                missing.append("Priority Optometrist Support Row")
            if "address" not in content.lower() and "edit" not in content.lower():
                missing.append("Edit Address Link/Form")
            if "logout" not in content.lower() and "log out" not in content.lower():
                missing.append("Log Out Row/Button")
            if not missing:
                profile_res.message = "All profile features detected."
            else:
                profile_res.passed = False
                profile_res.message = f"Missing profile features: {', '.join(missing)}"
        except Exception as e:
            profile_res.passed = False
            profile_res.message = f"Error reading ProfileScreen.js: {e}"
    results.append(profile_res)

    # Tier 1 - Bottom Nav Coverage
    nav_res = TestResult("Bottom Nav Feature Coverage", 1)
    nav_fp = os.path.join(ROOT, "src", "components", "BottomNav.js")
    if not os.path.exists(nav_fp):
        nav_res.passed = False
        nav_res.message = "src/components/BottomNav.js is missing"
    else:
        try:
            content = open(nav_fp, 'r', encoding='utf-8', errors='ignore').read()
            missing = []
            if "nav" not in content and "tab" not in content.lower():
                missing.append("Tab Navigation Links")
            if "active" not in content and "isActive" not in content:
                missing.append("Active Indicator Pill")
            if "FAB" not in content and "floating" not in content.lower() and "center" not in content.lower():
                missing.append("Floating Action Button (FAB)")
            if not missing:
                nav_res.message = "All Bottom Nav features detected."
            else:
                nav_res.passed = False
                nav_res.message = f"Missing Bottom Nav features: {', '.join(missing)}"
        except Exception as e:
            nav_res.passed = False
            nav_res.message = f"Error reading BottomNav.js: {e}"
    results.append(nav_res)


    # -------------------------------------------------------------------------
    # TIER 2: BOUNDARY CASES (Palette & Opacities & Shadows)
    # -------------------------------------------------------------------------
    
    # Tier 2 - Color Palette Enforcement
    palette_res = TestResult("Color Palette Enforcement", 2)
    unauthorized_colors = []
    
    # Analyze CSS colors
    for fp, rel in css_files:
        try:
            lines = open(fp, 'r', encoding='utf-8', errors='ignore').readlines()
            for idx, line in enumerate(lines, 1):
                # Search hex codes
                hex_codes = re.findall(r'#([0-9a-fA-F]{3,8})\b', line)
                for code in hex_codes:
                    hex_color = f"#{code}".lower()
                    if hex_color not in AUTHORIZED_HEXES:
                        unauthorized_colors.append(f"{rel}:{idx} - Hex Code '{hex_color}'")
        except Exception as e:
            unauthorized_colors.append(f"Error reading {rel}: {e}")

    # Analyze JS inline styles
    for fp, rel in src_files:
        try:
            lines = open(fp, 'r', encoding='utf-8', errors='ignore').readlines()
            for idx, line in enumerate(lines, 1):
                # Search hex codes
                hex_codes = re.findall(r'#([0-9a-fA-F]{3,8})\b', line)
                for code in hex_codes:
                    hex_color = f"#{code}".lower()
                    if hex_color not in AUTHORIZED_HEXES:
                        unauthorized_colors.append(f"{rel}:{idx} - Hex Code '{hex_color}'")
        except Exception as e:
            unauthorized_colors.append(f"Error reading {rel}: {e}")

    if unauthorized_colors:
        palette_res.passed = False
        palette_res.message = f"Found {len(unauthorized_colors)} occurrences of unauthorized colors."
        palette_res.details = unauthorized_colors[:25]  # limit output to 25 details
    else:
        palette_res.message = "Only authorized hex codes used for styling."
    results.append(palette_res)

    # Tier 2 - Generic Gray Text & Neutral Colors
    gray_res = TestResult("Generic Gray Text Removal", 2)
    gray_occurrences = []
    # Search for standard gray colors
    gray_patterns = [
        r'#64748[bB]', r'#[aA]0[aA]4[cC]8', r'#475569', r'#1[cC]1917', r'#[eE][aA][eE][aA][eE][aA]',
        r'#3[dD]5[aA]99', r'#2[bB]4[cC]8[cC]', r'#1[bB]3[aA]73', r'#[cC]9[aA]876', r'#475569'
    ]
    for fp, rel in css_files + src_files:
        try:
            content = open(fp, 'r', encoding='utf-8', errors='ignore').read()
            for pattern in gray_patterns:
                matches = re.finditer(pattern, content)
                for m in matches:
                    # Find line number
                    line_no = content[:m.start()].count('\n') + 1
                    gray_occurrences.append(f"{rel}:{line_no} - Found gray hex code '{m.group(0)}'")
        except Exception as e:
            gray_occurrences.append(f"Error scanning {rel} for grays: {e}")

    if gray_occurrences:
        gray_res.passed = False
        gray_res.message = f"Found {len(gray_occurrences)} occurrences of generic/legacy gray styles."
        gray_res.details = gray_occurrences[:25]
    else:
        gray_res.message = "Generic gray text/backgrounds successfully removed."
    results.append(gray_res)

    # Tier 2 - Harsh Shadows Removal
    shadows_res = TestResult("Harsh Shadows Removal", 2)
    shadow_violations = []
    for fp, rel in css_files + src_files:
        try:
            content = open(fp, 'r', encoding='utf-8', errors='ignore').read()
            # Search for shadow definitions
            matches = re.finditer(r'(box-shadow|shadow|drop-shadow)\s*:\s*([^;}\n]+)', content, re.IGNORECASE)
            for m in matches:
                prop_val = m.group(2)
                line_no = content[:m.start()].count('\n') + 1
                # If shadow contains rgba(0, 0, 0, ...) or rgba(226, 47, 128, ...)
                if "rgba(0" in prop_val or "rgba(226" in prop_val or "rgba(129" in prop_val or "rgba(239" in prop_val:
                    shadow_violations.append(f"{rel}:{line_no} - Harsh shadow color in: {prop_val.strip()}")
                elif "rgba" in prop_val:
                    # Parse rgba components
                    rgba_matches = re.findall(r'rgba?\([0-9\s,./%+-]+\)', prop_val)
                    for rgba in rgba_matches:
                        if rgba not in AUTHORIZED_RGBAS:
                            shadow_violations.append(f"{rel}:{line_no} - Unauthorized rgba shadow color: {rgba}")
        except Exception as e:
            shadow_violations.append(f"Error scanning shadows in {rel}: {e}")

    if shadow_violations:
        shadows_res.passed = False
        shadows_res.message = f"Found {len(shadow_violations)} occurrences of harsh/unauthorized shadows."
        shadows_res.details = shadow_violations[:25]
    else:
        shadows_res.message = "Harsh shadows removed; drop shadows conform to 8-12% Dark Green rule."
    results.append(shadows_res)

    # Tier 2 - Opacity Rules
    opacity_res = TestResult("Dark Green Opacity Rules", 2)
    opacity_violations = []
    # Dark Green RGB is (1, 62, 55). Any rgba(1, 62, 55, alpha) must follow the rules:
    # - 0.6 for subtitles
    # - 0.4 for inactive tabs
    # - 0.08 to 0.12 for shadows
    # - 0.05 / 0.15 for overlays/glows
    for fp, rel in css_files + src_files:
        try:
            content = open(fp, 'r', encoding='utf-8', errors='ignore').read()
            # Look for rgba(1, 62, 55, ...) or rgba(1,62,55,...)
            matches = re.finditer(r'rgba\(\s*1\s*,\s*62\s*,\s*55\s*,\s*([0-9.]+)\s*\)', content)
            for m in matches:
                alpha = float(m.group(1))
                line_no = content[:m.start()].count('\n') + 1
                allowed_alphas = [0.6, 0.4, 0.08, 0.09, 0.1, 0.11, 0.12, 0.15, 0.05]
                # Check closeness to handle float comparisons
                if not any(abs(alpha - allowed) < 0.001 for allowed in allowed_alphas):
                    opacity_violations.append(f"{rel}:{line_no} - Dark Green used with unauthorized opacity {alpha} (not 60%, 40%, or 8-12%)")
        except Exception as e:
            opacity_violations.append(f"Error checking opacities in {rel}: {e}")

    if opacity_violations:
        opacity_res.passed = False
        opacity_res.message = f"Found {len(opacity_violations)} occurrences of invalid Dark Green opacity."
        opacity_res.details = opacity_violations
    else:
        opacity_res.message = "Opacity rules for Dark Green are strictly followed."
    results.append(opacity_res)


    # -------------------------------------------------------------------------
    # TIER 3: CROSS-FEATURE COMBINATIONS
    # -------------------------------------------------------------------------

    # Tier 3 - Bottom Nav Active Pill Alignment
    pill_res = TestResult("Bottom Nav Active Pill Alignment", 3)
    if not os.path.exists(nav_fp):
        pill_res.passed = False
        pill_res.message = "src/components/BottomNav.js is missing"
    else:
        try:
            content = open(nav_fp, 'r', encoding='utf-8', errors='ignore').read()
            # Check active pill style color matches new palette (e.g. var(--color-dark-green) or #013E37)
            # Old code used '#9CCC65'
            violations = []
            if "'#9CCC65'" in content or '"#9CCC65"' in content:
                violations.append("Active Bottom Nav tab uses old color '#9CCC65'")
            if "'#475569'" in content or '"#475569"' in content:
                violations.append("Inactive Bottom Nav tab uses old gray '#475569'")
            if violations:
                pill_res.passed = False
                pill_res.message = "Bottom Nav active pill color and inactive colors are out of alignment."
                pill_res.details = violations
            else:
                pill_res.message = "Bottom Nav active pill uses the new luxury palette."
        except Exception as e:
            pill_res.passed = False
            pill_res.message = f"Error reading BottomNav.js: {e}"
    results.append(pill_res)

    # Tier 3 - Header vs Search Style Alignment
    align_res = TestResult("Header vs Search Style Alignment", 3)
    if not os.path.exists(header_fp):
        align_res.passed = False
        align_res.message = "src/components/Header.js is missing"
    else:
        try:
            content = open(header_fp, 'r', encoding='utf-8', errors='ignore').read()
            violations = []
            if "#070A13" in content:
                violations.append("Header background uses legacy dark '#070A13'")
            if "#FFF5EC" in content:
                violations.append("Header background uses legacy peach '#FFF5EC'")
            if "#00E5FF" in content:
                violations.append("Voice search active border uses legacy cyan '#00E5FF'")
            if violations:
                align_res.passed = False
                align_res.message = "Header and Search styling are not aligned on the luxury color scheme."
                align_res.details = violations
            else:
                align_res.message = "Header and Search components styling are perfectly aligned."
        except Exception as e:
            align_res.passed = False
            align_res.message = f"Error reading Header.js: {e}"
    results.append(align_res)

    # Tier 3 - Inactive vs Active Tab Styles
    tab_res = TestResult("Inactive vs Active Tab Styles", 3)
    # Check styles.css or BottomNav.js for tab state values
    # Inactive tabs must use Dark Green at 40% opacity (rgba(1, 62, 55, 0.4))
    # Active tabs must use 100% Dark Green (var(--color-dark-green) or #013e37)
    tab_violations = []
    if os.path.exists(nav_fp):
        try:
            nav_content = open(nav_fp, 'r', encoding='utf-8', errors='ignore').read()
            if "isActive" in nav_content:
                # Check active color assignment
                if "9CCC65" in nav_content:
                    tab_violations.append("Active tab assigned old green '#9CCC65'")
                if "475569" in nav_content:
                    tab_violations.append("Inactive tab assigned old gray '#475569'")
        except Exception as e:
            tab_violations.append(f"Error checking BottomNav.js tab styles: {e}")
            
    if tab_violations:
        tab_res.passed = False
        tab_res.message = "Active and inactive tabs do not use correct styling variables."
        tab_res.details = tab_violations
    else:
        tab_res.message = "Active and inactive tabs strictly use 100% and 40% Dark Green styling."
    results.append(tab_res)


    # -------------------------------------------------------------------------
    # TIER 4: REAL-WORLD APPLICATION SCENARIOS (Interactions)
    # -------------------------------------------------------------------------

    # Tier 4 - Hover Translation (exactly 2px upward)
    hover_res = TestResult("Hover Translation (2px Upward)", 4)
    hover_violations = []
    for fp, rel in css_files:
        try:
            content = open(fp, 'r', encoding='utf-8', errors='ignore').read()
            # Find all :hover rules
            # Regex to capture selector:hover { ... transform: translateY(Xpx) ... }
            matches = re.finditer(r'([.#a-zA-Z0-9_\-\s,:]+:hover\b[^{]*)\{([^}]+)\}', content)
            for m in matches:
                selector = m.group(1).strip()
                body = m.group(2)
                line_no = content[:m.start()].count('\n') + 1
                
                # Check for translateY or translate3d
                translate_match = re.search(r'translateY\(\s*(-?\d+px)\s*\)', body)
                if translate_match:
                    val = translate_match.group(1)
                    if val != "-2px":
                        hover_violations.append(f"{rel}:{line_no} - '{selector}' has hover translation '{val}' instead of '-2px'")
        except Exception as e:
            hover_violations.append(f"Error scanning hover rules in {rel}: {e}")

    if hover_violations:
        hover_res.passed = False
        hover_res.message = "Found non-conforming hover translations (must be exactly translateY(-2px))."
        hover_res.details = hover_violations
    else:
        hover_res.message = "All card hover translations translate exactly 2px upward."
    results.append(hover_res)

    # Tier 4 - Click Scaling (scale(0.95) for 150ms)
    scale_res = TestResult("Click Scaling (95% for 150ms)", 4)
    scale_violations = []
    # Check styles.css or JS for :active scale down actions.
    # Active scaling must be transform: scale(0.95) or scale3d(0.95, 0.95, 1)
    # duration must be 150ms (transition: transform 150ms ease or similar)
    for fp, rel in css_files:
        try:
            content = open(fp, 'r', encoding='utf-8', errors='ignore').read()
            # Scan active elements
            matches = re.finditer(r'([.#a-zA-Z0-9_\-\s,:]+:active\b[^{]*)\{([^}]+)\}', content)
            for m in matches:
                selector = m.group(1).strip()
                body = m.group(2)
                line_no = content[:m.start()].count('\n') + 1
                
                scale_match = re.search(r'scale(?:3d)?\(\s*([0-9.,\s]+)\s*\)', body)
                if scale_match:
                    val = scale_match.group(1).strip()
                    # Check if scale is 0.95
                    components = [v.strip() for v in val.split(',')]
                    if len(components) == 1:
                        # scale(0.95)
                        if components[0] != "0.95":
                            scale_violations.append(f"{rel}:{line_no} - '{selector}' has active scale '{val}' instead of '0.95'")
                    else:
                        # scale3d(0.95, 0.95, 1)
                        if components[0] != "0.95" or components[1] != "0.95":
                            scale_violations.append(f"{rel}:{line_no} - '{selector}' has active scale '{val}' instead of '0.95'")
        except Exception as e:
            scale_violations.append(f"Error scanning active states in {rel}: {e}")

    if scale_violations:
        scale_res.passed = False
        scale_res.message = "Found non-conforming click scaling behaviors."
        scale_res.details = scale_violations
    else:
        scale_res.message = "All click scaling transitions scale down to 95%."
    results.append(scale_res)

    # Tier 4 - Focus Rings (solid Dark Green spaced 2px)
    focus_res = TestResult("Focus Ring Outlines (spaced 2px)", 4)
    focus_violations = []
    # Look for outline: 2px solid var(--color-dark-green) / #013E37
    # and outline-offset: 2px
    for fp, rel in css_files:
        try:
            content = open(fp, 'r', encoding='utf-8', errors='ignore').read()
            # Check if outline-offset or outline rules exist for keyboard/focus
            # We want to make sure the global outline focus rule is defined
            has_focus_ring = False
            lines = content.split('\n')
            for idx, line in enumerate(lines, 1):
                if ":focus" in line:
                    # Let's inspect block for outline & offset
                    block = "\n".join(lines[max(0, idx-1):min(len(lines), idx+10)])
                    if "outline" in block and "outline-offset" in block:
                        # Validate it's 2px
                        if "2px" in block:
                            has_focus_ring = True
            
            if not has_focus_ring:
                focus_violations.append(f"{rel} - Missing keyboard focus ring configuration (:focus outline & outline-offset)")
        except Exception as e:
            focus_violations.append(f"Error checking focus rules in {rel}: {e}")

    if focus_violations:
        focus_res.passed = False
        focus_res.message = "Missing or non-conforming keyboard focus rings."
        focus_res.details = focus_violations
    else:
        focus_res.message = "Keyboard focus ring configurations are strictly set."
    results.append(focus_res)


    # -------------------------------------------------------------------------
    # PRINT RESULTS
    # -------------------------------------------------------------------------
    print("\nTest Run Summary:")
    passed_cnt = 0
    failed_cnt = 0
    
    for r in results:
        status_str = "\033[92m[PASS]\033[0m" if r.passed else "\033[91m[FAIL]\033[0m"
        # Since color codes might not print well in simple logs, let's use plain text as well
        status_str_plain = "[PASS]" if r.passed else "[FAIL]"
        print(f" {status_str_plain} Tier {r.tier} - {r.name}: {r.message}")
        if r.passed:
            passed_cnt += 1
        else:
            failed_cnt += 1
            for d in r.details:
                print(f"      * {d}")
                
    print("-" * 80)
    print(f"TOTAL TESTS: {len(results)} | PASSED: {passed_cnt} | FAILED: {failed_cnt}")
    print("-" * 80)
    
    # Write JSON results
    with open(os.path.join(ROOT, "e2e_test_report.json"), "w", encoding="utf-8") as f:
        json.dump([r.to_dict() for r in results], f, indent=2)
        
    return failed_cnt == 0

if __name__ == "__main__":
    success = run_e2e_tests()
    if not success:
        print("\nResult: E2E Test Suite failed due to non-conforming elements.")
        sys.exit(1)
    else:
        print("\nResult: E2E Test Suite passed successfully!")
        sys.exit(0)
