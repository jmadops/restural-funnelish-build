#!/usr/bin/env python3
"""
Generate 4 circular NeuroFuel Promise icons via fal.ai (Nano Banana Pro).
Restural-style: navy + gold on cream, cohesive vector feel, 1:1.
Saves into v2-images/decor/ (source) AND Restural Pages/v2-images/decor/ (repo).
"""
import os, sys, shutil, argparse
from pathlib import Path
import requests
import fal_client
from dotenv import load_dotenv

ROOT = Path("/Users/jaymilne/A/Workspace/Client Work/Restural/Funnelish Build")
OUT_SRC = ROOT / "v2-images" / "decor"
OUT_REPO = ROOT / "Restural Pages" / "v2-images" / "decor"

for env_path in [Path("/Users/jaymilne/A/Adgentiks/outreach-agent/.env"), Path("/Users/jaymilne/A/.env")]:
    if env_path.exists():
        load_dotenv(env_path)
        break

FAL_KEY = os.getenv("FAL_KEY")
if not FAL_KEY:
    print("ERROR: FAL_KEY not found"); sys.exit(1)
os.environ["FAL_KEY"] = FAL_KEY

STYLE = (
    "Circular badge/emblem composition on a soft cream background (#F5EFE4) "
    "with a subtle gold inner ring frame. Strict palette: deep navy (#0E1F5A) "
    "for the main shape, warm gold (#E0A832) for accents, muted sage as a "
    "secondary. Thin consistent line art with flat fill, editorial health-brand "
    "feel, Primal Queen quality, Restural brand tone. No text, no letters, "
    "no borders beyond the subtle gold ring. Centered, symmetrical, emblem-like. "
    "Square 1:1 aspect ratio."
)

PROMPTS = [
    ("clinical_natural",
     "A laboratory flask entwined with a single green leaf at its base, clean line-art, "
     "the flask in navy with a gold neckline and a single drop of gold inside. "
     "Represents clinically backed natural ingredients. " + STYLE),
    ("noninvasive",
     "A single gentle coffee mug silhouette in navy with soft rising steam lines in gold, "
     "symmetrical and calm, representing a non-invasive daily ritual. No needles, no pills. " + STYLE),
    ("pillfree",
     "A coffee mug in navy with a gold plus mark in the center replacing a classic pill bottle — "
     "a prescription pill bottle faintly outlined behind it being crossed out with a gold diagonal slash. " + STYLE),
    ("sideeffectfree",
     "A rounded shield emblem in navy with a bold gold checkmark at its center, "
     "small sparkle accents around it, symmetrical and protective feel. " + STYLE),
]


def download(url: str, dest: Path) -> None:
    r = requests.get(url, timeout=60); r.raise_for_status()
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(r.content)


def generate(slot: str, prompt: str) -> None:
    print(f"\n=== {slot} ===")
    result = fal_client.subscribe(
        "fal-ai/nano-banana-pro",
        arguments={
            "prompt": prompt,
            "aspect_ratio": "1:1",
            "num_images": 1,
            "output_format": "png",
        },
    )
    images = result.get("images") or []
    if not images:
        print(f"  FAIL no images: {result}"); return
    url = images[0]["url"]
    print(f"  → {url}")
    fname = f"nf_promise_{slot}.png"
    src = OUT_SRC / fname
    download(url, src)
    OUT_REPO.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, OUT_REPO / fname)
    print(f"  saved: {src}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="+")
    args = ap.parse_args()
    targets = PROMPTS if not args.only else [p for p in PROMPTS if p[0] in args.only]
    for slot, prompt in targets:
        generate(slot, prompt)
    print("\nDone.")


if __name__ == "__main__":
    main()
