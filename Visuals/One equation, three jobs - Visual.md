---
tags:
  - visual
  - interactive
  - stats
  - linear-model
  - differential-expression
  - batch-effect
aliases:
  - One equation, three jobs
date: 2026-10-12
status: permanent
type: visual
source: "Visuals/html/one-equation-three-jobs.html"
---
# One equation, three jobs

> [!abstract] Summary
> One linear model, ŷ = Xβ with β = (XᵀX)⁻¹Xᵀy, computed cell by cell on small tables. It is used three ways: a line through dose data (regression), a 0/1 group column whose β₁ is the log₂ fold change tested with t (differential expression), and a batch column whose fitted part is subtracted (like limma's removeBatchEffect). All numbers are simulated for teaching.

---

## Interactive Visual

> [!TIP] Preview
> You can interact with this visualization below, or [open it standalone in a new tab](html/one-equation-three-jobs.html).

<iframe src="html/one-equation-three-jobs.html" width="100%" height="750px" style="border: 1px solid #e0e0e0; border-radius: 8px;"></iframe>

---

## Key Takeaways

- **Topic Area**: Stats
- **Core Concept**: design matrix X, normal equations, fitted values, residuals, contrasts, batch correction
- **Caveat**: batch-corrected Y is for plots and clustering; for DE tests, keep batch in the design
- **Interactive File**: `Visuals/html/one-equation-three-jobs.html`
- **Source Origin**: `Visuals/html/one-equation-three-jobs.html`

---

## Related Notes

- [[What a t-test Sees - Visual|What a t-test Sees]]
- [[Testing 20,000 Genes at Once - Visual|Testing 20,000 Genes at Once]]
- [[MAGeCK-MLE, step by step - Visual|MAGeCK-MLE, step by step]]
- [[Counts to log-CPM Calculation - Visual|Counts to log-CPM]]
- [[Stats MOC]]
- [[Maths MOC]]
- [[Visuals MOC]]

