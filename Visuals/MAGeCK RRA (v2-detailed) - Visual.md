---
tags:
  - visual
  - interactive
  - biology
  - crispr
  - mageck
  - rra
  - knockout-screen
  - sgrna
  - v2-detailed
  - robust-rank-aggregation
  - fdr
aliases:
  - MAGeCK RRA (v2-detailed)
  - MAGeCK RRA, step by step (v2-detailed)
  - mageck-rra-v2-detailed
  - alpha-RRA v2
date: 2026-10-21
status: permanent
type: visual
source: "/Users/tusharsingh/Downloads/mageck-rra-step-by-step.html"
---
# MAGeCK RRA (v2-detailed)

> [!abstract] Summary
> Comprehensive 26-step calculation walkthrough of the MAGeCK Robust Rank Aggregation ($\alpha$-RRA) pipeline for pooled CRISPR screens. Follows individual sgRNA counts through size-factor normalization, negative binomial mean-variance modeling, one-sided negative binomial guide depletion $p$-values, rank ordering and uniform midpoint percentile mapping, dynamic $\alpha$-cutoff filtering, $\beta$ order statistics, permutation null calibration, and backward running minimum Benjamini-Hochberg FDR correction.

---

## Interactive Visual

> [!TIP] Preview
> You can interact with this visualization below, or [open it standalone in a new tab](html/mageck-rra-v2-detailed.html).

<iframe src="html/mageck-rra-v2-detailed.html" width="100%" height="750px" style="border: 1px solid #e0e0e0; border-radius: 8px;"></iframe>

---

## Key Takeaways

- **Topic Area**: Biology & Functional Genomics (Statistical Modeling)
- **Core Concept**: Aggregates guide RNAs by negative binomial depletion significance using $\alpha$-cutoff Beta order statistics, filtering out ineffective outlier guides and calibrating gene significance against a permutation null with monotonic Benjamini-Hochberg FDR adjustment.
- **Interactive File**: `Visuals/html/mageck-rra-v2-detailed.html` (mirrored as `Visuals/html/mageck-rra-step-by-step.html`)
- **Source Origin**: `/Users/tusharsingh/Downloads/mageck-rra-step-by-step.html`

---

## Related Notes

- [[MAGeCK RRA, step by step - Visual]]
- [[MAGeCK-MLE (v2-detailed) - Visual]]
- [[MAGeCK-MLE, step by step - Visual]]
- [[Why some guides came out 19 long - Visual]]
- [[A CRISPR Knockout Screen - Visual]]
- [[CRISPR Knockout Screen (Standalone) - Visual]]
- [[Testing 20,000 Genes at Once - Visual]]
- [[Why Counts Get Logged - Visual]]
- [[DNA Genes and Central Dogma]]
- [[Cancer Biology MOC]]
- [[Stats MOC]]
- [[Biology MOC]]
- [[Visuals MOC]]
