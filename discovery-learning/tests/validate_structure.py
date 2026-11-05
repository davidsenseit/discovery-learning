#!/usr/bin/env python3
"""Validate the self-contained Agent Skill structure without dependencies."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
text = (root / "SKILL.md").read_text(encoding="utf-8")
assert text.startswith("---\n"), "Missing YAML frontmatter"
front = text.split("---", 2)[1]
name = re.search(r"^name:\s*(\S+)", front, re.M)
assert name and name.group(1) == root.name, "Skill name must match directory"
assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name.group(1))
desc = re.search(r"^description:\s*(.+)", front, re.M)
assert desc and 0 < len(desc.group(1)) <= 1024
assert re.search(r"^license:\s*Apache-2\.0\s*$", front, re.M)
links = re.findall(r"\]\((references/[^)]+|assets/[^)]+|tests/[^)]+)\)", text)
for link in links:
    assert (root / link).is_file(), f"Missing reference: {link}"
assert len(list(root.rglob("*.md"))) >= 8
print(f"Validated {len(links)} references")
