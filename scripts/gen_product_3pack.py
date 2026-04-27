#!/usr/bin/env python3
"""
Generate a clean 3-pack NeuroFuel product render for the 3-month pricing card.
Uses fal nano-banana-pro/edit with the existing product catalog shot as a reference
so the packaging stays visually consistent with the 1-month card.
"""
import os, sys, shutil
from pathlib import Path
import requests
import fal_client
from dotenv import load_dotenv

ROOT = Path("/Users/jaymilne/A/Workspace/Client Work/Restural/Funnelish Build")
OUT_SRC = ROOT / "v2-images" / "product"
OUT_REPO = ROOT / "Restural Pages" / "v2-images" / "product"
REF_IMAGE = ROOT / "v2-images" / "product" / "nf_product_catalog.png"

for env_path in [Path("/Users/jaymilne/A/Adgentiks/outreach-agent/.env"), Path("/Users/jaymilne/A/.env")]:
    if env_path.exists():
        load_dotenv(env_path)
        break

FAL_KEY = os.getenv("FAL_KEY")
if not FAL_KEY:
    print("ERROR: FAL_KEY not found"); sys.exit(1)
os.environ["FAL_KEY"] = FAL_KEY

PROMPT = (
    "Hero product photography of THREE identical NeuroFuel boxes (the white box "
    "with the navy R logo and 'NeuroFuel' label) arranged in a clean trio — one "
    "in front, two slightly behind on either side — on a pure white seamless "
    "background with a soft shadow underneath. Same camera angle, same lighting, "
    "same box scale-in-frame as the reference 1-box shot. No additional props, "
    "no ingredients scattered around. Just the three boxes, clean, centered, "
    "premium e-commerce hero shot. Subtle cream gradient background. 1:1 square."
)


def upload_ref() -> str:
    print(f"Uploading reference: {REF_IMAGE}")
    url = fal_client.upload_file(str(REF_IMAGE))
    print(f"  → {url}")
    return url


def main():
    ref_url = upload_ref()
    print("\nGenerating 3-pack ...")
    result = fal_client.subscribe(
        "fal-ai/nano-banana-pro/edit",
        arguments={
            "prompt": PROMPT,
            "image_urls": [ref_url],
            "aspect_ratio": "1:1",
            "num_images": 1,
            "output_format": "png",
        },
    )
    images = result.get("images") or []
    if not images:
        print(f"FAIL: {result}"); sys.exit(1)
    url = images[0]["url"]
    print(f"  → {url}")
    dest = OUT_SRC / "nf_product_3pack.png"
    r = requests.get(url, timeout=60); r.raise_for_status()
    dest.write_bytes(r.content)
    OUT_REPO.mkdir(parents=True, exist_ok=True)
    shutil.copy2(dest, OUT_REPO / "nf_product_3pack.png")
    print(f"saved: {dest}")


if __name__ == "__main__":
    main()
