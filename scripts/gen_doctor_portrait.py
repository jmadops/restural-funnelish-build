#!/usr/bin/env python3
"""
Generate a tall 4:5 portrait of Dr. Steven Jones for the "Why We Built It"
founder section. Uses the existing dr_jones_email_header.png as a photo
reference so the face stays consistent across surfaces.
"""
import os, sys, shutil
from pathlib import Path
import requests
import fal_client
from dotenv import load_dotenv

ROOT = Path("/Users/jaymilne/A/Workspace/Client Work/Restural/Funnelish Build")
OUT_SRC = ROOT / "v2-images" / "social"
OUT_REPO = ROOT / "Restural Pages" / "v2-images" / "social"
REF_IMAGE = Path("/Users/jaymilne/A/Workspace/Client Work/Restural/R Email Agent/brand_kit/generated_images/plain_text_header/dr_jones_email_header.png")

for env_path in [Path("/Users/jaymilne/A/Adgentiks/outreach-agent/.output"), Path("/Users/jaymilne/A/Adgentiks/outreach-agent/.env"), Path("/Users/jaymilne/A/.env")]:
    if env_path.exists():
        load_dotenv(env_path)
        break

FAL_KEY = os.getenv("FAL_KEY")
if not FAL_KEY:
    print("ERROR: FAL_KEY not found"); sys.exit(1)
os.environ["FAL_KEY"] = FAL_KEY

PROMPT = (
    "Professional editorial portrait of Dr. Steven Jones (the man on the right "
    "side of the reference banner) — same face, same glasses, same beard. "
    "Waist-up portrait, slight angle, warm natural light, wearing a clean white "
    "clinician coat over a casual soft blue shirt, looking thoughtfully at "
    "camera with a calm, trustworthy expression. Background: softly blurred "
    "warm neutral studio or home office (not medical facility), cream and soft "
    "gold tones. Shot on 85mm lens, shallow depth of field. No text, no logos, "
    "no overlays, no letters. Editorial health-brand feel. "
    "Portrait orientation, 4:5 aspect ratio."
)


def main():
    print(f"Uploading reference: {REF_IMAGE}")
    ref_url = fal_client.upload_file(str(REF_IMAGE))
    print(f"  → {ref_url}")
    print("\nGenerating Dr. Jones portrait ...")
    result = fal_client.subscribe(
        "fal-ai/nano-banana-pro/edit",
        arguments={
            "prompt": PROMPT,
            "image_urls": [ref_url],
            "aspect_ratio": "4:5",
            "num_images": 1,
            "output_format": "png",
        },
    )
    images = result.get("images") or []
    if not images:
        print(f"FAIL: {result}"); sys.exit(1)
    url = images[0]["url"]
    print(f"  → {url}")
    dest = OUT_SRC / "nf_founder_dr_jones.png"
    r = requests.get(url, timeout=60); r.raise_for_status()
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(r.content)
    OUT_REPO.mkdir(parents=True, exist_ok=True)
    shutil.copy2(dest, OUT_REPO / "nf_founder_dr_jones.png")
    print(f"saved: {dest}")


if __name__ == "__main__":
    main()
