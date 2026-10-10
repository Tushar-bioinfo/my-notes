#!/usr/bin/env python3
"""
graph_index.py - Audit vault links, identify orphans/broken links, and refresh MOC indexes.

Usage:
    python scripts/graph_index.py [--refresh-mocs] [--audit]
"""

import sys
import re
from pathlib import Path
from collections import defaultdict

VAULT_ROOT = Path(__file__).resolve().parent.parent
VISUALS_DIR = VAULT_ROOT / "Visuals"
VISUALS_MOC = VISUALS_DIR / "Visuals MOC.md"


def get_graph():
    notes = {}
    out_links = defaultdict(set)
    in_links = defaultdict(set)

    for p in VAULT_ROOT.rglob("*.md"):
        if ".obsidian" in p.parts or "wiki/schema" in str(p):
            continue
        stem = p.stem
        notes[stem] = p
        content = p.read_text(encoding="utf-8", errors="replace")
        # Strip code blocks and inline code to avoid counting template examples as real links
        clean_content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
        clean_content = re.sub(r'`[^`\n]+`', '', clean_content)
        links = re.findall(r'\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]', clean_content)
        for link in links:
            target = link.strip()
            # If path like Folder/Note, extract base or handle relative
            target_stem = Path(target).stem
            out_links[stem].add(target_stem)
            in_links[target_stem].add(stem)

    return notes, out_links, in_links


def audit_vault():
    notes, out_links, in_links = get_graph()
    total_notes = len(notes)
    orphans = []
    broken_links = defaultdict(list)

    for stem, path in notes.items():
        if stem in ("Home", "README"):
            continue
        # An orphan has 0 in-links and 0 out-links, or no connection to any MOC
        has_moc_connection = any("MOC" in link for link in out_links[stem]) or any("MOC" in src for src in in_links[stem])
        if len(in_links[stem]) == 0 and len(out_links[stem]) == 0:
            orphans.append(stem)
        elif not has_moc_connection and not stem.endswith(" MOC"):
            orphans.append(stem)

        for target in out_links[stem]:
            if target not in notes and not (VAULT_ROOT / f"{target}.md").exists():
                broken_links[target].append(stem)

    print(f"📊 Vault Graph Status:")
    print(f"   Total Markdown Notes: {total_notes}")
    print(f"   Total Unique Connections: {sum(len(v) for v in out_links.values())}")
    print(f"   Potential Unconnected / Orphan Notes: {len(orphans)}")
    if orphans:
        print(f"   Unconnected: {', '.join(orphans[:8])}")
    print(f"   Broken / Unresolved Links: {len(broken_links)}")
    if broken_links:
        print(f"   Top Unresolved Targets: {', '.join(list(broken_links.keys())[:5])}")


def refresh_visuals_moc():
    if not VISUALS_DIR.exists():
        VISUALS_DIR.mkdir(parents=True, exist_ok=True)

    visual_notes = []
    for p in VISUALS_DIR.glob("*.md"):
        if p.stem == "Visuals MOC":
            continue
        visual_notes.append(p)

    print(f"Found {len(visual_notes)} visual notes in {VISUALS_DIR}")


def main():
    audit_vault()
    refresh_visuals_moc()


if __name__ == "__main__":
    main()
