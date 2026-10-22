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
  - v2-detailed
  - negative-binomial
  - wald-test
aliases:
  - MAGeCK-MLE (v2-detailed)
  - MAGeCK-MLE, count by count
  - mageck-mle-v2-detailed
  - MAGeCK MLE v2
date: 2026-10-21
status: permanent
type: visual
source: "/Users/tusharsingh/Downloads/mageck-mle-step-by-step.html"
---
# MAGeCK-MLE (v2-detailed)

> [!abstract] Summary
> Comprehensive 11-chapter walkthrough tracing counts $\to$ treatment effect ($\beta$) $\to$ uncertainty in MAGeCK's Maximum Likelihood Estimation algorithm for pooled CRISPR screens. Explains median-ratio library depth normalization, negative binomial generalized linear modeling (GLM), mean-variance dispersion curve fitting, log-likelihood profiling, IRLS parameter estimation, sandwich covariance estimation, Wald $z$-testing, permutation-based Monte Carlo nulls, Benjamini-Hochberg FDR, and optional EM expectation-maximization dud sgRNA efficiency downweighting.

---

## Interactive Visual

> [!TIP] Preview
> You can interact with this visualization below, or [open it standalone in a new tab](html/mageck-mle-v2-detailed.html).

<iframe src="html/mageck-mle-v2-detailed.html" width="100%" height="750px" style="border: 1px solid #e0e0e0; border-radius: 8px;"></iframe>

---

## Key Takeaways

- **Topic Area**: Biology & Functional Genomics (Statistical Modeling)
- **Core Concept**: Joint negative binomial GLM estimating gene-level knockout selection effects ($\beta$) across conditions with iterative reweighted least squares (IRLS), sandwich variance, empirical permutation null distributions, and EM sgRNA efficiency updates.
- **Interactive File**: `Visuals/html/mageck-mle-v2-detailed.html` (mirrored as `Visuals/html/mageck-mle-step-by-step.html`)
- **Source Origin**: `/Users/tusharsingh/Downloads/mageck-mle-step-by-step.html`

---

## Related Notes

- [[MAGeCK-MLE, step by step - Visual]]
- [[MAGeCK RRA (v2-detailed) - Visual]]
- [[MAGeCK RRA, step by step - Visual]]
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
