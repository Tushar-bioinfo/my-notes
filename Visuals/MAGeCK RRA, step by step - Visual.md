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
  - robust-rank-aggregation
  - fdr
  - stats
aliases:
  - MAGeCK RRA, step by step
  - MAGeCK RRA
  - Robust Rank Aggregation in CRISPR Screens
  - alpha-RRA
  - MAGeCK RRA (v1)
date: 2026-10-10
status: permanent
type: visual
source: "proff-viz"
---
# MAGeCK RRA, step by step

> [!abstract] Summary
> Interactive walkthrough of the MAGeCK Robust Rank Aggregation ($\alpha$-RRA) algorithm for pooled CRISPR screens. Follows raw sequencing read normalization, guide-level negative binomial p-value testing, ranking and uniform percentile mapping, $\alpha$-cutoff filtering, $\beta$ order statistics, permutation null distribution generation, and Benjamini-Hochberg FDR correction.

---

## Interactive Visual

> [!TIP] Detailed Walkthrough Available
> See also the expanded 26-step calculation edition: [[MAGeCK RRA (v2-detailed) - Visual]].

> [!TIP] Preview
> You can interact with this visualization below, or [open it standalone in a new tab](html/mageck-rra-step-by-step.html).

<iframe src="html/mageck-rra-step-by-step.html" width="100%" height="750px" style="border: 1px solid #e0e0e0; border-radius: 8px;"></iframe>

---

## Key Takeaways

- **Topic Area**: Functional Genomics & Statistical Modeling
- **Core Concept**: Ranks guide RNAs by negative binomial depletion p-values and aggregates them with $\alpha$-cutoff Beta order statistics to identify essential genes robust to single guide outliers.
- **Interactive File**: `Visuals/html/mageck-rra-step-by-step.html` (detailed version mirrored as `Visuals/html/mageck-rra-v2-detailed.html`; legacy v1 archived as `Visuals/html/mageck-rra-step-by-step-v1.html`)

---

## Related Notes

- [[MAGeCK RRA (v2-detailed) - Visual]]
- [[MAGeCK-MLE (v2-detailed) - Visual]]
- [[MAGeCK-MLE, step by step - Visual]]
- [[A CRISPR Knockout Screen - Visual]]
- [[CRISPR Knockout Screen (Standalone) - Visual]]
- [[Testing 20,000 Genes at Once - Visual]]
- [[Why Counts Get Logged - Visual]]
- [[DNA Genes and Central Dogma]]
- [[Cancer Biology MOC]]
- [[Stats MOC]]
- [[Biology MOC]]
- [[Visuals MOC]]

