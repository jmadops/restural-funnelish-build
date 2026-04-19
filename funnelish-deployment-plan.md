# Funnelish Deployment Plan — Restural NeuroFuel Lander

The complete plan for getting the Restural lander live on Funnelish at `restural.com`, sending traffic to the existing Shopify store at `tryrestural.com`.

## Architecture

| Domain | Platform | Role |
|---|---|---|
| `restural.com` | Funnelish | Single landing page (the lander we built) |
| `tryrestural.com` | Shopify | Full storefront — home, product pages, cart, checkout, fulfillment |

Funnelish is used **purely as a hosted landing page builder**. Shopify owns everything commerce-related: products, payment gateway, shipping, apps, fulfillment, and the entire checkout experience. The two platforms stay independent — no order sync, no product import, no Shopify connection inside Funnelish.

CTAs on the lander are absolute cross-domain URLs to Shopify cart permalinks. Customer flow:

```
Ad/traffic
  -> restural.com (Funnelish lander)
  -> click CTA
  -> tryrestural.com/cart/{variant_id}:1 (Shopify cart with product preloaded)
  -> Shopify checkout
  -> Shopify thank-you / fulfillment
```

## The Funnelish build itself

Minimum viable funnel — three things only:

1. **Funnel container** — one funnel, named whatever (e.g. "Restural NeuroFuel Lander").
2. **Step 1: Landing page** — one step, containing one Section › Row › Column with a single Custom HTML widget. The widget holds the entire body markup, `<style>` block, and `<script>` block.
3. **Domain** — `restural.com` connected to the funnel.

Things deliberately **not** built in Funnelish:
- No checkout page
- No thank-you page
- No products
- No payment gateway
- No shipping config
- No Shopify connection / order sync
- No OTOs or order bumps (would require Funnelish checkout, which we're not using)

## How the HTML gets pasted in

### One Custom HTML widget approach

The entire lander body lives inside a single Custom HTML widget. This works because:

- Funnelish allows arbitrary HTML/CSS/JS inside the widget.
- Class names use a `.restural-lp-*` prefix and CSS custom properties use `--rlp-*`, so there's no collision risk with Funnelish's own builder CSS.
- The page is ~134 KB — well within tolerance.
- The page already includes `@media` breakpoints at 1040px, 768px, and 640px, so responsive behavior is fully self-contained — Funnelish doesn't need to do anything for mobile.

### What can NOT live inside the widget

These belong in **Page Settings › Custom Codes › Head HTML** (Funnelish owns the document `<head>`):

- `<title>` and `<meta>` tags (description, OG, Twitter cards)
- `<link rel="preconnect">` for Google Fonts (better than `@import`)
- The Google Fonts stylesheet `<link>`
- Any SEO meta you want indexed
- Favicon link

Don't add a duplicate `<meta name="viewport">` — Funnelish sets one already.

### Wrapping section settings

The Section › Row › Column wrapping the Custom HTML widget needs:
- Section: full width, no padding, no max-width constraint
- Row: full width, no padding
- Column: 100% width, no padding

Otherwise Funnelish's default container will pinch the lander on mobile.

## CTA rewiring

The current HTML has 6 CTAs all pointing to `{{SHOPIFY_CART_PERMALINK}}` plus a nav cart icon and footer policy links. Each maps to a real Shopify URL on `tryrestural.com`:

| Location in HTML | Becomes |
|---|---|
| Nav "🛒 Cart" | `https://tryrestural.com/cart` |
| Hero "GET MY NEUROFUEL →" | `https://tryrestural.com/cart/{BUNDLE_VARIANT_ID}:1` |
| Pricing block — 3-month bundle "Add to Cart" | `https://tryrestural.com/cart/{BUNDLE_VARIANT_ID}:1` |
| Pricing block — 1-month starter "Add to Cart" | `https://tryrestural.com/cart/{STARTER_VARIANT_ID}:1` |
| "⚡ Start Your Recovery" | `https://tryrestural.com/cart/{BUNDLE_VARIANT_ID}:1` |
| Footer "Claim Offer" | `https://tryrestural.com/cart/{BUNDLE_VARIANT_ID}:1` |

Footer policy links (`{{RESTURAL_URL_PRIVACY}}`, etc.) resolve to Shopify policy pages:
- `https://tryrestural.com/policies/privacy-policy`
- `https://tryrestural.com/policies/terms-of-service`
- `https://tryrestural.com/policies/shipping-policy`
- `https://tryrestural.com/policies/refund-policy`
- Track order — wherever the existing tracking page lives

Inputs needed to finalize:
- Bundle (3-month) Shopify variant ID
- Starter (1-month) Shopify variant ID
- Confirmation that `tryrestural.com` is the final Shopify domain

## Domain setup

1. **In Shopify:** add `tryrestural.com` as a domain, set as primary. Remove `restural.com` from Shopify entirely.
2. **In Funnelish:** add `restural.com` as the funnel's domain.
3. **In DNS provider:** point `restural.com` A/CNAME records at Funnelish's host. Funnelish auto-issues SSL.
4. **Email:** MX records stay put — only web records change.

## Facebook tracking (cross-domain)

Two separate apex domains means cookies don't cross. To make Facebook treat the journey as one user:

### Setup

| Property | Action |
|---|---|
| `restural.com` (Funnelish) | Install FB Pixel via Funnelish › Funnel Settings › Tracking Codes. Verify domain in Facebook Business Manager. |
| `tryrestural.com` (Shopify) | Install **same Pixel ID** via Shopify's Facebook & Instagram sales channel app. Enable native CAPI. Verify domain in Facebook Business Manager. |

### Click ID forwarding

When ads send users in, Facebook adds `?fbclid=XYZ` to the lander URL. Need to capture and forward it (plus `_fbp` and `_fbc` cookies) to the Shopify cart URL when the user clicks a CTA. ~15 lines of JS in head custom code on Funnelish:
- On page load: read `fbclid` from URL, persist to cookie/localStorage
- On CTA click: append `fbclid`, `_fbp`, `_fbc` as query params to outbound `tryrestural.com/cart/...` URLs

Resulting CTA URL looks like:
```
https://tryrestural.com/cart/{variant_id}:1?fbclid=...&_fbp=...&_fbc=...
```

### Aggregated Event Measurement

In Facebook Events Manager, configure AEM (8 priority events) on `tryrestural.com` since that's where Purchase fires. The lander only needs `PageView` (auto) and optionally `InitiateCheckout` on CTA click.

### Why CAPI is enough on Shopify only

The conversion event Facebook actually optimizes against is `Purchase`, which fires on Shopify with full server-side CAPI via the native channel app. The lander's job is just to log `PageView` and pass identity forward — client-side Pixel handles that fine. No need to add Funnelish CAPI infrastructure for v1.

### When to add a third-party tracker

Hyros / Cometly / AnyTrack solve cross-domain attribution at the identity-stitching level. Skip for launch. Consider once monthly ad spend is high enough that the attribution gap matters (~$5K+/month). Funnelish has documented integrations for all three.

## Suggested order of operations

1. Finalize the lander HTML (currently `no-lab.html`).
2. Generate Funnelish-ready HTML version (CTA placeholders replaced with real Shopify cart URLs, `fbclid` forwarding script injected, head-only content stripped out into a separate snippet).
3. Stand up Funnelish funnel + step + Custom HTML widget. Paste body HTML.
4. Paste head HTML (fonts, meta, Pixel) into Page Settings › Custom Codes › Head HTML.
5. Configure section/row/column to be full-width zero-padding.
6. Connect `restural.com` domain.
7. Verify both domains in Facebook Business Manager. Install Pixel + CAPI on Shopify.
8. End-to-end test: click ad URL with `?fbclid=test123` → land → click CTA → confirm Shopify cart loads with correct product → confirm Pixel fires on both sides.
9. Switch DNS for `restural.com` (Shopify off, Funnelish on).

## What I need from you when ready

To produce the Funnelish-ready HTML for paste:
- The finalized lander HTML file
- Bundle (3-month) Shopify variant ID
- Starter (1-month) Shopify variant ID
- FB Pixel ID
- Confirmation of the Shopify domain (`tryrestural.com` or different)

Output will be either one file (everything inline in the body) or two snippets (head + body) — your call when we get there.
