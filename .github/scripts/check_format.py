#!/usr/bin/env python3
"""
check_format.py — Validates README.md table entries for the awesome-robot-vision list.

Checks enforced:
  1. Every content table row must have exactly 3 columns (Name | Highlights | References).
  2. The Name column must contain a Markdown link: [text](url).
  3. The Highlights column must not be empty.
  4. The References column must contain at least one Markdown link.

Exits with code 1 and prints all violations if any are found.
"""

import re
import sys
from pathlib import Path

README = Path(__file__).parent.parent.parent / "README.md"

# Matches a Markdown table row (starts and ends with |)
ROW_RE = re.compile(r"^\|(.+)\|$")
# Matches a separator row like |---|---|---|
SEPARATOR_RE = re.compile(r"^\|[\s\-:]+(\|[\s\-:]+)+\|$")
# Matches any Markdown link [text](url)
LINK_RE = re.compile(r"\[.+?\]\(.+?\)")

errors = []

lines = README.read_text(encoding="utf-8").splitlines()

# Detect which tables are 3-column content tables (skip header/separator rows)
in_content_table = False
header_cols = 0

for lineno, line in enumerate(lines, start=1):
    stripped = line.strip()

    if not ROW_RE.match(stripped):
        in_content_table = False
        header_cols = 0
        continue

    if SEPARATOR_RE.match(stripped):
        continue

    # Split row into columns (strip whitespace from each cell)
    cells = [c.strip() for c in stripped[1:-1].split("|")]

    # Detect header row — first row of a table
    if not in_content_table:
        header_cols = len(cells)
        in_content_table = True
        continue

    # Only validate 3-column tables (the content tables in this README)
    if header_cols != 3:
        continue

    name, highlights, references = cells[0], cells[1], cells[2]

    # Rule 1: Name column must have a link
    if not LINK_RE.search(name):
        errors.append(
            f"Line {lineno}: Name column has no Markdown link → {name!r}"
        )

    # Rule 2: Highlights column must not be empty
    if not highlights:
        errors.append(
            f"Line {lineno}: Highlights column is empty"
        )

    # Rule 3: References column must have at least one link
    if not LINK_RE.search(references):
        errors.append(
            f"Line {lineno}: References column has no links → {references!r}"
        )

if errors:
    print(f"❌  Found {len(errors)} format error(s) in README.md:\n")
    for e in errors:
        print(f"  • {e}")
    sys.exit(1)

print(f"✅  README.md format check passed ({len(lines)} lines checked).")
sys.exit(0)
