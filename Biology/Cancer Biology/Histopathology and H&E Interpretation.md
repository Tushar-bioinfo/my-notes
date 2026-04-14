---
tags:
  - biology
  - cancer-biology
  - pathology
  - histology
  - H&E
  - cornell
aliases:
  - H&E Staining
  - Morphological Patterns
  - Tumor Grading
date: 2026-04-14
status: permanent
---
# Histopathology and H&E Interpretation

> [!ABSTRACT] Summary
> H&E (hematoxylin and eosin) is the foundational stain of pathology: hematoxylin stains nuclei blue-purple (binds DNA/RNA), eosin stains cytoplasm and ECM pink (binds proteins). Systematic H&E interpretation follows a low→medium→high power approach: architecture first, cell populations second, cytologic features third. Common morphological patterns (glandular, solid, papillary, signet ring, spindle, etc.) point to specific diagnoses and grades. Tumor grading systems (Nottingham for breast, Gleason for prostate) are partially quantifiable by computational pathology — nuclear features, architecture assessment, and mitotic counting are all segmentation tasks.

---

## Cue Questions

> [!QUESTION] Key questions for self-testing
> - What does hematoxylin stain and why? What does eosin stain and why?
> - What determines hematoxylin intensity (DNA content, chromatin compaction, nucleolar RNA)?
> - List 5 things you CAN see on H&E and 5 things you CANNOT (need IHC/molecular).
> - What are the 3 steps of systematic H&E interpretation?
> - At low power, what are the 5 common architectural patterns of carcinoma?
> - At high power, what nuclear features do you evaluate?
> - What is the difference between coagulative and liquefactive necrosis?
> - Name 5 morphological patterns and their associated cancers.
> - Explain the Nottingham grading system for breast cancer (3 components).
> - How does Gleason grading work? Why is 3+4 ≠ 4+3?
> - Which grading components are quantifiable by computational methods?

---

## Notes

### 14.1 The H&E Stain — Chemistry

#### Hematoxylin (Blue-Purple = Basophilic)
- Source: *Haematoxylum campechianum* (logwood tree)
- Aluminum-hematein complex (mordant-dye)
- **Positively charged** → binds negatively charged structures
- **Stains NUCLEI:** DNA (phosphate backbone), RNA, acidic proteins

**Intensity reflects:**
- DNA content (more DNA = darker — tetraploid cells appear darker)
- Chromatin compaction (dense heterochromatin = very dark)
- Nucleolar RNA (prominent nucleoli = active ribosome biogenesis in cancer)

#### Eosin (Pink-Red = Eosinophilic)
- Xanthene dye
- **Negatively charged** → binds positively charged structures
- **Stains CYTOPLASM, ECM, collagen:** basic amino acids (lysine, arginine), proteins

**Intensity reflects:**
- Cytoplasmic protein content (more protein = more pink)
- Collagen density (dense collagen = bright pink)
- Keratinization (squamous differentiation = intense pink)
- Muscle fibers (eosinophilic)
- RBCs (very eosinophilic — filled with hemoglobin)

---

### 14.2 What H&E CAN and CANNOT Show

| CAN See on H&E | CANNOT See (Need IHC, ISH, Molecular) |
|---|---|
| Nuclear size and shape | Specific protein expression |
| Chromatin pattern | Gene mutations |
| Nucleolar size and number | Cell surface markers |
| Cytoplasmic amount and color | Specific cell lineages (often) |
| Tissue architecture | Viral DNA/RNA |
| Mitotic figures | Gene fusions |
| Necrosis | Receptor status (ER, PR, HER2) |
| Inflammatory infiltrates | Proliferation index (need Ki-67) |
| Blood vessels | Specific immune subsets (CD4 vs CD8) |
| Collagen/ECM density | Microsatellite instability |
| | PD-L1 expression |

---

### 14.3 Systematic H&E Interpretation

#### Step 1: Low Power (2×–4×) — ARCHITECTURE

| Question | What to Look For |
|---|---|
| Is tissue normal/abnormal? | Mass, lesion, distorted architecture |
| What organ/tissue? | Tissue-specific morphology |
| **Architecture pattern?** | See pattern table below |
| Necrosis? | Geographic necrosis = large dead areas |
| Desmoplasia? | Pink fibrotic stroma around tumor |

#### Step 2: Medium Power (10×) — CELL POPULATIONS

| Cell Type | H&E Appearance |
|---|---|
| **Tumor cells** | Abnormal morphology, enlarged nuclei |
| **Lymphocytes** | Small dark round nuclei |
| **Plasma cells** | Eccentric "clock-face" nucleus, perinuclear hof |
| **Neutrophils** | Segmented nuclei, may form microabscesses |
| **Eosinophils** | Bilobed nucleus, red granules |
| **Macrophages** | Large, pale cytoplasm, may be foamy |
| **Fibroblasts** | Spindle-shaped |
| **Endothelial cells** | Lining vessels |

Key questions: Tumor:stroma ratio? Immune cells infiltrating or at periphery? Vascular/perineural invasion?

#### Step 3: High Power (20×–40×) — CYTOLOGIC FEATURES

**Nuclear features:**
- Size (μm estimate)
- Shape: round, oval, irregular, pleomorphic
- Chromatin: fine vs. coarse vs. vesicular vs. hyperchromatic
- Nuclear membrane: smooth vs. irregular
- Nucleoli: absent, small, prominent, multiple
- Inclusions: viral (Cowdry A bodies in HSV), pseudoinclusions

**Cytoplasmic features:**
- Amount: scant, moderate, abundant
- Color: eosinophilic (pink), basophilic (blue), clear/empty
- Inclusions: mucin (pale blue vacuoles → signet ring), melanin (brown), hemosiderin (golden-brown)

**Mitotic figures:**
- Normal: bipolar (two chromatin masses)
- Abnormal: tripolar, multipolar, asymmetric
- Count per 10 HPF → mitotic rate → high = aggressive

**Necrosis types:**
- Coagulative: ghost cells (preserved architecture, no nuclei)
- Liquefactive: loss of architecture, debris
- Caseating: amorphous pink material (granulomas)

---

### 14.4 Common Morphological Patterns

| Pattern | Description | Cancer Example |
|---|---|---|
| **Glandular/tubular** | Organized gland formation | Adenocarcinoma (well-differentiated) |
| **Cribriform** | "Swiss cheese" sieve-like with punched-out lumens | Prostate (Gleason 3+3) |
| **Solid sheets/nests** | No gland formation | Poorly differentiated carcinoma |
| **Single file / Indian file** | Cells in linear chains | Invasive lobular breast cancer (E-cadherin loss) |
| **Signet ring** | Nucleus pushed to periphery by mucin vacuole | Diffuse gastric cancer, lobular breast |
| **Papillary** | Finger-like fronds with fibrovascular cores | Thyroid, ovarian, bladder |
| **Micropapillary** | Small clusters WITHOUT fibrovascular cores | Aggressive variant (breast, lung, bladder) |
| **Trabecular** | Cord-like arrangement | Hepatocellular carcinoma |
| **Spindle cell** | Elongated fusiform cells | Sarcomatoid carcinoma, sarcoma |
| **Rhabdoid** | Eccentric nucleus + eosinophilic inclusion body | Aggressive (SMARCB1 loss) |
| **Small blue cells** | High N:C ratio, minimal cytoplasm | Small cell carcinoma, lymphoma, neuroblastoma |
| **Clear cells** | Empty/transparent cytoplasm (lipids/glycogen dissolved) | Renal cell carcinoma, ovarian clear cell |
| **Keratin pearls** | Concentric lamellated eosinophilic structures | Well-differentiated squamous cell carcinoma |
| **Rosettes** | Radial arrangement around central neuropil/lumen | Neuroblastoma, medulloblastoma, retinoblastoma |
| **Starry sky** | Pale macrophages among dark lymphocytes | Burkitt lymphoma |

---

### 14.5 Tumor Grading Systems

#### Nottingham (Bloom-Richardson) Grade — Breast Cancer

| Component | Score 1 | Score 2 | Score 3 |
|---|---|---|---|
| **Tubule formation** | >75% tubules | 10–75% | <10% (solid sheets) |
| **Nuclear pleomorphism** | Small, uniform | Moderate variation | Marked variation, prominent nucleoli |
| **Mitotic count** (per 10 HPF) | Low | Intermediate | High |

**Total:** 3–5 = Grade 1 (well-diff) · 6–7 = Grade 2 (mod-diff) · 8–9 = Grade 3 (poorly-diff)

#### Gleason Grade — Prostate Cancer

| Pattern | Morphology |
|---|---|
| **3** | Variably sized individual glands |
| **4** | Fused glands, poorly formed, cribriform |
| **5** | No gland formation, solid sheets, single cells |

**Gleason score = Most common pattern + Worst pattern**
Example: 3+4=7 (favorable) vs. 4+3=7 (unfavorable) — **order matters!**

> [!IMPORTANT] Computational Pathology Opportunity
> Grading is **partially quantifiable** by AI:
> - Nuclear pleomorphism → nuclear size/shape feature extraction
> - Tubule formation → architectural pattern recognition
> - Mitotic count → mitosis detection (AMARA challenge)
> - All require **accurate cell segmentation** — your research domain

---

## Summary

> [!TIP] Cornell Summary
> H&E is the universal stain of pathology — hematoxylin (blue) stains DNA/RNA in nuclei, eosin (pink) stains cytoplasmic proteins and ECM. Systematic interpretation goes low→medium→high: architecture, cell populations, cytologic features. Each morphological pattern (glandular, solid, papillary, signet ring, etc.) carries diagnostic significance. Grading systems (Nottingham, Gleason, WHO) assess differentiation, nuclear features, and mitotic activity — all amenable to computational quantification through segmentation and pattern recognition. H&E shows morphology but cannot show molecular markers (ER, HER2, PD-L1, mutations) — this is the gap that spatial transcriptomics and computational pathology aim to bridge.

---

## Related

- [[Cancer Biology Reference Index]]
- [[Hallmarks of Cancer]]
- [[Molecular Classification of Cancer]]
- [[Spatial Biology and Computational Pathology]]
- [[Digital Pathology Guide for Beginners]]
- [[Beginner Digital Pathology Guide for H&E]]
- [[Cancer Biology MOC]]
