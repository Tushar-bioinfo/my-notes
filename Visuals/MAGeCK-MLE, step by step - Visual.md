---
tags:
  - visual
  - interactive
  - biology
  - crispr
  - mageck
  - mle
  - knockout-screen
  - sgrna
  - negative-binomial
  - stats
aliases:
  - MAGeCK-MLE, step by step
  - MAGeCK-MLE
  - MAGeCK MLE
  - Maximum Likelihood Estimation in CRISPR Screens
  - MAGeCK-MLE (v1)
date: 2026-10-10
status: permanent
type: visual
source: "proff-viz"
---
# MAGeCK-MLE, step by step

> [!abstract] Summary
> Step-by-step interactive calculation walkthrough of the MAGeCK Maximum Likelihood Estimation (MLE) method for pooled CRISPR screens. Follows median-ratio library size normalization, generalized linear modeling (GLM) with experimental design matrices, negative binomial noise estimation, Expectation-Maximization (EM) mixture modeling to downweight dud sgRNAs, and Wald z-tests for gene beta ($\beta$) scores across conditions.

---

## Interactive Visual

> [!TIP] Detailed Walkthrough Available
> See also the expanded 11-chapter count-by-count edition: [[MAGeCK-MLE (v2-detailed) - Visual]].

> [!TIP] Preview
> You can interact with this visualization below, or [open it standalone in a new tab](html/mageck-mle-step-by-step.html).

<iframe src="html/mageck-mle-step-by-step.html" width="100%" height="750px" style="border: 1px solid #e0e0e0; border-radius: 8px;"></iframe>

---

## Key Takeaways

- **Topic Area**: Functional Genomics & Statistical Modeling
- **Core Concept**: Fits multi-condition CRISPR knockout screens into a negative binomial GLM, using an EM mixture model to identify and discount ineffective (dud) sgRNAs and reporting gene-level beta ($\beta$) effect sizes.
- **Interactive File**: `Visuals/html/mageck-mle-step-by-step.html` (detailed version mirrored as `Visuals/html/mageck-mle-v2-detailed.html`; legacy v1 archived as `Visuals/html/mageck-mle-step-by-step-v1.html`)

---

## Related Notes

- [[MAGeCK-MLE (v2-detailed) - Visual]]
- [[MAGeCK RRA (v2-detailed) - Visual]]
- [[MAGeCK RRA, step by step - Visual]]
- [[A CRISPR Knockout Screen - Visual]]
- [[CRISPR Knockout Screen (Standalone) - Visual]]
- [[Testing 20,000 Genes at Once - Visual]]
- [[Why Counts Get Logged - Visual]]
- [[DNA Genes and Central Dogma]]
- [[Cancer Biology MOC]]
- [[Stats MOC]]
- [[Biology MOC]]
- [[Visuals MOC]]

