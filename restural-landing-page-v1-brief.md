# Task: Build Restural Landing Page v1

## Objective
Produce a single-file HTML landing page for Restural that mirrors the structural layout, section order, and conversion logic of the Primal Queen landing page, populated with Restural's product, brand, and visual assets.

This is a one-shot first-pass build. The goal is a usable draft to evaluate structure and flow, not a pixel-perfect final. Ship something complete and functional over something polished and partial.

## Inputs

**Reference structure (Primal Queen landing page):**
[PASTE PRIMAL QUEEN URL HERE]

**Target product (Restural product page on Shopify):**
[PASTE RESTURAL PRODUCT URL HERE]

**Additional context:**
- Restural sells neurological recovery devices (DTC, Shopify-based, founder-led)
- This page will live inside Funnelish, not Shopify
- CTAs go to a Shopify cart permalink (external URL, full https://)
- Cart permalink URL: [PASTE OR LEAVE AS {{SHOPIFY_CART_PERMALINK}} PLACEHOLDER]

## Phase 1: Extract Before You Build

Before writing any code, produce a structural breakdown of the Primal Queen page in this format:

### Section inventory
For each section on the Primal Queen page, document:
- Section name (hero, social proof bar, problem agitation, mechanism, product benefits, how it works, testimonials, founder story, guarantee, FAQ, final CTA, etc.)
- Position in page order
- Approximate height / screen real estate
- Primary job of the section (what is it converting, reassuring, or educating on)
- Component type (full-width image with text overlay, two-column text+image, testimonial carousel, icon grid, video embed, comparison table, accordion FAQ, sticky CTA, etc.)
- Copy length approximation (headline only, headline + subhead + body paragraph, headline + bullet list, etc.)

### Design token extraction
From the Primal Queen page, extract:
- Primary brand color, secondary color, accent color
- Background color treatment (white, cream, section-alternating, etc.)
- Heading font family and weight pattern
- Body font family and weight
- Button style (pill, rounded-rect, square, outlined, filled)
- Image treatment (full-bleed, contained, polaroid, product-on-background)
- Visual rhythm (tight vs spacious, how much whitespace between sections)

### Conversion structure
Identify where each of these appears in the page order:
- Primary CTA placements (how many, at what scroll depths)
- Social proof anchors (reviews, press logos, customer count, etc.)
- Risk reversal (guarantee, shipping, returns)
- Urgency or scarcity elements (if any)
- Mechanism / "how it works" explanation
- Objection handling (FAQ, comparison, before/after)

Output this breakdown as a markdown table or bullet outline before proceeding to Phase 2.

## Phase 2: Build the Restural Version

Using the structural skeleton from Phase 1, produce a single HTML file that:

### Follows Primal Queen's structure exactly
- Same section order
- Same section types (if Primal Queen has a founder-story section at position 7, Restural has a founder-story section at position 7)
- Same component types per section (if Primal Queen uses an accordion FAQ, Restural uses an accordion FAQ)
- Same number of CTAs in the same relative positions

### Uses Restural's content and brand
- Product name, benefits, mechanism pulled from the Restural product page
- Restural's brand voice (not Primal Queen's)
- Restural's color palette extracted from the product page (if unclear, default to a clean neurological/medical aesthetic: off-white background, dark navy or charcoal headings, muted accent color)
- Restural's product imagery referenced by placeholder URL

### Meets these technical requirements (non-negotiable)

1. **Single self-contained HTML file.** All CSS in a `<style>` block at the top. All JS (if any) in a `<script>` block at the bottom. No external CSS files, no external JS except where noted below.

2. **Vanilla HTML + vanilla CSS only.** No Tailwind, no React, no framework, no build step, no preprocessor syntax.

3. **Namespace every class with `restural-lp-`.** Example: `.restural-lp-hero`, `.restural-lp-cta-primary`, `.restural-lp-testimonial-card`. This prevents CSS collisions when pasted into Funnelish. Same rule for any IDs.

4. **Responsive via CSS media queries only.** Mobile-first, one breakpoint at 768px minimum. No JS-based responsive logic.

5. **CTA buttons link to the Shopify cart permalink.** Use full `https://` URL. Leave as `{{SHOPIFY_CART_PERMALINK}}` placeholder if URL not provided.

6. **All images referenced as placeholder URLs** in the format `{{RESTURAL_IMG_[descriptive-name]}}` (e.g. `{{RESTURAL_IMG_hero-product-shot}}`, `{{RESTURAL_IMG_founder-portrait}}`). List every placeholder used at the bottom of the file in an HTML comment so the user can batch-replace after uploading assets to Shopify's CDN.

7. **Fonts via Google Fonts import** at the top of the `<style>` block, using fonts that match Primal Queen's visual register (if Primal Queen uses a serif display font + clean sans, pick closest free Google Fonts equivalents).

8. **No script tags inside HTML blocks that try to call external APIs.** This landing page is static. No fetch calls, no analytics, no tracking (handled by Funnelish separately).

9. **Semantic HTML.** Use `<section>`, `<article>`, `<header>`, `<footer>`, `<nav>` appropriately. Headings in proper hierarchy (one `<h1>`, logical `<h2>` and `<h3>` nesting).

10. **Inline accessibility basics.** Alt text on every image (even placeholders), aria-labels on CTAs if icon-only, sufficient color contrast.

### Copy approach
- Match Primal Queen's copy length per section (if their hero has a 6-word headline, Restural's hero has a 6-word headline)
- Do not copy Primal Queen's actual wording. Write original copy for Restural based on the Restural product page
- If Restural's product page doesn't give you enough information for a specific section (e.g. founder story), write a reasonable placeholder with `[PLACEHOLDER: ...]` brackets and flag it at the bottom of the file for the user to replace

## Output format

Produce in this order:

1. **Phase 1 extraction** (markdown document, can be in the same response)
2. **Single HTML file** (complete, copy-pasteable)
3. **Summary at the end** with:
   - List of all placeholder image URLs used
   - List of any `[PLACEHOLDER: ...]` copy that needs user review
   - List of assumptions made where Restural's product page was ambiguous
   - Any sections where you intentionally deviated from Primal Queen's structure and why

## What good looks like

- User can paste the HTML into a Funnelish Custom HTML block and see a complete, navigable landing page
- Section order and flow mirrors Primal Queen 1:1
- Visual aesthetic feels like Restural, not like Primal Queen
- Mobile and desktop both render without layout breaks
- All CTAs are functional links to the cart permalink
- User can identify in one pass which assets and copy need replacing before launch

## What to avoid

- Do not reproduce Primal Queen's copy verbatim or near-verbatim. Extract structural patterns, not sentences.
- Do not use generic class names like `.container`, `.hero`, `.section`, `.card`, `.button`. Always prefix.
- Do not add a build step, framework, or preprocessor.
- Do not ask for clarification before Phase 1. Run the extraction with whatever information the Primal Queen page gives you.
- Do not produce a multi-file project. One HTML file, end to end.
