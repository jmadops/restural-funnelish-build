# V2 Asset Brief

Every image slot on the page, what it should look like, the exact dimensions it needs to render correctly, and the current state. Build/source in this order — I've prioritized by visual impact.

File-naming convention: save all final assets as `neurofuel-<slot-name>.jpg` (or `.png` if transparency needed) and drop URLs/paths back to me.

---

## Legend

| Symbol | Meaning |
|---|---|
| 🔴 | **Wrong image wired in — currently broken or misleading** |
| 🟡 | **Placeholder only — dashed empty box visible on page** |
| 🟢 | **Acceptable for now, but could be upgraded** |
| 📸 | Still photo needed |
| 🎥 | Short video clip needed (or high-res still as fallback) |

---

## Priority 1 — Fix what's already wrong

### 🔴 Hero image (arch-shaped)
**Location:** Right column of hero, taller than wide, top rounded arch shape
**Currently:** `6_2_cd21c43f...png` — this is actually an ad creative with "% OF STROKE SURVIVORS REPORTED AN EXPONENTIAL INCREASE…" overlay text baked into the image. The text overlay fights the headline and the 90-day badge on top of it.
**Required:** Clean hero product shot.
**Dimensions:** **800 × 1000 px** (4:5 portrait), min 600×750
**Shape mask applied by CSS:** arch — top 240px border-radius, bottom 24px
**Content options (pick one):**
  - (a) **Pure product shot:** Restural NeuroFuel packaging (coffee bag or box) on soft warm gradient background (cream/beige), centered, with light shadow under. No text overlays.
  - (b) **Lifestyle product hero:** A clean still life — the mug/product on a kitchen counter in morning light, steam optional, no people. Warm but clinical.
  - (c) **Hands + product:** Close-cropped shot of mature hands holding the branded mug, warm morning tones.
**Avoid:** text overlays, overlay graphics, multiple people, stock "senior with caregiver" cliché poses, anything that looks like an ad with burned-in marketing claims.
**Background:** Warm neutral (cream, beige, soft gradient) or pure white. NOT a busy kitchen or room.

### 🔴 Belief section — main image
**Location:** "Our Belief" section, right side, portrait 4:5 with rounded corners
**Currently:** `8_1.png` — looks like a medical professional / clinical setting image, not a warm morning-coffee moment.
**Required:** A morning scene with the product.
**Dimensions:** **680 × 850 px** (4:5 portrait), min 500×625
**Content:** Hands wrapped around the NeuroFuel mug in soft morning light. Or the mug sitting next to a packet on a kitchen counter. Warm, domestic, one-person-POV feel. No overlay text.
**Background:** Kitchen / dining table / window light.

### 🔴 Belief section — accent image (small square, overlapping)
**Location:** Bottom-left corner of the belief main image, small square with thick cream border
**Currently:** `nf_cuh.png` — the branded product shot. Fine but it's being re-used 3 places on the page.
**Required:** A different product angle or ingredient close-up.
**Dimensions:** **400 × 400 px** square, min 300×300
**Content options:**
  - (a) Close-up of a single sachet tearing open
  - (b) Coffee being poured into the mug (top-down)
  - (c) The lion's mane mushroom ingredient on wood / linen
**Avoid:** re-using the packaging shot from hero/final CTA.

---

## Priority 2 — Fill the empty placeholders

### 🟡 Problem section — "rehab" image
**Location:** First row of the dark Problem section, right column
**Currently:** empty dashed placeholder
**Dimensions:** **700 × 525 px** (4:3 landscape), rounded corners
**Content:** A stroke survivor in rehab — hand exercises, physio session, person walking with therapist, or close-up of a hand gripping a rail. Shot should feel serious and empathetic, not clinical-cold.
**Mood:** Documentary / editorial. Dark-friendly (image sits on navy background so mid-to-high contrast works).
**Avoid:** overly bright stock imagery, smiling "hero pose" stock, overlay text.

### 🟡 Problem section — "brain" illustration
**Location:** Second row of the dark Problem section, left column
**Currently:** empty dashed placeholder
**Dimensions:** **700 × 525 px** (4:3 landscape)
**Content:** Neural pathway / brain illustration. Options:
  - (a) Scientific brain cross-section with neural pathways highlighted
  - (b) 3D-rendered neuron cluster with glow
  - (c) Medical-style brain scan (MRI, colored overlay)
**Style:** Dark-friendly, blue/gold palette ideally. The existing "The Science" article image (`5_3e9324b5...png`) is a good reference — something in that aesthetic but wider crop.
**Avoid:** cartoon illustrations, kid-science textbook style.

### 🟡 Article inline — lion's mane mushroom
**Location:** Between "Lion's Mane: A Natural NGF Stimulator" heading and the 4x stat callout, in the main article body
**Currently:** empty dashed placeholder with "The Mushroom" sticker
**Dimensions:** **1000 × 500 px** (16:8 wide banner)
**Content:** Hero shot of a lion's mane mushroom — ideally on a wooden/linen surface, natural light, single mushroom front and center. Could also be a split composition: half mushroom, half molecular structure illustration.
**Mood:** Natural, ingredient-forward, editorial food-photography feel.

### 🟡 Manufacturing / facility
**Location:** Under the "Pharmaceutical-Grade, Lab Verified" heading. Currently has a big placeholder with a play button overlay.
**Currently:** empty placeholder
**Preference:** 🎥 **Short video** (15–30 sec, MP4, silent-friendly with captions)
**Dimensions:** **1440 × 720 px** (16:8), or 16:9 also works
**Content (video):** Facility tour — pan through lab, tech mixing/weighing ingredients, product packaging line, quality-control bench, lab coats, bright clean lighting. No narration needed — will play muted.
**Still fallback:** A single hero still from the facility works — same aspect ratio.
**Avoid:** stock "scientist in lab" footage from shutterstock. If no real facility footage exists, flag and we'll redesign this section to a certifications grid instead of faking it.

### 🟡 Who For / Not For — header image
**Location:** Wide banner above the two-column "FOR / NOT FOR" cards
**Currently:** `14_d4146be0...png` — likely the wrong shape / feels repurposed from another layout
**Required:** Wide lifestyle hero
**Dimensions:** **1400 × 525 px** (16:6 ultra-wide banner)
**Content:** Two-person scene — caregiver + stroke survivor drinking coffee together, or a stroke survivor in a warm domestic setting (morning kitchen, reading, writing). The image should visually convey "this is who I am" — the target buyer should recognize themselves.
**Avoid:** stock "elderly couple walks on beach" cliché, clinical/hospital setting, anyone looking sad or infirm.

### 🟡 Founder portrait
**Location:** Left column of dark "Why I Built NeuroFuel" founder section. Tall image with arched top.
**Currently:** empty dashed placeholder
**Dimensions:** **640 × 800 px** (4:5 portrait), shape: arch — top 160px border-radius, bottom 20px
**Content:** Professional portrait of the NeuroFuel founder. Chest-up or waist-up, soft natural light, looking at camera or slight angle. Casual professional wardrobe (not lab coat, not suit).
**Background:** Kitchen, home office, or neutral studio. NOT a medical facility.
**Note:** If there is no real founder / this is a generic brand, let me know — I'll refactor this section into "Our Medical Advisory Team" with the 3 doctor headshots we already have.

### 🟡 Magic banner — full-width "Here's where the magic happens"
**Location:** Full-width section between founder and quality badges
**Currently:** `1_2.jpg` — I think this is a product shot that's going to look stretched/wrong at 16:7 banner size
**Dimensions:** **1920 × 840 px** (16:7 ultra-wide banner), should look good with a dark gradient overlay (CSS is already set up for this)
**Content:** Dramatic lifestyle or lab scene. Options:
  - (a) Extreme close-up of coffee pouring into a mug, slow-motion liquid texture
  - (b) Lab bench with ingredients arranged (lion's mane, coffee beans, lab glassware)
  - (c) Overhead flatlay: NeuroFuel packaging surrounded by ingredients
**Note:** image gets a dark navy gradient overlay + overlay headline text. So the image can be visually rich; it doesn't need to be high-contrast because the overlay handles readability.

### 🟡 How-to-Use — 3 step photos
**Location:** "Three Steps, Two Minutes" section
**Currently:** empty dashed placeholders
**Dimensions each:** **520 × 400 px** (4:3 landscape), 3 images needed
**Content:**
  1. **Step 1 — Open your packet:** Hands tearing open a NeuroFuel sachet, close-up, contents visible.
  2. **Step 2 — Add hot water & stir:** Water being poured into the mug with the contents already inside, or spoon mid-stir.
  3. **Step 3 — Drink daily:** Person taking a sip from the branded mug, soft morning light. Face partly visible, warm.
**Consistency:** all 3 should be shot in the same lighting / same kitchen so they read as a sequence, not 3 stock photos glued together.

### 🟡 Timeline — 6 milestone circle photos
**Location:** Zigzag timeline "What to Expect with Consistent Use" section. Six small circle images, one per milestone.
**Currently:** empty circle placeholders
**Dimensions each:** **240 × 240 px** (1:1 square that gets masked to a circle), 6 images
**Content per milestone:**
  1. **Week 1 — Mental clarity:** Close-up of someone reading or focused at a desk
  2. **Week 2-3 — Movement gains:** Hand gripping something, or foot taking a confident step
  3. **Month 1 — Pain reduction:** Someone doing a gentle stretch, relaxed face
  4. **Month 2 — Therapy acceleration:** Physio session, productive movement
  5. **Month 3 — Independence:** Cooking / buttoning a shirt / dressing / driving
  6. **Month 6+ — Compounding gains:** Walking outside confidently, or hobby (gardening, crafts)
**Style:** candid, warm, varied subjects (not all the same person). All shot or selected with a consistent color cast so they feel like a series.

### 🟡 Pricing cards — 2 product images
**Location:** Top of each pricing tier card
**Currently:** `3_a2c6d81d` (1-mo) and `4_a1ab9f4d` (3-mo) — probably the right-ish product shots but might be inconsistent in crop/style
**Dimensions each:** **400 × 400 px** square
**Content:**
  - **1-Month Starter:** Single NeuroFuel package / box / bag, front-facing, white background.
  - **3-Month Recovery Plan:** Three packages / a family of three units stacked or grouped, showing clear "3x" visual cue. Same background, same lighting as the 1-month so they read as a consistent tier system.
**Important:** same background, same camera angle, same size-in-frame. The difference should only be quantity.

### 🟡 Final CTA product image
**Location:** Large circle product image above the final "Your Brain Can Rebuild" headline. Has a floating "90-Day Guarantee" gold badge on the corner (handled by CSS).
**Currently:** `nf_cuh.png` — OK but re-used elsewhere
**Dimensions:** **600 × 600 px** square (gets masked to a circle)
**Content:** Clean product packaging shot, centered, with a subtle warm background OR completely transparent PNG if you want the navy section color to show through.
**Ideal:** a slightly different angle from the hero shot so it doesn't feel like the exact same image twice.

---

## Priority 3 — Currently acceptable, upgrade when you can

### 🟢 Testimonial avatar photos (hero carousel + strip + detailed cards)
**Count:** 14 total avatar slots, currently using 9 unique stock avatars from the Restural advertorial CDN
**Status:** they're doing the job. Customers expect some level of stylized avatars in testimonials and mixing them across sections (carousel, strip, detailed) is fine.
**Upgrade path:** if you have real customer consent + photos, swap them in. Dimensions: **200 × 200 px** squares masked to circles, minimum 150×150.

### 🟢 Article inline — "The Science" neural image
**Currently:** `5_3e9324b5...png` — works well, looks like a proper scientific brain/neural illustration.
**Keep as-is** unless you have a higher-res version.

### 🟢 Article inline — "The Ritual" lifestyle
**Currently:** `2_3.jpg` — family/lifestyle photo. OK but a bit warm/busy.
**Upgrade path:** a true "morning coffee" still would work better here (see Belief brief for similar direction).

---

## Priority 4 — Consider video

### 🎥 Hero background micro-video (optional)
A 6–10 second looping video of steam rising from a mug, coffee being poured, or a subtle product rotation would add a lot of premium feel to the hero. Not required — a still image works — but worth mentioning.

### 🎥 Manufacturing / facility tour
See Priority 2 entry. This is the single highest-impact place to put a video on the page.

### 🎥 Testimonial videos (future)
PQ doesn't have these. But a 30-sec customer video in a prominent spot is often the single highest converting element on a page like this. Consider adding a video testimonial block between the detailed testimonials and the Who-For section in V3.

---

## What I've changed in V2 alongside this brief

- **Removed** the gold "Get 1 Month Free" sticker from the hero
- **Enhanced** the 90-day guarantee badge — now larger (124px), double-ring coral+gold frame, gold downward pointer at top, three-line "90 / DAY / MONEY-BACK GUARANTEE" stack, subtle glow-pulse animation. Mobile version simplified (86px, no animation).
- Re-took screenshots to `v2-screenshots/` so we can do side-by-side after new assets land.

---

## What to send me back

For each asset you create, send:
1. Final image URL (CDN or dropbox link, whatever works)
2. Slot name matching the headings above (e.g. "Hero image", "Belief section — main image")

When you have assets for Priority 1 + at least 3–4 Priority 2 slots, I'll wire them in and do another screenshot pass so we can iterate from there.
