---
tags:
  - biology
  - cancer-biology
  - metabolism
  - warburg
  - cornell
aliases:
  - Warburg Effect
  - Metabolic Reprogramming
  - Aerobic Glycolysis
date: 2026-04-14
status: permanent
---
# Cancer Metabolism

> [!ABSTRACT] Summary
> Cancer cells rewire their metabolism to balance energy production with biosynthesis and redox homeostasis. The Warburg effect (aerobic glycolysis) is the most famous but not the only metabolic alteration: glutamine addiction, lipid reprogramming, one-carbon metabolism, and maintained OXPHOS (especially in CSCs and drug-resistant cells) all contribute. The metabolic landscape is heterogeneous within a single tumor, with glycolytic and oxidative regions coexisting and even cooperating via lactate shuttling. FDG-PET imaging directly exploits the Warburg effect clinically.

---

## Cue Questions

> [!QUESTION] Key questions for self-testing
> - What is the Warburg effect? How is it different from anaerobic glycolysis?
> - Name 4 advantages of aerobic glycolysis for cancer cells.
> - How does FDG-PET exploit the Warburg effect?
> - What is glutamine addiction, and which oncogene drives it (MYC)?
> - Are mitochondria shut down in cancer? Why is this a misconception?
> - Which cancer cell populations rely on OXPHOS (CSCs, metastatic, drug-resistant)?
> - What is metabolic symbiosis in tumors?
> - What is the connection between lactate and immune suppression in the TME?
> - How does the pentose phosphate pathway support cancer growth?

---

## Notes

### 13.1 The Warburg Effect

**Normal cell metabolism:**
- Glucose → Glycolysis → Pyruvate
- Aerobic: Pyruvate → mitochondria → TCA cycle → OXPHOS → **36–38 ATP per glucose**
- Anaerobic: Pyruvate → Lactate → **2 ATP** (only when O₂ limited)

**Cancer cell metabolism (Warburg effect):**
- Glucose → Glycolysis → Pyruvate → **LACTATE** — even when **O₂ IS PRESENT** (aerobic glycolysis)
- Only 2 ATP per glucose, BUT glucose uptake is 10–50× higher
- Lactate production massively elevated

#### Why? 4 Advantages of Warburg Metabolism

| Advantage | Mechanism |
|---|---|
| **1. Speed** | Glycolysis is ~100× faster than OXPHOS → rapid ATP despite lower yield |
| **2. Biosynthetic precursors** | Intermediates feed into nucleotide synthesis (PPP), amino acid synthesis (serine → glycine → one-carbon), lipid synthesis (acetyl-CoA → fatty acids) |
| **3. TME acidification** | Lactate → low pH → immune suppression + MMP activation → invasion |
| **4. Redox homeostasis** | NADPH from pentose phosphate pathway → antioxidant → survive ROS |

> [!IMPORTANT] Cancer cells need BUILDING BLOCKS, not just energy.
> The Warburg effect is a biosynthetic strategy, not an energy strategy.

#### Clinical Detection: FDG-PET

| Step | Detail |
|---|---|
| ¹⁸F-fluorodeoxyglucose (FDG) | Glucose analog |
| High GLUT1 expression on cancer cells | FDG taken up preferentially |
| Phosphorylated by hexokinase | Trapped intracellularly (cannot be metabolized further) |
| PET detects radioactivity | Tumor imaging and staging |

---

### 13.2 Beyond Warburg — Other Metabolic Reprogramming

#### Glutamine Addiction
- Many cancer cells are **dependent on glutamine**
- Glutamine → glutamate → α-ketoglutarate → enters TCA cycle (anaplerosis)
- Provides carbon AND nitrogen for biosynthesis
- **MYC** directly drives glutamine metabolism (GLS, SLC1A5)
- Therapeutic target: GLS inhibitors (CB-839, in clinical trials)

#### Lipid Metabolism
- De novo fatty acid synthesis: **FASN** overexpression
- SREBP1 activation → cholesterol and fatty acid synthesis
- Fatty acid oxidation (FAO) in some cancers (leukemia, metastatic cells)
- Lipid droplet accumulation → energy storage and signaling

#### One-Carbon Metabolism
- Folate cycle + methionine cycle
- Purine and pyrimidine synthesis
- Methylation reactions (SAM → SAH)
- MTHFR, SHMT2, MTHFD2 upregulated in cancer
- Chemotherapy target: methotrexate, pemetrexed (antifolates)

---

### 13.3 Mitochondrial Metabolism — Not Shut Down

> [!WARNING] Common Misconception
> Mitochondria are NOT completely shut down in cancer. The TCA cycle provides essential biosynthetic intermediates, and OXPHOS still occurs.

**Cancer cells that rely on OXPHOS:**

| Population | Reason |
|---|---|
| **Cancer stem cells (CSCs)** | OXPHOS-dependent, glycolysis-independent |
| **Metastatic cells** | May shift to OXPHOS at metastatic site |
| **Drug-resistant cells** | Often OXPHOS-dependent |

OXPHOS inhibitors (IACS-010759) in clinical trials.

---

### 13.4 Metabolic Heterogeneity

- Different cells in the same tumor have **different metabolic states**
- Hypoxic cells (far from vessels): glycolytic
- Oxygenated cells (near vessels): may use OXPHOS

> [!NOTE] Metabolic Symbiosis
> Hypoxic cells produce lactate → oxygenated cells take up lactate (MCT1 transporter) → convert to pyruvate → OXPHOS. This **metabolic coupling** is visible with spatial transcriptomics.

---

## Summary

> [!TIP] Cornell Summary
> Cancer metabolism centers on the Warburg effect (aerobic glycolysis): fast ATP production + biosynthetic precursors + TME acidification + redox balance, at the cost of low ATP yield per glucose (compensated by 10–50× glucose uptake). Beyond Warburg, cancers exploit glutamine addiction (MYC-driven), lipid metabolism (FASN), and one-carbon metabolism (folate cycle, antifolate target). Mitochondria are NOT shut down — CSCs, metastatic cells, and drug-resistant cells depend on OXPHOS. Tumors show metabolic heterogeneity with spatial metabolic symbiosis (lactate shuttling), mappable by spatial transcriptomics. FDG-PET clinically exploits the Warburg effect for tumor imaging.

---

## Related

- [[Cancer Biology Reference Index]]
- [[Hallmarks of Cancer]]
- [[Tumor Microenvironment]]
- [[Angiogenesis and Metastasis]]
- [[Cancer Biology MOC]]
