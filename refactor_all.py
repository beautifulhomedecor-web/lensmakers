"""
Full color palette refactoring script for lensmakers-web.
Replaces all legacy colors with the new luxurious palette:
  Pure White:   #FFFFFF
  Cornsilk:     #FFF6DA
  Dark Green:   #013E37
  Rose Vale:    #A94A4A
"""
import re, os

# ============================================================
# 1. MASTER OVERRIDE BLOCK — appended to styles.css
# ============================================================
STYLES_PATH = 'styles.css'

OVERRIDE_BLOCK = """

/* ========================================================================
   LUXURY PALETTE MASTER OVERRIDE — DARK GREEN + CORNSILK + WHITE + ROSE VALE
   ======================================================================== */

/* ---- GLOBAL RESETS ---- */
body, html, #app {
  background: #FFFFFF !important;
  color: #013E37 !important;
}
.screen-container, .screen-transition-enter {
  background: #FFFFFF !important;
}

/* ---- HEADER ---- */
.top-header-wrapper, header.top-header-wrapper {
  background: rgba(255, 255, 255, 0.92) !important;
  backdrop-filter: blur(24px) saturate(1.8) !important;
  -webkit-backdrop-filter: blur(24px) saturate(1.8) !important;
  border-bottom: 1px solid #FFF6DA !important;
  box-shadow: 0 2px 20px rgba(1, 62, 55, 0.06) !important;
}
.top-header-wrapper .hamburger-bar,
.top-header-wrapper span[style*="background: '#FFFFFF'"],
.top-header-wrapper span[style*='background: \"#FFFFFF\"'],
.top-header-wrapper .menu-bar {
  background: #013E37 !important;
}
/* Logo text overrides */
.logo-lens { color: #013E37 !important; }
.logo-makers { color: #013E37 !important; }

/* Location pill */
.location-dropdown-pill, .location-pill {
  background: rgba(255, 246, 218, 0.6) !important;
  border: 1px solid #FFF6DA !important;
  color: rgba(1, 62, 55, 0.8) !important;
}

/* ---- SEARCH BAR ---- */
.search-bar-wrapper, .search-input-container, [class*="search-bar"] {
  background: rgba(255, 246, 218, 0.5) !important;
  border: 1px solid #FFF6DA !important;
  box-shadow: 0 2px 12px rgba(1, 62, 55, 0.06) !important;
}
.search-bar-wrapper input, .search-input-container input, [class*="search-bar"] input {
  background: transparent !important;
  color: #013E37 !important;
}
.search-bar-wrapper input::placeholder,
.search-input-container input::placeholder {
  color: rgba(1, 62, 55, 0.5) !important;
}
.search-bar-wrapper svg, .search-input-container svg,
[class*="search-bar"] svg, [class*="search-bar"] i {
  color: #013E37 !important;
  stroke: #013E37 !important;
}

/* ---- HERO SECTION — Strip dark gradient ---- */
.hero-section, .hero-section.dark-anchor, div.hero-section {
  background: linear-gradient(160deg, #FFFFFF 0%, #FFF6DA 100%) !important;
  color: #013E37 !important;
}
.hero-section * { color: #013E37 !important; }

/* Hero CTA button */
.hero-section .btn-shop-now, .hero-section button,
.hero-section [class*="btn-primary"] {
  background: #013E37 !important;
  color: #FFFFFF !important;
  box-shadow: 0 6px 24px rgba(1, 62, 55, 0.25) !important;
}
.hero-section .btn-shop-now:hover, .hero-section button:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 10px 30px rgba(1, 62, 55, 0.35) !important;
}

/* Carousel dots */
.carousel-dot-active {
  background: #013E37 !important;
}
.carousel-dot {
  background: rgba(1, 62, 55, 0.25) !important;
}

/* ---- CATEGORY QUICK LINKS ---- */
.category-card, .quick-link-card, [class*="category-card"] {
  background: #FFF6DA !important;
  border: 1px solid #FFF6DA !important;
  box-shadow: 0 4px 16px rgba(1, 62, 55, 0.08) !important;
  backdrop-filter: blur(12px) !important;
}
.category-card svg, .category-card i,
.quick-link-card svg, .quick-link-card i {
  color: #013E37 !important;
  stroke: #013E37 !important;
}
.category-card .label-primary { color: #013E37 !important; font-weight: 700 !important; }
.category-card .label-secondary { color: rgba(1, 62, 55, 0.6) !important; }

/* Category icon circles */
.shape-circle-btn, [class*="icon-circle"] {
  background: #FFF6DA !important;
  border: 1.5px solid rgba(1, 62, 55, 0.15) !important;
}
.shape-circle-btn svg, [class*="icon-circle"] svg {
  color: #013E37 !important;
  stroke: #013E37 !important;
}

/* ---- PROMOTIONAL BANNERS — Full dark-green replacement ---- */
.promo-banner, [class*="promo-banner"], [class*="banner-card"],
.blue-cut-banner, [class*="blue-cut"] {
  background: #013E37 !important;
  color: #FFFFFF !important;
}
.promo-banner *, [class*="promo-banner"] *,
.blue-cut-banner *, [class*="blue-cut"] * {
  color: #FFFFFF !important;
}
.promo-banner button, [class*="promo-banner"] button,
.promo-banner [class*="btn"], [class*="promo-banner"] [class*="btn"],
.blue-cut-banner button, [class*="blue-cut"] button {
  background: #FFF6DA !important;
  color: #013E37 !important;
}
.promo-banner svg, [class*="promo-banner"] svg,
.blue-cut-banner svg, [class*="blue-cut"] svg {
  stroke: #013E37 !important;
  color: #013E37 !important;
}

/* ---- PRODUCT CARDS ---- */
.product-card-glass, [class*="product-card"], .product-card {
  background: #FFFFFF !important;
  border: 1px solid #FFF6DA !important;
  box-shadow: 0 4px 20px rgba(1, 62, 55, 0.08) !important;
}
.product-card-glass:hover, [class*="product-card"]:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 8px 28px rgba(1, 62, 55, 0.14) !important;
}
/* Product image area wash */
.product-card-glass .image-area, [class*="product-card"] .image-area,
.product-card-glass > div:first-child, [class*="product-card"] > div:first-child {
  background: rgba(255, 246, 218, 0.4) !important;
}
/* Product typography */
.product-card-glass .product-name, [class*="product-card"] .product-name,
.product-card-glass h3, [class*="product-card"] h3 {
  color: #013E37 !important;
  font-weight: 700 !important;
}
.product-card-glass .product-price, [class*="product-card"] .product-price {
  color: #013E37 !important;
}
/* Promo badges */
.product-card-glass .badge, [class*="product-card"] .badge,
[class*="promo-sticker"], .sale-badge, [class*="discount-tag"] {
  background: #A94A4A !important;
  color: #FFFFFF !important;
}

/* ---- BUTTONS (global) ---- */
.btn-primary-pill, [class*="btn-primary"] {
  background: #013E37 !important;
  color: #FFFFFF !important;
  box-shadow: 0 4px 16px rgba(1, 62, 55, 0.2) !important;
  transition: transform 150ms ease, box-shadow 150ms ease !important;
}
.btn-primary-pill:hover, [class*="btn-primary"]:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 8px 24px rgba(1, 62, 55, 0.3) !important;
}
.btn-primary-pill:active, [class*="btn-primary"]:active {
  transform: scale(0.95) !important;
  transition-duration: 150ms !important;
}
.btn-secondary-pill, [class*="btn-secondary"] {
  background: #FFF6DA !important;
  color: #013E37 !important;
  border: 1px solid #FFF6DA !important;
}

/* Card hover (all interactive cards) */
.category-card:hover, .product-card-glass:hover,
.premium-special-card:hover, [class*="product-card"]:hover,
[class*="shop-card"]:hover {
  transform: translateY(-2px) !important;
  transition: transform 200ms var(--spring-gentle) !important;
}

/* Button active scale */
button:active, [role="button"]:active {
  transform: scale(0.95) !important;
  transition: transform 150ms ease !important;
}

/* Focus rings */
*:focus-visible {
  outline: 2px solid #013E37 !important;
  outline-offset: 2px !important;
}

/* ---- CART SCREEN ---- */
.free-frame-alert, [class*="cart-alert"], [class*="offer-alert"] {
  background: #FFF6DA !important;
  border: 1px solid rgba(1, 62, 55, 0.15) !important;
  color: #013E37 !important;
}
.free-frame-alert *, [class*="cart-alert"] * { color: #013E37 !important; }
.free-frame-alert button, [class*="cart-alert"] button {
  background: #013E37 !important;
  color: #FFFFFF !important;
}
/* Cart line item dividers */
.cart-item + .cart-item, [class*="cart-item"] + [class*="cart-item"] {
  border-top: 1px solid #FFF6DA !important;
}

/* ---- PROFILE SCREEN ---- */
.avatar-circle, [class*="avatar"] {
  background: #FFF6DA !important;
  border: 3px solid #013E37 !important;
  color: #013E37 !important;
}
.stats-box, [class*="stat-box"], [class*="stats-card"] {
  background: #FFF6DA !important;
  border: 1px solid rgba(1, 62, 55, 0.1) !important;
}
.stats-box .stat-number, [class*="stat-box"] .stat-number {
  color: #013E37 !important;
  font-size: 24px !important;
  font-weight: 800 !important;
}
.btn-logout, [class*="logout"] {
  background: transparent !important;
  border: 1.5px solid #A94A4A !important;
  color: #A94A4A !important;
}

/* ---- WISHLIST ---- */
[class*="wishlist"] svg, [class*="heart"] svg, .heart-icon {
  color: #A94A4A !important;
  stroke: #A94A4A !important;
}
[class*="badge-notification"], .notification-dot {
  background: #A94A4A !important;
}

/* ---- BOTTOM NAVIGATION ---- */
nav.bottom-nav {
  background: rgba(255, 255, 255, 0.96) !important;
  backdrop-filter: blur(20px) saturate(1.8) !important;
  -webkit-backdrop-filter: blur(20px) saturate(1.8) !important;
  border-top: 1px solid #FFF6DA !important;
  box-shadow: 0 -4px 24px rgba(1, 62, 55, 0.06) !important;
}
/* Inactive tabs */
nav.bottom-nav .tab-item { color: rgba(1, 62, 55, 0.4) !important; }
nav.bottom-nav .tab-item i, nav.bottom-nav .tab-item svg { color: rgba(1, 62, 55, 0.4) !important; stroke: rgba(1, 62, 55, 0.4) !important; }
/* Active tab */
nav.bottom-nav .tab-item.active, nav.bottom-nav .tab-active { color: #013E37 !important; }
nav.bottom-nav .tab-item.active i, nav.bottom-nav .tab-item.active svg,
nav.bottom-nav .tab-active i, nav.bottom-nav .tab-active svg { color: #013E37 !important; stroke: #013E37 !important; }
/* Active pill indicator */
nav.bottom-nav .tab-active::after, nav.bottom-nav .active-pill {
  content: '';
  display: block;
  width: 20px;
  height: 3px;
  background: #013E37 !important;
  border-radius: 2px;
  margin: 3px auto 0;
}

/* Cart badge */
nav.bottom-nav .cart-badge, nav.bottom-nav [class*="badge"] {
  background: #A94A4A !important;
  color: #FFFFFF !important;
}

/* ---- SECTION HEADINGS & TEXT ---- */
h1, h2, h3, h4, h5, h6 { color: #013E37 !important; }
p, span, label, a { color: inherit; }

/* Subtitle text */
[class*="subtitle"], [class*="sub-text"], [class*="description"] {
  color: rgba(1, 62, 55, 0.6) !important;
}

/* ---- BORDERS & DIVIDERS ---- */
[class*="divider"], hr {
  border-color: #FFF6DA !important;
  background: #FFF6DA !important;
}

/* ---- MODAL / SHEET ---- */
.modal-backdrop {
  background: rgba(1, 62, 55, 0.35) !important;
  backdrop-filter: blur(8px) !important;
}
.modal-sheet, [class*="bottom-sheet"], [class*="modal-card"] {
  background: #FFFFFF !important;
  border: 1px solid #FFF6DA !important;
  box-shadow: 0 -8px 40px rgba(1, 62, 55, 0.12) !important;
}

/* ---- LEGACY COLOR KILL ---- */
/* Kill dark blue / dark navy globals */
[style*="#070A13"], [style*="#0A112A"], [style*="#0F1535"] {
  background: #FFFFFF !important;
  color: #013E37 !important;
}
/* Kill lime green */
[style*="#84CC16"], [style*="#9CCC65"], [style*="#A8FF00"] {
  color: #013E37 !important;
}
"""

with open(STYLES_PATH, 'r', encoding='utf-8') as f:
    css = f.read()

# Remove any previous override block to avoid duplication
css = re.sub(r'/\* ={60,}\n   LUXURY PALETTE MASTER OVERRIDE.*', '', css, flags=re.DOTALL)
css = css.rstrip() + '\n' + OVERRIDE_BLOCK

with open(STYLES_PATH, 'w', encoding='utf-8') as f:
    f.write(css)

print("styles.css: luxury palette override block appended.")

# ============================================================
# 2. BottomNav.js — inline color fixes
# ============================================================
BN_PATH = 'src/components/BottomNav.js'
with open(BN_PATH, 'r', encoding='utf-8') as f:
    bn = f.read()

# Nav container
bn = bn.replace("background: '#FFFFFF',\n        borderTop: '1px solid #EAEAEA'",
                 "background: 'rgba(255,255,255,0.96)',\n        backdropFilter: 'blur(20px)',\n        WebkitBackdropFilter: 'blur(20px)',\n        borderTop: '1px solid #FFF6DA'")

# Active icon color (was #9CCC65)
bn = bn.replace("color: isActive ? '#9CCC65' : '#475569'",
                 "color: isActive ? '#013E37' : 'rgba(1, 62, 55, 0.4)'")
# Active badge background (was #9CCC65)
bn = bn.replace("background: '#9CCC65',\n                    color: '#000000'",
                 "background: '#A94A4A',\n                    color: '#FFFFFF'")
# Text color
bn = bn.replace("color: isActive ? '#9CCC65' : '#475569',",
                 "color: isActive ? '#013E37' : 'rgba(1, 62, 55, 0.4)',")

# Remove old boxShadow: 'none'
bn = re.sub(r"boxShadow: 'none',\s*\n(\s+display: 'flex',\s*\n\s+alignItems: 'center',\s*\n\s+justifyContent: 'space-around')",
            r"boxShadow: '0 -4px 24px rgba(1,62,55,0.06)',\n\1", bn)

# Add active indicator pill via marginTop style + pill div
bn = re.sub(
    r"(\{tab\.label\}\s*</span>)\s*(\s*</div>\s*\);?\s*\}\))\s*(\s*</nav>)",
    r"\1\n            {isActive && (\n              <div style={{ width: '20px', height: '3px', background: '#013E37', borderRadius: '2px', margin: '3px auto 0' }} />\n            )}\2\3",
    bn
)

with open(BN_PATH, 'w', encoding='utf-8') as f:
    f.write(bn)

print("BottomNav.js: refactored.")

# ============================================================
# 3. Header.js — inline color fixes
# ============================================================
HDR_PATH = 'src/components/Header.js'
with open(HDR_PATH, 'r', encoding='utf-8') as f:
    hdr = f.read()

# Header background
hdr = re.sub(
    r"background: activeTab === 'home' \? '#070A13' : '[^']+',",
    "background: 'rgba(255, 255, 255, 0.92)',\n          backdropFilter: 'blur(24px) saturate(1.8)',\n          WebkitBackdropFilter: 'blur(24px) saturate(1.8)',\n          borderBottom: '1px solid #FFF6DA',",
    hdr
)

# Hamburger bars (background: '#FFFFFF' -> '#013E37')
hdr = hdr.replace(
    "background: '#FFFFFF', borderRadius: '2px', display: 'block'",
    "background: '#013E37', borderRadius: '2px', display: 'block'"
)

# Logo color
hdr = re.sub(r"color: '#FFFFFF'([^}]*?)(lens|makers)", 
             lambda m: f"color: '#013E37'{m.group(1)}{m.group(2)}", hdr)

# Bell / notification button in header
hdr = re.sub(
    r"background: 'rgba\(255, 255, 255, 0\.08\)', border: '1px solid rgba\(255, 255, 255, 0\.15\)',\s*color: '#FFFFFF'",
    "background: 'rgba(255, 246, 218, 0.6)', border: '1px solid #FFF6DA', color: '#013E37'",
    hdr
)

# All white colors within the header -> dark green or cornsilk
# Notification bell badge (lime green -> rose vale)
hdr = re.sub(r"(background:\s*'#84CC16')", "background: '#A94A4A'", hdr)
hdr = re.sub(r"(background:\s*'#9CCC65')", "background: '#A94A4A'", hdr)

# Search bar background
hdr = re.sub(
    r"(background:\s*'rgba\(255, 255, 255, 0\.\d+\)')([^}]*?border:\s*'1px solid [^']+')(.*?search)",
    lambda m: "background: 'rgba(255, 246, 218, 0.5)'" + m.group(2).replace(m.group(2).split("'1px solid")[1], "'1px solid #FFF6DA'") + m.group(3) if 'search' in m.group(3) else m.group(0),
    hdr,
    flags=re.DOTALL
)
# simpler catch for search container bg
hdr = re.sub(r"background: 'rgba\(255, 248, 231, 0\.9\)'", "background: 'rgba(255, 246, 218, 0.5)'", hdr)
hdr = re.sub(r"background: '#FFF5EC'", "background: 'rgba(255, 246, 218, 0.5)'", hdr)

# Search icon / mic: white/light -> dark green
hdr = re.sub(r"color: '#FFFFFF'", "color: '#013E37'", hdr)
hdr = re.sub(r"color: 'rgba\(255, 255, 255, 0\.\d+\)'", "color: 'rgba(1, 62, 55, 0.6)'", hdr)

# Location pill
hdr = re.sub(r"background: 'rgba\(0, 0, 0, 0\.\d+\)'", "background: 'rgba(255, 246, 218, 0.7)'", hdr)

# Autocomplete dropdown
hdr = re.sub(r"background:\s*'#1C2240'", "background: '#FFFFFF'", hdr)
hdr = re.sub(r"background:\s*'#2D3A6B'", "background: '#FFF6DA'", hdr)

# Log-out icon
hdr = re.sub(r"color:\s*'#FFFFFF'\s*\}", "color: '#013E37' }", hdr)

with open(HDR_PATH, 'w', encoding='utf-8') as f:
    f.write(hdr)

print("Header.js: refactored.")

# ============================================================
# 4. HomeScreen.js — hero section color fix
# ============================================================
HS_PATH = 'src/screens/HomeScreen.js'
with open(HS_PATH, 'r', encoding='utf-8') as f:
    hs = f.read()

# Hero background
hs = re.sub(
    r"background: 'linear-gradient\(180deg, #070A13[^']+\)'",
    "background: 'linear-gradient(160deg, #FFFFFF 0%, #FFF6DA 100%)'",
    hs
)
hs = re.sub(r"background: '#070A13'", "background: '#FFFFFF'", hs)
hs = re.sub(r"background: '#0A112A'", "background: '#FFFFFF'", hs)
hs = re.sub(r"background: '#0F1535'", "background: '#FFFFFF'", hs)
hs = re.sub(r"color: '#FFFFFF'", "color: '#013E37'", hs)

# Hero text (explicit white text in hero)
hs = re.sub(r"(className=\"hero-section[^\"]*\"[^>]*>.*?)(color:\s*'#FFFFFF')", 
            lambda m: m.group(1) + "color: '#013E37'", hs, flags=re.DOTALL)

# Dark hero gradient overrides
hs = re.sub(r"'linear-gradient\(135deg, #070A13[^']+\)'", "'linear-gradient(135deg, #FFFFFF 0%, #FFF6DA 100%)'", hs)
hs = re.sub(r"'linear-gradient\(180deg, #0[0-9A-Fa-f]{5}[^']+\)'",
            "'linear-gradient(160deg, #FFFFFF 0%, #FFF6DA 100%)'", hs)

# Category cards bg 
hs = re.sub(r"background: 'rgba\(255, 255, 255, 0\.08\)'", "background: '#FFF6DA'", hs)
hs = re.sub(r"background: 'rgba\(255, 255, 255, 0\.1\)'", "background: '#FFF6DA'", hs)
hs = re.sub(r"background: 'rgba\(255, 255, 255, 0\.12\)'", "background: '#FFF6DA'", hs)

# Promo/banner dark bg
hs = re.sub(r"background: '#013B30'", "background: '#013E37'", hs)
hs = re.sub(r"background: '#1C4E3D'", "background: '#013E37'", hs)
hs = re.sub(r"background: '#0D2B24'", "background: '#013E37'", hs)
hs = re.sub(r"background: '#00695C'", "background: '#013E37'", hs)
hs = re.sub(r"background: 'rgba\(1, 79, 68[^']+\)'", "background: '#013E37'", hs)

# Lime green -> dark green
hs = re.sub(r"color:\s*'#84CC16'", "color: '#013E37'", hs)
hs = re.sub(r"color:\s*'#9CCC65'", "color: '#013E37'", hs)
hs = re.sub(r"background:\s*'#84CC16'", "background: '#013E37'", hs)
hs = re.sub(r"background:\s*'#9CCC65'", "background: '#013E37'", hs)

# CTA shop button
hs = re.sub(
    r"(background:\s*'#84CC16'|background:\s*'#9CCC65'|background:\s*'rgba\(132, 204, 22[^']+\)')",
    "background: '#013E37'",
    hs
)

# Category wrapper border
hs = re.sub(r"border:\s*'1px solid rgba\(255, 255, 255, 0\.\d+\)'", "border: '1px solid #FFF6DA'", hs)

# Accent rose vale on badges
hs = re.sub(r"background:\s*'#EF5350'", "background: '#A94A4A'", hs)
hs = re.sub(r"background:\s*'#FF6B6B'", "background: '#A94A4A'", hs)

with open(HS_PATH, 'w', encoding='utf-8') as f:
    f.write(hs)

print("HomeScreen.js: refactored.")

print("\nAll files refactored successfully!")
