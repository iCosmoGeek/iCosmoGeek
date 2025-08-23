#!/usr/bin/env python3
import os, sys, re, json
from pathlib import Path
import datetime as dt
import requests

CONTENT_DIR = Path(os.environ.get("CONTENT_DIR", "content/posts/weekly"))
SITE_BASE_URL = os.environ.get("SITE_BASE_URL", "").rstrip("/")

LINKEDIN_TOKEN = os.environ.get("LINKEDIN_TOKEN", "").strip()
LINKEDIN_OWNER = os.environ.get("LINKEDIN_OWNER", "").strip()  # e.g., urn:li:person:...
FB_PAGE_ID = os.environ.get("FB_PAGE_ID", "").strip()
FB_PAGE_TOKEN = os.environ.get("FB_PAGE_TOKEN", "").strip()

def latest_week_folder() -> Path:
    candidates = []
    if not CONTENT_DIR.exists():
        print(f"ERROR: {CONTENT_DIR} not found", file=sys.stderr)
        sys.exit(1)
    for p in CONTENT_DIR.iterdir():
        if p.is_dir() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", p.name):
            candidates.append(p)
    if not candidates:
        print("ERROR: No weekly folders found", file=sys.stderr)
        sys.exit(1)
    # Dates in ISO sort chronologically; pick max
    return sorted(candidates)[-1]

def parse_frontmatter_and_body(md: str):
    title = ""
    fm = {}
    body = md
    if md.startswith("---"):
        parts = md.split("\n---", 1)
        if len(parts) == 2:
            fm_block = parts[0].strip("-\n")
            body = parts[1].lstrip("-\n")
            for line in fm_block.splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip()] = v.strip().strip('"')
            title = fm.get("title", "")
    return title or fm.get("title", ""), body

def extract_summary_paragraph(body: str) -> str:
    lines = body.splitlines()
    summary_idx = None
    for i, line in enumerate(lines):
        if line.strip().lower() == "## summary":
            summary_idx = i
            break
    if summary_idx is None:
        return ""
    # Collect next non-empty paragraph until a blank line
    para = []
    for line in lines[summary_idx+1:]:
        if line.strip() == "":
            if para:
                break
            else:
                continue
        # stop if next heading
        if line.strip().startswith("#"):
            break
        para.append(line.rstrip())
    text = " ".join(para).strip()
    # Collapse spaces
    return re.sub(r"\s+", " ", text)

def first_sentence(text: str, max_len: int = 240) -> str:
    # Keep it concise for social
    s_match = re.split(r"(?<=[.!?])\s+", text)
    snippet = s_match[0] if s_match else text
    if len(snippet) <= max_len:
        return snippet
    # Trim gracefully
    t = snippet[:max_len].rsplit(" ", 1)[0].rstrip(",;:—-")
    return t + "…"

def build_post_text(title: str, summary: str, url: str) -> str:
    lead = first_sentence(summary, max_len=240)
    return f"{title}\n{lead}\nRead: {url}"

def post_linkedin(text: str, url: str):
    if not (LINKEDIN_TOKEN and LINKEDIN_OWNER):
        print("LinkedIn: missing token or owner; skipping.", file=sys.stderr)
        return
    # Use v2/shares (simpler than UGC). Requires w_member_social and owner URN.
    payload = {
        "owner": LINKEDIN_OWNER,
        "text": { "text": text },
        "content": {
            "contentEntities": [
                {"entityLocation": url}
            ],
            "title": text.split("\n", 1)[0]
        },
        "distribution": { "linkedInDistributionTarget": {} }
    }
    resp = requests.post(
        "https://api.linkedin.com/v2/shares",
        headers={
            "Authorization": f"Bearer {LINKEDIN_TOKEN}",
            "X-Restli-Protocol-Version": "2.0.0",
            "Content-Type": "application/json"
        },
        data=json.dumps(payload),
        timeout=20
    )
    if resp.status_code >= 400:
        print(f"LinkedIn error {resp.status_code}: {resp.text}", file=sys.stderr)
    else:
        print("LinkedIn: posted.")

def post_facebook(text: str, url: str):
    if not (FB_PAGE_ID and FB_PAGE_TOKEN):
        print("Facebook: missing page id/token; skipping.", file=sys.stderr)
        return
    api = f"https://graph.facebook.com/v19.0/{FB_PAGE_ID}/feed"
    resp = requests.post(api, data={
        "message": text,
        "link": url,
        "access_token": FB_PAGE_TOKEN
    }, timeout=20)
    if resp.status_code >= 400:
        print(f"Facebook error {resp.status_code}: {resp.text}", file=sys.stderr)
    else:
        print("Facebook: posted.")

def main():
    folder = latest_week_folder()
    md_path = folder / "index.md"
    if not md_path.exists():
        print(f"ERROR: {md_path} not found", file=sys.stderr)
        sys.exit(1)
    md = md_path.read_text(encoding="utf-8")
    title, body = parse_frontmatter_and_body(md)
    week_slug = folder.name
    if not SITE_BASE_URL:
        print("ERROR: SITE_BASE_URL not set", file=sys.stderr)
        sys.exit(1)
    url = f"{SITE_BASE_URL}/posts/weekly/{week_slug}/"
    summary = extract_summary_paragraph(body)
    text = build_post_text(title or f"What I Read This Week — {week_slug}", summary or "", url)

    print("Prepared social post:\n", text, "\n")

    # Post per platform (skip if secrets not present)
    post_linkedin(text, url)
    post_facebook(text, url)

if __name__ == "__main__":
    main()
