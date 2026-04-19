# Restural V2 Rebuild Plan — Match Primal Queen Structure

Source of truth: `restural-lp-v1.html` (current) vs `screenshots/primalqueen-full.png` + `primal-queen-sales.md` swipe.

---

## 1. Where V1 Landed

V1 is a clean first pass of the PQ skeleton. It's structurally on-brief but diverges from PQ in 6 meaningful ways and the visual language is a navy/coral Playfair serif, not Restural's real Poppins + green (`#3AAA35`) + navy (`#10247F`) system.

**V1 sections, in order:**
1. Topbar countdown (hours/min/sec)
2. Nav
3. Flash strip ("Free Shipping — Today Only")
4. Hero — 2-col navy gradient, coral CTA, oval product photo slot, floating "90-Day Money Back" badge, single testimonial card below
5. Testimonial strip (5 cards)
6. Marquee
7. Problem — dark bg, 2-col alternating images with editorial text, blue-bordered callout
8. CTA block
9. Scientific article — Dr. Steven Jones byline, 4 stat callouts (4x, 89%, 82%, 75%, 72%), numbered references (1–20)
10. CTA block
11. "NeuroFuel Standard" — 6 icon badges + 3 authority tags
12. Scarcity box (red)
13. Detailed testimonials (4 cards, 2-col)
14. Founder — dark, 2-col portrait + copy + 6-ingredient grid (mostly placeholder)
15. CTA block
16. Timeline — zigzag 6 steps (Week 1 → Month 6+), circle image slots
17. How to use — 3 steps, square images
18. Comparison — 6 cards pricing $ vs $1.35/day (NeuroFuel highlighted)
19. Manufacturing blurb (text only)
20. Pricing — 2 cards + countdown, 3-Mo featured
21. FAQ — 13 Qs, accordion
22. Final CTA
23. Footer

**Strongest parts:** hero oval + floating badge, alternating dark-bg problem section, full scientific article with citations, zigzag timeline, pricing card pair, 13-Q FAQ. All mirror PQ's conversion anchors.

**Weakest parts:** palette is wrong (navy/coral Playfair vs Restural's green/navy Poppins), founder is 3 `[PLACEHOLDER]` paragraphs, there's no product photography, no buyer qualification section, only one marquee, no sticky bottom CTA, no review-aggregation block with star breakdown, and the comparison section was reframed as cost-vs-therapy which drifts from PQ's ingredient-density framing.

---

## 2. Key Decisions Before Rebuild

These I can't decide for you — flag before V2 starts:

### D1. Product: NeuroFuel coffee or EMS device?
V1 positions **NeuroFuel coffee** (lion's mane) with a `restural.com` footer. But `brand-identity.md` + `brand-brief.md` describe Restural as an **EMS foot-drop device** (Parkinson's / stroke / MS). The live Shopify store sells the EMS device. This is the single biggest fork — every section below assumes we commit to one.

- If **NeuroFuel coffee** (new SKU, separate from EMS): keep V1's copy and product story, but we still need product photography.
- If **EMS device**: most of V1's copy (coffee, "one cup a day", Lion's Mane, hericenones) has to be rewritten and the 3-step "how to use" becomes "strap on → turn on → walk". The article still works — Dr. Steven Jones is already a Restural authority figure — but the mechanism swaps from NGF/lion's-mane to EMS/neural-muscle reactivation.

**My recommendation:** commit to one before V2 generation. If unclear, I'd lean EMS since that's what the brand actually sells and has asset URLs ready (`brand-identity.md` has CDN URLs for product shots, Dr. Jones headshot, 90-day badge, us-vs-them graphic, foot/brain/muscle icons).

### D2. Brand palette: port the real Restural system or keep V1's?
V1 uses navy (`#1A2B5E`) + coral (`#F07060`) + Playfair Display. Real Restural uses navy (`#10247F`) + green (`#3AAA35`) + Poppins. PQ uses magenta/purple + yellow accents + green CTA. To match PQ's *energy* (bold accent on dark bg) while staying on-brand Restural, the cleanest translation is: **navy dark sections + green CTAs + orange accent highlights (`#DE7920` star-rating orange) for "X MORE" stats and emphasis**. Drop Playfair for Poppins.

### D3. Article length: keep the 3000–5000-word treatment?
PQ's article is a huge conversion lift — 57 citations, doctor-authored, deep mechanism explanation. V1's article is \~600 words with 20 citations. If you want true PQ parity, expand to 2–3x and add subheadings with pull-quotes. If you want to ship faster, keep V1-size but tighten.

### D4. Sticky bottom bar?
PQ has one ("NEW YEAR SALE — ENDS SOON — REDEEM OFFER"). V1 doesn't. Easy add but changes page rhythm.

---

## 3. Target Structure (PQ Order, Restural Content)

**23 sections in this exact order.** Bold = new vs V1. Italic = exists in V1 but needs rework.

| # | Section | PQ Source | V1 State | V2 Action |
|---|---|---|---|---|
| 1 | Countdown topbar | Sec 1 | ✓ exists | Restyle to navy `#10247F`, keep d/h/m/s |
| 2 | Nav header | Sec 2 | ✓ exists | Add product-line subtitle ("EMS foot activation" or "Recovery coffee"), add Cart icon |
| 3 | Hero — 2-col w/ product image + testimonial carousel | Sec 3 | *needs rework* | Swap oval to contained product shot (EMS box or coffee pouch). Replace single testimonial card with **auto-rotating 5-testimonial carousel** below CTA. Green CTA instead of coral. Keep floating "GET 1 MONTH FREE" / "90-DAY GUARANTEE" circle badge. |
| 4 | Marquee #1 | Sec 4 | ✓ exists | Color: green on white or navy on yellow to match PQ's high-contrast strip |
| 5 | **Ancestral / problem narrative** (dark bg) | Sec 5 | *needs rework* | V1's dark-bg 2-col alternating works. Reframe from "stroke recovery stalls" to the PQ formula: *"How recovery worked before corporate medicine overloaded us with pills"* — position Restural as the back-to-basics / neuroplasticity-respecting alternative. Keep blue callout box. |
| 6 | CTA block | — | ✓ exists | Keep |
| 7 | **Product belief statement** | Sec 6 | ❌ missing | **Add.** Single bold statement — "Our belief: neural pathways rebuild when you give the brain what it needs daily, not weekly." Handle the "I don't want another device/drink" objection. 1 short section, conversational, ends with CTA. |
| 8 | Results timeline (zigzag) | Sec 7 | ✓ exists | Keep V1's 6-step zigzag. Re-skin markers green, not navy-to-coral gradient. Replace circle image placeholders with actual lifestyle/product photos. |
| 9 | How to use — 3 steps | Sec 8 | ✓ exists (later in V1) | **Move up** from V1 position 17 to right after timeline. Rewrite steps to match product (see D1). |
| 10 | **Ingredient / mechanism comparison** | Sec 9 | *reframed* | V1 has cost comparison ($1.35/day vs $3,600 therapy). PQ uses "X MORE [nutrient] than [vegetable]" cards. **Decision:** keep V1's cost angle **or** swap to mechanism-comparison cards ("Passive rehab: 1x repetitions. EMS: 10,000+ contractions per session"). I'd keep cost AND add a mechanism row — two 6-card grids stacked. Orange `#DE7920` for the "X MORE" stat numbers. |
| 11 | Manufacturing credibility | Sec 10 | *needs expansion* | V1 is text-only. PQ has a video + GMP/Lab/USA badges. **Add facility video slot** + 3 certification badges. If no video available, substitute a large facility photo. |
| 12 | Scarcity alert | Sec 11 | ✓ exists | Keep. |
| 13 | Reviews showcase (detailed) | Sec 12 | ✓ exists | V1 has 4 cards. **Expand to 6–8** with photos, locations, dates. Add 5-star visual per card. |
| 14 | **Who is Restural for / NOT for** | Sec 13 | ❌ missing | **Add.** Two-column list: FOR (stroke survivors, Parkinson's patients, MS foot drop, caregivers) / NOT FOR (pre-diagnosis, pregnancy, pacemaker users — genuine contraindications build trust). This qualifies the buyer and signals medical seriousness. |
| 15 | **Founder story — part 1 (struggle)** | Sec 14 | *placeholder* | **Write the full story.** Needs: founder name, photo, personal catalyst moment (family member's stroke / own MS diagnosis / physio career), list of failed alternatives (pills, AFO braces, generic rehab apps, etc.). 400–500 words, first person, warm tone. |
| 16 | **Founder story — part 2 (resolution)** | Sec 15 | *placeholder* | Continue: the discovery moment (clinical trial, published paper, collaboration with Dr. Jones), prototyping, forming the company, mission line. 300–400 words. End with the "that's why Restural exists" beat. |
| 17 | **"Here's where the magic happens" transition** | Sec 16 | ❌ missing | Full-width banner image with bold overlay text. Visual pause — sets up product-feature section. Restural angle: maybe lab/manufacturing interior or a close-up of the device/coffee being used. |
| 18 | Quality badges row | Sec 17 | ✓ exists | V1's "NeuroFuel Standard" is the right shape. Swap copy to Restural's actual claims: "Non-Invasive / Medical-Grade / FDA-Registered Facility / 90-Day Guarantee / Clinically Backed / Neurologist Endorsed". |
| 19 | **Marquee #2 (repeat)** | Sec 18 | ❌ missing | **Add.** Same marquee pattern, positioned just before pricing to re-energize urgency. |
| 20 | Pricing / product order | Sec 19 | ✓ exists | Keep 2-card layout. If EMS: mirror the PDP's Buy 1 / **Buy 2 (default)** / Bundle. If coffee: 1-Month / 3-Month. Add "4,014 purchases today" live counter line above pricing (PQ's bandwagon mechanic). Keep countdown. |
| 21 | **Trustpilot-style review aggregation** | Sec 20 | ❌ missing | **Add.** Big "4.8 / 5 — 12,038 reviews" header, 5-bar star distribution (90 / 7 / 2 / 0 / 1 per brand brief), 4–6 individual verified reviews with avatar initial, country, date, helpful-vote counts. Sort tabs (Most Recent / Highest / With Photos) can be cosmetic only. |
| 22 | FAQ accordion | Sec 21 | ✓ exists | Keep 13 Qs. Rewrite for actual product (D1). |
| 23 | **Sticky bottom CTA bar** | Sec 22 | ❌ missing | **Add.** Fixed-bottom bar: "Sale Ends Tonight" + green "CLAIM OFFER" button. Appears after user scrolls past hero, hides over footer. |
| 24 | Footer | Sec 23 | ✓ exists | Keep. |

---

## 4. Restural-Specific Brand Adaptations

These are the "small things" to re-design on brand rather than 1:1 copy from PQ:

- **Hero image shape:** PQ uses a large pink-bordered oval with lifestyle photo + product overlaid + yellow "12 MONTHS" sticker + "GET 1 MONTH FREE" circle. V1 uses an oval placeholder. **Restural option:** keep the oval but make it a cleaner medical look — white background, product front-and-center (EMS box or coffee pouch), small green "90-DAY GUARANTEE" floating badge in the Restural brand voice. Or go arch-shaped (the shape in `final-desktop-hero.png` the green variant preview) which reads more clinical/trustworthy than the PQ femme aesthetic.
- **Color system:**
  - `#10247F` navy for dark sections (problem, founder, pricing, final CTA, topbar)
  - `#3AAA35` green for all CTAs (replaces V1's coral)
  - `#F3F3F3` light gray for alternating sections (replaces V1's `#F2F6FC` pale blue)
  - `#DE7920` orange as the "emphasis" color — use it for star ratings, "X MORE" stats, highlighted words in headlines (replacing PQ's yellow `#EFF759`)
  - `#FF6B6B` coral reserved ONLY for sale-price strikethrough animations
- **Typography:** Poppins everywhere. H1 600 weight at 2.4–2.8rem. H2 600 at 1.9–2.2rem. Body 400 at 15–16px. Drop Playfair entirely.
- **Button shape:** 8px border-radius rectangles (per brand brief), NOT pills. Uppercase, 600 weight, 15–18px.
- **Image treatment:** PQ uses playful pink-bordered cutouts + handwritten yellow scribbles + emoji. Restural should stay cleaner — contained product shots on white, rounded 12–16px corners, no scribbles, no emoji. Swap PQ's emoji timeline icons (🛌😌⚡️🌺🧘‍♀️🔥) for small line-art clinical icons.
- **Guarantee badge:** PQ uses 365-day. Restural's real offer is 90-day — **keep it at 90** (PQ's 365 is a category outlier and changing yours is a business decision, not a design one). Make the "90-DAY" circle badge a consistent asset that appears under every CTA.
- **Urgency honesty:** PQ leans heavily on "X purchases today" + "February risk of selling out" — Restural's medical context makes overtly aggressive urgency feel off. I'd keep the countdown + marquee + sticky bar, but drop the scarcity alert's tone slightly and remove any "selling out" language unless that's actually true for an EMS device.

---

## 5. Asset Requirements (V2 Prep)

Before V2 build, gather or flag these:

**Ready to use (already in `brand-identity.md`):**
- Product shots (EMS hero, lifestyle, angles) — 4 CDN URLs
- Dr. Steven Jones headshot — CDN URL
- 90-day guarantee badge — CDN URL
- Us-vs-them comparison graphic — CDN URL
- Icon set (foot, brain, muscle, paralysis, person, sport) — 7 CDN URLs
- 3 additional doctor headshots (Chen, Mitchell, Kim) for review credibility

**Need to source:**
- Founder photo + bio (if founder-led angle is true — if not, drop founder section and replace with "Our Team" / "Our Clinical Advisors" card grid)
- 6 customer headshots for detailed testimonials
- 5 short customer headshots for hero carousel
- Facility video or photo for manufacturing section
- "Magic happens" transition banner image
- 3 "how to use" step photos (if EMS: unbox → strap on → walk; if coffee: tear sachet → pour water → drink)
- Lifestyle / before-after photos for timeline milestones

**Decisions to write:**
- Actual founder story (or "why we built this" without a named founder)
- Real review count + star distribution if different from PDP's 4.8/5 from 12,038

---

## 6. Execution Strategy — Re-runs & Screenshots

You mentioned using re-runs to advantage. Here's how I'd sequence it:

### Pass 1 — Scaffold (1 re-run)
Generate V2 HTML with all 23 sections in place, Restural palette, product committed per D1, but with placeholder images and placeholder founder story. Same one-shot brief as V1 but with:
- Explicit section list (copy table above)
- Restural design tokens (green `#3AAA35`, navy `#10247F`, Poppins, 8px radius)
- Explicit "replace V1 coral with green" instruction
- Explicit "add sticky bottom bar + trustpilot review section + who-for-not-for + magic-happens banner + belief statement + second marquee"

Open in browser, full-page screenshot desktop + mobile.

### Pass 2 — Section surgery (3–5 re-runs, one per problem section)
For each section that didn't land, run a targeted prompt: *"Rewrite just the [founder section] of this HTML — keep everything else identical. Rewrite to [specific instruction]. Output full file."* Sections most likely to need surgery:
- Founder story (always needs a second pass once you've written real copy)
- Ingredient/mechanism comparison cards (the hybrid cost + mechanism idea needs iteration)
- Hero testimonial carousel (getting the auto-rotate behavior + layout right)
- Trustpilot review block (custom layout, easy to get wrong)
- Pricing cards (tier copy and featured-state styling)

### Pass 3 — Visual polish (2 re-runs)
- Pass focused only on spacing / rhythm / mobile breakpoints
- Pass focused on image placements once real photos are dropped in

### Screenshots to capture along the way
- **Desktop full-page** after each major pass (1440×full)
- **Mobile full-page** at 375px — PQ holds up on mobile and V1 hasn't been stress-tested there
- **Hero viewport** (1440×900) side-by-side with `pq-section-hero.png` for direct comparison
- **Founder section** side-by-side with PQ screenshot at the 5k mark
- **Pricing section** side-by-side with PQ pricing region

Tools: any headless browser screenshot utility. `tools/browser_use.py` in the A folder could script this if you want the comparison automated.

---

## 7. Open Questions for You

1. Product: coffee or EMS device? (D1)
2. Founder: is there a real founder story to tell, or do we pivot to "medical advisory team"?
3. Expanded article: 2–3x longer, or keep V1 length?
4. Keep the cost-vs-therapy comparison section (V1's departure from PQ) or swap to a PQ-style mechanism/ingredient comparison?
5. Real review numbers — pull from PDP (4.8 / 12,038) or write new?
6. Sticky bottom bar — yes/no?

Answer these and I'll generate V2.
