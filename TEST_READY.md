# E2E Test Suite Status

The E2E test infrastructure has been successfully initialized and configured.

## Runner Command
To run the E2E test suite, execute the following command at the project root:
```bash
python e2e_tests.py
```

## E2E Test Suite Coverage Summary

| Tier | Test Name | Target | Verification Check |
|---|---|---|---|
| **Tier 1** | Header Feature Coverage | `src/components/Header.js` | Asserts presence of location selector, voice search, active tabs, and notification badges. |
| **Tier 1** | Search Feature Coverage | `src/components/Header.js` | Asserts presence of search input, voice trigger, and autocomplete results. |
| **Tier 1** | Hero Section Feature Coverage | `src/screens/HomeScreen.js` | Asserts presence of hero title, subtitle, CTA button, and floating/animated badge. |
| **Tier 1** | Quick Links Feature Coverage | `src/screens/ShopScreen.js` | Asserts presence of category filter chips and size selectors. |
| **Tier 1** | Product Cards Feature Coverage | `src/screens/ShopScreen.js` | Asserts presence of product title, price, color indicator, and add to cart action. |
| **Tier 1** | Cart Feature Coverage | `src/screens/CartScreen.js` | Asserts presence of BOGO banner, step indicator lines, address cards, total calculations, and place order button. |
| **Tier 1** | Profile Feature Coverage | `src/screens/ProfileScreen.js` | Asserts presence of settings toggles, optometrist VIP support row, edit address link, and log out button. |
| **Tier 1** | Bottom Nav Feature Coverage | `src/components/BottomNav.js` | Asserts presence of tab links, active tab indicators, and central Floating Action Button (FAB). |
| **Tier 2** | Color Palette Enforcement | `styles.css` & `src/` | Scans for any unauthorized hex colors. Only `#FFFFFF`, `#FFF6DA`, `#013E37`, and `#A94A4A` (and their rgb/rgba components) are allowed. |
| **Tier 2** | Generic Gray Text Removal | `styles.css` & `src/` | Scans for outdated neutral gray styles/hexes like `#64748B`, `#A0A4C8`, `#475569`, etc. |
| **Tier 2** | Harsh Shadows Removal | `styles.css` & `src/` | Asserts that box/drop-shadows do not use harsh black or red/pink shades and follow the transparent Dark Green rule. |
| **Tier 2** | Dark Green Opacity Rules | `styles.css` & `src/` | Asserts that Dark Green is only used with authorized opacities (60% for subtitles, 40% for inactive tabs, and 8%-12% for shadows). |
| **Tier 3** | Bottom Nav Active Pill Alignment | `src/components/BottomNav.js` | Verifies active bottom navigation items use the new luxury palette instead of legacy colors (e.g. green `#9CCC65`). |
| **Tier 3** | Header vs Search Style Alignment | `src/components/Header.js` | Verifies search inputs inside the header match the luxury scheme and avoid mixing outdated color schemes. |
| **Tier 3** | Inactive vs Active Tab Styles | `styles.css` & `src/` | Verifies visual separation of active vs inactive tabs using 100% and 40% Dark Green styling rules. |
| **Tier 4** | Hover Translation (2px Upward) | `styles.css` | Verifies that all `:hover` rules with translations translate exactly translateY(-2px) upward. |
| **Tier 4** | Click Scaling (95% for 150ms) | `styles.css` & `src/` | Verifies active click transition scale is exactly 95% with 150ms transition duration. |
| **Tier 4** | Focus Ring Outlines (spaced 2px) | `styles.css` | Verifies that a solid Dark Green (#013E37) outline spaced 2px away (`outline-offset: 2px`) is defined for keyboard focus states. |

## Run Results on Current Codebase
- **Total Tests**: 18
- **Passed**: 9 (all Tier 1 structural feature coverage checks pass)
- **Failed**: 9 (all design system palette, opacities, active tab colors, hover translate heights, and click scale factors fail due to non-conforming elements)
- **Report File**: `e2e_test_report.json`
- **Console Log Capture**: `e2e_test_output.txt`
