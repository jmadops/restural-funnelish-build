#!/usr/bin/env python3
"""
Upload local image files to the Restural Shopify store's Files library via the
Admin GraphQL API, then return the resulting cdn.shopify.com URLs.

Flow:
  1. stagedUploadsCreate     — request an S3 staged-upload target per file
  2. POST file binary        — push the raw bytes to Shopify's staging bucket
  3. fileCreate              — register each staged upload as a File (async)
  4. Poll node(id: ...)       — wait until fileStatus == READY, grab preview URL

Credentials pulled from:
  /Users/jaymilne/A/Workspace/Client Work/Restural/Restural Custom Liquid Agent/.env
  (SHOPIFY_STORE + SHOPIFY_ACCESS_TOKEN)

Usage:
  python scripts/upload_to_shopify.py <path1> <path2> ...
  python scripts/upload_to_shopify.py v2-images/social/nf_review_avatar_*.png

Prints a JSON manifest { filename: cdn_url } to stdout + writes it to
scripts/.shopify_upload_manifest.json for consumers to read.
"""
from __future__ import annotations

import json
import mimetypes
import os
import sys
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

ENV_FILE = Path(
    "/Users/jaymilne/A/Workspace/Client Work/Restural/Restural Custom Liquid Agent/.env"
)
load_dotenv(ENV_FILE)

STORE = os.getenv("SHOPIFY_STORE")
TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")
if not STORE or not TOKEN:
    print("ERROR: SHOPIFY_STORE / SHOPIFY_ACCESS_TOKEN missing", file=sys.stderr)
    sys.exit(1)

API_VERSION = "2024-10"
GRAPHQL_URL = f"https://{STORE}/admin/api/{API_VERSION}/graphql.json"
HEADERS = {"X-Shopify-Access-Token": TOKEN, "Content-Type": "application/json"}

MANIFEST_PATH = Path(__file__).parent / ".shopify_upload_manifest.json"


def gql(query: str, variables: dict | None = None) -> dict:
    resp = requests.post(
        GRAPHQL_URL,
        headers=HEADERS,
        json={"query": query, "variables": variables or {}},
        timeout=60,
    )
    resp.raise_for_status()
    payload = resp.json()
    if "errors" in payload:
        raise RuntimeError(f"GraphQL errors: {payload['errors']}")
    data = payload.get("data") or {}
    # Surface user errors embedded in any top-level mutation result
    for node in data.values():
        if isinstance(node, dict):
            errs = node.get("userErrors") or []
            if errs:
                raise RuntimeError(f"userErrors: {errs}")
    return data


STAGED_UPLOADS_CREATE = """
mutation stagedUploadsCreate($input: [StagedUploadInput!]!) {
  stagedUploadsCreate(input: $input) {
    stagedTargets {
      url
      resourceUrl
      parameters { name value }
    }
    userErrors { field message }
  }
}
"""

FILE_CREATE = """
mutation fileCreate($files: [FileCreateInput!]!) {
  fileCreate(files: $files) {
    files {
      id
      fileStatus
      alt
      ... on MediaImage {
        image { url }
      }
      ... on GenericFile { url }
    }
    userErrors { field message }
  }
}
"""

NODE_QUERY = """
query node($id: ID!) {
  node(id: $id) {
    ... on MediaImage {
      id fileStatus
      image { url }
    }
    ... on GenericFile {
      id fileStatus url
    }
  }
}
"""


def stage_upload(path: Path) -> dict:
    mime = mimetypes.guess_type(path.name)[0] or "image/png"
    variables = {
        "input": [
            {
                "resource": "FILE",
                "filename": path.name,
                "mimeType": mime,
                "httpMethod": "POST",
                "fileSize": str(path.stat().st_size),
            }
        ]
    }
    data = gql(STAGED_UPLOADS_CREATE, variables)
    targets = data["stagedUploadsCreate"]["stagedTargets"]
    if not targets:
        raise RuntimeError("stagedUploadsCreate returned no targets")
    return targets[0]


def post_to_staging(target: dict, path: Path) -> None:
    form = {p["name"]: p["value"] for p in target["parameters"]}
    with path.open("rb") as fh:
        files = {"file": (path.name, fh, mimetypes.guess_type(path.name)[0] or "image/png")}
        resp = requests.post(target["url"], data=form, files=files, timeout=300)
    if resp.status_code not in (200, 201, 204):
        raise RuntimeError(f"Staged upload failed {resp.status_code}: {resp.text[:400]}")


def register_file(resource_url: str, filename: str) -> str:
    variables = {
        "files": [
            {
                "alt": filename,
                "contentType": "IMAGE",
                "originalSource": resource_url,
            }
        ]
    }
    data = gql(FILE_CREATE, variables)
    files = data["fileCreate"]["files"]
    if not files:
        raise RuntimeError(f"fileCreate returned no files for {filename}")
    return files[0]["id"]


def poll_for_url(file_id: str, timeout: int = 120) -> str:
    start = time.time()
    while time.time() - start < timeout:
        data = gql(NODE_QUERY, {"id": file_id})
        node = data.get("node") or {}
        status = node.get("fileStatus")
        if status == "READY":
            image = node.get("image") or {}
            url = image.get("url") or node.get("url")
            if url:
                return url
            raise RuntimeError(f"File {file_id} READY but no url in payload: {node}")
        if status == "FAILED":
            raise RuntimeError(f"File {file_id} FAILED: {node}")
        time.sleep(2)
    raise TimeoutError(f"File {file_id} did not reach READY within {timeout}s")


def upload_one(path: Path) -> str:
    print(f"[{path.name}]", flush=True)
    target = stage_upload(path)
    print(f"  staged: {target['resourceUrl'][:80]}...", flush=True)
    post_to_staging(target, path)
    print(f"  posted to staging", flush=True)
    file_id = register_file(target["resourceUrl"], path.name)
    print(f"  registered: {file_id}", flush=True)
    cdn_url = poll_for_url(file_id)
    print(f"  cdn: {cdn_url}", flush=True)
    return cdn_url


def main():
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        sys.exit(1)

    paths = [Path(p) for p in sys.argv[1:]]
    for p in paths:
        if not p.exists():
            print(f"ERROR: {p} does not exist", file=sys.stderr)
            sys.exit(1)

    manifest: dict[str, str] = {}
    if MANIFEST_PATH.exists():
        try:
            manifest = json.loads(MANIFEST_PATH.read_text())
        except Exception:
            manifest = {}

    for path in paths:
        url = upload_one(path)
        manifest[path.name] = url
        MANIFEST_PATH.write_text(json.dumps(manifest, indent=2))

    print("\n=== Manifest ===", flush=True)
    print(json.dumps(manifest, indent=2), flush=True)


if __name__ == "__main__":
    main()
