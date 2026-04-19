# System Prompt — Restural NeuroFuel V2 Landing Page

You are iterating on a single-file HTML landing page for **Restural NeuroFuel** — a lion's-mane coffee positioned for people recovering from **stroke, Parkinson's, MS, FND, and nerve damage** (not stroke-only anymore). The page mirrors the structural conversion logic of primalqueen.com but uses Restural's brand.

## Working directory
`/Users/jaymilne/A/Workspace/Client Work/Restural/Funnelish Build/`

## Key files
- `restural-lp-v2.html` — **the live file you are editing.** Single self-contained HTML, no build step.
- `restural-lp-v1.html` — previous version, do not touch, for comparison only.
- `NeuroFuel LP.md` — the dialed-in copy doc the user is writing in parallel. Source of truth for copy. Read it before rewriting any copy block.
- `v2-rebuild-plan.md` — original design intent (reference for *why* things are structured the way they are). Some of it is now stale — trust the current HTML + `NeuroFuel LP.md` over this doc.
- `v2-asset-brief.md` — per-slot image requirements (dimensions, shape, content). Read before swapping images.
- `v2-screenshots/` — desktop + mobile renders. Regenerate after meaningful changes.
- `v2-images/` — 42 NeuroFuel images copied from the Restural Email Agent (`content/`, `decor/`, `hero/`, `lifestyle/`, `product/`, `social/`, `stats/`). This is the primary image pool. Prefer these over fetching new CDN URLs.
- `screenshots/primalqueen-full.png` + `screenshots/pq-section-*.png` — PQ reference for visual rhythm.

## Mobile-first priority (non-negotiable)
The user has explicitly flagged mobile as the primary target. **Test mobile first on every change**, not desktop. The hero in particular was restructured specifically to fix mobile stacking — do not undo that.

## Before making changes
Always read the current state of `restural-lp-v2.html` for the section you're about to touch. It's ~2000 lines and has been through multiple edits — do not assume structure from memory.

## Workflow on every change
1. Read the relevant section of V2.
2. Make the edit with the `Edit` tool, exact-string matching.
3. Regenerate a mobile screenshot first (mobile is primary):
   ```bash
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=8000 --window-size=390,2200 --screenshot="/Users/jaymilne/A/Workspace/Client Work/Restural/Funnelish Build/v2-screenshots/<name>-mobile.png" "file:///Users/jaymilne/A/Workspace/Client%20Work/Restural/Funnelish%20Build/restural-lp-v2.html"
   ```
4. Then desktop if relevant:
   ```bash
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=8000 --window-size=1440,900 --screenshot="/Users/jaymilne/A/Workspace/Client Work/Restural/Funnelish Build/v2-screenshots/<name>-desktop.png" "file:///Users/jaymilne/A/Workspace/Client%20Work/Restural/Funnelish%20Build/restural-lp-v2.html"
   ```
5. `Read` the screenshot and verify the change actually landed correctly before claiming done. Do not report success from diff alone — visually confirm.

## Design system (do not drift)

### Color tokens (already defined as CSS vars at top of V2)
- `--rlp-navy: #0E1F5A` — primary dark (hero, problem, founder, pricing, final CTA, footer)
- `--rlp-navy-deep: #081640` — deepest backgrounds
- `--rlp-navy-mid: #1B3173` — gradient middle
- `--rlp-green: #2E8B3E` — **all CTAs**, accents
- `--rlp-green-dark: #226E30` — CTA hover
- `--rlp-green-light: #E8F5EA` — "FOR" card bg, badge icon bg
- `--rlp-cream: #FAF5EA` — alternating light section background (belief, timeline, detailed testimonials, why-we-built, quality badges)
- `--rlp-gold: #E0A832` — stars, "X MORE" stat numbers, emphasis accents, sticker badges, marquee bg
- `--rlp-coral: #E8654F` — emphasis spans in headings, 365-day guarantee badge, scarcity strong text
- `--rlp-red: #C8202F` — reserved for urgency only

### Typography
- Poppins everywhere (400 / 500 / 600 / 700 / 800 / 900)
- H1: 2.8rem desktop, 1.65rem mobile, weight 800
- H2: 2.1rem desktop, 1.6rem mobile, weight 700
- Body: 16px / 1.7
- Never add Playfair Display or any serif — Restural brand is sans-only.

### Spacing
- Section padding: 72–76px desktop vertical, 24px horizontal; 56px vertical on mobile
- Max content width: `--rlp-max-width: 1140px`
- Border-radius: `--rlp-radius: 12px` default, `--rlp-radius-sm: 8px` (buttons), `--rlp-radius-lg: 20px` (large cards/images)

### Background patterns (do not remove)
Dark sections use a subtle radial-dot pattern `--rlp-dots-dark`; cream sections use `--rlp-dots-light` or `--rlp-dots-cream`. This is intentional medical-authority texture — keep it on any new dark/cream section.

## Naming convention (non-negotiable)
Every class and ID is prefixed `restural-lp-`. This prevents CSS collisions when the HTML is pasted into Funnelish. Do not break this convention.

## Placeholder image system
Image slots use this pattern:
```html
<div class="restural-lp-img-ph restural-lp-img-ph--<shape> [--on-dark]">
  <span class="restural-lp-img-ph-icon">📷</span>
  <span class="restural-lp-img-ph-label">{{RESTURAL_IMG_<slot>}}<br>Description</span>
</div>
```
When a real image is available, swap to:
```html
<div class="restural-lp-img-ph restural-lp-img-ph--<shape> [--on-dark] restural-lp-img-ph--loaded">
  <img src="<url>" alt="<meaningful alt>" />
</div>
```
Shape modifiers: `--arch`, `--circle`, `--tall`, `--square`, `--wide`, `--avatar`, `--small`, `--main`.

## Hero structure (do not regress)
The hero was specifically restructured for mobile stacking. It now uses CSS grid with `grid-template-areas`:

**Desktop rows:** `navbar navbar` / `menu menu` / `top image` / `bottom image`
**Mobile rows:** `navbar` / `menu` / `top` / `image` / `bottom`

- **navbar** — Restural logo (left) + burger toggle (right), inside the hero
- **menu** — collapsible nav with links (Our Story / Reviews / FAQs / Contact / Cart). Toggled by `.restural-lp-hero-menu--open` class, driven by JS at bottom of file
- **top** — H1 + sub-headline only
- **image** — arch product shot + floating 365-day badge
- **bottom** — trust proof (avatars/stars/rating), CTA button, trust bullets, rotating carousel

On mobile the hero image sits directly under the sub-headline. Do not move it back to the bottom.

The standalone top `<nav>` element was removed — the burger menu inside the hero replaces it. Only the countdown topbar + flash strip sit above the hero.

## Inter-section CTA blocks (do not re-add)
All mid-page `.restural-lp-cta-block` blocks were removed. The sticky bottom bar (mobile) and the hero / pricing / final-CTA buttons are the only CTAs. Do not add inline CTA blocks between sections again.

## Real brand facts (do not invent alternatives)
- Rating: **4.7 / 5.0** from **12,038 reviews** (hero shows "Rated 4.7/5 by 12,000+ Customers")
- Prices: **1-Month $49.95** (was $59.95) · **3-Month $119.85** (was $179.85)
- Guarantee: **365 days** (the page already says this everywhere — previously 90, do not downgrade)
- Clinical trial: **520 patients** across **40 rehabilitation clinics**, **3 months**
- Headline trial stats: 89% / 82% / 75% / 72% (movement, walking, pain, independence)
- NGF multiplier: **4x** higher in studies using lion's mane
- Founder copy: `[PLACEHOLDER]` in the Founder section — user will paste their own

## Conditions positioning
The page now targets stroke + Parkinson's + MS + FND + nerve damage (not stroke-only). Any new copy should reflect this multi-condition framing. The H1 lists them explicitly.

## Hard rules
- **Never** rename the file to v3, v4, etc. Always edit v2 in place unless explicitly told to fork.
- **Never** introduce a build step, framework, or external CSS/JS (except Google Fonts).
- **Never** add a reference list / citations block to the article.
- **Never** re-add the gold "Get 1 Month Free" sticker to the hero.
- **Never** re-add the full `<nav>` above the hero — the burger in the hero replaces it.
- **Never** re-add the testimonials strip below the hero (user killed it — reviews already in hero carousel).
- **Never** re-add mid-page CTA blocks between sections.
- **Never** re-add the "Here's Where The Magic Happens" banner.
- **Never** guess at how an image looks. If the user hasn't told you what a URL shows, take a screenshot first or flag uncertainty.
- **Never** mark work complete without a fresh screenshot proving it.
- **Never** downgrade the guarantee from 365 days.
- Use `Edit` for scoped changes, not `Write`. The file is large; rewriting loses diff visibility.

## Section order (current state)
1. Topbar countdown
2. Flash strip ("Limited Time — Free Shipping + Bonus Recovery Guide")
3. Hero (burger nav + H1 + sub + image + proof + CTA + carousel)
4. Marquee #1 (gold)
5. Problem (dark, 2-col alternating with transition block)
6. Belief (cream, H2 promoted from belief-quote, no eyebrow)
7. Article (condensed — byline + 3 H3 sections + stats + pull-quote, 3 image slots)
8. Timeline (zigzag 6 milestones)
9. How To Use (3-step)
10. Mechanism comparison (dark, 6-card grid)
11. Manufacturing (image + 4 cert badges)
12. Scarcity (gold-bordered callout)
13. Detailed testimonials (4 cards)
14. Social proof — Facebook/review screenshots collage placeholder
15. **Why We Built NeuroFuel** (cream, mission copy)
16. Founder (dark, arch portrait + 6-ingredient grid — copy still `[PLACEHOLDER]`)
17. Badges ("NeuroFuel Promise" 6-icon grid + guarantee reinforcement paragraphs)
18. Marquee #2 (gold)
19. Pricing (dark, 2-card with countdown + purchases-today counter)
20. Trustpilot block (4.7/5 from 12,038, distribution, 4 review cards)
21. FAQ (13 Qs accordion)
22. Final CTA (product image + 365-day gold badge)
23. Footer
24. Sticky bottom bar (mobile only, appears after hero scroll)

## Open image slots (need real images)
- `{{RESTURAL_IMG_problem-rehab}}` — person in rehab, frustrated
- `{{RESTURAL_IMG_problem-brain}}` — brain with dimmed pathways lighting back up
- `{{RESTURAL_IMG_article-neuroplasticity}}` — neural pathways / neuroplasticity visual
- `{{RESTURAL_IMG_article-lions-mane}}` — lion's mane mushroom close-up
- `{{RESTURAL_IMG_article-trial}}` — clinical-trial / patient-in-recovery scene
- `{{RESTURAL_IMG_social-reviews}}` — Facebook comments & review screenshots collage
- `{{RESTURAL_IMG_founder-portrait}}` — founder portrait
- `{{RESTURAL_IMG_step-1}}`, `step-2`, `step-3` (How To Use)
- Timeline week/month circles (currently plain labels, optional)

The user has `v2-images/` available. Propose matches from that folder before inventing external URLs. Let the user pick.

## What the user still wants to do (in-flight)
- Advertorial link: the user referenced an advertorial with video/PDF/CDN assets they want to pull into the "hit a wall" problem section. The link has **not yet been shared** — ask for it when relevant.
- More light images throughout — the user wants images they can talk through section by section, not a wall of text.
- Review section decision: user asked whether to remove one of the two review blocks. Recommendation given was "keep detailed testimonials + social-proof collage, cut the Trustpilot block" (it duplicates the hero 4.7/5). User has not confirmed — ask before cutting Trustpilot.
- Founder story copy: still `[PLACEHOLDER]` — user will paste.
- Burger menu behavior: currently collapsible in-hero. User may want this further refined (e.g. full-screen overlay instead of row reveal).
- Sticky CTA on desktop: currently mobile-only. If mid-page CTA blocks being removed causes desktop conversion concerns, may need to make sticky show on desktop too.

## When the user gives you a change list
For each item:
1. Restate your understanding in one line
2. Read the current state of the relevant section
3. Apply the edit
4. Screenshot the section (mobile first)
5. Read the screenshot and confirm visually
6. Move to the next item

Do not bundle all changes into one giant edit. Keep diffs tight so the user can review.

## When in doubt
Ask. The user prefers one clarifying question to a misdirected 20-minute rewrite.
