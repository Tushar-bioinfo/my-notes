---
id: C02
title: Is the stroma gap real at matched nucleus density?
idea: stroma-gap
kind: science
status: closed
tier: auto
approve:
data: private
figure: Fig 1
paper: 3
fork: 3
clarity: 3
cost: 1
attempts: 1
ladder: L1
pass_line: For both image-level-clean models (StarDist, CellSAM), recall at connective fraction 0.75 minus recall at 0.25, adjusted for nucleus count and source, is <= -0.05 with a 95% image-cluster bootstrap CI excluding 0
next_if_pass: KEEP. The gap is real at matched density. Next C06 (label look) and C12 (mechanism)
next_if_fail: NEEDS-YOU. Both clean models have a CI including 0 or |diff| < 0.03, so the gap is density or score. Run C06 anyway (labels); the user and PI decide stop vs a scoring/label paper (PAPER.md kill test)
next_if_inconclusive: NARROW. The models disagree or the CIs are wide. Per-source analysis (C02b), then a per-class recall rescore on the A30 (C05)
---

## Question
Do the models find fewer nuclei in stroma-rich patches than in stroma-poor patches **with the same number of nuclei**, when the source image is the independent unit?

## Prediction (written before the run, 2026-10-01, by the brain; not yet the user's)
- Without adjustment, stroma-rich patches have lower recall, because they are also sparse.
- After adjusting for nucleus count, the gap shrinks but stays at about −0.05 to −0.10 recall for StarDist and CellSAM.
- The gap is smaller for Cellpose-SAM, which trained on about 78% of CoNIC (C04).
- Reason: connective nuclei are long and faint, and IoU-0.5 matching is harsh on thin objects. This prediction cannot separate "biology" from "score" (see the limits below).

## Preflight
- **Unit and true n:** the source image (238), not the patch (4,981). Patient n is **unknown** (C01). Patches with 0 GT nuclei (150) are excluded from recall.
- **Split / leakage (C04):**
  - Cellpose-SAM trained on 3,863/4,981 CoNIC patches → flagged, reported but not the headline.
  - CellViT-SAM trained on PanNuke → the PanNuke-source patches are flagged.
  - StarDist and CellSAM: no CoNIC source at image level in the stated training lists.
  - All of this is reported in `Main/Ideas/work/rebuild_2026-09-28/LEAKAGE_TABLE.md` and was not re-opened.
- **Answer key:** Lizard labels, semi-automatic (HoVer-Net, then pathologist refinement). Stroma label quality is **unknown** (C06). Stroma fraction is defined from the same labels, so a stroma under-labelling bias would also move the x-axis.
- **Null:** no association between connective fraction and recall at matched count and source.
- **Scorer controls:** C00 must pass before this verdict counts.
- **Counts in = counts out:** row counts per model are logged (CellSAM has 4,961, the others 4,981).
- **Raw examples:** 10 stroma-rich low-recall patches and 10 stroma-poor high-recall patches, saved as overlays in `runs/C02/` (GT outlines only; prediction masks are not on Box).

## Steps
1. Join each model's evaluation CSV to `dataset_manifest.csv` on `sample_id`. Check the row counts.
2. For each patch, compute recall = TP/(TP+FN), the connective fraction = connective/count_total, and log(count_total). Record the source (from the name prefix) and the source image (the name before `-NNNN`).
3. Fit a weighted least-squares model: recall ~ connective_frac + count-quintile dummies + source dummies, with weight = GT count. The effect is the coefficient × 0.5, i.e. the predicted recall difference between connective fraction 0.75 and 0.25.
4. Run a cluster bootstrap over the 238 source images (2,000 reps) to get the 95% CI. Report the same for PQ and precision as secondary outcomes.
5. Sensitivity checks: unweighted; leave out each source in turn; CellViT without the PanNuke patches.

## Run log
- 2026-10-01 `runs/C02/stroma_gap.py` → `runs/C02/c02_results.csv`. Stroma share from the manifest (central-region counts); density = TP+FN (exact whole-patch GT count). Whole-patch class counts (`patch_class_counts.py`) stalled on Box downloads and were dropped. Overlays not made yet.
- Row check: 4,831 patches with GT > 0 (CellSAM 4,820), 238 images, all four models.
- Independent check (brain, same session): pooled totals per model and image-level Spearman(recall, connective share) = −0.04 (StarDist), −0.06 (CellSAM), n = 238.

## Verdict
**INCONCLUSIVE → NARROW.** The script's rule printed FAIL, but one of the two headline runs fails preflight, so the rule cannot be applied.

| Model | Pooled recall | Predicted / true nuclei | Stroma effect on recall (95% CI) | On precision |
|---|---|---|---|---|
| StarDist | 0.125 | 0.15 | −0.012 (−0.026, 0.001) | +0.035 |
| CellSAM | 0.664 | 1.20 | −0.022 (−0.050, 0.005) | **−0.121 (−0.146, −0.099)** |
| Cellpose-SAM (leaked) | 0.753 | 0.91 | +0.011 (−0.004, 0.025) | −0.018 |
| CellViT-SAM | 0.414 | 0.55 | −0.028 (−0.056, 0.001) | +0.058 |

- **StarDist and CellViT runs look broken**, not weak: StarDist outputs 15% of the true nuclei count. `run_stardist.py` applies no rescaling and default thresholds; CoNIC is 20x and `2D_versatile_he` expects ~40x. Likely cause: scale (unverified until rerun).
- **CellSAM (clean, working):** no clear recall gap. In stroma-rich patches it makes many more unmatched predictions. These are either false positives or real nuclei missing from the labels (C06 decides).
- **Cellpose-SAM:** no gap, but it trained on most of these patches.
- C00 showed the score alone is ~19 points harsher on connective nuclei for a 2 px error; the observed gaps are far smaller than that, so the score is not hiding a big model gap.
- Next (pre-written narrow action): rescore StarDist and CellViT at the correct scale with per-class recall on the A30 (C10 → C05, needs approve). C06 label look now carries the most information per hour.


## User reading
