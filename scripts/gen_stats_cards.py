#!/usr/bin/env python3
"""
Generate 6 NeuroFuel stat-card illustrations via fal.ai (Nano Banana Pro, text-to-image).
Saves into v2-images/stats/ (source) AND Restural Pages/v2-images/stats/ (git repo).
"""
import os, sys, shutil, argparse
from pathlib import Path
import requests
import fal_client
from dotenv import load_dotenv

ROOT = Path("/Users/jaymilne/A/Workspace/Client Work/Restural/Funnelish Build")
OUT_SRC = ROOT / "v2-images" / "stats"
OUT_REPO = ROOT / "Restural Pages" / "v2-images" / "stats"

for env_path in [Path("/Users/jaymilne/A/outreach-agent/.env"), Path("/Users/jaymilne/A/.env")]:
    if env_path.exists():
        load_dotenv(env_path)
        break

FAL_KEY = os.getenv("FAL_KEY")
if not FAL_KEY:
    print("ERROR: FAL_KEY not found"); sys.exit(1)
os.environ["FAL_KEY"] = FAL_KEY

STYLE = (
    "Clean modern editorial illustration, thin line art with flat fill, "
    "palette strictly: deep navy (#0E1F5A), warm gold (#E0A832), soft cream "
    "(#F5EFE4), muted sage green. Centered composition on soft cream background "
    "with subtle radial glow. No text. No borders. No photoreal elements. "
    "Editorial health-brand aesthetic like Primal Queen, Restural tone. "
    "Square 1:1."
)

PROMPTS = [
    ("ngf", "Stylised human brain silhouette in deep navy viewed from the side, with thin gold neural pathways branching outward and upward from the cortex like growing tree roots. Small sparkle accents. " + STYLE),
    ("bbb", "Abstract cross-section of a protective cellular barrier membrane rendered as a stack of rounded capsule shapes in navy, with a single glowing gold droplet passing cleanly through the barrier leaving a trailing arrow. " + STYLE),
    ("bioav", "A minimalist human silhouette cross-section showing a gold droplet being absorbed into flowing navy bloodstream lines radiating outward. Clean diagrammatic feel. " + STYLE),
    ("adherence", "A simple 4x7 calendar grid in navy outline on cream, with 94 percent of cells filled with small gold checkmarks and a subtle glowing highlight across the filled week. " + STYLE),
    ("synergy", "A coffee bean and a lion's mane mushroom rendered as paired icons meeting at center, connected by a gold plus-sign that emits outward rays. Symmetrical, emblem-like composition. " + STYLE),
    ("clinical", "A hexagonal beta-glucan molecular structure in navy line-art, centered, with a small gold clinical-grade stamp badge overlapping the lower right. " + STYLE),
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
    fname = f"nf_stats_card_{slot}.png"
    src = OUT_SRC / fname
    download(url, src)
    OUT_REPO.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, OUT_REPO / fname)
    print(f"  saved: {src}\n         {OUT_REPO / fname}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="+", help="slot keys to generate (e.g. ngf bbb)")
    args = ap.parse_args()
    targets = PROMPTS if not args.only else [p for p in PROMPTS if p[0] in args.only]
    for slot, prompt in targets:
        generate(slot, prompt)
    print("\nDone.")


if __name__ == "__main__":
    main()
