#!/usr/bin/env python3
import os, json, sys, re
from pathlib import Path
from datetime import datetime, timedelta, date
from zoneinfo import ZoneInfo
from typing import List, Dict, Tuple

from google.oauth2 import service_account
from googleapiclient.discovery import build
from dateutil import parser as dateparser

SHEET_ID = os.environ["SHEET_ID"]
SHEET_NAME = os.environ.get("SHEET_NAME", "iCGWeeklyReads")
CONTENT_DIR = Path(os.environ.get("CONTENT_DIR", "content/posts/weekly"))
TIMEZONE = os.environ.get("TIMEZONE", "America/Los_Angeles")
WEEK_START_OVERRIDE = os.environ.get("WEEK_START_OVERRIDE", "").strip()

# NOTE: switched to read/write scope for post-publish updates
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

def get_creds():
  creds_json = os.environ.get("GOOGLE_CREDENTIALS")
  if not creds_json:
    print("ERROR: GOOGLE_CREDENTIALS not set", file=sys.stderr)
    sys.exit(1)
  info = json.loads(creds_json)
  return service_account.Credentials.from_service_account_info(info, scopes=SCOPES)

def monday_of(date_obj: date) -> date:
  return date_obj - timedelta(days=date_obj.weekday())

def parse_week_start(val: str) -> date | None:
  if not val:
    return None
  try:
    return dateparser.parse(val).date()
  except Exception:
    pass
  # Excel serial fallback
  if re.fullmatch(r"\d{5,}", val):
    base = date(1899, 12, 30)
    try:
      return base + timedelta(days=int(val))
    except Exception:
      return None
  return None

def truthy(val: str) -> bool:
  s = str(val).strip().lower()
  return s in ("true", "yes", "y", "1", "✓", "x", "checked")

def build_service(creds):
  return build("sheets", "v4", credentials=creds)

def fetch_rows(service) -> Tuple[List[List[str]], Dict[str, int]]:
  rng = f"{SHEET_NAME}!A:Z"
  resp = service.spreadsheets().values().get(spreadsheetId=SHEET_ID, range=rng).execute()
  values = resp.get("values", [])
  if not values or len(values) < 2:
    return [], {}
  headers = values[0]
  rows = values[1:]
  idx = {h: i for i, h in enumerate(headers)}
  required = ["WeekStart", "Title", "URL", "Summary", "Include"]
  for k in required:
    if k not in idx:
      print(f"ERROR: Missing required header: {k}", file=sys.stderr)
      sys.exit(1)
  return rows, idx

def get_target_monday() -> date:
  if WEEK_START_OVERRIDE:
    return monday_of(dateparser.parse(WEEK_START_OVERRIDE).date())
  today = datetime.now(ZoneInfo(TIMEZONE)).date()
  return monday_of(today)

def sanitize_text(s: str) -> str:
  return (s or "").replace("\r", "").strip()

def yaml_escape(s: str) -> str:
  return s.replace("\\", "\\\\").replace('"', '\\"')

def build_markdown(week_date: date, entries: List[Dict[str, str]], weekly_intro: str) -> str:
  readable_date = week_date.strftime("%B %-d, %Y")
  title = f"What I Read This Week — {readable_date}"

  fm = [
    "---",
    f'title: "{yaml_escape(title)}"',
    f"date: {week_date.isoformat()}",
    "draft: false",
    "tags: [weekly, roundup]",
    "---",
    "",
    "## Summary",
    weekly_intro.strip(),
    "",
  ]

  body_lines = []
  for e in entries:
    t = e["Title"]
    u = e["URL"]
    s = e["Summary"]
    tags = e.get("Tags", "")
    tagline = f"\n<sub>Tags: {tags}</sub>" if tags else ""
    body_lines.append(f"### [{t}]({u})")
    body_lines.append(s)
    if tagline:
      body_lines.append(tagline)
    body_lines.append("")

  return "\n".join(fm + body_lines).strip() + "\n"

def col_letter(n: int) -> str:
  # n is 0-based column index; returns A1 column letters
  s = ""
  n = int(n)
  while True:
    n, r = divmod(n, 26)
    s = chr(ord('A') + r) + s
    if n == 0:
      break
    n -= 1
  return s

def mark_as_published(service, idx: Dict[str, int], sheet_rows_to_update: List[int]):
  """
  sheet_rows_to_update: 1-based sheet row numbers (e.g., 2 for first data row).
  Sets Include=FALSE, Status=Published, PublishedAt=<timestamp> (if columns exist).
  """
  if not sheet_rows_to_update:
    return

  body_data = []
  include_col = idx.get("Include")
  status_col = idx.get("Status")
  published_at_col = idx.get("PublishedAt")

  now = datetime.now(ZoneInfo(TIMEZONE)).isoformat(timespec="seconds")

  if include_col is not None:
    col = col_letter(include_col)
    for r in sheet_rows_to_update:
      body_data.append({
        "range": f"{SHEET_NAME}!{col}{r}:{col}{r}",
        "values": [["FALSE"]],
      })

  if status_col is not None:
    col = col_letter(status_col)
    for r in sheet_rows_to_update:
      body_data.append({
        "range": f"{SHEET_NAME}!{col}{r}:{col}{r}",
        "values": [["Published"]],
      })

  if published_at_col is not None:
    col = col_letter(published_at_col)
    for r in sheet_rows_to_update:
      body_data.append({
        "range": f"{SHEET_NAME}!{col}{r}:{col}{r}",
        "values": [[now]],
      })

  if not body_data:
    print("Note: No write-back columns found (Include/Status/PublishedAt). Skipping updates.", file=sys.stderr)
    return

  service.spreadsheets().values().batchUpdate(
    spreadsheetId=SHEET_ID,
    body={
      "valueInputOption": "USER_ENTERED",
      "data": body_data
    }
  ).execute()
  print(f"Marked {len(sheet_rows_to_update)} rows as Published.", file=sys.stderr)

def main():
  creds = get_creds()
  service = build_service(creds)
  rows, idx = fetch_rows(service)
  target = get_target_monday()
  print(f"Target Monday: {target}", file=sys.stderr)

  selected: List[Dict[str, str]] = []
  weekly_intro = ""
  rows_to_update: List[int] = []  # 1-based sheet row numbers

  for i, r in enumerate(rows, start=2):  # start=2 because row 1 is header
    def col(name):
      j = idx.get(name)
      return sanitize_text(r[j]) if j is not None and j < len(r) else ""

    wk = parse_week_start(col("WeekStart"))
    if not wk or wk != target:
      continue
    if not truthy(col("Include")):
      continue
    summary = col("Summary")
    if not summary:
      continue
    title = col("Title")
    url = col("URL")
    tags = col("Tags")
    intro = col("WeeklyIntro")
    if not title or not url:
      continue

    selected.append({
      "Title": title,
      "URL": url,
      "Summary": summary,
      "Tags": tags
    })
    weekly_intro = intro or weekly_intro  # last row's intro wins
    rows_to_update.append(i)

  if not selected:
    print("No entries to publish for this week. Exiting.", file=sys.stderr)
    return

  out_dir = CONTENT_DIR / target.isoformat()
  out_dir.mkdir(parents=True, exist_ok=True)
  out_file = out_dir / "index.md"
  md = build_markdown(target, selected, weekly_intro)
  out_file.write_text(md, encoding="utf-8")
  print(f"Wrote {out_file}", file=sys.stderr)

  # Post-publish: mark rows as published (Include=FALSE, Status=Published, PublishedAt=timestamp)
  try:
    mark_as_published(service, idx, rows_to_update)
  except Exception as e:
    print(f"WARNING: Failed to mark rows as published: {e}", file=sys.stderr)

if __name__ == "__main__":
  main()
