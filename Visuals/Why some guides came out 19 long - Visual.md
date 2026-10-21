---
tags:
  - visual
  - interactive
  - biology
  - crispr
  - sgrna
  - cutadapt
  - fastq
  - bwa
  - functional-genomics
aliases:
  - Why some guides came out 19 long
  - crispr-v2
  - CRISPR 19-mer Guide Walk
  - Adapter Cut Walk
date: 2026-10-21
status: permanent
type: visual
source: "/Users/tusharsingh/Downloads/crispr-v2.html"
---
# Why some guides came out 19 long

> [!abstract] Summary
> Interactive step-by-step walkthrough tracing an NGS read from raw FASTQ through adapter trimming to the final CRISPR sgRNA count matrix. Demonstrates how human U6 promoter transcription initiation (requiring a 5' G) causes guides naturally starting with G to omit an extra base, trimming down to 19 nt under cutadapt, and why rigid 20-mer counters discard valid reads while aligners like BWA correctly count them.

---

## Interactive Visual

> [!TIP] Preview
> You can interact with this visualization below, or [open it standalone in a new tab](html/why-some-guides-came-out-19-long.html).

<iframe src="html/why-some-guides-came-out-19-long.html" width="100%" height="750px" style="border: 1px solid #e0e0e0; border-radius: 8px;"></iframe>

---

## Key Takeaways

- **Topic Area**: Biology & Functional Genomics
- **Core Concept**: U6 transcription start site requirement (5' G), 19-nt vs. 20-nt sgRNA cassettes, cutadapt tag trimming, and counting matrix quantification
- **Interactive File**: `Visuals/html/why-some-guides-came-out-19-long.html` (mirrored as `Visuals/html/crispr-v2.html`)
- **Source Origin**: `/Users/tusharsingh/Downloads/crispr-v2.html`

---

## Related Notes

- [[A CRISPR Knockout Screen - Visual]]
- [[CRISPR Knockout Screen (Standalone) - Visual]]
- [[MAGeCK RRA, step by step - Visual]]
- [[MAGeCK-MLE, step by step - Visual]]
- [[DNA Genes and Central Dogma]]
- [[Mutations and Genomic Alterations]]
- [[Biology MOC]]
- [[Visuals MOC]]
