# E2E Test Infrastructure & Design

This document details the End-to-End (E2E) testing infrastructure, philosophy, feature inventory, test runner architecture, and detailed verification scenarios (Tiers 1 to 4) for the **Lens Makers Web application**.

---

## 1. Test Philosophy
The E2E testing infrastructure is designed to programmatically verify the visual, structural, and behavioral specifications of the Lens Makers web app. Because standard browser automation tools (like Selenium or Playwright) may not be configured in the headless system or are heavy to spin up, our E2E runner uses a **Static-Semantic Parsing and Validation** approach:
1. **Opaque-box Verification**: The suite evaluates the final built/served artifacts (HTML, CSS, JS files) directly from the codebase.
2. **Behavioral Simulation**: Interactive states (hover, click, focus) are checked by analyzing CSS selectors, inline style rules, and AST configuration properties to ensure interaction specifications are strictly set.
3. **Palette & Design System Checks**: It programmatically asserts that the luxury theme rules are honored across all source files, rejecting any unauthorized colors or incorrect layout/opacity configurations.

---

## 2. Feature Inventory
The E2E test suite targets the following core features:
- **Header**: Contains location bar, action buttons, active tab indicators, and notification count pills.
- **Search**: Contains input field, voice search button, and style alignment with the rest of the header.
- **Hero Section**: Serves as the landing view with the main luxury title, subtitle, primary CTA button, and floating animated badge.
- **Quick Links / Category Controls**: Allows navigation/filtering of products by category or size.
- **Product Cards**: Displays product titles, prices, frame colors, and the "Add to Cart" button.
- **Cart**: Handles BOGO banner alerts, step indicator lines, address cards, total calculation, and checkout summaries.
- **Profile**: Manages settings toggles, optometrist support links, address edit views, and the log out button.
- **Bottom Nav**: Contains tab buttons, active tab pill indicator, and the Floating Action Button (FAB).

---

## 3. Test Runner Design
The test runner is implemented in `e2e_tests.py`. It is a pure Python script that:
- Loads and parses `index.html`, `styles.css`, and all JS components/screens in `src/`.
- Extracts styling parameters using regular expressions, AST parsers, and text search.
- Aggregates results into a structured JSON report and outputs a detailed CLI report.
- Fails with a non-zero exit code if any conformance checks do not pass.

---

## 4. Test Scenarios (Tiers 1 to 4)

### Tier 1: Feature Coverage
Checks the presence of DOM elements and critical structural components:
- **Header Test**: Asserts that `Header.js` renders location bar, notification pill, active tab indicator, and circle action buttons.
- **Search Test**: Asserts that search bar elements exist with input, placeholder, and voice search buttons.
- **Hero Section Test**: Asserts that `HomeScreen.js` contains a hero heading, subtitle, primary CTA button, and floating/animated badges.
- **Quick Links Test**: Asserts that `ShopScreen.js` includes category filter chips and size selectors.
- **Product Cards Test**: Asserts that product list items in `ShopScreen.js` render product titles, prices, color pickers, and "Add to Cart" button.
- **Cart Test**: Asserts that `CartScreen.js` contains the BOGO alert banner, progress step lines, address cards, total due, and place order button.
- **Profile Test**: Asserts that `ProfileScreen.js` contains settings toggles, optometrist Priority VIP row, edit address link, and the log out button.
- **Bottom Nav Test**: Asserts that `BottomNav.js` renders the navigation links, the Floating Action Button, and active navigation indicators.

### Tier 2: Boundary Cases (Palette & Style Constraints)
Ensures that the design system constraints are strictly enforced:
- **Authorized Hex Codes Only**: Verifies that `styles.css` and all JS files in `src/` use ONLY the following hex codes for styling:
  - `#FFFFFF` (Pure White)
  - `#FFF6DA` (Cornsilk)
  - `#013E37` (Dark Green)
  - `#A94A4A` (Rose Vale)
- **Generic Gray Text Removal**: Checks that neutral text uses Dark Green at 60% (`rgba(1, 62, 55, 0.6)`) or 40% (`rgba(1, 62, 55, 0.4)`) instead of standard gray colors (e.g., `#64748B`, `#A0A4C8`, `#475569`, etc.).
- **Harsh Shadows Removal**: Ensures drop shadows use a highly transparent Dark Green (8% to 12% opacity, i.e., `rgba(1, 62, 55, 0.08)` to `rgba(1, 62, 55, 0.12)`) instead of harsh black or pink shadow rules.
- **Opacity Verification**: Ensures that opacity values for Dark Green (60% and 40%) are correctly implemented using RGBA/opacity properties where appropriate.

### Tier 3: Cross-Feature Combinations
Checks consistency across different components:
- **Bottom Nav Active Pill**: Checks that the active nav tab styling conforms to the Dark Green color scheme and contrast rules.
- **Header vs Search Style Alignment**: Verifies that search elements inside the header align with the overall background and color theme of the header component.
- **Active vs Inactive Tabs**: Verifies that active tabs are visually distinguished from inactive tabs using the correct text/background styles (e.g. 100% Dark Green vs 40% Dark Green).

### Tier 4: Real-World Application Scenarios
Verifies interactive behavior properties:
- **Hover Transitions**: Asserts that cards translate exactly 2px upward on hover (`transform: translateY(-2px);`).
- **Click Scaling**: Asserts that buttons scale down to 95% for exactly 150ms on click (`transform: scale(0.95); transition: transform 150ms ease;`).
- **Focus Indicators**: Asserts that focus rings use a solid Dark Green (#013E37) outline spaced 2px away (`outline: 2px solid var(--color-dark-green); outline-offset: 2px;` or similar focus-ring rules).
