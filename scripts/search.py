#!/usr/bin/env python3
"""
search.py - Search notes, visuals, tags, and graph connections across the vault.

Usage:
    python scripts/search.py <query> [--tag <tag>] [--type visual|all]
"""

import sys
import re
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent


def parse_frontmatter(content: str):
    if not content.startswith("---"):
        return {}, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    raw_fm = parts[1]
    body = parts[2]
    meta = {}
    for line in raw_fm.strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            k = k.strip()
            v = v.strip()
            if v.startswith("[") and v.endswith("]"):
                meta[k] = [x.strip() for x in v[1:-1].split(",") if x.strip()]
            else:
                meta[k] = v
    return meta, body


def search_vault(query: str, tag_filter: str = None, visual_only: bool = False):
    results = []
    q_words = [w.lower() for w in query.lower().split() if w]

    for p in VAULT_ROOT.rglob("*.md"):
        if ".obsidian" in p.parts or "wiki/schema" in str(p):
            continue

        try:
            content = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        meta, body = parse_frontmatter(content)
        stem = p.stem

        if visual_only and meta.get("type") != "visual" and "Visuals" not in p.parts:
            continue

        if tag_filter:
            tags = meta.get("tags", [])
            if isinstance(tags, str):
                tags = [tags]
            if not any(tag_filter.lower() in t.lower() for t in tags):
                continue

        # Score matching
        text_lower = (stem + " " + content).lower()
        match_count = sum(text_lower.count(qw) for qw in q_words)
        stem_match = sum(stem.lower().count(qw) for qw in q_words)

        if match_count > 0:
            # Find links
            links = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)
            # Find a snippet
            snippet = ""
            for line in body.splitlines():
                line_clean = line.strip()
                if any(qw in line_clean.lower() for qw in q_words) and not line_clean.startswith("#"):
                    snippet = line_clean
                    break

            if not snippet and len(body.strip()) > 0:
                snippet = body.strip().splitlines()[0]

            score = match_count + (stem_match * 10)
            rel_path = str(p.relative_to(VAULT_ROOT))
            results.append({
                "title": stem,
                "path": rel_path,
                "score": score,
                "tags": meta.get("tags", []),
                "snippet": snippet[:140],
                "links": links[:5],
                "is_visual": meta.get("type") == "visual" or "Visuals" in p.parts
            })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)

    query = sys.argv[1]
    tag_filter = None
    visual_only = False

    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--tag" and i + 1 < len(sys.argv):
            tag_filter = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--visual" or (sys.argv[i] == "--type" and i + 1 < len(sys.argv) and sys.argv[i+1] == "visual"):
            visual_only = True
            i += 2 if sys.argv[i] == "--type" else 1
        else:
            i += 1

    hits = search_vault(query, tag_filter=tag_filter, visual_only=visual_only)
    if not hits:
        print(f"No matching notes found for '{query}'.")
        return

    print(f"\n🔍 Found {len(hits)} matching note(s) for '{query}':\n")
    for idx, hit in enumerate(hits[:10], 1):
        badge = "🎨 [VISUAL] " if hit["is_visual"] else "📄 "
        print(f"{idx}. {badge}{hit['title']} ({hit['path']})")
        if hit['snippet']:
            print(f"   Excerpt: {hit['snippet']}")
        if hit['links']:
            print(f"   Links: {', '.join(f'[[{l}]]' for l in hit['links'])}")
        print()


if __name__ == "__main__":
    main()
