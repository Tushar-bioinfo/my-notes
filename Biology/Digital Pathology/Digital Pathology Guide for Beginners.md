---
tags:
  - biology
  - digital-pathology
  - histology
  - cornell
aliases:
  - Digital Pathology Guide
date: 2026-04-14
status: permanent
---
# 🔬 Digital Pathology Guide for Beginners
## H&E Staining: Normal Tissue vs. Tumor — A Visual Reference

> [!ABSTRACT] Summary
> This guide covers H&E appearance of all major tissue types: epithelial (squamous, glandular, transitional), connective (fibrous, adipose, cartilage/bone), muscle (skeletal, smooth, cardiac), nervous tissue, blood/lymphoid tissue, and liver. For each tissue, it contrasts normal architecture with tumor features, providing a systematic visual reference for learning digital pathology and building intuition for computational pathology tasks like cell segmentation and tissue classification.

---

## Cue Questions

> [!QUESTION] Key questions for self-testing
> - What are the 5 major tissue types, and how does each appear on H&E?
> - How do you distinguish squamous from glandular epithelium on H&E?
> - What features distinguish normal glandular architecture from adenocarcinoma?
> - What does desmoplasia look like on H&E?
> - How do you identify lymphocytes vs. neutrophils vs. macrophages on H&E?
> - What is the difference between skeletal, smooth, and cardiac muscle on H&E?
> - What are the key H&E features that suggest malignancy (nuclear atypia, loss of architecture, mitotic figures)?
> - At what magnification should you assess architecture vs. cytology?

---

> **How to Read H&E Stains**
> - **Hematoxylin (H):** Stains nuclei **purple/blue** — DNA, RNA-rich structures
> - **Eosin (E):** Stains cytoplasm & ECM **pink/red** — proteins, collagen
> - **Key principle:** More purple = more nuclear activity = often more aggressive

---

## 📋 Table of Contents
1. [Epithelial Tissues](#1-epithelial-tissues)
   - Squamous Epithelium
   - Glandular (Columnar) Epithelium
   - Transitional Epithelium (Urothelium)
2. [Connective Tissues](#2-connective-tissues)
   - Fibrous / Stromal Connective Tissue
   - Adipose Tissue
   - Cartilage & Bone
3. [Muscle Tissues](#3-muscle-tissues)
   - Smooth Muscle
   - Skeletal Muscle
4. [Neural Tissue](#4-neural-tissue)
5. [Hematopoietic & Lymphoid Tissue](#5-hematopoietic--lymphoid-tissue)
   - Lymph Node
   - Bone Marrow
6. [Hepatic (Liver) Tissue](#6-hepatic-liver-tissue)
7. [Key Tumor Concepts Glossary](#7-key-tumor-concepts-glossary)
8. [Quick Comparison Cheat Sheet](#8-quick-comparison-cheat-sheet)

---

## 1. Epithelial Tissues

### 1.1 Squamous Epithelium

#### 🟢 Normal Squamous Epithelium
**Location:** Skin (epidermis), oral cavity, esophagus, cervix (ectocervix), vagina

**H&E Appearance:**
- Cells arranged in **flat, layered sheets**
- Cells flatten progressively from basal → surface layer
- **Basal layer:** Small, cuboidal cells with dark nuclei, high N:C ratio
- **Superficial layers:** Large, flat, pale-pink cells with small/absent nuclei (keratinization)
- **Intercellular bridges (desmosomes)** may be visible
- Orderly maturation from bottom to top

**Annotated Image Links:**
1. 🔗 [Normal Stratified Squamous – Skin Epidermis (WebPathology)](https://www.webpathology.com/image.asp?case=1028&n=1)
2. 🔗 [Normal Squamous Epithelium – Esophagus (PathologyOutlines)](https://www.pathologyoutlines.com/topic/esophagusnormalhistology.html)
3. 🔗 [Stratified Squamous – Cervix Ectocervix (LibrePathology)](https://librepathology.org/wiki/Cervix)

---

#### 🔴 Squamous Cell Carcinoma (SCC)
**Common Sites:** Skin, oral cavity, esophagus, lung, cervix, head & neck

**H&E Appearance:**
- **Disorganized nests and sheets** of squamous cells invading stroma
- **Keratin pearls:** Concentric whorls of pink keratin — hallmark of well-differentiated SCC
- Cells show **pleomorphism** (variable size/shape), hyperchromatic nuclei
- **Intercellular bridges** still visible in well-diff SCC
- **Mitotic figures** (normal and abnormal) — "atypical mitoses" = aggressive sign
- **Desmoplastic stroma** reaction around invasive nests
- Loss of surface maturation — full-thickness atypia

**Grading Hints:**
| Grade | Features |
|-------|----------|
| Well-differentiated | Keratin pearls, some maturation, fewer mitoses |
| Moderately differentiated | Partial maturation, more nuclear atypia |
| Poorly differentiated | No keratin, sheets of pleomorphic cells, many mitoses |

**Annotated Image Links:**
1. 🔗 [SCC Skin – Keratin Pearls Annotated (WebPathology)](https://www.webpathology.com/image.asp?case=25&n=1)
2. 🔗 [Squamous Cell Carcinoma – Lung (PathologyOutlines)](https://www.pathologyoutlines.com/topic/lungtumorssquamouscell.html)
3. 🔗 [SCC Esophagus with Invasion (LibrePathology)](https://librepathology.org/wiki/Squamous_cell_carcinoma_of_the_esophagus)

---

### 1.2 Glandular (Columnar) Epithelium

#### 🟢 Normal Glandular Epithelium
**Location:** Colon, stomach, endometrium, breast ducts & lobules, prostate, pancreas

**H&E Appearance:**
- Tall columnar cells with **basally placed, oval nuclei** (nuclei at bottom of cell)
- **Abundant pale cytoplasm** (mucin-secreting cells appear vacuolated/pale)
- Cells line tubular or glandular structures in **neat, regular arrangements**
- **Single-cell layer** lining — no stratification or overlap
- Glands are **round/oval** with smooth outlines
- Surrounding lamina propria is loose, vascular

**Annotated Image Links:**
1. 🔗 [Normal Colonic Mucosa with Crypts (WebPathology)](https://www.webpathology.com/image.asp?case=382&n=1)
2. 🔗 [Normal Gastric Glandular Epithelium (PathologyOutlines)](https://www.pathologyoutlines.com/topic/stomachnormalhistology.html)
3. 🔗 [Normal Breast Ducts & Lobules (PathologyOutlines)](https://www.pathologyoutlines.com/topic/breastnormal.html)

---

#### 🔴 Adenocarcinoma
**Common Sites:** Colon, lung, breast, prostate, stomach, pancreas, endometrium

**H&E Appearance:**
- **Irregular, angulated, back-to-back glands** — "gland-in-gland" cribriform pattern
- **Nuclei are enlarged, hyperchromatic, stratified** (stacked on top of each other)
- Loss of basal nuclear polarity — nuclei move toward lumen
- **Prominent nucleoli** ("owl-eye" nucleoli in some types)
- **Mucin pools** with floating tumor cells = mucinous adenocarcinoma
- **Signet ring cells:** Nucleus pushed to periphery by intracellular mucin = aggressive
- Tumor cells invading through muscularis mucosae into submucosa
- **Desmoplastic stroma** is abundant

**Grading Hints (Colon – Gland Formation):**
| Grade | Gland Formation |
|-------|----------------|
| Well (G1) | >95% gland-forming |
| Moderate (G2) | 50–95% gland-forming |
| Poor (G3) | <50% gland-forming |

**Annotated Image Links:**
1. 🔗 [Colonic Adenocarcinoma – Gland Architecture (WebPathology)](https://www.webpathology.com/image.asp?case=14&n=1)
2. 🔗 [Lung Adenocarcinoma – Acinar Pattern (PathologyOutlines)](https://www.pathologyoutlines.com/topic/lungtumorsadenopatterns.html)
3. 🔗 [Breast Invasive Ductal Carcinoma (LibrePathology)](https://librepathology.org/wiki/Invasive_ductal_carcinoma_of_the_breast)

---

### 1.3 Transitional Epithelium (Urothelium)

#### 🟢 Normal Urothelium
**Location:** Bladder, ureter, renal pelvis

**H&E Appearance:**
- **3–7 cell layers** thick
- **"Umbrella cells"** at surface: Large, dome-shaped, binucleated cells — unique feature
- Intermediate cells: Pear-shaped, with oval nuclei
- Basal cells: Small, cuboidal
- Nuclei are uniform, round, with fine chromatin

**Annotated Image Links:**
1. 🔗 [Normal Urothelium – Umbrella Cells (WebPathology)](https://www.webpathology.com/image.asp?case=609&n=1)
2. 🔗 [Normal Bladder Histology (PathologyOutlines)](https://www.pathologyoutlines.com/topic/bladdernormal.html)
3. 🔗 [Urothelium – Leeds Virtual Pathology](https://www.virtualpathology.leeds.ac.uk)

---

#### 🔴 Urothelial Carcinoma (TCC)
**H&E Appearance:**
- **Loss of umbrella cells**
- Full-thickness cellular atypia (CIS = carcinoma in situ)
- Nuclei: large, irregular, hyperchromatic, prominent nucleoli
- **Papillary fronds** (low-grade) or flat, high-grade invasive nests
- Invasion into lamina propria = T1; muscularis propria = T2
- **Dyscohesion** — cells fall apart, single-cell infiltration

**Annotated Image Links:**
1. 🔗 [High-Grade Urothelial Carcinoma (WebPathology)](https://www.webpathology.com/image.asp?case=303&n=1)
2. 🔗 [Bladder TCC – Grading Guide (PathologyOutlines)](https://www.pathologyoutlines.com/topic/bladdertcc.html)
3. 🔗 [Urothelial CIS vs Papillary TCC (LibrePathology)](https://librepathology.org/wiki/Transitional_cell_carcinoma_of_the_bladder)

---

## 2. Connective Tissues

### 2.1 Fibrous / Stromal Connective Tissue

#### 🟢 Normal Fibrous Stroma
**H&E Appearance:**
- **Fibroblasts:** Spindle-shaped cells with elongated, pale nuclei — minimal cytoplasm
- **Collagen fibers:** Pink, wavy, eosinophilic bundles
- **Ground substance:** Pale/clear background
- Low cellularity — mostly acellular pink collagen
- Nuclei are spaced well apart, uniform in size

**Annotated Image Links:**
1. 🔗 [Normal Dermis – Fibroblasts & Collagen (WebPathology)](https://www.webpathology.com/image.asp?case=1028&n=3)
2. 🔗 [Normal Fibrous Connective Tissue (PathologyOutlines)](https://www.pathologyoutlines.com/topic/softtissuenormal.html)
3. 🔗 [Collagen & Fibroblast Histology (LibrePathology)](https://librepathology.org/wiki/Soft_tissue)

---

#### 🔴 Fibrosarcoma / Desmoplastic Stroma in Tumors
**H&E Appearance:**
- **Fibrosarcoma:** "Herringbone/Chevron" pattern — interlacing fascicles of spindle cells
- High cellularity, nuclear atypia, mitoses
- **Desmoplastic stroma in carcinomas:** Dense, hypocellular pink collagen surrounding tumor nests — "reactive" fibroblasts
- Keloid-like thick collagen bundles in some tumors

**Annotated Image Links:**
1. 🔗 [Fibrosarcoma – Herringbone Pattern (WebPathology)](https://www.webpathology.com/image.asp?case=261&n=1)
2. 🔗 [Desmoplastic Stroma in Breast Cancer (PathologyOutlines)](https://www.pathologyoutlines.com/topic/breastinvasiveductal.html)
3. 🔗 [Fibrosarcoma Histology (LibrePathology)](https://librepathology.org/wiki/Fibrosarcoma)

---

### 2.2 Adipose Tissue

#### 🟢 Normal Adipose Tissue
**H&E Appearance:**
- **Large, empty-appearing cells** — fat dissolved during processing, leaving empty vacuoles
- Thin rim of **pale cytoplasm** with **peripheral, flattened nucleus** ("signet ring-like" but benign)
- Delicate fibrovascular septa separating lobules
- Uniform cell size

**Annotated Image Links:**
1. 🔗 [Normal White Adipose Tissue (WebPathology)](https://www.webpathology.com/image.asp?case=412&n=1)
2. 🔗 [Normal Fat – Lobular Architecture (PathologyOutlines)](https://www.pathologyoutlines.com/topic/softtissuelipomaatypical.html)
3. 🔗 [Adipose Tissue Histology (LibrePathology)](https://librepathology.org/wiki/Lipoma)

---

#### 🔴 Liposarcoma
**H&E Appearance:**
- **Lipoblasts** = pathognomonic cells — multiple sharp cytoplasmic vacuoles "scalloping" the nucleus
- Well-differentiated liposarcoma: Resembles lipoma but with **atypical stromal cells**, hyperchromatic nuclei, variation in adipocyte size
- Myxoid liposarcoma: Pale blue myxoid background + delicate "chicken-wire" vasculature
- Pleomorphic liposarcoma: Bizarre giant cells, no recognizable fat

**Annotated Image Links:**
1. 🔗 [Liposarcoma – Lipoblasts (WebPathology)](https://www.webpathology.com/image.asp?case=270&n=1)
2. 🔗 [Well-Differentiated Liposarcoma (PathologyOutlines)](https://www.pathologyoutlines.com/topic/softtissueliposarcoma.html)
3. 🔗 [Myxoid Liposarcoma Histology (LibrePathology)](https://librepathology.org/wiki/Liposarcoma)

---

### 2.3 Cartilage & Bone

#### 🟢 Normal Cartilage (Hyaline)
**H&E Appearance:**
- **Chondrocytes** sit in **lacunae** (clear spaces within matrix)
- Matrix: Homogeneous, glassy, pale blue/purple — type II collagen
- Cells appear rounded, uniform
- No blood vessels in cartilage

**Annotated Image Links:**
1. 🔗 [Hyaline Cartilage – Lacunae & Chondrocytes (WebPathology)](https://www.webpathology.com/image.asp?case=823&n=1)
2. 🔗 [Normal Cartilage Histology (PathologyOutlines)](https://www.pathologyoutlines.com/topic/bonenormalhistology.html)
3. 🔗 [Cartilage Types – Virtual Pathology Leeds](https://www.virtualpathology.leeds.ac.uk)

---

#### 🔴 Chondrosarcoma / Osteosarcoma
**Chondrosarcoma H&E:**
- Hypercellular cartilage with **binucleated chondrocytes** and nuclear atypia
- More than one cell per lacuna = suspicious
- Myxoid change, necrosis in high grade

**Osteosarcoma H&E:**
- **Malignant osteoid** (pink, lace-like mineralizing matrix) produced by malignant spindle cells
- High-grade pleomorphic cells, atypical mitoses
- "Lace-like osteoid" = hallmark

**Annotated Image Links:**
1. 🔗 [Chondrosarcoma – Hypercellularity (WebPathology)](https://www.webpathology.com/image.asp?case=193&n=1)
2. 🔗 [Osteosarcoma – Malignant Osteoid (WebPathology)](https://www.webpathology.com/image.asp?case=195&n=1)
3. 🔗 [Osteosarcoma Histology (PathologyOutlines)](https://www.pathologyoutlines.com/topic/boneosteosarcoma.html)

---

## 3. Muscle Tissues

### 3.1 Smooth Muscle

#### 🟢 Normal Smooth Muscle
**Location:** Uterus (myometrium), GI tract wall, blood vessel walls

**H&E Appearance:**
- **Spindle-shaped cells** with **central, elongated "cigar-shaped" nuclei**
- Nuclei have blunt ends — key distinguishing feature from fibroblasts
- Arranged in **interlacing fascicles**
- Pale eosinophilic cytoplasm, no striations
- Cells are **tightly packed** with minimal intervening stroma

**Annotated Image Links:**
1. 🔗 [Normal Myometrium – Smooth Muscle Bundles (WebPathology)](https://www.webpathology.com/image.asp?case=714&n=1)
2. 🔗 [Smooth Muscle – GI Wall (PathologyOutlines)](https://www.pathologyoutlines.com/topic/colonrectumnormalhistology.html)
3. 🔗 [Uterine Smooth Muscle Histology (LibrePathology)](https://librepathology.org/wiki/Uterus)

---

#### 🔴 Leiomyosarcoma
**H&E Appearance:**
- Fascicles of spindle cells with **nuclear atypia** and **pleomorphism**
- **Cigar-shaped nuclei** still present but enlarged, hyperchromatic
- **Mitotic figures** > 5–10/10 HPF (high-power fields) = malignant
- Coagulative tumor cell necrosis ("ghost cells" — cells without nuclei)
- Compare with Leiomyoma (benign): same architecture but NO atypia, NO necrosis, < 5 mitoses/10 HPF

**Annotated Image Links:**
1. 🔗 [Leiomyosarcoma – Mitoses & Atypia (WebPathology)](https://www.webpathology.com/image.asp?case=259&n=1)
2. 🔗 [Uterine LMS vs Leiomyoma Comparison (PathologyOutlines)](https://www.pathologyoutlines.com/topic/uterusleiomyosarcoma.html)
3. 🔗 [Leiomyosarcoma Histology (LibrePathology)](https://librepathology.org/wiki/Leiomyosarcoma)

---

### 3.2 Skeletal Muscle

#### 🟢 Normal Skeletal Muscle
**H&E Appearance:**
- Large cells with **cross-striations** (transverse banding pattern)
- **Multiple peripheral nuclei** per cell (vs. smooth muscle: 1 central nucleus)
- Abundant **eosinophilic (pink) cytoplasm**
- Cells run in parallel bundles (fascicles)
- Endomysium (thin connective tissue) separates individual fibers

**Annotated Image Links:**
1. 🔗 [Normal Skeletal Muscle – Cross-Striations (WebPathology)](https://www.webpathology.com/image.asp?case=808&n=1)
2. 🔗 [Skeletal Muscle Histology – Longitudinal & Cross Section (PathologyOutlines)](https://www.pathologyoutlines.com/topic/softtissuenormal.html)
3. 🔗 [Skeletal Muscle – Peripheral Nuclei (LibrePathology)](https://librepathology.org/wiki/Soft_tissue)

---

#### 🔴 Rhabdomyosarcoma (RMS)
**H&E Appearance:**
- **"Strap cells"** or "tadpole cells" — elongated cells with cross-striations (rare but diagnostic)
- **Rhabdomyoblasts:** Round to oval cells with abundant pink cytoplasm
- Embryonal RMS: Loose myxoid stroma + primitive small round cells
- Alveolar RMS: Cells line fibrovascular septa like alveoli — very aggressive
- Pleomorphic RMS: Bizarre giant cells

**Annotated Image Links:**
1. 🔗 [Embryonal Rhabdomyosarcoma (WebPathology)](https://www.webpathology.com/image.asp?case=264&n=1)
2. 🔗 [Alveolar RMS – Fibrovascular Pattern (PathologyOutlines)](https://www.pathologyoutlines.com/topic/softtissuerhabdomyosarcoma.html)
3. 🔗 [RMS with Rhabdomyoblasts (LibrePathology)](https://librepathology.org/wiki/Rhabdomyosarcoma)

---

## 4. Neural Tissue

### 🟢 Normal Neural Tissue (Brain / Nerve)

#### Cerebral Cortex
**H&E Appearance:**
- **Neurons:** Large cells with **prominent central nucleolus**, abundant cytoplasm, Nissl substance (basophilic granules)
- **Neuropil:** Pale pink background — axons, dendrites, synapses
- **Astrocytes:** Small cells with pale nuclei and indistinct cytoplasm
- **Oligodendrocytes:** "Fried egg" appearance — round nucleus with clear halo (processing artifact)
- **Microglia:** Small, elongated dark nuclei; ramified shape

**Annotated Image Links:**
1. 🔗 [Normal Brain – Neurons & Glia (WebPathology)](https://www.webpathology.com/image.asp?case=505&n=1)
2. 🔗 [Normal Cerebral Cortex Histology (PathologyOutlines)](https://www.pathologyoutlines.com/topic/CNSnormal.html)
3. 🔗 [CNS Histology – Neurons, Astrocytes, Oligodendrocytes (LibrePathology)](https://librepathology.org/wiki/Brain)

---

#### 🔴 Glioblastoma (GBM) / Gliomas
**H&E Appearance:**
- **Pseudopalisading necrosis** = tumor cells arranging around areas of necrosis — HALLMARK of GBM
- **Microvascular proliferation** = glomeruloid vessel tufts ("ball of worms")
- High cellularity, nuclear pleomorphism, hyperchromasia
- Infiltrating pattern — tumor cells spread along white matter tracts
- **Gemistocytic astrocytes** in lower-grade astrocytomas: plump cells with abundant glassy pink cytoplasm
- **Oligodendroglioma:** "Fried egg" cells + "chicken-wire" vasculature

**Grade Indicators:**
| Feature | Grade II | Grade III | Grade IV (GBM) |
|---------|----------|-----------|----------------|
| Mitoses | Rare | Present | Many |
| Necrosis | Absent | Absent | Pseudopalisading |
| MVD | Absent | Absent | Glomeruloid tufts |

**Annotated Image Links:**
1. 🔗 [GBM – Pseudopalisading Necrosis (WebPathology)](https://www.webpathology.com/image.asp?case=508&n=1)
2. 🔗 [Glioblastoma Multiforme – Full Guide (PathologyOutlines)](https://www.pathologyoutlines.com/topic/cnstumorsgbm.html)
3. 🔗 [Oligodendroglioma vs Astrocytoma (LibrePathology)](https://librepathology.org/wiki/Glioblastoma_multiforme)

---

## 5. Hematopoietic & Lymphoid Tissue

### 5.1 Lymph Node

#### 🟢 Normal Lymph Node
**H&E Appearance:**
- **Cortex:** Lymphoid follicles — dense blue clusters
  - **Primary follicles:** Uniform, dark blue
  - **Secondary follicles:** Pale germinal center + dark mantle zone
- **Germinal center:** Large cells (centroblasts/centrocytes), tingible body macrophages (phagocytosing debris)
- **Paracortex:** T-cell zone — diffuse small lymphocytes
- **Medullary cords & sinuses:** Plasma cells, macrophages
- **Capsule:** Thin pink fibrous layer

**Annotated Image Links:**
1. 🔗 [Normal Lymph Node – Follicle Architecture (WebPathology)](https://www.webpathology.com/image.asp?case=604&n=1)
2. 🔗 [Lymph Node Histology – Annotated (PathologyOutlines)](https://www.pathologyoutlines.com/topic/lymphnodesnormal.html)
3. 🔗 [Secondary Follicle – Germinal Center (LibrePathology)](https://librepathology.org/wiki/Lymph_node)

---

#### 🔴 Lymphoma — Diffuse Large B-Cell Lymphoma (DLBCL)
**H&E Appearance:**
- **Effacement of normal architecture** — follicles destroyed
- **Diffuse sheets of large lymphoid cells**
- Cells 2–3x larger than normal lymphocytes
- **Vesicular nuclei** with **prominent nucleoli** (centroblastic type: multiple nucleoli at membrane; immunoblastic type: single central nucleolus)
- High mitotic rate
- Tingible body macrophages scattered = "starry sky pattern"

**Annotated Image Links:**
1. 🔗 [DLBCL – Effacement & Large Cells (WebPathology)](https://www.webpathology.com/image.asp?case=622&n=1)
2. 🔗 [DLBCL Histology Full Guide (PathologyOutlines)](https://www.pathologyoutlines.com/topic/lymphomaDLBCL.html)
3. 🔗 [Hodgkin vs DLBCL Comparison (LibrePathology)](https://librepathology.org/wiki/Diffuse_large_B-cell_lymphoma)

---

#### 🔴 Hodgkin Lymphoma (HL)
**H&E Appearance:**
- **Reed-Sternberg (RS) cells** = HALLMARK
  - Large binucleated/multinucleated cells
  - **"Owl-eye" nucleoli** — large, eosinophilic, prominent
  - Abundant pale cytoplasm
- Background: Mixed inflammatory cells — eosinophils, plasma cells, lymphocytes
- Lacunar variant RS cells in nodular sclerosis HL

**Annotated Image Links:**
1. 🔗 [Reed-Sternberg Cells – Owl-Eye Nucleoli (WebPathology)](https://www.webpathology.com/image.asp?case=630&n=1)
2. 🔗 [Hodgkin Lymphoma – All Subtypes (PathologyOutlines)](https://www.pathologyoutlines.com/topic/lymphomahodgkin.html)
3. 🔗 [Classic HL – Nodular Sclerosis (LibrePathology)](https://librepathology.org/wiki/Hodgkin_lymphoma)

---

### 5.2 Bone Marrow

#### 🟢 Normal Bone Marrow
**H&E Appearance:**
- **Cellularity:** ~50% cells, 50% fat (varies with age — "100 minus age" rule)
- **Hematopoietic cells:** Three lineages visible
  - **Erythroid:** Small, round cells, pink cytoplasm, dense nucleus
  - **Myeloid:** Large cells with horseshoe/multilobed nuclei (mature); round nuclei (immature)
  - **Megakaryocytes:** Giant cells with **multilobed, complex nucleus** — easy to spot
- Adipocytes as white spaces

**Annotated Image Links:**
1. 🔗 [Normal Bone Marrow Biopsy – All Lineages (WebPathology)](https://www.webpathology.com/image.asp?case=655&n=1)
2. 🔗 [Normal Marrow Histology (PathologyOutlines)](https://www.pathologyoutlines.com/topic/bonemarrownonneoplastic.html)
3. 🔗 [Bone Marrow – Megakaryocytes (LibrePathology)](https://librepathology.org/wiki/Bone_marrow)

---

#### 🔴 Acute Leukemia (AML/ALL)
**H&E Appearance:**
- **Hypercellular marrow** — fat spaces replaced by blasts
- **Blasts:** Immature cells with high N:C ratio, fine chromatin, prominent nucleoli
- **AML blasts:** May show **Auer rods** (pink rod-shaped inclusions in cytoplasm) — PATHOGNOMONIC
- Loss of normal trilineage maturation
- Megakaryocytes reduced or abnormal

**Annotated Image Links:**
1. 🔗 [AML – Hypercellular Marrow with Blasts (WebPathology)](https://www.webpathology.com/image.asp?case=661&n=1)
2. 🔗 [AML – Auer Rods Guide (PathologyOutlines)](https://www.pathologyoutlines.com/topic/leukemiaAML.html)
3. 🔗 [ALL vs AML Comparison (LibrePathology)](https://librepathology.org/wiki/Acute_myeloid_leukemia)

---

## 6. Hepatic (Liver) Tissue

#### 🟢 Normal Liver
**H&E Appearance:**
- **Hepatocytes:** Large, polygonal cells with **central round nucleus** + prominent nucleolus
- **Binucleated hepatocytes** are NORMAL (not alarming)
- Cells arranged in **1-cell-thick plates** (liver cell plates)
- **Portal tracts:** Contain portal vein branch, hepatic artery branch, bile duct
- **Sinusoids:** Between hepatocyte plates — lined by Kupffer cells (resident macrophages)
- **Central vein** at center of hepatic lobule

**Annotated Image Links:**
1. 🔗 [Normal Liver Lobular Architecture (WebPathology)](https://www.webpathology.com/image.asp?case=401&n=1)
2. 🔗 [Normal Liver Histology – Full Description (PathologyOutlines)](https://www.pathologyoutlines.com/topic/livernormal.html)
3. 🔗 [Liver – Portal Tract & Central Vein (LibrePathology)](https://librepathology.org/wiki/Liver)

---

#### 🔴 Hepatocellular Carcinoma (HCC)
**H&E Appearance:**
- Cells resemble hepatocytes but with **nuclear atypia, pleomorphism**
- **Thick liver cell plates** (> 2 cells thick = abnormal)
- **Bile production** — green bile pigment in cytoplasm (pathognomonic for hepatocellular origin)
- **Mallory-Denk bodies:** Eosinophilic cytoplasmic inclusions
- Loss of portal tract architecture
- **Pseudoacinar (pseudoglandular) pattern** — cells forming gland-like structures
- Venous invasion common

**Annotated Image Links:**
1. 🔗 [HCC – Thick Trabeculae & Bile Production (WebPathology)](https://www.webpathology.com/image.asp?case=404&n=1)
2. 🔗 [Hepatocellular Carcinoma – Grading Guide (PathologyOutlines)](https://www.pathologyoutlines.com/topic/liverhcc.html)
3. 🔗 [HCC vs Cholangiocarcinoma (LibrePathology)](https://librepathology.org/wiki/Hepatocellular_carcinoma)

---

## 7. Key Tumor Concepts Glossary

| Term | Definition | Significance |
|------|-----------|--------------|
| **Pleomorphism** | Variable cell/nuclear size and shape | Marker of malignancy |
| **Hyperchromasia** | Dark-staining nuclei (more DNA) | High nuclear activity |
| **N:C Ratio** | Nuclear:Cytoplasmic ratio | Elevated in malignant cells |
| **Mitotic figure** | Cell in active division (dark clumped chromatin) | High = aggressive |
| **Atypical mitosis** | Tripolar/multipolar spindle | Strong malignancy marker |
| **Necrosis** | Ghost outlines of dead cells | Common in high-grade tumors |
| **Desmoplasia** | Dense fibrous stroma around tumor | Reactive stroma response |
| **Invasion** | Tumor crossing basement membrane | Defines malignancy |
| **Keratin pearl** | Concentric whorls of keratin | SCC marker |
| **Auer rod** | Pink cytoplasmic rod in blasts | AML pathognomonic |
| **Reed-Sternberg cell** | Binucleated owl-eye giant cell | Hodgkin lymphoma |
| **Lipoblast** | Multi-vacuolated cell scalloping nucleus | Liposarcoma marker |
| **Pseudopalisading** | Tumor cells around central necrosis | GBM hallmark |
| **Starry sky** | Tingible-body macrophages in blue lymphoid background | Burkitt/DLBCL |
| **Signet ring cell** | Mucin pushes nucleus to side | Mucinous adenocarcinoma |

---

## 8. Quick Comparison Cheat Sheet

```
NORMAL CELL                         MALIGNANT CELL
─────────────────────────────────────────────────────────────
Small, uniform nucleus          →   Large, irregular nucleus
Fine, dispersed chromatin       →   Coarse, hyperchromatic
Inconspicuous nucleolus         →   Prominent nucleolus
Low N:C ratio                   →   High N:C ratio
Rare mitoses                    →   Frequent/atypical mitoses
Organized architecture          →   Disorganized, infiltrative
Single cell layer (epithelium)  →   Stratified, irregular
Even spacing between cells      →   Crowded, overlapping nuclei
Maintained polarity             →   Loss of polarity
No necrosis                     →   Coagulative/geographic necrosis
```

---

## 📚 Recommended Learning Resources

| Resource | Best For | Link |
|----------|---------|------|
| **WebPathology** | Case-based H&E images | https://www.webpathology.com |
| **PathologyOutlines** | Comprehensive diagnostic criteria | https://www.pathologyoutlines.com |
| **LibrePathology** | Open-access, beginner-friendly | https://librepathology.org |
| **Leeds Virtual Pathology** | Virtual slides, high magnification | https://www.virtualpathology.leeds.ac.uk |
| **PathPresenter** | Annotated digital slides | https://www.pathpresenter.net |
| **TCGA Pathology Portal** | Cancer genomics + histology | https://portal.gdc.cancer.gov |
| **Human Protein Atlas** | Normal tissue H&E + IHC | https://www.proteinatlas.org |
| **PathoPic** | University of Basel image library | https://www.patho.unibas.ch |

---

> 💡 **Beginner Tips:**
> 1. **Start at low power (4x–10x):** Assess architecture first — arrangement of cells and glands
> 2. **Move to high power (40x):** Evaluate nuclear features — size, shape, chromatin, nucleoli
> 3. **Count mitoses at 40x** in the most cellular ("hot spot") area
> 4. **Normal = organized. Abnormal = chaotic** — use this as your first filter
> 5. **Compare to adjacent normal tissue** always present on the same slide

---

## Summary

> [!TIP] Cornell Summary
> H&E interpretation starts with tissue identification (epithelial, connective, muscle, nervous, lymphoid), then assesses architecture at low power and cytology at high power. Normal tissue is organized with predictable patterns; tumors disrupt architecture (loss of polarity, irregular glands, solid sheets), alter nuclei (enlargement, pleomorphism, hyperchromasia, prominent nucleoli), and increase mitotic activity. Desmoplastic stroma and inflammatory infiltrates are additional H&E clues. For digital pathology, the key insight is: normal = organized, abnormal = chaotic — use this as your first computational filter.

---

*Guide compiled for educational purposes. Always correlate with clinical, radiological, and IHC findings for diagnosis.*

---

## Related

- [[Digital Pathology MOC]]
- [[Beginner Digital Pathology Guide for H&E]]
- [[Histopathology and H&E Interpretation]]
- [[Cancer Biology MOC]]
- [[Computational Pathology MOC]]
