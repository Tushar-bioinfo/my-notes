#!/usr/bin/env python3
"""
ingest.py - Ingest HTML files, web pages, or notes into the Obsidian knowledge graph.

Usage:
    python scripts/ingest.py <path_or_url> [--domain <domain>] [--title <title>] [--tags <tag1,tag2>] [--move]
"""

import sys
import os
import re
import shutil
import urllib.request
import urllib.parse
from html.parser import HTMLParser
from pathlib import Path
from datetime import date

VAULT_ROOT = Path(__file__).resolve().parent.parent
VISUALS_DIR = VAULT_ROOT / "Visuals"
HTML_DIR = VISUALS_DIR / "html"
VISUALS_MOC = VISUALS_DIR / "Visuals MOC.md"
HOME_MD = VAULT_ROOT / "Home.md"

DOMAIN_MOCS = {
    "Cancer Biology": VAULT_ROOT / "Biology" / "Cancer Biology" / "Cancer Biology MOC.md",
    "Digital Pathology": VAULT_ROOT / "Biology" / "Digital Pathology" / "Digital Pathology MOC.md",
    "Biology": VAULT_ROOT / "Biology" / "Biology MOC.md",
    "Machine Learning": VAULT_ROOT / "ML" / "ML MOC.md",
    "Deep Learning": VAULT_ROOT / "DL" / "DL MOC.md",
    "Mathematics": VAULT_ROOT / "Maths" / "Maths MOC.md",
    "Statistics": VAULT_ROOT / "Stats" / "Stats MOC.md",
    "Projects": VAULT_ROOT / "Projects" / "Projects MOC.md",
}

DOMAIN_KEYWORDS = {
    "Cancer Biology": [
        "cancer", "tumor", "tumour", "hallmarks", "oncogene", "suppressor", "microenvironment",
        "tme", "angiogenesis", "metastasis", "apoptosis", "necrosis", "hypoxia", "stroma",
        "carcinoma", "immunotherapy", "chemotherapy", "tp53", "kras", "egfr", "her2"
    ],
    "Digital Pathology": [
        "pathology", "h&e", "histology", "histopathology", "wsi", "whole slide", "stain",
        "hematoxylin", "eosin", "tissue", "slide", "biopsy", "morphology", "nuclei",
        "cellbound", "patch", "tile"
    ],
    "Biology": [
        "crispr", "cas9", "grna", "knockout", "guide rna", "gene", "genes", "dna", "rna",
        "cpm", "counts to log-cpm", "library size", "sequencing", "transcription", "translation",
        "mutation", "central dogma", "cell", "cells", "metabolism", "metabolic"
    ],
    "Deep Learning": [
        "neural network", "transformer", "cnn", "attention", "vit", "resnet", "backpropagation",
        "loss function", "gradient descent", "embedding", "latent space", "diffusion", "weights",
        "deep learning", "pytorch", "gpu", "softmax", "cross-entropy", "kl divergence",
        "notation", "layers", "layer", "activation"
    ],
    "Machine Learning": [
        "machine learning", "random forest", "svm", "clustering", "pca", "kmeans", "supervised",
        "unsupervised", "regression", "classification", "overfitting", "regularization",
        "cross-validation", "feature engineering"
    ],
    "Statistics": [
        "p-value", "fdr", "false discovery", "hypothesis testing", "distribution", "normal distribution",
        "bayesian", "variance", "standard deviation", "correlation", "t-test", "anova", "bootstrap",
        "confidence interval", "likelihood", "prior", "posterior", "benjamini", "hochberg",
        "bonferroni", "multiple testing", "fwer", "log-counts", "heteroscedasticity", "sample mean",
        "standard error"
    ],
    "Mathematics": [
        "matrix", "eigenvalue", "vector", "linear algebra", "calculus", "differential",
        "manifold", "topology", "optimization", "convex", "geometry"
    ]
}


class HTMLContentExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False
        self.in_h1 = False
        self.h1_texts = []
        self.in_script_or_style = False
        self.text_chunks = []
        self.meta_desc = ""

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag in ("script", "style", "noscript"):
            self.in_script_or_style = True
        elif tag == "title":
            self.in_title = True
        elif tag == "h1":
            self.in_h1 = True
        elif tag == "meta":
            attrs_dict = dict((k.lower(), v) for k, v in attrs if k and v)
            if attrs_dict.get("name", "").lower() in ("description", "og:description"):
                self.meta_desc = attrs_dict.get("content", "")

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in ("script", "style", "noscript"):
            self.in_script_or_style = False
        elif tag == "title":
            self.in_title = False
        elif tag == "h1":
            self.in_h1 = False

    def handle_data(self, data):
        if self.in_script_or_style:
            return
        if self.in_title:
            self.title += data.strip() + " "
        elif self.in_h1:
            self.h1_texts.append(data.strip())
        text = data.strip()
        if text:
            self.text_chunks.append(text)


def extract_proff_metadata(html_raw: str):
    """Extract metadata from Proff visual framework in HTML."""
    meta = {
        "title": "",
        "sub": "",
        "eyebrow": "",
        "scenes": [],
        "chunks": []
    }
    pages = re.findall(r"Proff\.page\s*\(\s*\{([^}]+)\}\s*\)", html_raw, re.DOTALL)
    for p in pages:
        tm = re.search(r"title\s*:\s*['\"]([^'\"]+)['\"]", p)
        if tm and not meta["title"]:
            meta["title"] = tm.group(1).strip()
        sm = re.search(r"sub\s*:\s*['\"]([^'\"]+)['\"]", p)
        if sm and not meta["sub"]:
            meta["sub"] = sm.group(1).strip()
        em = re.search(r"eyebrow\s*:\s*['\"]([^'\"]+)['\"]", p)
        if em and not meta["eyebrow"]:
            meta["eyebrow"] = em.group(1).strip()

    scene_matches = re.findall(r"title\s*:\s*['\"]([^'\"]{3,100})['\"]", html_raw)
    for s in scene_matches:
        s_clean = s.strip()
        if s_clean not in ("dark", "neon", "lab", "article", meta["title"]) and s_clean not in meta["scenes"]:
            meta["scenes"].append(s_clean)

    calls = re.findall(r"Proff\.(?:section|prose|fact|qna|deck|card|step|tiles|compare)\s*\((.*?)\)", html_raw, re.DOTALL)
    for c in calls:
        strs = re.findall(r"['\"]([^'\"]{8,250})['\"]", c)
        for s in strs:
            s_clean = re.sub(r"<[^>]+>", " ", s).replace("**", "").replace("*", "").strip()
            if s_clean and not any(kw in s_clean for kw in ["var(--", "function", "return", "document.", "window."]):
                meta["chunks"].append(s_clean)

    return meta


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    return text.strip('-') or "visual-page"


def clean_title(title: str) -> str:
    title = re.sub(r'\s+', ' ', title).strip()
    # Remove common site suffixes like " | GitHub", " - Wikipedia", etc.
    title = re.split(r'\s+[|\-–—]\s+', title)[0].strip()
    return title


def get_all_vault_notes():
    notes = {}
    for p in VAULT_ROOT.rglob("*.md"):
        if ".obsidian" in p.parts or "wiki/schema" in str(p):
            continue
        stem = p.stem
        if stem.endswith(" MOC") or stem in ("Home", "README"):
            continue
        notes[stem] = p
    return notes


def find_related_notes(text: str, vault_notes: dict, max_links=5):
    text_lower = text.lower()
    matches = []
    for note_name in vault_notes:
        if len(note_name) < 4 or note_name.lower() in ("test", "todo", "draft", "scratch", "readme", "config"):
            continue
        note_lower = note_name.lower()
        # Look for whole word or phrase match
        pattern = r'\b' + re.escape(note_lower) + r'\b'
        count = len(re.findall(pattern, text_lower))
        if count > 0:
            matches.append((note_name, count))

    matches.sort(key=lambda x: x[1], reverse=True)
    return [name for name, _ in matches[:max_links]]


def detect_domain(text: str, default="Biology"):
    text_lower = text.lower()
    scores = {}
    for domain, kws in DOMAIN_KEYWORDS.items():
        score = sum(text_lower.count(kw) for kw in kws)
        scores[domain] = score

    best_domain = max(scores, key=scores.get)
    if scores[best_domain] > 0:
        return best_domain
    return default


def ensure_dirs():
    HTML_DIR.mkdir(parents=True, exist_ok=True)
    if not VISUALS_MOC.exists():
        create_visuals_moc()


def create_visuals_moc():
    content = """---
tags:
  - moc
  - visuals
date: {date_str}
status: permanent
---
# Visuals MOC

> [!abstract] Map of Content for all visual explanations, interactive models, HTML simulations, and `proff-viz` artifacts.

## Overview
This hub tracks interactive visualizations and visual reference pages across all scientific and quantitative domains. Every visual has a companion note linking it directly into the Obsidian knowledge graph.

## 🧬 Biology & Digital Pathology Visuals


## 🤖 Machine Learning & Deep Learning Visuals


## 📐 Mathematics & Statistics Visuals


## 🌐 General & Web Visuals


## Ingestion Flow
To add an HTML file, run:
```bash
python scripts/ingest.py path/to/file.html
```
or tell any agent: *"Ingest this HTML file / page."*

## Cross-Topic Bridges
- [[Home]]
- [[Biology MOC]]
- [[Digital Pathology MOC]]
- [[Cancer Biology MOC]]
- [[ML MOC]]
- [[DL MOC]]
- [[Stats MOC]]
""".format(date_str=date.today().isoformat())
    VISUALS_MOC.write_text(content, encoding="utf-8")


def add_to_visuals_moc(note_name: str, domain: str, summary: str = ""):
    if not VISUALS_MOC.exists():
        create_visuals_moc()

    content = VISUALS_MOC.read_text(encoding="utf-8")
    link_line = f"- [[{note_name}]]"
    if summary:
        link_line += f" — *{summary[:90].strip()}...*"

    if f"[[{note_name}]]" in content:
        return  # already present

    target_section = "## 🌐 General & Web Visuals"
    if domain in ("Cancer Biology", "Digital Pathology", "Biology"):
        target_section = "## 🧬 Biology & Digital Pathology Visuals"
    elif domain in ("Machine Learning", "Deep Learning"):
        target_section = "## 🤖 Machine Learning & Deep Learning Visuals"
    elif domain in ("Mathematics", "Statistics"):
        target_section = "## 📐 Mathematics & Statistics Visuals"

    pattern = re.escape(target_section) + r"\n+"
    replacement = f"{target_section}\n\n{link_line}\n"
    new_content = re.sub(pattern, replacement, content, count=1)
    if new_content == content:
        # Fallback append before Ingestion Flow
        new_content = content.replace("## Ingestion Flow", f"{link_line}\n\n## Ingestion Flow")

    VISUALS_MOC.write_text(new_content, encoding="utf-8")


def add_to_domain_moc(note_name: str, domain: str):
    moc_path = DOMAIN_MOCS.get(domain)
    if not moc_path or not moc_path.exists():
        return

    content = moc_path.read_text(encoding="utf-8")
    if f"[[{note_name}]]" in content:
        return

    link_line = f"- [[{note_name}]] *(Interactive Visual)*"
    if "## Visuals & Walkthroughs" in content:
        pattern = r"(## Visuals & Walkthroughs\n+)"
        new_content = re.sub(pattern, rf"\1{link_line}\n", content, count=1)
        moc_path.write_text(new_content, encoding="utf-8")
        return

    # Find a good place to insert, e.g. before Bridges or Reference Materials
    for marker in ("## Bridges", "## Reference Materials", "## Cross-Topic Bridges"):
        if marker in content:
            new_content = content.replace(marker, f"## Visuals & Walkthroughs\n\n{link_line}\n\n{marker}")
            moc_path.write_text(new_content, encoding="utf-8")
            return

    # If no marker found, append to end
    new_content = content.rstrip() + f"\n\n## Visuals & Walkthroughs\n\n{link_line}\n"
    moc_path.write_text(new_content, encoding="utf-8")


def ingest_html(source: str, domain: str = None, title: str = None, tags: list = None, move: bool = False):
    ensure_dirs()
    today_str = date.today().isoformat()

    is_url = source.startswith("http://") or source.startswith("https://")
    html_raw = ""
    orig_name = ""

    if is_url:
        req = urllib.request.Request(source, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as resp:
            html_raw = resp.read().decode("utf-8", errors="replace")
        orig_name = urllib.parse.urlparse(source).path.split("/")[-1] or "page.html"
    else:
        src_path = Path(source).resolve()
        if not src_path.exists():
            raise FileNotFoundError(f"Source file not found: {source}")
        html_raw = src_path.read_text(encoding="utf-8", errors="replace")
        orig_name = src_path.name

    extractor = HTMLContentExtractor()
    extractor.feed(html_raw)

    proff_meta = extract_proff_metadata(html_raw)

    extracted_title = clean_title(title or proff_meta["title"] or extractor.title or (extractor.h1_texts[0] if extractor.h1_texts else Path(orig_name).stem))
    if not extracted_title:
        extracted_title = "Interactive Visual"

    all_chunks = extractor.text_chunks + proff_meta["chunks"] + proff_meta["scenes"]
    if proff_meta["sub"]:
        all_chunks.insert(0, proff_meta["sub"])
    full_text = " ".join(all_chunks)

    summary = ""
    if extractor.meta_desc:
        summary = extractor.meta_desc
    elif proff_meta["sub"]:
        summary = proff_meta["sub"]
        if proff_meta["scenes"]:
            summary += f". Key stages: {', '.join(proff_meta['scenes'][:4])}."
    elif extractor.text_chunks:
        summary = " ".join(extractor.text_chunks[:4])
    elif proff_meta["scenes"]:
        summary = f"Interactive visual exploring: {', '.join(proff_meta['scenes'][:4])}."
    else:
        summary = "Interactive visual artifact."
    summary = re.sub(r'\s+', ' ', summary).strip()
    if len(summary) > 300:
        summary = summary[:297] + "..."

    detected_domain = domain or detect_domain(extracted_title + " " + full_text)
    slug = slugify(extracted_title)
    dest_html_file = HTML_DIR / f"{slug}.html"

    # Avoid overwriting different files with identical names
    counter = 1
    while dest_html_file.exists() and not is_url and dest_html_file.resolve() != Path(source).resolve():
        dest_html_file = HTML_DIR / f"{slug}-{counter}.html"
        counter += 1

    if is_url:
        dest_html_file.write_text(html_raw, encoding="utf-8")
    else:
        src_path = Path(source).resolve()
        if move:
            shutil.move(src_path, dest_html_file)
        else:
            shutil.copy2(src_path, dest_html_file)

    vault_notes = get_all_vault_notes()
    related_notes = find_related_notes(extracted_title + " " + full_text, vault_notes)

    tag_list = ["visual", "interactive", slugify(detected_domain)]
    if tags:
        tag_list.extend([slugify(t) for t in tags])
    tag_list = list(dict.fromkeys(tag_list))  # deduplicate preserving order

    companion_note_name = f"{extracted_title} - Visual"
    companion_path = VISUALS_DIR / f"{companion_note_name}.md"

    # Relative path from Visuals/ note to Visuals/html/ file is "html/<filename>"
    rel_html_path = f"html/{dest_html_file.name}"

    related_links_md = ""
    for note in related_notes:
        related_links_md += f"- [[{note}]]\n"
    if detected_domain in DOMAIN_MOCS:
        moc_stem = DOMAIN_MOCS[detected_domain].stem
        related_links_md += f"- [[{moc_stem}]]\n"
    related_links_md += "- [[Visuals MOC]]\n"

    frontmatter_tags = "\n".join(f"  - {t}" for t in tag_list)

    note_content = f"""---
tags:
{frontmatter_tags}
aliases:
  - {extracted_title}
date: {today_str}
status: permanent
type: visual
source: "{source}"
---
# {extracted_title}

> [!abstract] Summary
> {summary}

---

## Interactive Visual

> [!TIP] Preview
> You can interact with this visualization below, or [open it standalone in a new tab]({rel_html_path}).

<iframe src="{rel_html_path}" width="100%" height="750px" style="border: 1px solid #e0e0e0; border-radius: 8px;"></iframe>

---

## Key Takeaways

- **Topic Area**: {detected_domain}
- **Interactive File**: `Visuals/{rel_html_path}`
- **Source Origin**: `{source}`

---

## Related Notes

{related_links_md}
"""

    companion_path.write_text(note_content, encoding="utf-8")
    add_to_visuals_moc(companion_note_name, detected_domain, summary)
    add_to_domain_moc(companion_note_name, detected_domain)

    # Ensure Home.md links to Visuals MOC
    if HOME_MD.exists():
        home_text = HOME_MD.read_text(encoding="utf-8")
        if "[[Visuals MOC]]" not in home_text:
            home_text = home_text.replace("- [[Inbox/test|Inbox]]", "- [[Visuals MOC]]\n- [[Inbox/test|Inbox]]")
            HOME_MD.write_text(home_text, encoding="utf-8")

    return {
        "title": extracted_title,
        "html_file": str(dest_html_file),
        "note_file": str(companion_path),
        "domain": detected_domain,
        "related": related_notes
    }


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)

    source = sys.argv[1]
    domain = None
    title = None
    tags = []
    move = False

    i = 2
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == "--domain" and i + 1 < len(sys.argv):
            domain = sys.argv[i + 1]
            i += 2
        elif arg == "--title" and i + 1 < len(sys.argv):
            title = sys.argv[i + 1]
            i += 2
        elif arg == "--tags" and i + 1 < len(sys.argv):
            tags = [t.strip() for t in sys.argv[i + 1].split(",")]
            i += 2
        elif arg == "--move":
            move = True
            i += 1
        else:
            i += 1

    try:
        res = ingest_html(source, domain=domain, title=title, tags=tags, move=move)
        print(f"✅ Ingested successfully!")
        print(f"Title: {res['title']}")
        print(f"Domain: {res['domain']}")
        print(f"HTML File: {res['html_file']}")
        print(f"Companion Note: {res['note_file']}")
        print(f"Connected to {len(res['related'])} related notes: {', '.join(res['related']) or 'None'}")
    except Exception as e:
        print(f"❌ Error during ingestion: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
