---
tags:
  - biology
  - cancer-biology
  - oncogenes
  - tumor-suppressors
  - cornell
aliases:
  - TP53
  - RB1
  - PTEN
  - KRAS
  - Oncogene Activation
date: 2026-04-14
status: permanent
---
# Oncogenes and Tumor Suppressors

> [!ABSTRACT] Summary
> Cancer is driven by two classes of gene alterations: gain-of-function in oncogenes (one mutant allele sufficient, dominant) and loss-of-function in tumor suppressors (usually both alleles required, Knudson two-hit model). Oncogenes arise through point mutations (KRAS), amplification (HER2, MYC), translocations (BCR-ABL), or viral insertion (HPV E6/E7). The three most important tumor suppressors — TP53, RB1, and PTEN — guard genome integrity, cell cycle control, and growth factor signaling respectively. Their pathways are disrupted in virtually all cancers.

---

## Cue Questions

> [!QUESTION] Key questions for self-testing
> - What is the difference between a proto-oncogene and an oncogene?
> - Name the 4 mechanisms of oncogene activation, with one example each.
> - What KRAS mutations are common, and which is specifically targetable (sotorasib)?
> - Why is MYC considered "undruggable"? What H&E features does MYC amplification cause?
> - Explain Knudson's two-hit hypothesis using retinoblastoma.
> - What are the 5 normal functions of p53, and the 4 ways it is inactivated in cancer?
> - How does the RB pathway control the G1/S checkpoint?
> - Why do CDK4/6 inhibitors only work when RB is functional?
> - What is PTEN, and what happens when it is lost?
> - What is haploinsufficiency, and which tumor suppressors show it?

---

## Notes

### 4.1 Oncogenes — Mechanisms of Activation

Oncogenes arise from proto-oncogenes through gain-of-function alterations. A **single mutant allele is sufficient** (dominant).

#### 1. Point Mutation (Constitutive Activation)

> [!EXAMPLE] KRAS — The Most Commonly Mutated Oncogene
> - **Mutations:** G12D, G12V, G12C, G13D
> - Glycine at position 12 replaced → GTP hydrolysis prevented → RAS always in GTP-bound (active) state
> - Downstream MAPK and PI3K signaling always on
> - Found in: **pancreatic (90%)**, colorectal (45%), lung adenocarcinoma (30%)
> - **G12C specifically targetable:** sotorasib, adagrasib

#### 2. Gene Amplification (Overexpression)

| Gene | Cancer | Frequency | Therapeutic Target |
|---|---|---|---|
| **HER2/ERBB2** | Breast | 15–20% | Trastuzumab, pertuzumab, T-DM1 |
| **MYC** | Many | Variable | "Undruggable" — but major cancer dependency |
| **EGFR** | Glioblastoma, lung | Variable | EGFRvIII deletion mutant, constitutively active |

> [!NOTE] MYC-amplified tumors on H&E
> Large nuclei, prominent nucleoli, high mitotic rate.

#### 3. Chromosomal Translocation

| Translocation | Fusion/Result | Cancer | Therapy |
|---|---|---|---|
| **t(9;22)** BCR-ABL1 | Constitutive tyrosine kinase | CML | Imatinib (Gleevec) — paradigm of targeted therapy |
| **t(14;18)** IGH-BCL2 | BCL2 overexpression → anti-apoptotic | Follicular lymphoma | — |
| **t(8;14)** IGH-MYC | MYC overexpression → explosive proliferation | Burkitt lymphoma | H&E: "starry sky" appearance |
| **TMPRSS2-ERG** | Androgen-responsive promoter drives ERG | ~50% prostate cancers | — |

#### 4. Viral Oncogene Insertion

| Virus | Oncogenes | Mechanism | Cancer |
|---|---|---|---|
| **HPV** | E6, E7 | E6 degrades p53; E7 inactivates RB — dismantles both pathways simultaneously | Cervical, oropharyngeal |
| **EBV** | LMP1, EBNA1 | LMP1 mimics CD40 signaling → proliferation | Nasopharyngeal, Burkitt, gastric |

---

### 4.2 Tumor Suppressor Genes — Detailed Profiles

Tumor suppressors require **loss-of-function in BOTH alleles** (Knudson's two-hit hypothesis), though haploinsufficiency exists for some.

#### Knudson's Two-Hit Model

| | Hereditary Form | Sporadic Form |
|---|---|---|
| **Germline** | Born with ONE mutant allele | Both alleles normal |
| **Somatic** | Only ONE more hit needed → high penetrance | Need TWO independent hits → very low probability |
| **Presentation** | Often bilateral, early onset | Usually unilateral, later onset |
| **Example** | Bilateral retinoblastoma | Unilateral retinoblastoma |

**Mechanisms of inactivation:** Point mutation, frameshift, deletion, promoter methylation (1st or 2nd hit), LOH, CN-LOH

---

#### TP53 — "Guardian of the Genome"

| Property | Detail |
|---|---|
| **Location** | 17p13.1 |
| **Protein** | p53, 393 aa, transcription factor |
| **Mutated in** | >50% of ALL human cancers (most commonly mutated gene) |

**5 Normal Functions of p53:**
1. **Cell cycle arrest:** senses DNA damage (ATM/ATR) → activates p21 (G1/S checkpoint)
2. **DNA repair:** activates GADD45
3. **Apoptosis:** activates PUMA, NOXA, BAX (if damage irreparable)
4. **Metabolic regulation:** suppresses glycolysis (TIGAR), activates OXPHOS (SCO2)
5. **Angiogenesis inhibition:** activates thrombospondin-1 (TSP1)

**How p53 is Inactivated in Cancer:**
- **Missense mutations** in DNA-binding domain: R175H, R248Q, R273H (hotspots)
  - Mutant p53 acts as dominant negative (forms non-functional tetramers with wild-type)
  - Some mutations confer **gain of function** (actively promotes invasion, metastasis, chemoresistance)
- **17p deletion** (loss of one allele)
- **MDM2 amplification** (MDM2 ubiquitinates p53 → degradation — functional equivalent of TP53 mutation)
- **ARF (CDKN2A) deletion** → cannot inhibit MDM2 → p53 degraded
- **Viral oncoproteins:** HPV E6, HBV HBx → p53 degradation

> [!TIP] H&E Correlation
> TP53-mutant tumors often show high-grade morphology, increased nuclear pleomorphism, high mitotic rate, necrosis. But some TP53-mutant tumors are deceptively well-differentiated — molecular testing is essential.

---

#### RB1 — "The Gatekeeper"

| Property | Detail |
|---|---|
| **Location** | 13q14.2 |
| **Protein** | RB, 928 aa |
| **Key pathway** | RB binds E2F → genes OFF → no S-phase entry |

**Normal function:** Hypophosphorylated RB binds E2F transcription factors. When cell should divide: Cyclin D–CDK4/6 phosphorylates RB → releases E2F → S-phase genes activated.

**How RB is Inactivated:**
- RB1 mutation/deletion (direct)
- CDKN2A (p16) loss → CDK4/6 unchecked → RB always phosphorylated
- CCND1 (Cyclin D1) amplification → CDK4/6 hyperactive
- CDK4 amplification
- HPV E7 → binds and degrades RB

> [!WARNING] CDK4/6 Inhibitors
> Palbociclib, ribociclib, abemaciclib work **ONLY if RB is functional**. If RB is lost → CDK4/6 inhibitors won't work. The RB pathway is disrupted in virtually ALL cancers: **"many genes, one pathway."**

---

#### PTEN — "The Lipid Phosphatase"

| Property | Detail |
|---|---|
| **Location** | 10q23.3 |
| **Function** | Dephosphorylates PIP3→PIP2 (reverses PI3K action) |
| **Without PTEN** | PI3K-AKT-mTOR pathway constitutively active |
| **Mutated in** | Endometrial (50–80%), glioblastoma (30–40%), prostate (20–30%), breast (15–30%) |
| **Germline syndrome** | Cowden syndrome → multiple benign and malignant tumors |

---

### 4.3 The "Two-Hit" Exceptions

#### Haploinsufficiency
Some tumor suppressors show phenotype with only **ONE hit:**
- **PTEN:** 50% expression is insufficient for full tumor suppression
- **CDKN1B** (p27), **DMP1**, **TGFBR2**

#### Dominant Negative
Mutant protein interferes with remaining wild-type:
- **TP53:** mutant p53 forms non-functional tetramers with WT p53
- Some TP53 mutations confer additional oncogenic gain-of-function (actively promote invasion, metastasis)

---

## Summary

> [!TIP] Cornell Summary
> Oncogenes are activated by point mutations (KRAS G12C), amplification (HER2, MYC), translocations (BCR-ABL), or viral insertion (HPV E6/E7) — one allele is enough. Tumor suppressors are inactivated by the two-hit model (Knudson): both alleles must be lost, though haploinsufficiency and dominant-negative effects are exceptions. TP53 (>50% of all cancers), RB1 (virtually all cancers through its pathway), and PTEN (PI3K-AKT brake) are the three pillars. CDK4/6 inhibitors require intact RB. PARP inhibitors exploit BRCA loss. These molecular facts directly influence what pathologists see on H&E and what computational pathology models can predict.

---

## Related

- [[Cancer Biology Reference Index]]
- [[Mutations and Genomic Alterations]]
- [[Hallmarks of Cancer]]
- [[Cell Cycle Deregulation]]
- [[Signal Transduction in Cancer]]
- [[Cancer Biology MOC]]
