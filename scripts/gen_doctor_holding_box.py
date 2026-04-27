#!/usr/bin/env python3
"""
Generate a portrait of Dr. Steven Jones holding the Restural NeuroFuel box,
to anchor the Belief section ("Your Brain Doesn't Need More Pills"). Uses two
reference images: the existing Dr. Jones email header for the face/likeness,
and nf_product_1box_cream.png for the actual product packaging the AI should
render in his hands.

No text, no overlays, no captions on the generated image.
"""
import os, sys, shutil
from pathlib import Path
import requests
import fal_client
from dotenv import load_dotenv

ROOT = Path("/Users/jaymilne/A/Workspace/Client Work/Restural/Funnelish Build")
OUT_SRC = ROOT / "v2-images" / "social"
OUT_REPO = ROOT / "Restural Pages" / "v2-images" / "social"
DR_REF = Path(
    "/Users/jaymilne/A/Workspace/Client Work/Restural/R Email Agent/"
    "brand_kit/generated_images/plain_text_header/dr_jones_email_header.png"
)
BOX_REF = ROOT / "v2-images" / "product" / "nf_product_1box_cream.png"

for env_path in [
    Path("/Users/jaymilne/A/Adgentiks/outreach-agent/.output"),
    Path("/Users/jaymilne/A/Adgentiks/outreach-agent/.env"),
    Path("/Users/jaymilne/A/.env"),
]:
    if env_path.exists():
        load_dotenv(env_path)
        break

FAL_KEY = os.getenv("FAL_KEY")
if not FAL_KEY:
    print("ERROR: FAL_KEY not found"); sys.exit(1)
os.environ["FAL_KEY"] = FAL_KEY

PROMPT = (
    "Professional editorial portrait of Dr. Steven Jones (the man in the first "
    "reference image — same face, same glasses, same beard, same warm trustworthy "
    "expression). He is holding the Restural NeuroFuel cream-and-navy product box "
    "from the second reference image in front of him at chest height with both "
    "hands, label facing the camera, box clearly readable. Waist-up, slight angle, "
    "warm natural studio light, wearing a clean white clinician coat over a soft "
    "blue collared shirt, looking directly at camera with a calm confident smile. "
    "Background: softly blurred warm neutral studio with cream and soft beige "
    "tones, no medical clutter. Shot on 85mm lens, shallow depth of field, sharp "
    "focus on face and box. ABSOLUTELY NO TEXT, NO LOGOS overlay, NO CAPTIONS, NO "
    "WATERMARKS, NO LETTERS — only the existing label printed on the product box "
    "is allowed. Editorial health-brand feel, premium magazine quality. Portrait "
    "orientation, 4:5 aspect ratio."
)


def main():
    print(f"Uploading Dr. Jones reference: {DR_REF}")
    dr_url = fal_client.upload_file(str(DR_REF))
    print(f"  → {dr_url}")
    print(f"Uploading product box reference: {BOX_REF}")
    box_url = fal_client.upload_file(str(BOX_REF))
    print(f"  → {box_url}")
    print("\nGenerating Dr. Jones holding the box ...")
    result = fal_client.subscribe(
        "fal-ai/nano-banana-pro/edit",
        arguments={
            "prompt": PROMPT,
            "image_urls": [dr_url, box_url],
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
    dest = OUT_SRC / "nf_founder_dr_jones_holding_box.png"
    r = requests.get(url, timeout=60); r.raise_for_status()
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(r.content)
    OUT_REPO.mkdir(parents=True, exist_ok=True)
    shutil.copy2(dest, OUT_REPO / "nf_founder_dr_jones_holding_box.png")
    print(f"saved: {dest}")


if __name__ == "__main__":
    main()
