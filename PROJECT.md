# Project: Lens Makers Retheming (Luxurious Aesthetic)

## Architecture
- Mobile web app using React 18 and Babel Standalone loaded dynamically via index.html.
- Styling defined in styles.css and inline styles inside src/components/ and src/screens/.
- Data flow: Local products array from src/data/products.js, states in screen/component JS files.

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | E2E Test Suite Setup | Design and code E2E tests for Tiers 1-4 based on user requirements | none | IN-PROGRESS |
| 2 | styles.css Retheming | Overhaul CSS variables in :root and override selectors to use new palette | M1 | PLANNED |
| 3 | React Components Retheming | Retheme inline styles and colors in src/components/ | M2 | PLANNED |
| 4 | React Screens Retheming | Retheme inline styles and colors in src/screens/ | M3 | PLANNED |
| 5 | E2E Verification | Ensure all Tier 1-4 tests pass on the rethemed app | M4 | PLANNED |
| 6 | Adversarial Hardening | Implement Tier 5 tests and fix any uncovered gaps | M5 | PLANNED |

## Interface Contracts
- CSS custom properties in styles.css are the source of truth for variables.
- Strict Palette Enforcement:
  * Pure White (#FFFFFF): Base backgrounds, bottom nav background base.
  * Cornsilk (#FFF6DA): Glassmorphic surfaces with backdrop blur, structural borders, BOGO alerts.
  * Dark Green (#013E37): Brand typography, active navigation state, primary CTA button, titles.
  * Rose Vale (#A94A4A): Accents, notification counts, alerts, sale tags, and error alerts.
- Opacities of Dark Green:
  * 60% opacity for subtitles and secondary details.
  * 40% opacity for inactive tabs and muted text.
  * Highly transparent (8%-12%) for soft, organic drop shadows (no harsh black shadows).
- Interactive states:
  * Cards translate exactly 2px upward on hover (`transform: translateY(-2px);`).
  * Buttons scale down to 95% for exactly 150ms on click (`transform: scale(0.95); transition: transform 150ms ease;`).
  * Solid Dark Green focus ring spaced 2px away for keyboard focus indicator (`outline: 2px solid var(--color-dark-green); outline-offset: 2px;`).
