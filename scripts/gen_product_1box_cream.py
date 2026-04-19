#!/usr/bin/env python3
"""
Render a single NeuroFuel box on the same cream background + lighting as
the 3-pack (nf_product_3pack.png), so the 1-month and 3-month pricing cards
read as a consistent tier system.
"""
import os, sys, shutil
from pathlib import Path
import requests
import fal_client
from dotenv import load_dotenv

ROOT = Path("/Users/jaymilne/A/Workspace/Client Work/Restural/Funnelish Build")
OUT_SRC = ROOT / "v2-images" / "product"
OUT_REPO = ROOT / "Restural Pages" / "v2-images" / "product"
REF_IMAGE = ROOT / "v2-images" / "product" / "nf_product_3pack.png"

for env_path in [Path("/Users/jaymilne/A/outreach-agent/.env"), Path("/Users/jaymilne/A/.env")]:
    if env_path.exists():
        load_dotenv(env_path)
        break

FAL_KEY = os.getenv("FAL_KEY")
if not FAL_KEY:
    print("ERROR: FAL_KEY not found"); sys.exit(1)
os.environ["FAL_KEY"] = FAL_KEY

PROMPT = (
    "Hero product photography of a SINGLE NeuroFuel box (the white box with the "
    "navy R logo and 'NeuroFuel' label), centered, on the same soft cream "
    "background as the reference image. Same camera angle, same soft lighting, "
    "same subtle shadow underneath, same scale-in-frame as one of the boxes in "
    "the reference trio. No additional props, no ingredients. Clean premium "
    "e-commerce hero shot. 1:1 square."
)


def main():
    print(f"Uploading reference: {REF_IMAGE}")
    ref_url = fal_client.upload_file(str(REF_IMAGE))
    print(f"  → {ref_url}")
    print("\nGenerating 1-box-on-cream ...")
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
    dest = OUT_SRC / "nf_product_1box_cream.png"
    r = requests.get(url, timeout=60); r.raise_for_status()
    dest.write_bytes(r.content)
    OUT_REPO.mkdir(parents=True, exist_ok=True)
    shutil.copy2(dest, OUT_REPO / "nf_product_1box_cream.png")
    print(f"saved: {dest}")


if __name__ == "__main__":
    main()
