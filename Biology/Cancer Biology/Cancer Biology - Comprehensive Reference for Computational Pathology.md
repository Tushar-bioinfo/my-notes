---
tags:
  - biology
  - cancer-biology
  - computational-pathology
aliases:
  - Cancer Biology Reference
---
# Cancer Biology: A Comprehensive Reference for Computational Pathology 
Researchers

---

## Table of Contents

1. [The Cell: Molecular 
Architecture](#1-the-cell-molecular-architecture)
2. [DNA, Genes, and the 
Central Dogma](#2-dna-genes-and-the-central-dogma)
3. [Mutations and Genomic 
Alterations](#3-mutations-and-genomic-alterations)
4. [Oncogenes and Tumor Suppressors](#4-oncogenes-and-tumor-suppressors)
5. [The Hallmarks of Cancer](#5-the-hallmarks-of-cancer)
6. [Cell Cycle Deregulation](#6-cell-cycle-deregulation)
7. [Signal Transduction in Cancer](#7-signal-transduction-in-cancer)
8. [Epigenetics in Cancer](#8-epigenetics-in-cancer)
9. [Tumor Evolution and 
Heterogeneity](#9-tumor-evolution-and-heterogeneity)
10. [The Tumor Microenvironment](#10-the-tumor-microenvironment)
11. [Immune Evasion and Immunology](#11-immune-evasion-and-immunology)
12. [Angiogenesis and Metastasis](#12-angiogenesis-and-metastasis)
13. [Cancer Metabolism](#13-cancer-metabolism)
14. [Histopathology and H&E 
Interpretation](#14-histopathology-and-he-interpretation)
15. [Molecular Classification of 
Cancer](#15-molecular-classification-of-cancer)
16. [Spatial Biology and the TME](#16-spatial-biology-and-the-tme)
17. [Clinical Relevance for Computational 
Pathology](#17-clinical-relevance-for-computational-pathology)
18. [Glossary](#18-glossary)
19. [References](#19-references)

---

## 1. The Cell: Molecular Architecture

### 1.1 Cellular Organization

Every eukaryotic cell is partitioned into functionally distinct 
compartments. Understanding these is not merely academic — each 
compartment harbors proteins that are mutated, overexpressed, or lost in 
cancer, and many of these alterations produce morphological changes 
visible in H&E.

```
┌─────────────────────────────────────────────────────────────────────┐
│                         PLASMA MEMBRANE                              │
│  - Phospholipid bilayer with embedded proteins                      │
│  - Receptor tyrosine kinases (RTKs): EGFR, HER2, FGFR, VEGFR      │
│  - G-protein coupled receptors (GPCRs)                              │
│  - Cell adhesion molecules: E-cadherin, integrins, selectins        │
│  - MHC class I (antigen presentation — immune evasion target)      │
│  - Transporters and ion channels                                    │
│                                                                      │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │                      CYTOPLASM                               │   │
│   │                                                              │   │
│   │  ┌───────────────────────────────────────────────────────┐  │   │
│   │  │                    NUCLEUS                             │  │   │
│   │  │  - Nuclear envelope (double membrane with pores)      │  │   │
│   │  │  - Chromatin (DNA + histones)                         │  │   │
│   │  │    • Euchromatin: open, transcriptionally active       │  │   │
│   │  │    • Heterochromatin: condensed, transcriptionally     │  │   │
│   │  │      silent                                            │  │   │
│   │  │  - Nucleolus: ribosomal RNA synthesis                  │  │   │
│   │  │    (prominent in cancer cells = active ribosome        │  │   │
│   │  │     biogenesis)                                        │  │   │
│   │  │  - Nuclear bodies: Cajal bodies, PML bodies            │  │   │
│   │  └───────────────────────────────────────────────────────┘  │   │
│   │                                                              │   │
│   │  MITOCHONDRIA                                                │   │
│   │  - Oxidative phosphorylation (ATP production)                │   │
│   │  - Apoptosis initiation: cytochrome c release               │   │
│   │  - Warburg effect: cancer cells shift away from OXPHOS      │   │
│   │  - Mitochondrial DNA mutations found in some cancers       │   │
│   │                                                              │   │
│   │  ENDOPLASMIC RETICULUM                                       │   │
│   │  - Rough ER: ribosome-studded, protein synthesis            │   │
│   │  - Smooth ER: lipid synthesis, detoxification               │   │
│   │  - ER stress → unfolded protein response (UPR) in tumors    │   │
│   │                                                              │   │
│   │  GOLGI APPARATUS                                              │   
│
│   │  - Post-translational modification, sorting, secretion       │   
│
│   │  - Aberrant glycosylation in cancer (altered cell surface)  │   │
│   │                                                              │   │
│   │  LYSOSOMES & AUTOPHAGOSOMES                                  │   │
│   │  - Degradation of macromolecules                             │   │
│   │  - Autophagy: survival mechanism under stress                │   │
│   │  - Controversial role in cancer: tumor-suppressive vs.       │   │
│   │    tumor-promoting depending on context                      │   │
│   │                                                              │   │
│   │  CYTOSKELETON                                                │   │
│   │  - Microfilaments (actin): cell shape, motility               │   
│
│   │  - Microtubules (tubulin): mitotic spindle, intracellular    │   
│
│   │    transport (chemotherapy target: taxanes)                  │   
│
│   │  - Intermediate filaments: structural support                │   
│
│   │    • Cytokeratins (epithelial — important diagnostic marker) │   
│
│   │    • Vimentin (mesenchymal — EMT marker)                     │   
│
│   │                                                              │   
│
│   │  CENTROSOME                                                   │   
│
│   │  - Microtubule organizing center                             │   │
│   │  - Amplification in cancer → multipolar spindles →           │   │
│   │    chromosomal instability (CIN)                              │   
│
│   │                                                              │   
│
│   └──────────────────────────────────────────────────────────────┘   
│
│                                                                      
│
└─────────────────────────────────────────────────────────────────────┘
```

### 1.2 Key Molecular Players

| Molecule Type | Function | Cancer Relevance |
|---|---|---|
| **DNA** | Information storage | Mutations, translocations, copy number 
alterations |
| **RNA** | Information transfer, regulation | Alternative splicing in 
cancer, miRNA dysregulation, lncRNA in oncogenesis |
| **Proteins** | Effectors of all cellular processes | Mutant proteins 
with gain/loss of function, overexpression, mislocalization |
| **Lipids** | Membrane structure, signaling | Altered membrane 
composition, PI3K lipid signaling |
| **Glycans** | Cell surface modification | Aberrant glycosylation is a 
universal cancer feature |
| **Metabolites** | Energy, building blocks, signaling | Metabolic 
rewiring (Warburg effect, glutamine addiction) |

### 1.3 Cell-Cell and Cell-Matrix Interactions

Normal tissue architecture depends on adhesive interactions:

```
EPITHELIAL CELLS (connected to each other)
    │
    ├── Tight junctions (occludin, claudins)     → Barrier function
    │                                                Loss in cancer → 
disruption of polarity
    │
    ├── Adherens junctions (E-cadherin/β-catenin) → Cell-cell adhesion
    │                                                Loss of E-cadherin 
→ EMT → invasion
    │                                                β-catenin → Wnt 
signaling when freed
    │
    ├── Desmosomes (desmoglein, desmocollin)      → Mechanical 
attachment
    │
    └── Gap junctions (connexins)                  → Intercellular 
communication
    
EPITHELIAL CELLS (connected to basement membrane)
    │
    └── Hemidesmosomes (integrin α6β4 → laminin)  → Anchorage to 
basement membrane
                                                    Loss → detachment → 
invasion

BASEMENT MEMBRANE
    - Type IV collagen, laminin, nidogen, perlecan
    - The KEY barrier between in situ and invasive carcinoma
    - Breached during invasion → cancer becomes invasive
```

The loss of these adhesive structures is directly visible in H&E as the 
transition from organized, well-demarcated epithelial islands to 
infiltrative, irregular cell clusters.

---

## 2. DNA, Genes, and the Central Dogma

### 2.1 Genome Organization

The human genome contains ~3.2 billion base pairs distributed across 23 
chromosome pairs (46 total chromosomes: 22 pairs of autosomes + 1 pair 
of sex chromosomes).

```
GENOME COMPOSITION:
┌─────────────────────────────────────────────────┐
│  ~1-2%    Protein-coding genes (~20,000)        │
│           Exons (actually translated)           │
│                                                  │
│  ~25-30%  Introns (transcribed but spliced out) │
│           Regulatory sequences (promoters,       │
│           enhancers, silencers, insulators)     │
│                                                  │
│  ~50-60%  Repetitive sequences                   │
│           - LINEs (Long Interspersed Nuclear     │
│             Elements) — can be retrotransposed   │
│           - SINEs (Short Interspersed Nuclear    │
│             Elements, e.g., Alu)                │
│           - Satellite DNA, telomeres             │
│           - Endogenous retroviruses              │
│                                                  │
│  ~5-10%   Non-coding RNAs                       │
│           - miRNAs (~2,000)                      │
│           - lncRNAs (~60,000+)                  │
│           - circRNAs, piRNAs, snoRNAs           │
│                                                  │
│  NOTE: "Junk DNA" is a misnomer. Much of the    │
│  non-coding genome has regulatory functions.     │
│  Cancer-associated mutations frequently occur    │
│  in non-coding regulatory elements.              │
└─────────────────────────────────────────────────┘
```

### 2.2 The Central Dogma — Expanded

The original dogma (DNA → RNA → Protein) has been substantially 
elaborated:

```
                    ┌──────────────┐
                    │   DNA        │
                    │ (genome)     │
                    └──────┬───────┘
                           │
                    TRANSCRIPTION (RNA polymerase II)
                    Regulated by:
                    • Chromatin accessibility (histone modifications)
                    • Transcription factors (TFs)
                    • Enhancers (can be millions of bp away)
                    • Promoter methylation (silencing)
                    • Insulators (CTCF protein)
                           │
                           ▼
                    ┌──────────────┐
                    │  pre-mRNA    │
                    └──────┬───────┘
                           │
                    RNA PROCESSING
                    • 5' capping
                    • 3' polyadenylation
                    • SPLICING: introns removed, exons joined
                      - Alternative splicing → multiple protein isoforms
                      - Dysregulated in cancer: exon skipping, intron 
retention
                      - Splicing factor mutations (SF3B1, U2AF1) in 
myeloid cancers
                           │
                           ▼
                    ┌──────────────┐
                    │ Mature mRNA  │
                    └──────┬───────┘
                           │
                    REGULATION AT RNA LEVEL
                    • miRNA binding → degradation or translational 
repression
                      (miR-21, miR-155 are oncomiRs; let-7 is tumor 
suppressive)
                    • lncRNA interactions (XIST, HOTAIR, MALAT1)
                    • RNA-binding proteins (RBPs)
                    • RNA modifications (m6A, m5C — epitranscriptomics)
                    • mRNA stability/degradation
                           │
                           ▼
                    TRANSLATION (ribosomes)
                    Regulated by:
                    • mTOR signaling (controls ribosome biogenesis, 
translation)
                    • eIF4E (eukaryotic initiation factor — oncogenic 
when amplified)
                    • Upstream open reading frames (uORFs)
                           │
                           ▼
                    ┌──────────────┐
                    │   Protein    │
                    └──────┬───────┘
                           │
                    POST-TRANSLATIONAL MODIFICATION
                    • Phosphorylation (kinases/phosphatases)
                    • Ubiquitination (proteasomal degradation — MDM2/p53 
axis)
                    • Acetylation (histone 
acetyltransferases/deacetylases)
                    • Methylation, glycosylation, SUMOylation, 
nitrosylation
                           │
                           ▼
                    PROTEIN FATE
                    • Correct folding (chaperones: HSP90 — cancer 
dependency)
                    • Subcellular localization (nuclear import/export)
                    • Complex formation (dimerization, multi-protein 
complexes)
                    • Degradation (ubiquitin-proteasome system, 
autophagy)
```

### 2.3 Gene Regulation — The Layers

Understanding gene regulation is essential because cancer is 
fundamentally a disease of dysregulated gene expression:

```
Layer 1: CHROMATIN ACCESSIBILITY
   ┌──────────────────────────────────────────┐
   │  Closed chromatin (heterochromatin)      │
   │  → DNA wrapped tightly around histones   │
   │  → Transcription factors cannot bind     │
   │  → Gene is OFF                           │
   │                                          │
   │  Open chromatin (euchromatin)            │
   │  → Nucleosomes spaced apart              │
   │  → DNA accessible to TFs                │
   │  → Gene can be ON                        │
   │                                          │
   │  Controlled by:                          │
   │  • Histone acetylation (H3K27ac) → open  │
   │  • Histone methylation (H3K27me3) → closed│
   │  • ATP-dependent chromatin remodelers    │
   │    (SWI/SNF — mutated in ~20% of cancers)│
   │  • DNA methylation at CpG islands        │
   └──────────────────────────────────────────┘

Layer 2: TRANSCRIPTIONAL REGULATION
   ┌──────────────────────────────────────────┐
   │  Promoter: ~1kb upstream of TSS          │
   │  → Core promoter (TATA box, initiator)  │
   │  → Proximal promoter elements            │
   │                                          │
   │  Enhancers: can be millions of bp away   │
   │  → Loop to promoter via mediator complex │
   │  → Tissue-specific gene expression        │
   │  → Super-enhancers: clusters of enhancers│
   │    driving oncogene expression in cancer  │
   │                                          │
   │  Silencers/Insulators:                    │
   │  → CTCF protein marks boundaries         │
   │  → Topologically associating domains      │
   │    (TADs) organize chromatin into loops   │
   │  → TAD disruption in cancer can bring    │
   │    enhancers near oncogenes (e.g., TAL1   │
   │    activation in T-ALL via enhancer hijacking)│
   └──────────────────────────────────────────┘

Layer 3: EPIGENETIC MEMORY
   ┌──────────────────────────────────────────┐
   │  Polycomb Repressive Complex 2 (PRC2)    │
   │  → Deposits H3K27me3 → gene silencing    │
   │  → EZH2 is the catalytic subunit         │
   │  → EZH2 gain-of-function mutations in    │
   │    lymphoma (silences tumor suppressors) │
   │  → EZH2 inhibitors are FDA-approved     │
   │                                          │
   │  DNA methylation:                         │
   │  → CpG island hypermethylation in cancer │
   │    silences tumor suppressors without     │
   │    mutating the DNA sequence              │
   │  → CpG island methylator phenotype       │
   │    (CIMP) in glioma, colorectal cancer   │
   │  → DNMT3A mutations in AML               │
   │  → Demethylating agents: azacitidine,   │
   │    decitabine                             │
   └──────────────────────────────────────────┘
```

---

## 3. Mutations and Genomic Alterations

### 3.1 Types of Somatic Alterations in Cancer

```
╔════════════════════════════════════════════════════════════════════════╔══════════════════════════════════════════════════════════════════════════╗
║                    SOMATIC ALTERATIONS IN CANCER                       
  ║
╠════════════════════════════════════════════════════════════════════════╠══════════════════════════════════════════════════════════════════════════╣
║                                                                        
  ║
║  SINGLE NUCLEOTIDE VARIANTS (SNVs)                                     
 ║
║  - Most common type of somatic mutation                                
 ║
║  - Transition: purine→purine (A↔G) or pyrimidine→pyrimidine (C↔T)      
║
║  - Transversion: purine↔pyrimidine                                     
 ║
║  - C→T transitions at CpG sites = most common mutation in cancer       
 ║
║  - Mutational signatures: specific patterns reveal etiology            
  ║
║    • Signature 1 (C>T at CpG): aging/deamination                       
  ║
║    • Signature 2 (C>T at TpC): APOBEC activity                         
  ║
║    • Signature 4 (C>A): tobacco smoking                                
  ║
║    • Signature 7 (C>T at dipyrimidine): UV exposure                    
  ║
║    • Signature 3: HR deficiency (BRCA1/2 mutations)                    
  ║
║    • ~50+ signatures catalogued (COSMIC database)                      
  ║
║                                                                        
  ║
║  SMALL INSERTIONS AND DELETIONS (INDELs)                               
 ║
║  - Frameshift mutations in coding regions → truncated or altered 
proteins║
║  - Microsatellite instability (MSI) → frameshifts in repetitive        
 ║
║    sequences → hallmark of mismatch repair deficiency                  
  ║
║                                                                        
  ║
║  COPY NUMBER ALTERATIONS (CNAs)                                        
 ║
║  - Amplifications: oncogenes (MYC, HER2/ERBB2, EGFR, MDM2, CCND1)     
║
║  - Deletions: tumor suppressors (CDKN2A, PTEN, RB1, SMAD4)            
 ║
║  - Focal amplifications vs. whole chromosome/arm gains                 
 ║
║  - Copy number neutral loss of heterozygosity (CN-LOH): uniparental    
║
║    disomy → both copies carry mutant allele                            
  ║
║                                                                        
  ║
║  STRUCTURAL VARIANTS (SVs)                                             
 ║
║  - Translocations: t(9;22) BCR-ABL in CML, t(14;18) BCL2 in follicular 
║
║    lymphoma, t(11;14) CCND1 in mantle cell lymphoma                    
 ║
║  - Inversions, tandem duplications                                     
  ║
║  - Chromothripsis: catastrophic shattering and reassembly of one or    
 ║
║    a few chromosomes → dozens of rearrangements in one event           
 ║
║  - Chromoplexy: coordinated rearrangements across multiple chromosomes 
 ║
║  - BFB (breakage-fusion-bridge) cycles → gene amplification            
 ║
║  - Extrachromosomal DNA (ecDNA): circular DNA fragments carrying       
║
║    oncogenes, can segregate unevenly, drive rapid evolution            
  ║
║                                                                        
  ║
║  WHOLE GENOME DUPLICATION (WGD)                                        
 ║
║  - Occurs in ~30% of cancers                                           
║
║  - Tetraploidy → subsequent loss of chromosomes → aneuploidy           
 ║
║  - Promotes genomic instability                                        
 ║
║                                                                        
  ║
╚════════════════════════════════════════════════════════════════════════╚══════════════════════════════════════════════════════════════════════════╝
```

### 3.2 Mutational Processes and Signatures

Each mutational process leaves a characteristic pattern:

```
EXAMPLE: UV-INDUCED MUTAGENESIS (Signature 7)

  UV light → pyrimidine dimers (C-C, C-T, T-C, T-T)
  → If not repaired by NER (nucleotide excision repair)
  → C>T transitions at dipyrimidine sites
  → CC>TT tandem mutations (pathognomonic for UV)
  
  Clinical relevance:
  → Melanoma, squamous cell carcinoma of skin
  → If you see Signature 7 in a tumor → sun exposure was the cause
  → This is how we know a cancer is UV-driven vs. something else

EXAMPLE: APOBEC MUTAGENESIS (Signatures 2 and 13)

  APOBEC (Apolipoprotein B mRNA Editing Catalytic Polypeptide-like)
  → Cytidine deaminases, normally antiviral defense
  → In cancer: off-target activity on genomic DNA
  → C>T and C>G at TCA/T motifs
  → Common in bladder, breast, head/neck, lung cancers
  → APOBEC activity creates "kataegis" (localized hypermutation 
clusters)
  → Active process → ongoing mutation → therapeutic 
vulnerability?
```

### 3.3 DNA Repair Pathways and Their Deficiencies

Defective DNA repair is a root cause of genomic instability:

| Repair Pathway | Type of Damage | Key Genes | Cancer Association |
|---|---|---|---|
| **Mismatch Repair (MMR)** | Base-base mismatches, insertion/deletion 
loops | MLH1, MSH2, MSH6, PMS2 | Lynch syndrome, MSI-high tumors, ~15% 
colorectal cancer |
| **Homologous Recombination (HR)** | Double-strand breaks, interstrand 
crosslinks | BRCA1, BRCA2, PALB2, RAD51, ATM, CHEK2 | Hereditary 
breast/ovarian cancer, pancreatic cancer; PARP inhibitor sensitivity |
| **Non-Homologous End Joining (NHEJ)** | Double-strand breaks | 
KU70/80, DNA-PKcs, XRCC4, LIG4 | Lymphoid malignancies (V(D)J 
recombination defects) |
| **Nucleotide Excision Repair (NER)** | Bulky adducts, UV-induced 
pyrimidine dimers | XPA-XPG, ERCC1-6 | Xeroderma pigmentosum (extreme UV 
sensitivity → skin cancers) |
| **Base Excision Repair (BER)** | Oxidized, alkylated, deaminated bases 
| OGG1, MUTYH, APE1, XRCC1 | MUTYH-associated polyposis |
| **Fanconi Anemia Pathway** | Interstrand crosslinks | FANCA-FANCW (22 
genes) | Fanconi anemia → AML, squamous cell carcinomas |
| **Translesion Synthesis (TLS)** | Replication past DNA damage | POLη, 
POLι, REV1, REV3L | XP-variant; polymerase η defects → UV mutagenesis |

**Clinical significance of DNA repair deficiencies:**

```
MMR deficiency / MSI-High:
  → Pembrolizumab (anti-PD-1) FDA-approved for ANY MSI-H solid tumor
  → First tissue-agnostic FDA approval
  → High mutational burden → neoantigens → immune recognition
  → Can be detected by: IHC for MMR proteins, PCR for microsatellites,
    or NGS-based MSI scoring

HR deficiency (BRCA1/2 mutations):
  → PARP inhibitors (olaparib, rucaparib, niraparib, talazoparib)
  → Synthetic lethality: HR-deficient cells depend on PARP for repair
  → PARP inhibition → accumulation of DNA damage → cell death in 
HR-deficient cells
  → Normal cells (HR-proficient) can survive PARP inhibition
  → "BRCAness" phenotype: HR deficiency without BRCA mutation → may also 
respond
  → HR deficiency score (Myriad myChoice, FoundationFocus)
```

---

## 4. Oncogenes and Tumor Suppressors

### 4.1 Oncogenes — Detailed Mechanisms

Oncogenes arise from proto-oncogenes through gain-of-function 
alterations. A single mutant allele is sufficient (dominant).

```
MECHANISMS OF ONCOGENE ACTIVATION:

1. POINT MUTATION (constitutive activation)
   ┌─────────────────────────────────────────────────────────────┐
   │  KRAS: G12D, G12V, G12C, G13D mutations                  │
   │  → Glycine at position 12 replaced by Asp/Val/Cys/Asp    │
   │  → GTP hydrolysis prevented → RAS always in GTP-bound    │
   │    (active) state                                          │
   │  → Downstream MAPK and PI3K signaling always on           │
   │  → Found in: pancreatic (90%), colorectal (45%),           │
   │    lung adenocarcinoma (30%)                               │
   │  → G12C specifically targetable (sotorasib, adagrasib)    │
   └─────────────────────────────────────────────────────────────┘

2. GENE AMPLIFICATION (overexpression)
   ┌─────────────────────────────────────────────────────────────┐
   │  HER2/ERBB2: amplification in 15-20% of breast cancer     │
   │  → 20-50 copies of the gene → massive HER2 overexpression │
   │  → Excessive growth factor signaling                       │
   │  → Targetable with trastuzumab, pertuzumab, T-DM1         │
   │                                                             │
   │  MYC: amplified in many cancers                            │
   │  → Transcription factor driving growth and metabolism       │
   │  → "Undruggable" — but a major cancer dependency           │
   │  → Myc-amplified tumors show distinct H&E features:        │
   │    large nuclei, prominent nucleoli, high mitotic rate     │
   │                                                             │
   │  EGFR: amplified in glioblastoma, lung cancer              │
   │  → EGFRvIII: deletion mutant, constitutively active        │
   └─────────────────────────────────────────────────────────────┘

3. CHROMOSOMAL TRANSLOCATION (novel fusion protein or deregulated 
expression)
   ┌─────────────────────────────────────────────────────────────┐
   │  t(9;22)(q34;q11) → BCR-ABL1 fusion in CML               │
   │  → Constitutively active tyrosine kinase                   │
   │  → Drives proliferation, inhibits apoptosis                │
   │  → Targeted by imatinib (Gleevec) — paradigm of targeted  │
   │    therapy                                                  │
   │                                                             │
   │  t(14;18) → IGH-BCL2 in follicular lymphoma               │
   │  → BCL2 overexpression under immunoglobulin heavy chain   │
   │    enhancer → anti-apoptotic → cells can't die             │
   │                                                             │
   │  t(8;14) → IGH-MYC in Burkitt lymphoma                    │
   │  → MYC overexpression → explosive proliferation            │
   │  → H&E: "starry sky" appearance (macrophages consuming     │
   │    apoptotic tumor cells against a background of rapidly    │
   │    dividing dark blue lymphocytes)                         │
   │                                                             │
   │  TMPRSS2-ERG fusion in ~50% of prostate cancers            │
   │  → Androgen-responsive promoter (TMPRSS2) drives ETS      │
   │    transcription factor (ERG) overexpression               │
   └─────────────────────────────────────────────────────────────┘

4. VIRAL ONCOGENE INSERTION
   ┌─────────────────────────────────────────────────────────────┐
   │  HPV E6/E7 in cervical, oropharyngeal cancer              │
   │  → E6 degrades p53 → loss of tumor suppressor             │
   │  → E7 inactivates RB → loss of cell cycle control          │
   │  → Together: dismantle the two most important tumor        │
   │    suppressor pathways simultaneously                     │
   │                                                             │
   │  EBV in nasopharyngeal carcinoma, Burkitt lymphoma,       │
   │  gastric cancer                                             │
   │  → LMP1 mimics CD40 signaling → proliferation              │
   │  → EBNA1 maintains viral genome, alters host gene          │
   │    expression                                               │
   └─────────────────────────────────────────────────────────────┘
```

### 4.2 Tumor Suppressor Genes — Detailed Mechanisms

Tumor suppressors require loss-of-function in BOTH alleles (Knudson's 
two-hit hypothesis), though haploinsufficiency exists for some genes.

```
CLASSIC TWO-HIT MODEL (Knudson):
  Retinoblastoma as the paradigm:
  
  Hereditary form:
    Individual born with ONE mutant RB1 allele (germline)
    → Every cell has one hit
    → Only one more somatic hit needed → very high penetrance
    → Often bilateral
    → Explains familial cancer syndromes
  
  Sporadic form:
    Individual born with TWO normal RB1 alleles
    → Need TWO independent somatic hits in the same cell
    → Very low probability
    → Usually unilateral
    → Explains sporadic (non-familial) cancer

MOLECULAR MECHANISMS OF TUMOR SUPPRESSOR INACTIVATION:

  First hit:  Point mutation, frameshift, deletion, promoter methylation
  Second hit: Loss of heterozygosity (LOH), deletion, promoter 
methylation,
              point mutation, CN-LOH

  Note: Promoter hypermethylation can serve as a "hit" without
        changing the DNA sequence — this is an epigenetic mechanism
        of tumor suppressor silencing.
```

**Detailed Tumor Suppressor Profiles:**

```
TP53 — "Guardian of the Genome"
┌─────────────────────────────────────────────────────────────────────┐
│  Chromosomal location: 17p13.1                                       │
│  Protein: p53, 393 amino acids, transcription factor                │
│  Mutated in: >50% of ALL human cancers (most commonly mutated gene) │
│                                                                      │
│  Normal function:                                                    │
│  1. SENSES DNA damage → activated by ATM/ATR kinases               │
│  2. ACTIVATES transcription of:                                      │
│     • p21 → cell cycle arrest (G1/S checkpoint)                    │
│     • GADD45 → DNA repair                                           │
│     • PUMA, NOXA, BAX → apoptosis (if damage irreparable)         │
│  3. METABOLIC regulation:                                            │
│     • Suppresses glycolysis (TIGAR)                                 │
│     • Activates oxidative phosphorylation (SCO2)                    │
│  4. ANGIOGENESIS inhibition:                                         │
│     • Activates thrombospondin-1 (TSP1) → anti-angiogenic          │
│  5. CELLULAR SENESCENCE: permanent cell cycle arrest                 │
│                                                                      │
│  How it's inactivated in cancer:                                     │
│  • Missense mutations in DNA-binding domain (most common):          │
│    - R175H, R248Q, R273H ("hotspot" mutations)                    │
│    - Mutant p53 acts as dominant negative (tetramer with wild-type) │
│    - Some mutations confer GAIN OF FUNCTION (mutant p53 actively   │
│      promotes invasion, metastasis, chemoresistance)                │
│  • Deletion of 17p (loss of one allele)                             │
│  • MDM2 amplification (MDM2 ubiquitinates p53 → proteasomal        │
│    degradation — functional equivalent of TP53 mutation)             │
│  • ARF (CDKN2A) deletion → cannot inhibit MDM2 → p53 degraded      │
│  • Viral oncoproteins: HPV E6, HBV HBx → p53 degradation          │
│                                                                      │
│  H&E correlation:                                                    │
│  • TP53-mutant tumors often show: high-grade morphology,           │
│    increased nuclear pleomorphism, high mitotic rate, necrosis     │
│  • But not always — some TP53-mutant tumors are deceptively        │
│    well-differentiated                                               │
│  • This is why molecular testing is essential                       │
└─────────────────────────────────────────────────────────────────────┘

RB1 — "The Gatekeeper"
┌─────────────────────────────────────────────────────────────────────┐
│  Chromosomal location: 13q14.2                                       │
│  Protein: RB (Retinoblastoma protein), 928 amino acids               │
│                                                                      │
│  Normal function:                                                    │
│  - Hypophosphorylated RB binds E2F transcription factors             │
│  - E2F is the master regulator of S-phase gene expression            │
│  - RB-E2F complex → genes OFF → no S-phase entry                    │
│  - When cell should divide:                                          │
│    Cyclin D-CDK4/6 phosphorylates RB → releases E2F → S-phase genes │
│    Cyclin E-CDK2 hyperphosphorylates RB → full release               │
│                                                                      │
│  How it's inactivated in cancer:                                     │
│  • RB1 mutation/deletion (direct)                                    │
│  • CDKN2A (p16) loss → CDK4/6 unchecked → RB always phosphorylated  │
│  • CCND1 (Cyclin D1) amplification → CDK4/6 hyperactive → RB       │
│    always phosphorylated                                             │
│  • CDK4 amplification → same effect                                  │
│  • HPV E7 protein → binds and degrades RB                            │
│                                                                      │
│  Therapeutic implication:                                            │
│  CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib)           │
│  → Work ONLY if RB is functional                                     │
│  → If RB is lost → CDK4/6 inhibitors won't work                     │
│  → Molecular testing for RB status is critical for treatment        │
│                                                                      │
│  The RB pathway is disrupted in virtually ALL cancers, but the       │
│  specific mechanism varies. This is a key concept:                   │
│  "Many genes, one pathway"                                          │
└─────────────────────────────────────────────────────────────────────┘

PTEN — "The Lipid Phosphatase"
┌─────────────────────────────────────────────────────────────────────┐
│  Chromosomal location: 10q23.3                                       │
│  Protein: PTEN (Phosphatase and Tensin Homolog)                     │
│                                                                      │
│  Normal function:                                                    │
│  - Dephosphorylates PIP3 → PIP2 (reverses PI3K action)             │
│  - PI3K → PIP2 → PIP3 → AKT activation → survival, growth          │
│  - PTEN → PIP3 → PIP2 → AKT OFF → controlled growth                │
│  - Without PTEN: PI3K-AKT-mTOR pathway is constitutively active     │
│                                                                      │
│  How it's inactivated:                                               │
│  • Mutation (missense, nonsense, frameshift)                        │
│  • Deletion (10q loss)                                               │
│  • Promoter methylation                                             │
│  • Protein instability (C-terminal phosphorylation → degradation)   │
│                                                                      │
│  Mutated in: endometrial (50-80%), glioblastoma (30-40%),           │
│  prostate (20-30%), breast (15-30%), thyroid                        │
│                                                                      │
│  Cowden syndrome: germline PTEN mutation → multiple benign and      │
│  malignant tumors                                                    │
└─────────────────────────────────────────────────────────────────────┘
```

### 4.3 The "Two-Hit" Exception: Haploinsufficiency and Dominant 
Negatives

```
HAPLOINSUFFICIENCY:
  Some tumor suppressors show phenotype with only ONE hit:
  - PTEN: 50% expression is insufficient for full tumor suppression
  - CDKN1B (p27): haploinsufficient tumor suppressor
  - DMP1: haploinsufficient
  - TGFBR2: reduced expression (not complete loss) promotes cancer

DOMINANT NEGATIVE:
  Mutant protein interferes with remaining wild-type:
  - TP53: mutant p53 forms non-functional tetramers with WT p53
  - TP53: some mutations confer ADDITIONAL oncogenic properties
    (gain-of-function mutants → actively promote invasion, metastasis)
```

---

## 5. The Hallmarks of Cancer

### 5.1 The Original Six Hallmarks (Hanahan & Weinberg, 2000)

```
╔════════════════════════════════════════════════════════════════════════╔══════════════════════════════════════════════════════════════════════════╗
║                   HALLMARK 1: SUSTAINED PROLIFERATIVE SIGNALING       
║
╠═══════════════════════════════════════════════════════════════════════║╠══════════════════════════════════════════════════════════════════════════╣
║                                                                        
║
║  Normal: Growth factor → receptor → signal cascade → controlled       
║
║          division → signal terminates                                 
 ║
║                                                                        
║
║  Cancer strategies:                                                    
║
║  1. Autocrine signaling: tumor produces its OWN growth factors        
║
║     → Tumor makes TGF-α → stimulates its own EGFR → self-sustaining   
║
║                                                                        
║
║  2. Constitutive receptor activation:                                  
║
║     → Mutant EGFR (L858R in lung cancer) → always signaling           
║
║     → HER2 amplification → too many receptors → too much signaling    
║
║     → FLT3-ITD in AML → internal tandem duplication → always active   
║
║                                                                       
 ║
║  3. Downstream pathway activation:                                     
║
║     → RAS mutations → signaling without receptor input                
║
║     → BRAF V600E → MAPK pathway always on (melanoma, thyroid)         
║
║                                                                        
║
║  4. Ligand-independent dimerization:                                   
║
║     → ALK fusions (EML4-ALK in lung cancer) → always dimerized       ║
║                                                                        
║
║  H&E appearance: Hypercellularity, increased mitotic figures,          
║
║  high nuclear:cytoplasmic ratio                                        
║
╚════════════════════════════════════════════════════════════════════════╚══════════════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════════════╔══════════════════════════════════════════════════════════════════════════╗
║                   HALLMARK 2: EVADING GROWTH SUPPRESSORS               
║
╠════════════════════════════════════════════════════════════════════════╠══════════════════════════════════════════════════════════════════════════╣
║                                                                        
║
║  Normal: Contact inhibition, TGF-β tumor-suppressive signaling,       
║
║          Hippo pathway (YAP/TAZ inactivation), p16/RB checkpoint      
 ║
║                                                                        
║
║  Cancer strategies:                                                    
║
║  1. RB pathway disruption (most common)                                
║
║     → CDKN2A (p16) deletion/silencing → CDK4/6 uninhibited →         ║
║       RB phosphorylated → E2F released → S-phase entry               ║
║     → RB1 mutation → E2F always free                                  
║
║     → CCND1 (Cyclin D1) amplification → excessive CDK4/6 activity     
║
║                                                                        
║
║  2. TGF-β pathway inactivation                                         
║
║     → TGFBR2 mutation (MSI-H cancers — frameshift in poly-A tract)    
║
║     → SMAD4 mutation/deletion (pancreatic, colorectal cancer)         
║
║     → Note: TGF-β has DUAL roles — early tumor suppressive,           
║
║       late tumor-promoting (EMT, immune evasion)                      
║
║                                                                        
║
║  3. Hippo pathway inactivation                                         
 ║
║     → YAP/TAZ nuclear translocation → transcription of growth genes   
║
║     → NF2 (Merlin) loss in mesothelioma, schwannoma                   
║
║     → YAP/TAZ activation visible as: enlarged nuclei, increased      ║
║       cell size, organ overgrowth                                     
║
║                                                                       
 ║
║  4. Contact inhibition loss                                            
 ║
║     → NF2/LATS1/2 inactivation → YAP/TAZ active → cells grow         ║
║       despite contact with neighbors                                   
║
╚════════════════════════════════════════════════════════════════════════╚══════════════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════════════╔══════════════════════════════════════════════════════════════════════════╗
║                   HALLMARK 3: RESISTING CELL DEATH                     
║
╠════════════════════════════════════════════════════════════════════════╠══════════════════════════════════════════════════════════════════════════╣
║                                                                        
║
║  Apoptosis (Programmed Cell Death) — Two Pathways:                     
║
║                                                                        
║
║  EXTRINSIC PATHWAY:                          INTRINSIC PATHWAY:       
║
║  Death ligand → Death receptor               Cellular stress →        
║
║  (FasL → Fas)                                (DNA damage, hypoxia,    
║
║       │                                       oncogene activation)    
║
║       ▼                                              │               ║
║  FADD + Caspase-8                              p53 ACTIVATED          
║
║       │                                              │               
║
║       ▼                                              ▼               
║
║  Caspase-8 activated                         BAX/BAK activated        
║
║       │                                     (pro-apoptotic BCL2       
║
║       │                                      family members)          
║
║       │                                              │               ║
║       │                                              ▼               ║
║       │                                      Mitochondrial outer      
║
║       │                                      membrane permeabilized   
║
║       │                                     (MOMP)                    
║
║       │                                              │               
║
║       │                                              ▼               
║
║       │                                      Cytochrome c released    
║
║       │                                              │               ║
║       │                                              ▼               ║
║       │                                      Apaf-1 + Caspase-9       
║
║       │                                     (apoptosome)             
║
║       │                                              │               
║
║       └──────────────────────┬───────────────────────┘               
║
║                                │                                      
║
║                                ▼                                      
║
║                         Caspase-3/7 activation                        
║
║                                │                                      
║
║                                ▼                                      
║
║                         APOPTOSIS EXECUTION                           
║
║                         (DNA fragmentation, membrane blebbing,        
║
║                          cell breakdown into apoptotic bodies)         
║
║                                                                        
║
║  Cancer evasion strategies:                                            
║
║  • BCL2 overexpression (t(14;18) in follicular lymphoma) → blocks    ║
║    MOMP → apoptosis blocked at intrinsic pathway                     ║
║  • BCL2 amplification in many solid tumors                            
║
║  • BCL-XL, MCL1 overexpression → alternative anti-apoptotic proteins 
║
║  • TP53 mutation → no PUMA/NOXA/BAX → intrinsic pathway blocked     ║
║  • FLIP overexpression → blocks caspase-8 → extrinsic blocked       ║
║  • IAP (Inhibitor of Apoptosis) family: XIAP, cIAP1/2 → block       ║
║    caspases directly                                                  
║
║  • Fas receptor downregulation → immune cells can't trigger death    
║
║  • CD95 (Fas) silencing by methylation                                
║
║                                                                        
║
║  NON-APOPTOTIC CELL DEATH:                                            
║
║  • Necroptosis: RIPK1/RIPK3/MLKL-mediated → inflammatory cell death   
║
║  • Pyroptosis: Gasdermin-mediated → inflammatory cell death            
║
║  • Ferroptosis: Iron-dependent lipid peroxidation → cell death        
║
║    → Interesting: some tumors are ferroptosis-sensitive              
║
║    → GPX4 is the key protective enzyme; system Xc- imports cystine  ║
║    → Erastin/sorafenib can trigger ferroptosis                       ║
║  • Autophagic cell death: excessive self-digestion                    
║
║                                                                       
 ║
║  H&E appearance:                                                       
║
║  • Few apoptotic bodies (normal tissue has more)                      
║
║  • Paradoxically: may see necrosis in tumor centers                   
║
║    (outgrowing blood supply → but individual cells resist apoptosis)  
║
╚═══════════════════════════════════════════════════════════════════════║╚══════════════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════════════╔══════════════════════════════════════════════════════════════════════════╗
║                   HALLMARK 4: REPLICATIVE IMMORTALITY                  
║
╠════════════════════════════════════════════════════════════════════════╠══════════════════════════════════════════════════════════════════════════╣
║                                                                        
║
║  Telomere biology:                                                     
║
║                                                                        
║
║  Telomere structure:                                                   
║
║  ┌──────────────────────────────────────────┐                         
║
║  │  5'-TTAGGG-TTAGGG-TTAGGG-...-3' (G-rich) │                        
║
║  │  3'-AATCCC-AATCCC-AATCCC-...-5' (C-rich) │                        
║
║  │     ↑↑↑                                  │                         
║
║  │     T-loop (3' end folds back, invades   │                         
║
║  │     double helix → protected)            │                         
║
║  │                                          │                         
║
║  │  Bound by shelterin complex:             │                         
║
║  │  TRF1, TRF2, POT1, TIN2, TPP1, RAP1     │                         ║
║  │  → Protects from DNA damage response     │                         
║
║  │  → Prevents end-to-end fusions           │                         
║
║  └──────────────────────────────────────────┘                         
║
║                                                                       
 ║
║  The end replication problem:                                          
║
║  DNA polymerase requires a primer → cannot replicate the 3' end       
║
║  → Each cell division → telomere shortens by 50-200 bp              ║
║  → After ~50-70 divisions → critically short telomeres                
║
║  → DNA damage response → senescence or crisis (massive cell death)   
║
║                                                                       
 ║
║  The Hayflick Limit:                                                   
║
║  Population doublings before senescence:                               
║
║  - Fibroblasts: ~50-70                                                
║
║  - Endothelial cells: ~15-30                                          
 ║
║  - Embryonic stem cells: unlimited (express telomerase)               
║
║                                                                       
 ║
║  Cancer solution: TELOMERASE REACTIVATION                              
║
║                                                                        
║
║  TERT (Telomerase Reverse Transcriptase):                              
║
║  - Catalytic subunit of telomerase                                     
║
║  - Normally silenced in most somatic cells                             
 ║
║  - Reactivated in ~90% of cancers                                     
║
║  - Mechanism: TERT promoter mutations (C228T, C250T) in many cancers  
║
║  - ETS transcription factors (mutated or overexpressed) drive TERT    
║
║  - MYC directly activates TERT transcription                          
║
║                                                                        
║
║  Alternative Lengthening of Telomeres (ALT):                           
║
║  - Homologous recombination-based telomere extension                   
║
║  - Used by ~10% of cancers (more common in sarcomas, neuroendocrine) ║
║  - Associated with ATRX/DAXX mutations                                
║
║  - ALT-positive tumors show ALT-associated PML bodies                 
║
║                                                                        
║
║  H&E appearance: No direct morphological correlate, but              ║
║  telomerase-active tumors show high proliferative index,              
║
║  lack of senescent cells                                              
║
╚════════════════════════════════════════════════════════════════════════╚══════════════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════════════╔══════════════════════════════════════════════════════════════════════════╗
║                   HALLMARK 5: INDUCING ANGIOGENESIS                    
 ║
╠════════════════════════════════════════════════════════════════════════╠══════════════════════════════════════════════════════════════════════════╣
║                                                                        
║
║  Angiogenic switch:                                                    
║
║  Tumor grows to ~1-2mm → diffusion limit of oxygen → hypoxia          
║
║  → HIF-1α stabilized → VEGF transcription → new blood vessel growth   
║
║                                                                        
║
║  Pro-angiogenic factors:          Anti-angiogenic factors:           ║
║  • VEGF-A, -B, -C, -D            • Thrombospondin-1 (TSP1)           ║
║  • FGF (basic FGF, acidic FGF)    • Endostatin (from collagen XVIII)  
║
║  • PDGF                           • Angiostatin (from plasminogen)    
 ║
║  • Angiopoietin-2                  • Tumstatin                         
║
║  • HGF                            • Vasohibin                         
║
║  • IL-8                                                               
 ║
║                                                                        
║
║  Normal: pro/anti balance → vessels only when needed                   
║
║  Cancer: shift to pro-angiogenic → vessels grow toward tumor         ║
║                                                                        
║
║  Tumor vessels are ABNORMAL:                                           
║
║  • Irregular diameter                                                  
║
║  • Excessive branching                                                 
 ║
║  • Leaky (pericytes deficient) → high interstitial pressure            
║
║  • Chaotic blood flow → regions of hypoxia/reperfusion                
║
║  • This is why drug delivery to tumors is often poor                  
║
║                                                                        
║
║  Anti-angiogenic therapy:                                              
║
║  • Bevacizumab (anti-VEGF-A): colorectal, lung, glioblastoma, RCC    ║
║  • Aflibercept (VEGF trap): colorectal                                
║
║  • Tyrosine kinase inhibitors: sunitinib, sorafenib, pazopanib        
║
║  • Problem: tumors develop resistance (alternative pathways,          
║
║    vessel co-option, vascular mimicry)                                
║
║                                                                        
║
║  H&E appearance:                                                       
║
║  • Microvessel density: count CD31/CD34-stained vessels               
║
║  • Glomeruloid microvascular proliferation (glioblastoma)             
 ║
║  • Areas of hemorrhage (leaky vessels)                                
║
║  • Geographic necrosis (areas outgrowing blood supply)                
 ║
╚════════════════════════════════════════════════════════════════════════╚══════════════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════════════╔══════════════════════════════════════════════════════════════════════════╗
║                   HALLMARK 6: ACTIVATING INVASION & METASTASIS         
║
╠════════════════════════════════════════════════════════════════════════╠══════════════════════════════════════════════════════════════════════════╣
║                                                                        
║
║  The Invasion-Metastasis Cascade:                                      
║
║                                                                        
║
║  LOCAL INVASION → INTRAVASATION → CIRCULATION → EXTRAVASATION →      ║
║  MICROMETASTASIS → COLONIZATION                                       
║
║                                                                       
 ║
║  EPITHELIAL-MESENCHYMAL TRANSITION (EMT):                              
║
║  The key program enabling invasion                                     
║
║                                                                        
║
║  ┌──────────────────────┐       ┌──────────────────────────┐         ║
║  │  EPITHELIAL STATE    │       │  MESENCHYMAL STATE        │         
║
║  │                      │  EMT  │                           │         
║
║  │  • E-cadherin (+)   │──────►│  • N-cadherin (+)        │         ║
║  │  • Cytokeratins (+) │       │  • Vimentin (+)          │         ║
║  │  • Polarity (+)     │       │  • Fibronectin (+)       │         ║
║  │  • Immobile (+)     │       │  • Motile (+)            │         ║
║  │  • Organized (+)    │       │  • Invasive (+)          │         ║
║  │                      │◄──────│  • ECM-degrading (+)     │         ║
║  │                      │  MET  │                           │         
║
║  └──────────────────────┘       └──────────────────────────┘         
║
║                                                                       
 ║
║  EMT Transcription Factors:                                            
║
║  • SNAIL (SNAI1), SLUG (SNAI2) → repress E-cadherin                 ║
║  • TWIST1, TWIST2                                                      
║
║  • ZEB1, ZEB2                                                          
║
║  • GOOSECOID, FOXC2                                                    
║
║                                                                        
║
║  EMT induction signals:                                                
║
║  • TGF-β (major inducer)                                               
║
║  • Wnt/β-catenin                                                       
║
║  • Notch signaling                                                     
║
║  • Hypoxia (HIF-1α → Twist)                                           
║
║  • Inflammatory cytokines (TNF-α, IL-6 → NF-κB → Snail)              
║
║                                                                       
 ║
║  EMT is not binary — it exists on a SPECTRUM:                          
║
║  • Hybrid/partial EMT states → most metastatic potential              
║
║  • Collective migration: groups of cells with partial EMT             
 ║
║  • This is relevant for segmentation: EMT states produce              
║
║    cells with intermediate morphology                                 
║
║                                                                        
║
║  ECM degradation:                                                      
║
║  • Matrix metalloproteinases (MMPs): MMP-2, MMP-9, MT1-MMP          ║
║  • Urokinase plasminogen activator (uPA/uPAR system)                  
║
║  • Cathepsins (cysteine proteases)                                    
 ║
║  • Heparanase                                                          
║
║                                                                        
║
║  The metastatic cascade in detail:                                     
║
║  1. Local invasion: EMT, MMP secretion, basement membrane breach      
║
║  2. Intravasation: enter blood/lymphatic vessels                      
║
║     • Macrophages facilitate (TMEM = tumor microenvironment of        
║
║       metastasis: tumor cell + macrophage + endothelial cell)         
║
║  3. Circulation: CTCs (circulating tumor cells)                      ║
║     • Most die in circulation (anoikis, shear stress, immune attack) ║
║     • Survival strategies: platelet cloaking, complement inhibition   
║
║     • CTC clusters: 20-50x more metastatic than single CTCs           
║
║  4. Arrest: at distant capillary bed or through active homing          
║
║     • Size entrapment, adhesion molecule interactions                  
║
║  5. Extravasation: exit vessel into parenchyma                        
║
║     • Trans-endothelial migration                                     
║
║  6. Micrometastasis: small cluster of dormant cancer cells            
║
║     • Can remain dormant for YEARS (clinical challenge)               
║
║     • Waking: angiogenic switch, immunosuppression, niche signals     
║
║  7. Colonization: overt metastatic growth                             
 ║
║     • Requires adaptation to new tissue microenvironment               
║
║     • "Seed and soil": Paget's hypothesis — not random distribution    
║
║       - Breast cancer → bone, brain, liver, lung                      
║
║       - Colon cancer → liver (portal circulation)                     
║
║       - Prostate cancer → bone (osteoblastic lesions)                 
║
║       - Melanoma → brain, lung, liver                                 
 ║
║     • Pre-metastatic niche: primary tumor prepares distant site        
║
║       by secreting factors that recruit bone marrow-derived cells      
║
║                                                                        
║
║  H&E appearance:                                                       
║
║  • Invasive front: irregular cell clusters breaking away              
║
║  • Lymphovascular invasion: tumor within vessels                      
 ║
║  • Perineural invasion: tumor wrapping around nerves                   
║
║  • Metastatic deposits: foreign tissue in lymph nodes, organs          
║
╚════════════════════════════════════════════════════════════════════════╚══════════════════════════════════════════════════════════════════════════╝
```

### 5.2 The Emerging Hallmarks (Hanahan & Weinberg, 2011)

```
HALLMARK 7: REPROGRAMMING ENERGY METABOLISM
  → See Section 13 (Cancer Metabolism) below

HALLMARK 8: EVADING IMMUNE DESTRUCTION
  → See Section 11 (Immune Evasion and Immunology) below
```

### 5.3 The Enabling Characteristics

```
ENABLING CHARACTERISTIC 1: GENOME INSTABILITY & MUTATION
┌─────────────────────────────────────────────────────────────────────┐
│  Sources of genomic instability:                                     │
│                                                                      │
│  1. DNA REPAIR DEFICIENCY (see Section 3.3)                         │
│     → MMR deficiency → MSI → 10-100x normal mutation rate          │
│     → HR deficiency → large-scale rearrangements                   │
│     → NER deficiency → UV-specific mutagenesis                      │
│                                                                      │
│  2. CHROMOSOMAL INSTABILITY (CIN)                                    │
│     → Aneuploidy: abnormal chromosome number                        │
│     → Causes: centrosome amplification, merotelic attachments,     │
│       spindle assembly checkpoint defects (BUB1, MAD2),             │
│       cohesin mutations (STAG2), condensin defects                   │
│     → Consequence: copy number variation, loss of heterozygosity    │
│                                                                      │
│  3. REPLICATION STRESS                                               │
│     → Oncogene activation (MYC, RAS) → premature S-phase entry    │
│     → Replication forks stall and collapse                         │
│     → DNA double-strand breaks → genomic rearrangements             │
│     → Common fragile sites are particularly vulnerable               │
│                                                                      │
│  4. TELOMERE CRISIS                                                  │
│     → Critically short telomeres → end-to-end fusions               │
│     → Breakage-fusion-bridge (BFB) cycles → amplifications          │
│     → Chromothripsis from mitotic errors                            │
│                                                                      │
│  5. MUTATOR PHENOTYPE                                                │
│     → Loeb & Loeb hypothesis: some cancers have elevated mutation   │
│       rates from the start (e.g., POLE/POLD1 proofreading mutations)│
│     → Ultra-hypermutated tumors (>100 mut/Mb) in POLE-mutant       │
│       endometrial and colorectal cancers                            │
│     → These tumors are highly immunogenic → respond to              │
│       immunotherapy                                                 │
└─────────────────────────────────────────────────────────────────────┘

ENABLING CHARACTERISTIC 2: TUMOR-PROMOTING INFLAMMATION
┌─────────────────────────────────────────────────────────────────────┐
│  Inflammation's dual role:                                           │
│                                                                      │
│  ANTI-TUMOR:                                                         │
│  • Th1 CD4+ T cells, CD8+ T cells → tumor cell killing             │
│  • M1 macrophages → anti-tumor, antigen presentation                 │
│  • NK cells → innate tumor cell killing                              │
│  • Type I interferons → immune activation, anti-proliferative       │
│                                                                      │
│  PRO-TUMOR:                                                          │
│  • NF-κB in tumor cells → survival, proliferation, angiogenesis    │
│  • STAT3 in tumor cells → survival, immune evasion                  │
│  • Inflammatory mediators: PGE2, IL-6, IL-1β, TNF-α               │
│  • M2 macrophages → immune suppression, angiogenesis, matrix       │
│    remodeling → invasion                                             │
│  • Myeloid-derived suppressor cells (MDSCs) → T cell suppression   │
│  • Th17 cells → context-dependent, can promote tumor growth         │
│  • Reactive oxygen species (from inflammatory cells) → DNA damage  │
│    → mutations                                                      │
│                                                                      │
│  Inflammation → cancer examples:                                     │
│  • H. pylori gastritis → gastric cancer                              │
│  • Inflammatory bowel disease → colorectal cancer                    │
│  • Hepatitis B/C → hepatocellular carcinoma                         │
│  • HPV infection → cervical cancer                                   │
│  • Chronic pancreatitis → pancreatic cancer                          │
│                                                                      │
│  H&E appearance:                                                     │
│  • Inflammatory infiltrates (lymphocytes, plasma cells, neutrophils) │
│  • Granulation tissue (new capillaries + fibroblasts + inflammatory)│
│  • Desmoplasia (fibrotic stroma from chronic inflammation)          │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 6. Cell Cycle Deregulation

### 6.1 The Normal Cell Cycle

```
                    ┌─────────────────────────────┐
                    │                              │
                    ▼                              │
  ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐
  │    G1    │──►│    S    │──►│    G2    │──►│    M    │
  │  phase   │   │  phase  │   │  phase  │   │  phase  │
  │          │   │         │   │         │   │         │
  │ Cell     │   │ DNA     │   │ Prepare │   │ Mitosis │
  │ growth   │   │ synthesis│   │ for     │   │ Cytokine-│
  │          │   │         │   │ division │   │ sis     │
  └────┬─────┘   └─────────┘   └─────────┘   └────┬────┘
       │                                          │
       │                                          │
       ▼                                          │
  ┌─────────┐                                     │
  │    G0   │◄────────────────────────────────────┘
  │  phase  │         (some cells return to G0)
  │ Quies-  │
  │ cent    │
  └─────────┘
```

### 6.2 Cell Cycle Regulation — Molecular Details

```
G1/S CHECKPOINT (The Restriction Point)
═══════════════════════════════════════════

Growth factor signal → RAS → MAPK → MYC → Cyclin D transcription
                                                          │
                                                          ▼
                                          Cyclin D + CDK4/6 complex
                                                          │
                                          ┌───────────────┤
                                          ▼               ▼
                                    RB phosphorylation    p16 (CDKN2A) 
                                    (first step)         INHIBITS CDK4/6
                                          │
                                          ▼
                                    E2F partially released
                                          │
                                          ▼
                                    Cyclin E + CDK2 complex
                                          │
                                          ▼
                                    RB hyperphosphorylated
                                          │
                                          ▼
                                    E2F fully released
                                          │
                                          ▼
                                    S-phase gene transcription
                                    (DNA polymerase, PCNA, 
                                     thymidine kinase, etc.)
                                          │
                                          ▼
                                    S-PHASE ENTRY

If DNA DAMAGE detected:
    ATM/ATR → CHK1/CHK2 → p53 → p21 → INHIBITS CDK2 → CELL CYCLE ARREST
                                         │
                                         ▼
                                    Time for DNA repair
                                         │
                                    ┌────┴────┐
                                    ▼         ▼
                               Repair      Irreparable
                               success     damage
                                    │         │
                                    ▼         ▼
                               Re-enter     APOPTOSIS
                               cell cycle   (via PUMA, NOXA, BAX)

G2/M CHECKPOINT
═══════════════════════════════════════════

After S-phase, if DNA replication is incomplete or DNA is damaged:
    ATM/ATR → CHK1 → CDC25C phosphorylation → CYTOPLASMIC RETENTION
                            │
                            ▼
                    Cannot activate CDK1 (CDC2)
                            │
                            ▼
                    Cyclin B-CDK1 NOT activated
                            │
                            ▼
                    NO ENTRY INTO M-PHASE

SPINDLE ASSEMBLY CHECKPOINT (SAC)
═══════════════════════════════════════════

During mitosis, ensures all chromosomes properly attached to spindle:
    Unattached kinetochores → MAD2/BUBR1 → Mitotic Checkpoint Complex
                                              │
                                              ▼
                                         Inhibits APC/C
                                              │
                                              ▼
                                         Securin NOT degraded
                                         Separase NOT activated
                                         Cohesin NOT cleaved
                                              │
                                              ▼
                                         NO ANAPHASE ENTRY

If SAC is defective → aneuploidy (mis-segregated chromosomes)
```

### 6.3 Cell Cycle Deregulation in Cancer

```
Almost ALL cancers disrupt the G1/S checkpoint. The mechanism varies:

                    RB PATHWAY DISRUPTION
                    ═════════════════════
    
    Normal:    p16 ──| CDK4/6 ──| RB ──| E2F ── cell division
               (inhibit)   (inhibit)  (inhibit)
    
    Cancer:    ONE of these disruptions is sufficient:
    
    ┌──────────────────────────────────────────────────────────────┐
    │  Mechanism              │ Cancer Type           │ Frequency  │
    │  ─────────────────────  │ ─────────────────     │ ─────────  │
    │  CDKN2A (p16) deletion │ Pancreatic, glioma    │ ~50-80%   │
    │  CDKN2A methylation     │ Various               │ ~20-40%   │
    │  CCND1 amplification    │ Breast, HNSCC, MCL    │ ~15-30%   │
    │  CDK4 amplification     │ Liposarcoma, glioma   │ ~10-20%   │
    │  CDK6 amplification    │ Glioblastoma, sarcoma  │ ~5-15%    │
    │  RB1 mutation/deletion │ Retinoblastoma, SCLC  │ ~5-100%   │
    │  HPV E7 (RB inactiv.)  │ Cervical, oropharynx  │ ~90%+     │
    └──────────────────────────────────────────────────────────────┘

The key insight: it doesn't matter HOW you break the circuit.
The result is the same: E2F is free → S-phase entry → proliferation.
This is why CDK4/6 inhibitors work regardless of the specific 
disruption mechanism (as long as RB is intact).
```

---

## 7. Signal Transduction in Cancer

### 7.1 Major Oncogenic Signaling Pathways

```
RECEPTOR TYROSINE KINASE (RTK) → RAS-MAPK → PROLIFERATION
                         ╲
                          ╲→ PI3K-AKT-mTOR → SURVIVAL, GROWTH

┌────────────────────────────────────────────────────────────────────────┌──────────────────────────────────────────────────────────────────────────┐
│                                                                        
  │
│  GROWTH FACTOR (EGF, FGF, PDGF, VEGF, HGF)                             
│
│       │                                                                
  │
│       ▼                                                                
  │
│  RECEPTOR TYROSINE KINASE (EGFR, FGFR, PDGFR, VEGFR, MET)              
│
│  (dimerization → autophosphorylation on tyrosine residues)             
 │
│       │                                                                
  │
│       ├──► GRB2/SOS ──► RAS (GDP → GTP)                               
│
│       │                    │                                          
   │
│       │                    ├──► RAF ──► MEK ──► ERK ──►                
 │
│       │                    │     (MAPK cascade)       │                
  │
│       │                    │                         ▼                 
 │
│       │                    │              TRANSCRIPTION FACTORS        
    │
│       │                    │              (ELK1, c-FOS, c-JUN →        
  │
│       │                    │               AP-1, MYC → proliferation)  
 │
│       │                    │                                           
  │
│       │                    └──► PI3K (p110α)                           
  │
│       │                          │                                     
  │
│       ├──► PI3K ◄────────────────┤                                     
  │
│       │     │                    │                                     
  │
│       │     ▼                    │                                     
  │
│       │   PIP2 → PIP3            │                                     
  │
│       │     │                    │                                     
  │
│       │     ├──► AKT (PKB) ◄────┤                                      
 │
│       │     │     │              │                                     
  │
│       │     │     ├──► mTOR ──► protein synthesis, cell growth         
 │
│       │     │     │    │                                               
 │
│       │     │     │    └──► HIF-1α ──► angiogenesis                    
│
│       │     │     │                                                    
 │
│       │     │     ├──► FOXO ──► (inhibited → survival genes off →      
  │
│       │     │     │          actually pro-survival because FOXO        
 │
│       │     │     │          is tumor-suppressive and AKT inhibits it) 
  │
│       │     │     │                                                    
 │
│       │     │     ├──► GSK3β ──► (inhibited → β-catenin stabilized →   
 │
│       │     │     │            Wnt pathway activation)                 
 │
│       │     │     │                                                    
 │
│       │     │     ├──► BAD phosphorylation ──► apoptosis inhibited     
  │
│       │     │     │                                                    
 │
│       │     │     └──► MDM2 ──► p53 degradation ──► growth, survival  
│
│       │     │                                                         
  │
│       │     ▼                                                          
 │
│       │   PTEN (PIP3 → PIP2) = NEGATIVE REGULATOR ◄── TUMOR           
│
│       │     ↑                            SUPPRESSOR                   
  │
│       │     │                                                          
  │
│       │   PTEN loss → PIP3 accumulates → AKT always on                 
│
│       │                                                                
  │
│       └──► JAK-STAT pathway                                            
 │
│             │                                                          
 │
│             ├──► STAT3 ──► survival, proliferation, immune evasion     
│
│             ├──► STAT5 ──► hematopoietic growth                        
 │
│             └──► SOCS (suppressor of cytokine signaling) = brake       
  │
│                                                                        
  │
│  WNT/β-CATENIN PATHWAY                                                 
 │
│  ══════════════════════                                                
  │
│  Off state: β-catenin bound by DESTRUCTION COMPLEX                     
  │
│    (APC + AXIN + GSK3β + CK1) → β-catenin phosphorylated              
│
│    → ubiquitinated by β-TrCP → proteasomal degradation                
 │
│                                                                        
  │
│  On state: Wnt → Frizzled → Dishevelled → inhibits destruction complex 
│
│    → β-catenin accumulates → enters nucleus → TCF/LEF transcription    
│
│    → MYC, Cyclin D1, AXIN2, LGR5 (stem cell genes)                    
│
│                                                                       
   │
│  Cancer: APC mutation (colorectal), CTNNB1 mutation (β-catenin         
│
│    stabilization in hepatocellular, endometrial), RNF43 mutation       
 │
│                                                                        
  │
│  NOTCH PATHWAY                                                         
 │
│  ═══════════════                                                       
 │
│  Notch receptor + ligand (Jagged/Delta) on neighboring cell            
 │
│  → Cleavage (ADAM + γ-secretase) → NICD released                       
│
│  → NICD enters nucleus → RBP-Jκ → transcription of HES, HEY genes      
│
│                                                                        
  │
│  Cancer: Context-dependent — oncogenic in T-ALL (NOTCH1 activating),   
│
│    tumor-suppressive in squamous cancers (NOTCH loss-of-function)      
 │
│                                                                        
  │
│  HEDGEHOG PATHWAY                                                      
 │
│  ═══════════════════                                                   
 │
│  Hedgehog ligand → PTCH1 → SMO released → GLI transcription factors   
│
│  → Basal cell carcinoma (PTCH1 or SMO mutations), medulloblastoma     
│
│  → SMO inhibitors (vismodegib, sonidegib)                              
│
│                                                                        
  │
│  TGF-β PATHWAY (DUAL ROLE)                                             
│
│  ═════════════════════════════                                         
 │
│  TGF-β → TGFBR2 → TGFBR1 → SMAD2/3 phosphorylation                   │
│  → SMAD2/3 + SMAD4 → nucleus → transcription                           
│
│  → Early: tumor-suppressive (cell cycle arrest via p15, p21)           
│
│  → Late: tumor-promoting (EMT, immune evasion, metastasis)             
│
│  → SMAD4 loss in pancreatic/colorectal cancer → tumor-suppressive      
│
│    arm lost, but alternative signaling still promotes EMT              
 │
│                                                                        
  │
└────────────────────────────────────────────────────────────────────────└──────────────────────────────────────────────────────────────────────────┘
```

---

## 8. Epigenetics in Cancer

### 8.1 The Epigenetic Landscape in Cancer

```
DNA METHYLATION
═══════════════

Normal methylation:
  • CpG ISLAND methylation → gene silencing
    → Normally unmethylated at gene promoters (genes ON)
    → Methylated at repetitive elements (retrotransposon silencing)
  • Global HYPOMETHYLATION in cancer:
    → Genomic instability
    → Retrotransposon reactivation (LINE-1)
    → Oncogene activation (by demethylation of normally silent loci)
  • Focal HYPERMETHYLATION in cancer:
    → Tumor suppressor gene silencing (CpG island methylator phenotype)
    → Does not require DNA mutation — functionally equivalent to 
mutation
    → Reversible (unlike mutations) → therapeutic target

  Writers: DNMT1 (maintenance), DNMT3A/3B (de novo)
  Erasers: TET1/2/3 (oxidize 5mC → 5hmC → 5fC → 5caC → unmethylated C)
  Readers: MBD proteins (MBD1, MeCP2, MBD2/3/4) → recruit repressive 
complexes

  Cancer examples:
  • DNMT3A mutations in AML (~20%) → aberrant methylation patterns
  • TET2 mutations in myeloid neoplasms (~15-30%) → impaired 
demethylation
    → hypermethylation phenotype
  • IDH1/2 mutations in glioma, AML → produce 2-HG (oncometabolite)
    → 2-HG inhibits TET2 and JmjC histone demethylases
    → CpG island hypermethylation phenotype (G-CIMP in glioma)
  • MLH1 promoter methylation → MMR deficiency → MSI → colorectal cancer
  • BRCA1 promoter methylation → BRCA1 silencing → breast/ovarian cancer
    (mimics germline BRCA1 mutation → "BRCAness" → PARP inhibitor 
response)
  • CDKN2A (p16) promoter methylation → cell cycle deregulation

HISTONE MODIFICATIONS
═════════════════════

  "Histone code" — combinatorial patterns of modifications:
  
  ┌──────────────────────────────────────────────────────────────────────┌──────────────────────────────────────────────────────────────────────┐
  │  Active marks:                                                      
│
  │  • H3K4me3 → promoter activation                                    
│
  │  • H3K36me3 → gene body of active genes                            │
  │  • H3K27ac → active enhancers and promoters                        │
  │  • H3K9ac → open chromatin (associated with transcription)         │
  │  • H3K4me1 → enhancer marking (poised or active)                   │
  │                                                                     
│
  │  Repressive marks:                                                  
│
  │  • H3K27me3 → Polycomb-mediated silencing                          │
  │  • H3K9me3 → heterochromatin (constitutive silencing)              │
  │  • H3K9me2 → facultative heterochromatin                           │
  │  • H4K20me3 → pericentric heterochromatin                          │
  │                                                                     
│
  │  Bivalent marks:                                                    
│
  │  • H3K4me3 + H3K27me3 simultaneously → "poised" genes             │
  │    (developmental regulators in embryonic stem cells)               
│
  │  • In cancer: resolve to either active or repressed                
│
  │    → Aberrant activation of developmental programs (EMT genes)      
│
  │      or silencing of differentiation genes                          
│
  └─────────────────────────────────────────────────────────────────────└──────────────────────────────────────────────────────────────────────┘

  Writers, Erasers, Readers — all mutated in cancer:

  ┌──────────────────┬───────────────────┬──────────────────────────────┐┌──────────────────┬───────────────────┬──────────────────────────────┐
  │  Modification    │  Enzyme (cancer)  │  Cancer type                 
│
  │  ──────────────  │  ────────────────  │  ──────────────────         
 │
  │  H3K27me3 (write)│  EZH2 (mutated)   │  Lymphoma (GOF), prostate    
│
  │  H3K27me3 (erase)│  UTX/KDM6A (mut)  │  Myeloid cancers, bladder    
│
  │  H3K4me3 (write) │  MLL1 (transloc.) │  AML, ALL                    
│
  │  H3K9me3 (write) │  SUV39H1          │  Various (overexpressed)     
│
  │  H3K27ac (write) │  CBP/p300 (mut.)  │  Lymphoma, AML              │
  │  H3K27me3 (read) │  EED (mutated)    │  Myeloid malignancies        
│
  │  H3K4me3 (erase) │  LSD1/KDM1A       │  AML, SCLC (overexpressed)  
│
  │  Chromatin remodel│ SWI/SNF (SMARCB1,│  Rhabdoid, ovarian, various 
│
  │                   │ SMARCA4, ARID1A)  │  (collectively ~20% of all  
 │
  │                   │                   │  cancers)                    
│
  └──────────────────┴───────────────────┴──────────────────────────────┘└──────────────────┴───────────────────┴──────────────────────────────┘

CHROMATIN REMODELING
════════════════════

  SWI/SNF complex:
  • 29 genes encoding subunits
  • Mutated collectively in >20% of all human cancers
  • ARID1A: Ovarian clear cell, endometrial, gastric
  • SMARCB1 (INI1): Rhabdoid tumors (loss is diagnostic)
  • SMARCA4: Small cell carcinoma of ovary, lung
  • PBRM1: Renal cell carcinoma (~40%)
  • Mechanism: loss of chromatin remodeling → aberrant gene expression
  • Synthetic lethality: SWI/SNF-mutant cancers depend on EZH2
    → EZH2 inhibitors in SWI/SNF-mutant cancers
```

---

## 9. Tumor Evolution and Heterogeneity

### 9.1 Clonal Evolution Models

```
LINEAR EVOLUTION (Nowak Model):
═══════════════════════════════

  Normal → Clone A → Clone B → Clone C → Clone D
          (founder) (acquires  (acquires  (acquires
                     mutation X) mutation Y) mutation Z)

  Each successive clone outcompetes the previous
  → Single dominant clone at any given time
  → Early models of colorectal cancer (Vogelstein model)

BRANCHING EVOLUTION (More realistic for most cancers):
══════════════════════════════════════════════════════

                         Clone A (founder)
                        ╱         ╲
                      ╱               ╲
               Clone B                  Clone C
              (mutation X)             (mutation Y)
              ╱      ╲                    │
            ╱          ╲                   │
      Clone D        Clone E           Clone F
     (mut. X,Z)    (mut. X,W)        (mut. Y,Z)
        │              │                 │
        ▼              ▼                 ▼
    Subclone D1    Subclone E1       Subclone F1

  Multiple subclones coexist simultaneously
  → Intra-tumor heterogeneity
  → Different parts of the tumor have different mutation profiles
  → This is the most common evolutionary pattern observed

PUNCTUATED EVOLUTION:
═════════════════════

  Normal ──────────────► MACROEVOLUTIONARY EVENT
                         (massive genomic rearrangement
                          — chromothripsis, BFB cycles,
                           whole genome doubling)
                              │
                         Highly rearranged clone
                              │
                         ┌────┴────┐
                         ▼         ▼
                    Subclones with
                    additional point
                    mutations

  Fits observations where many rearrangements occur simultaneously
  rather than through gradual stepwise accumulation

NEUTRAL EVOLUTION:
═══════════════════

  Many passenger mutations accumulate without selection
  → Expanding population creates many subclones
  → No single subclone has a selective advantage
  → Predicts a specific distribution of variant frequencies
  → Observed in some pediatric cancers and certain cancer types
```

### 9.2 Spatial and Temporal Heterogeneity

```
SPATIAL HETEROGENEITY:
═══════════════════════

  Primary tumor:
  ┌─────────────────────────────────────────┐
  │  Region 1: Clone A (KRAS mut, TP53 mut) │
  │  ┌───────────────────┐                   │
  │  │ Region 2:         │  Clone A + B      │
  │  │ (KRAS, TP53,      │  (additional      │
  │  │  SMAD4 loss)       │  SMAD4 loss)      │
  │  └───────────────────┘                   │
  │         ┌─────────────┐                   │
  │         │ Region 3:   │  Clone A + C      │
  │         │ (KRAS, TP53,│  (additional      │
  │         │  PIK3CA mut) │  PIK3CA mut)      │
  │         └─────────────┘                   │
  └─────────────────────────────────────────┘

  Different metastases: each may arise from a different clone
  → Liver metastasis: Clone A + B
  → Lung metastasis: Clone A + C
  → Brain metastasis: Clone A + B + D

  Clinical implication:
  • Single biopsy may miss clinically relevant subclones
  • Different metastases may respond differently to therapy
  • This is why spatial transcriptomics / multi-region sampling matters
  • Your work on whole-cell segmentation + spatial mapping 
    contributes to understanding spatial heterogeneity

TEMPORAL HETEROGENEITY:
═══════════════════════

  Pre-treatment:  Clones A, B, C coexist (B is dominant)
                    │
  Treatment (e.g., targets B's dependency)
                    │
                    ▼
  During treatment: B is killed, C (resistant) expands
                    │
                    ▼
  Post-treatment:  C is now dominant → clinical relapse
                    │
  Next treatment (targets C)
                    │
                    ▼
  New resistant clone D emerges → second relapse

  This is why serial biopsies and liquid biopsies (ctDNA)
  are important for monitoring treatment response
```

---

## 10. The Tumor Microenvironment

### 10.1 Cellular Components — Detailed

```
╔════════════════════════════════════════════════════════════════════════╔══════════════════════════════════════════════════════════════════════════╗
║              TUMOR MICROENVIRONMENT — CELLULAR COMPONENTS              
 ║
╠════════════════════════════════════════════════════════════════════════╠══════════════════════════════════════════════════════════════════════════╣
║                                                                        
║
║  1. TUMOR CELLS (Epithelial origin for carcinomas)                     
║
║     ─────────────────────────────────────────────                      
 ║
║     Subtypes within a single tumor:                                    
║
║     • Cancer stem cells (CSCs): self-renewing, treatment-resistant     
║
║       Markers: CD44+CD24- (breast), CD133+ (glioma, colon),           
║
║       ALDH1+ (various)                                                
║
║     • Proliferating cancer cells: actively cycling                    
║
║     • Quiescent/senescent cancer cells: not dividing, but viable      
║
║     • Hypoxic cancer cells: near necrosis, treatment-resistant         
║
║     • EMT-transitioning cancer cells: at invasive front               
║
║                                                                       
 ║
║     H&E morphology:                                                    
║
║     • Enlarged, hyperchromatic nuclei (dark purple, irregular)        
║
║     • Pleomorphic (variable size and shape)                           
 ║
║     • Prominent nucleoli (active ribosome biogenesis)                  
║
║     • Irregular nuclear membranes                                      
║
║     • High N:C ratio (nuclear:cytoplasmic)                            
║
║     • Abnormal mitoses (tripolar, multipolar spindles)                
 ║
║     • Necrotic debris within tumor nests                               
║
║                                                                        
║
║  2. IMMUNE CELLS                                                       
║
║     ──────────────                                                     
 ║
║                                                                        
║
║     T LYMPHOCYTES:                                                     
║
║     ┌─────────────────────────────────────────────────────────────┐    
║
║     │  CD8+ T cells (Cytotoxic):                                 │    
║
║     │  • Kill tumor cells via perforin/granzyme or Fas/FasL      │    
║
║     │  • Tumor-infiltrating lymphocytes (TILs): prognostic       │    
║
║     │  • Immunoscore (CD8+ at core + invasive margin) →         │    
║
║     │    prognostic in colorectal cancer (potentially superior    │   
 ║
║     │    to TNM staging in some studies)                         │    
║
║     │  • Exhausted T cells: PD-1+, TIM-3+, LAG-3+ → dysfunctional│   
║
║     │    → reinvigorated by checkpoint inhibitors                 │   
 ║
║     │  • H&E: Small round dark nuclei, minimal cytoplasm          │    
║
║     │    Cannot distinguish CD8 from CD4 on H&E — need IHC       │    
║
║     │                                                           │    
║
║     │  CD4+ T cells (Helper):                                    │    
║
║     │  • Th1: anti-tumor (IFN-γ, IL-2) → activate CD8+ & NK    │    ║
║     │  • Th2: pro-tumor (IL-4, IL-5, IL-13) → M2 polarization   │    ║
║     │  • Th17: context-dependent (IL-17, IL-22) → angiogenesis   │    
║
║     │  • Tfh: help B cells in tertiary lymphoid structures        │   
 ║
║     │                                                           │    ║
║     │  Regulatory T cells (Tregs):                               │    
║
║     │  • FOXP3+CD25+CD4+                                        │    
║
║     │  • Suppress effector T cells via:                         │    
║
║     │    - CTLA-4 (outcompetes CD28 for B7 ligands)              │    
║
║     │    - IL-10, TGF-β secretion                               │    ║
║     │    - Metabolic disruption (CD39/CD73 → adenosine)         │    ║
║     │    - Cytolysis of APCs                                     │    
║
║     │  • High Tregs → immunosuppressed TME → worse prognosis    │    
║
║     │  • Targeted by anti-CTLA4 (ipilimumab) → Treg depletion   │    
║
║     └─────────────────────────────────────────────────────────────┘   
 ║
║                                                                        
║
║     B LYMPHOCYTES:                                                     
║
║     • Tertiary lymphoid structures (TLS) in tumors → good prognosis   
║
║     • Antibody-dependent cellular cytotoxicity (ADCC)                 
 ║
║     • Plasma cells: may produce tumor-targeting antibodies             
║
║     • Regulatory B cells (Bregs): immunosuppressive                    
║
║     • H&E: Small lymphocytes with clumped chromatin, may form         
║
║       follicular structures with germinal centers (TLS)               
 ║
║                                                                        
║
║     NATURAL KILLER (NK) CELLS:                                         
║
║     • Innate anti-tumor immunity                                       
║
║     • Kill cells with low MHC-I (common in tumors → immune evasion)   
║
║     • "Missing self" recognition                                      
  ║
║     • Activating receptors: NKG2D, NKp30, NKp44, NKp46               ║
║     • Inhibitory receptors: KIR, NKG2A                                
║
║     • H&E: Cannot distinguish from T cells on H&E                     
 ║
║                                                                        
║
║     MACROPHAGES:                                                       
║
║     ┌─────────────────────────────────────────────────────────────┐    
║
║     │  Tumor-Associated Macrophages (TAMs):                       │    
║
║     │                                                           │    ║
║     │  M1 (Classically activated):                              │    ║
║     │  • Induced by: IFN-γ + LPS                               │    ║
║     │  • Anti-tumor: produce IL-12, TNF-α, NO                  │    ║
║     │  • Antigen presentation → activate T cells                 │    
║
║     │  • H&E: Large cells with round/oval nucleus, abundant     │    
║
║     │    eosinophilic (pink) cytoplasm, may be foamy             │    
║
║     │                                                           │    ║
║     │  M2 (Alternatively activated):                            │    ║
║     │  • Induced by: IL-4, IL-13, IL-10                        │    ║
║     │  • Pro-tumor:                                             │    ║
║     │    - Promote angiogenesis (VEGF)                           │    
║
║     │    - Immunosuppression (IL-10, TGF-β, arginase)           │    
║
║     │    - Matrix remodeling (MMP secretion) → invasion         │    
║
║     │    - Promote metastasis (EGF signaling loop with tumor)   │    
║
║     │  • High TAM density → worse prognosis in most cancers     │    
║
║     │  • H&E: May be difficult to distinguish from tumor cells  │    
║
║     │    without IHC (CD68, CD163 for M2; CD80, HLA-DR for M1)  │    
║
║     │  • CRITICALLY: M1/M2 is a spectrum, not binary            │    
║
║     │    → Spatial transcriptomics can resolve this better      │    
║
║     └─────────────────────────────────────────────────────────────┘   
 ║
║                                                                        
║
║     MYELOID-DERIVED SUPPRESSOR CELLS (MDSCs):                         
║
║     • Heterogeneous population of immature myeloid cells              
║
║     • M-MDSC (monocytic): CD11b+CD14+HLA-DRlow                      ║
║     • PMN-MDSC (polymorphonuclear): CD11b+CD15+                      ║
║     • Functions:                                                      
║
║       - Arginase-1 → deplete L-arginine → T cell dysfunction        ║
║       - iNOS → NO → T cell apoptosis                                ║
║       - ROS → T cell damage                                         ║
║       - Expand Tregs                                                 ║
║     • H&E: Difficult to identify specifically without IHC             
║
║                                                                       
 ║
║     DENDRITIC CELLS:                                                   
║
║     • Conventional DCs (cDC1, cDC2): antigen presentation            ║
║     • cDC1 (BATF3+, XCR1+): cross-presentation to CD8+ T cells       ║
║       → Critical for anti-tumor immunity                              
║
║     • Plasmacytoid DCs (pDCs): type I interferon production           
║
║     • Tumor can impair DC maturation → tolerogenic DCs                
║
║     • H&E: Not identifiable on H&E (need CD11c, CD123 IHC)          ║
║                                                                        
║
║  3. CANCER-ASSOCIATED FIBROBLASTS (CAFs)                              
║
║     ─────────────────────────────────────────────                     
  ║
║     ┌─────────────────────────────────────────────────────────────┐    
║
║     │  Subtypes (single-cell RNA-seq revealed heterogeneity):    │    
║
║     │                                                           │    
║
║     │  Myofibroblastic CAFs (myCAFs):                           │    
║
║     │  • α-SMA+, ACTA2+, TAGLN+                               │    ║
║     │  • Contractile, produce ECM (collagen, fibronectin)       │    ║
║     │  • Prominent in desmoplastic tumors (pancreatic cancer)    │    
║
║     │  • H&E: Spindle-shaped, elongated nuclei, pink cytoplasm  │    
║
║     │    Embedded in dense pink collagenous stroma               │    
║
║     │                                                           │    ║
║     │  Inflammatory CAFs (iCAFs):                               │    ║
║     │  • IL-6, CXCL12, LIF expression                          │    ║
║     │  • Paracrine signaling to tumor and immune cells           │    
║
║     │  • Immunomodulatory                                       │    
║
║     │                                                           │    
║
║     │  Antigen-presenting CAFs (apCAFs):                        │    
║
║     │  • Express MHC class II molecules                          │    
║
║     │  • Can present antigen to CD4+ T cells                    │    ║
║     │  • May induce T cell anergy/tolerance                     │    ║
║     │                                                           │    ║
║     │  ECM-producing CAFs:                                      │    ║
║     │  • Dense collagen deposition → desmoplasia                │    ║
║     │  • Physical barrier to immune cell infiltration           │    ║
║     │  • Altered ECM stiffness → integrin signaling → tumor    │    ║
║     │    cell mechanotransduction → invasion                    │    ║
║     │  • H&E: Dense pink collagen (trichrome: blue-green)       │    ║
║     └─────────────────────────────────────────────────────────────┘    
║
║                                                                        
║
║  4. ENDOTHELIAL CELLS & VASCULATURE                                    
║
║     ──────────────────────────────────────                             
 ║
║     • Tumor vessels: leaky, tortuous, irregular, poorly covered       
║
║       by pericytes                                                    
 ║
║     • Endothelial-to-mesenchymal transition (EndMT):                   
║
║       contributes to CAFs                                              
║
║     • Vascular mimicry: tumor cells form vessel-like channels          
║
║     • Vasculogenic mimicry: especially in aggressive tumors            
║
║       (melanoma, hepatocellular carcinoma)                             
║
║     • H&E: Blood vessels appear as tubular structures with             
║
║       red blood cells; tumor vessels have irregular walls              
║
║                                                                        
║
║  5. PERICYTES                                                          
║
║     • Wrap around endothelial cells                                    
 ║
║     • Deficient in tumors → vessel leakiness                           
║
║     • NG2+, PDGFRβ+, α-SMA+ (subset)                                 ║
║                                                                        
║
║  6. ADIPOCYTES (Fat cells)                                             
║
║     • Cancer-associated adipocytes (CAAs):                             
║
║       dedifferentiated, release free fatty acids                       
║
║     • Fuel tumor metabolism (lipid transfer)                           
 ║
║     • Secrete adipokines (leptin, adiponectin) → signaling            
║
║     • H&E: Clear/empty cells (fat dissolved during processing)        
║
║       with thin eccentric nuclei                                       
║
║                                                                        
║
╚════════════════════════════════════════════════════════════════════════╚══════════════════════════════════════════════════════════════════════════╝
```

### 10.2 Acellular Components

```
EXTRACELLULAR MATRIX (ECM)
═══════════════════════════

  Basement membrane (if present — lost in invasive carcinoma):
  • Type IV collagen (network)
  • Laminin (network)
  • Nidogen/entactin (linker)
  • Perlecan (heparan sulfate proteoglycan)
  • Functions: barrier, polarity, signaling

  Interstitial matrix:
  • Collagen I (most abundant ECM protein in stroma)
  • Collagen III (reticular fibers)
  • Fibronectin
  • Elastin
  • Proteoglycans (decorin, biglycan, lumican)
  • Hyaluronan (glycosaminoglycan, no protein core)

  Tumor ECM is ALTERED:
  • Increased collagen I deposition → desmoplasia
  • Aligned collagen fibers (TACS: tumor-associated collagen signatures)
    → TACS-1: relaxed collagen near tumor
    → TACS-2: parallel collagen around tumor boundary
    → TACS-3: perpendicular collagen radiating from tumor → invasion 
marker
  • Crosslinking by LOX (lysyl oxidase) → stiffening → 
mechanotransduction
  • ECM remodeling by MMPs → creates migratory tracks
  • H&E: Pink eosinophilic stroma (dense collagen = desmoplasia)

SOLUBLE FACTORS
═══════════════

  Cytokines:     IL-6 (STAT3 → survival), IL-1β (inflammation),
                 TNF-α (NF-κB → survival/invasion), IL-10 
(immunosuppression),
                 TGF-β (EMT, immunosuppression, fibrosis)

  Chemokines:    CXCL12/SDF-1 (attracts CXCR4+ tumor cells → 
metastasis),
                 CCL2 (monocyte recruitment → TAMs),
                 CCL5 (Treg recruitment),
                 CXCL9/10 (T cell recruitment, IFN-γ induced),
                 CXCL8/IL-8 (angiogenesis, neutrophil recruitment)

  Growth factors: VEGF (angiogenesis), EGF, HGF (scatter factor),
                 PDGF (fibroblast recruitment), FGF,
                 TGF-β (context-dependent)

  Metabolites:   Lactate (Warburg effect → acidifies TME → immune 
suppression),
                 Adenosine (immunosuppressive, from CD39/CD73 on 
Tregs/MDSCs),
                 Prostaglandin E2 (PGE2 → immune suppression, 
angiogenesis),
                 Kynurenine (from IDO → tryptophan depletion → T cell 
anergy)

  Exosomes/EVs:  Carry miRNAs, proteins, DNA → paracrine communication
                 • Prepare pre-metastatic niche
                 • Transfer resistance mechanisms
                 • Immune modulation
                 • Organ-specific metastatic conditioning
```

---

## 11. Immune Evasion and Immunology

### 11.1 Cancer Immunoediting

```
The three Es of cancer immunoediting:

ELIMINATION                     EQUILIBRIUM                      ESCAPE
(Immunosurveillance)            (Equilibrium)                    (Immune 
Evasion)

  Immune system                  Immune system                    Immune 
system
  detects and                    contains but                     cannot 
contain
  destroys tumor                  cannot eliminate                 tumor 
→ clinical
  cells                           all tumor cells                  
cancer develops
       │                               │                               │
       ▼                               ▼                               ▼
  Immuno-                        Immunoselection                   
Immune
  genic cells                    for resistant                     
evasion
  are killed                     variants                          
mechanisms
       │                               │                               │
       ▼                               ▼                               ▼
  Tumor                           Resistant                         
Clinical
  eliminated                      clones survive                   
cancer
                                   (sculpting)
```

### 11.2 Immune Evasion Mechanisms — Detailed

```
╔════════════════════════════════════════════════════════════════════════╔══════════════════════════════════════════════════════════════════════════╗
║              IMMUNE EVASION MECHANISMS IN CANCER                       
 ║
╠════════════════════════════════════════════════════════════════════════╠══════════════════════════════════════════════════════════════════════════╣
║                                                                        
║
║  1. IMMUNE CHECKPOINT EXPLOITATION                                     
║
║     ═════════════════════════════                                      
 ║
║                                                                        
║
║     PD-1/PD-L1 Axis:                                                  
║
║     ┌──────────────────────────────────────────────────────────────┐  
 ║
║     │                                                              │   
║
║     │  TUMOR CELL                     T CELL                      │   
║
║     │                                                              │  
 ║
║     │   PD-L1 ────────────────── PD-1                            │   ║
║     │   (B7-H1)                    (CD279)                        │   
║
║     │       │                         │                            │  
 ║
║     │       └──── INHIBITORY ────────┘                            │   
║
║     │            SIGNAL                                            │  
 ║
║     │                                                              │   
║
║     │  Result: T cell becomes EXHAUSTED → can't kill tumor       │   ║
║     │                                                              │   
║
║     │  PD-L1 expression on tumor:                                  │   
║
║     │  • Constitutive: PTEN loss → PI3K/AKT → PD-L1 upregulation │   ║
║     │  • Adaptive: IFN-γ from T cells → PD-L1 induction          │   ║
║     │    (tumor senses immune attack → puts up shield)             │   
║
║     │  • Oncogene-driven: EGFR, ALK → PD-L1 upregulation         │   ║
║     │                                                              │   
║
║     │  Therapeutic targeting:                                      │   
║
║     │  • Anti-PD-1: pembrolizumab, nivolumab, cemiplimab         │   ║
║     │  • Anti-PD-L1: atezolizumab, durvalumab, avelumab          │   ║
║     └──────────────────────────────────────────────────────────────┘   
║
║                                                                        
║
║     CTLA-4 Axis:                                                       
║
║     ┌──────────────────────────────────────────────────────────────┐   
║
║     │                                                              │   
║
║     │  APC (antigen-          T CELL                              │   
║
║     │   presenting cell)                                           │  
 ║
║     │                                                              │   
║
║     │   B7-1/B7-2 ──────┬──── CD28 (stimulatory)                │   ║
║     │   (CD80/86)        │                                         │   
║
║     │                    └──── CTLA-4 (inhibitory)                │   
║
║     │                         (higher affinity than CD28 →        │   
║
║     │                          outcompetes CD28 for B7 binding)    │   
║
║     │                                                              │   
║
║     │  Result: T cell priming is inhibited in lymph node          │   
║
║     │  Also: Tregs constitutively express CTLA-4 → suppressive    │   
║
║     │                                                              │   
║
║     │  Therapeutic targeting:                                      │   
║
║     │  • Ipilimumab (anti-CTLA-4): first checkpoint inhibitor     │   
║
║     │  • Tremelimumab                                              │  
 ║
║     └──────────────────────────────────────────────────────────────┘   
║
║                                                                        
║
║  2. MHC CLASS I DOWNREGULATION                                         
║
║     ══════════════════════════                                         
 ║
║     • CD8+ T cells recognize antigen presented on MHC-I              ║
║     • Tumor cells reduce/lose MHC-I → invisible to CD8+ T cells      ║
║     • Mechanisms:                                                      
║
║       - B2M mutation (β2-microglobulin, essential for MHC-I 
stability)║
║       - TAP1/2 downregulation (transporter for antigen 
processing)    ║
║       - NLRC5 silencing (master regulator of MHC-I genes)             
║
║       - HLA loss of heterozygosity (lose one haplotype)               
║
║       - Epigenetic silencing of antigen processing genes              
║
║     • Consequence: resistant to T cell-mediated killing              
║
║     • BUT: NK cells detect "missing self" → kill MHC-low cells       
║
║     • Tumor counter: upregulate HLA-E/G (non-classical MHC) →        
║
║       inhibit NK cells via NKG2A                                      
 ║
║     • Monalizumab (anti-NKG2A) → reactivates NK cells                ║
║                                                                        
║
║  3. ANTIGEN LOSS                                                       
 ║
║     ════════════════                                                   
 ║
║     • Tumor stops expressing the antigen that T cells recognize        
║
║     • Selective pressure: T cells kill antigen-positive cells →       
║
║       only antigen-negative cells survive                             
 ║
║     • Antigenic modulation: internalize antigen-antibody complexes     
║
║     • Defective antigen processing: proteasome subunit mutations       
║
║       → altered peptide repertoire → T cells can't recognize          
║
║                                                                       
 ║
║  4. IMMUNOSUPPRESSIVE CELLS                                            
║
║     ════════════════════════                                           
 ║
║     • Tregs (see above): suppress effector T cells                    
║
║     • M2 macrophages/TAMs (see above): immunosuppressive             
║
║     • MDSCs (see above): broad immunosuppression                     
║
║     • Tolerogenic DCs: induce T cell anergy or Treg differentiation   
║
║     • Bregs: IL-10 and TGF-β producing B cells                       ║
║                                                                        
║
║  5. IMMUNOSUPPRESSIVE METABOLITES                                      
║
║     ════════════════════════════                                       
 ║
║     • IDO (indoleamine 2,3-dioxygenase):                              
║
║       Tryptophan → Kynurenine → T cell anergy and death             ║
║       (tryptophan depletion → GCN2 activation → T cell arrest)        
║
║     • CD39/CD73 on Tregs and tumor cells:                             
 ║
║       ATP → ADP → AMP → Adenosine                                     
║
║       Adenosine → A2A receptor on T cells → suppressed               
║
║     • Arginase (from MDSCs, TAMs):                                    
║
║       L-arginine depletion → CD3ζ chain downregulation →              
║
║       T cell dysfunction                                              
║
║     • Hypoxia → HIF-1α → adenosine pathway upregulation              ║
║     • Lactate (from Warburg effect):                                  
║
║       Acidifies TME → inhibits T cell and NK cell function            
║
║       → M2 polarization of macrophages                                
║
║                                                                       
 ║
║  6. PHYSICAL BARRIERS                                                  
║
║     ═════════════════                                                  
 ║
║     • Dense ECM (desmoplasia) → T cells can't physically infiltrate   
║
║       → Characteristic of pancreatic cancer ("immune desert")         
║
║     • Abnormal vasculature → poor T cell trafficking                  
║
║     • Immune-excluded phenotype: T cells at periphery but not in      
║
║       tumor core → physical barrier                                   
║
║                                                                       
 ║
║  7. OTHER CHECKPOINTS                                                  
 ║
║     ═══════════════════                                                
 ║
║     • LAG-3 (lymphocyte activation gene 3)                           ║
║     • TIM-3 (T cell immunoglobulin and mucin domain 3)               ║
║     • TIGIT (T cell immunoreceptor with Ig and ITIM domains)          
║
║     • VISTA                                                           
║
║     • B7-H3, B7-H4                                                    
║
║     → All being investigated as therapeutic targets                   
║
║     → Combination checkpoint blockade is a major clinical direction   
║
║                                                                       
 ║
╚════════════════════════════════════════════════════════════════════════╚══════════════════════════════════════════════════════════════════════════╝
```

### 11.3 Tumor Immune Phenotypes (Relevant for Your Research)

```
Three major immune phenotypes visible in H&E and detectable by 
spatial transcriptomics:

IMMUNE-INFLAMED ("Hot"):
  ┌────────────────────────────────────────────┐
  │  ████████████████████████                   │
  │  ██ TUMOR ████ TILs ██ TUMOR ████ TILs ██  │
  │  ████████████████████████                   │
  │  T cells infiltrating throughout tumor     │
  │  PD-L1 often positive (adaptive resistance)│
  │  IFN-γ signature present                    │
  │  Best response to checkpoint inhibitors     │
  │  H&E: Lymphocytes diffusely scattered       │
  │    within tumor cell nests                  │
  └────────────────────────────────────────────┘

IMMUNE-EXCLUDED:
  ┌────────────────────────────────────────────┐
  │  TILs     ████████████████     TILs         │
  │  ═════    ██ TUMOR      ██    ═════         │
  │  ═════    ██ TUMOR      ██    ═════         │
  │  ═════    ██ TUMOR      ██    ═════         │
  │  TILs at periphery, stroma around tumor    │
  │  Physical/chemical barrier prevents          │
  │    infiltration                             │
  │  CAF-enriched stroma (TGF-β signaling)      │
  │  Vascular adhesion issues                   │
  │  Checkpoint inhibitors may not work alone   │
  │  H&E: Lymphocytes ring the tumor but        │
  │    don't penetrate the tumor nests          │
  │  THIS IS WHERE SPATIAL ANALYSIS IS CRITICAL │
  └────────────────────────────────────────────┘

IMMUNE-DESERt ("Cold"):
  ┌────────────────────────────────────────────┐
  │  ████████████████████████████████████        │
  │  ██ TUMOR ██ TUMOR ██ TUMOR ██ TUMOR ██    │
  │  ██ TUMOR ██ TUMOR ██ TUMOR ██ TUMOR ██    │
  │  ████████████████████████████████████        │
  │  Few or no T cells anywhere                │
  │  Low neoantigen burden                     │
  │  Poor antigen presentation (MHC-I loss)     │
  │  Wnt/β-catenin activation (excludes T cells)│
  │  Checkpoint inhibitors generally ineffective│
  │  Need: vaccines, oncolytic viruses,        │
  │    adoptive cell therapy to prime response  │
  │  H&E: Sparse inflammatory infiltrate        │
  │    throughout the entire specimen            │
  └────────────────────────────────────────────┘

RELEVANCE TO YOUR RESEARCH:
  • Whole-cell segmentation + cell typing → classify immune phenotype
  • Spatial distribution of immune cells → inflamed/excluded/desert
  • Spatial transcriptomics → immune gene signatures in specific regions
  • Combined: morphology + expression → comprehensive immune profiling
  • This has direct clinical implications for treatment selection
```

---

## 12. Angiogenesis and Metastasis

(Detailed in Hallmark 5 and 6 above; additional details below)

### 12.1 Tumor Vasculature — Pathology Relevance

```
TUMOR VESSELS VS NORMAL VESSELS:

  Normal vessel:                     Tumor vessel:
  ┌──────────────────┐              ┌──────────────────┐
  │  Endothelial      │              │  Endothelial      │
  │  (tight junctions)│              │  (gaps, loose    │
  │                   │              │   junctions)      │
  │  Pericytes (full  │              │  Pericytes (few,  │
  │  coverage)       │              │   loose attachment│
  │                   │              │                   │
  │  Basement         │              │  Basement         │
  │  membrane (intact)│              │  membrane (loose,│
  │                   │              │   irregular)      │
  │  Regular lumen    │              │  Irregular lumen, │
  │  Normal blood flow│              │  Sluggish/chaotic │
  └──────────────────┘              └──────────────────┘

Consequences of abnormal vasculature:
  1. Leakiness → high interstitial fluid pressure → poor drug delivery
  2. Hemorrhage → areas of hemosiderin deposition (yellow-brown on H&E)
  3. Hypoxia → HIF-1α → VEGF → more abnormal vessels (vicious cycle)
  4. Hypoxia → glycolytic shift → acidification → immune suppression
  5. Hypoxia → EMT → metastasis
  6. Intermittent flow → reperfusion injury → more DNA damage → 
mutations

H&E appearance of tumor vessels:
  • Irregular, dilated, thin-walled vessels
  • Red blood cells in lumen (or extravasated = hemorrhage)
  • Vessels at tumor periphery may be more normal
  • Glomeruloid vessels (in glioblastoma): tufted, complex vascular
    proliferations = WHO grade IV feature
```

---

## 13. Cancer Metabolism

### 13.1 The Warburg Effect

```
NORMAL CELL METABOLISM:
═══════════════════════

  Glucose → Glycolysis → Pyruvate
                              │
               ┌──────────────┤
               │              │
          Aerobic:        Anaerobic:
          Pyruvate →      Pyruvate → Lactate
          Mitochondria     (only when O2 is limited)
          (TCA cycle →     → 2 ATP per glucose
           OXPHOS → 
           36-38 ATP per glucose)

  Normal cells PREFER OXPHOS when oxygen is available.
  Glycolysis is the backup plan for hypoxia.

CANCER CELL METABOLISM (Warburg Effect):
════════════════════════════════════════

  Glucose → Glycolysis → Pyruvate → LACTATE
                              │
                              │ Even when OXYGEN IS PRESENT
                              │ (aerobic glycolysis)
                              │
                              │ → Only 2 ATP per glucose
                              │ → BUT: much faster than OXPHOS
                              │ → Glucose uptake 10-50x higher
                              │ → Lactate production ↑↑↑

  WHY? Advantages of Warburg metabolism:
  1. SPEED: Glycolysis is ~100x faster than OXPHOS
     → Rapid ATP production despite lower yield
  2. BIOSYNTHETIC PRECURSORS:
     → Glycolytic intermediates feed pentose phosphate pathway → 
nucleotides
     → 3-phosphoglycerate → serine → glycine → one-carbon metabolism → 
nucleotides
     → Pyruvate → acetyl-CoA → fatty acid synthesis → membrane lipids
     → Cancer cells need BUILDING BLOCKS, not just energy
  3. ACIDIFICATION:
     → Lactate → acidified TME → immune suppression
     → Matrix degradation (MMPs activated at low pH)
     → Invasion promotion
  4. REDOX HOMEOSTASIS:
     → NADPH from pentose phosphate pathway → antioxidant → survive ROS

  Detected clinically: FDG-PET scan
  18F-fluorodeoxyglucose (FDG) is a glucose analog
  → Taken up by cancer cells (high GLUT1 expression)
  → Trapped intracellularly (phosphorylated but not metabolized)
  → PET detects the radioactivity → tumor imaging
```

### 13.2 Metabolic Reprogramming Beyond Warburg

```
GLUTAMINE ADDICTION:
  • Many cancer cells are dependent on glutamine
  • Glutamine → glutamate → α-ketoglutarate → enters TCA cycle
  • Provides carbon and nitrogen for biosynthesis
  • MYC drives glutamine metabolism (GLS, SLC1A5)
  • Therapeutic target: GLS inhibitors (CB-839 in clinical trials)

LIPID METABOLISM:
  • De novo fatty acid synthesis (FASN overexpression in cancer)
  • SREBP1 activation (cholesterol and fatty acid synthesis)
  • Fatty acid oxidation (FAO) in some cancers (leukemia, metastatic)
  • Lipid droplet accumulation → energy storage and signaling

ONE-CARBON METABOLISM:
  • Folate cycle + methionine cycle
  • Purine and pyrimidine synthesis
  • Methylation reactions (SAM → SAH)
  • MTHFR, SHMT2, MTHFD2 → upregulated in cancer
  • Chemotherapy target: methotrexate, pemetrexed (antifolates)

MITOCHONDRIAL METABOLISM:
  • Not completely shut down (common misconception)
  • TCA cycle provides biosynthetic intermediates
  • OXPHOS still occurs, especially in:
    - Cancer stem cells (rely on OXPHOS, glycolysis-independent)
    - Metastatic cells (may shift to OXPHOS at metastatic site)
    - Drug-resistant cells (often OXPHOS-dependent)
  • OXPHOS inhibitors (IACS-010759) in clinical trials

METABOLIC HETEROGENEITY:
  • Different cells in the same tumor have different metabolic states
  • Hypoxic cells: glycolytic
  • Oxygenated cells near vessels: may use OXPHOS
  • Metabolic symbiosis: hypoxic cells produce lactate → 
    oxygenated cells take up lactate (MCT1) → convert to pyruvate → 
OXPHOS
  • This metabolic coupling can be mapped with spatial transcriptomics
```

---

## 14. Histopathology and H&E Interpretation

### 14.1 The H&E Stain — Chemistry and What It Shows

```
HEMATOXYLIN:
  • Extracted from Haematoxylum campechianum (logwood tree)
  • Aluminum-hematein complex (mordant-dye)
  • Positively charged → binds negatively charged structures
  • Stains NUCLEI blue-purple (basophilic)
  • Binds: DNA (phosphate backbone), RNA (phosphate), acidic proteins
  
  Hematoxylin intensity reflects:
  • DNA content (more DNA = darker — tetraploid cells darker)
  • Chromatin compaction (dense heterochromatin = very dark)
  • Nucleolar RNA (prominent nucleoli in cancer = more rRNA)

EOSIN:
  • Xanthene dye (eosin Y, eosin B)
  • Negatively charged → binds positively charged structures
  • Stains CYTOPLASM, ECM, collagen pink-red (eosinophilic)
  • Binds: basic amino acids (lysine, arginine), proteins
  
  Eosin intensity reflects:
  • Cytoplasmic protein content (more protein = more pink)
  • Collagen density (dense collagen = bright pink)
  • Keratinization (squamous differentiation = intense pink)
  • Muscle fibers (eosinophilic)
  • RBCs (very eosinophilic — filled with hemoglobin)

WHAT YOU CAN AND CANNOT SEE ON H&E:

  CAN SEE:                         CANNOT SEE (need IHC, ISH, 
molecular):
  • Nuclear size and shape         • Specific protein 
expression
  • Chromatin pattern              • Gene mutations
  • Nucleolar size and number      • Cell surface markers
  • Cytoplasmic amount and color   • Specific cell lineages (often)
  • Tissue architecture            • Viral DNA/RNA
  • Mitotic figures                • Gene fusions
  • Necrosis                       • Receptor status (ER, PR, HER2)
  • Inflammatory infiltrates       • Proliferation index (need Ki-67 
IHC)
  • Blood vessels                  • Specific immune subsets
  • Collagen/ECM density           • Microsatellite instability
                                   • PD-L1 expression (need IHC)
```

### 14.2 Systematic H&E Interpretation for Computational Pathology

```
STEP 1: LOW POWER (2x-4x) — ARCHITECTURE
═══════════════════════════════════════════
  • Is the tissue normal or abnormal?
  • What organ/tissue type is this?
  • Is there a mass/lesion?
  • What is the overall architecture?
    - Glandular? (adenocarcinoma pattern)
    - Sheets/nests? (solid/ductal pattern)
    - Single cells infiltrating? (diffuse pattern — signet ring, 
lobular)
    - Papillary? (finger-like projections)
    - Trabecular? (cord-like)
  • Where is the tumor relative to normal tissue?
  • Is there necrosis? (geographic necrosis = large areas of dead 
tissue)
  • Is there desmoplasia? (pink fibrotic stroma around tumor)

STEP 2: MEDIUM POWER (10x) — CELL POPULATIONS
═══════════════════════════════════════════════
  • What cell types are present?
    - Tumor cells (abnormal morphology)
    - Lymphocytes (small dark round nuclei)
    - Plasma cells (eccentric clock-face nucleus, perinuclear hof)
    - Neutrophils (segmented nuclei, may be in microabscesses)
    - Eosinophils (bilobed nucleus, red granules)
    - Macrophages (large, pale cytoplasm, may be foamy)
    - Fibroblasts (spindle-shaped)
    - Endothelial cells (lining vessels)
  • What is the ratio of tumor to stroma?
  • Are immune cells at the periphery or infiltrating?
  • Are there vascular or perineural invasion?

STEP 3: HIGH POWER (20x-40x) — CYTOLOGIC FEATURES
═══════════════════════════════════════════════════
  • Nuclear features:
    - Size (microns if possible to estimate)
    - Shape (round, oval, irregular, pleomorphic)
    - Chromatin: fine vs. coarse vs. vesicular vs. hyperchromatic
    - Nuclear membrane: smooth vs. irregular
    - Nucleoli: absent, small, prominent, multiple
    - Inclusions: viral (Cowdry A bodies in HSV), nuclear 
pseudoinclusions
  • Cytoplasmic features:
    - Amount: scant, moderate, abundant
    - Color: eosinophilic (pink), basophilic (blue), clear/empty
    - Inclusions: mucin (pale blue vacuoles → signet ring cells),
      melanin (brown pigment), hemosiderin (golden-brown)
  • Mitotic figures:
    - Normal: bipolar (two distinct chromatin masses)
    - Abnormal: tripolar, multipolar, asymmetric
    - Count per 10 HPF (high-power fields) → mitotic rate
    - Very high mitotic rate = aggressive behavior
  • Apoptotic bodies:
    - Fragmented nuclear material
    - Eosinophilic cytoplasmic bodies
  • Necrosis:
    - Coagulative: ghost cells (preserved architecture, no nuclei)
    - Liquefactive: loss of architecture, debris
    - Caseating (granulomas): amorphous pink material
```

### 14.3 Common Morphological Patterns and Their Significance

```
┌──────────────────────────────────────────────────────────────────────┐
│  PATTERN                SIGNIFICANCE           CANCER EXAMPLE       │
│  ────────               ─────────────           ──────────────      │
│                                                                      │
│  Glandular/tubular      Well-differentiated    Adenocarcinoma      │
│  (organized glands)     adenocarcinoma         (various organs)     │
│                                                                      │
│  Cribriform             "Swiss cheese" pattern  Prostate (Gleason   │
│  (sieve-like, with     → intermediate grade     pattern 3+3)        │
│  punched-out lumens)                                                │
│                                                                      │
│  Solid sheets/nests     Poorly differentiated   Various             │
│  (no gland formation)   → higher grade                             │
│                                                                      │
│  Single file/Indian     Lobular carcinoma       Invasive lobular    │
│  file pattern           (loss of E-cadherin)    breast cancer       │
│                                                                      │
│  Signet ring cells      Intracytoplasmic        Diffuse type        │
│  (nucleus pushed to     mucin vacuole           gastric cancer,     │
│  periphery by mucin)                            lobular breast     │
│                                                                      │
│  Papillary              Finger-like fronds      Thyroid, ovarian,   │
│  (fibrovascular cores   with fibrovascular      bladder             │
│  covered by epithelium) cores                                       │
│                                                                      │
│  Micropapillary         No fibrovascular core   Aggressive variant  │
│  (small papillary       → lymphovascular        in breast, lung,   │
│  clusters without       invasion prone           bladder            │
│  fibrovascular cores)                                                │
│                                                                      │
│  Trabecular             Cord-like arrangement   Hepatocellular      │
│                         (hepatocellular         carcinoma           │
│                         pattern)                                     │
│                                                                      │
│  Spindle cell           Mesenchymal appearance  Sarcomatoid          │
│  (elongated, fusiform)  → sarcoma or           carcinoma,          │
│                         sarcomatoid             sarcoma              │
│                         differentiation                               
│
│                                                                      
│
│  Rhabdoid               Eccentric nucleus,     Aggressive variant   │
│  (large eosinophilic    prominent nucleolus,   in many cancers     │
│   cytoplasmic inclusion) inclusion body        (SMARCB1 loss)       │
│                                                                      │
│  Small blue cells       High N:C ratio,         Small cell          │
│  (dense dark nuclei     minimal cytoplasm,     carcinoma,           │
│   with very little      high mitotic rate       lymphoma,           │
│   cytoplasm)                                   neuroblastoma       │
│                                                                      │
│  Clear cells            Cytoplasm cleared of    Renal cell           │
│  (empty/transparent     lipids/glycogen        carcinoma,           │
│   cytoplasm)            (dissolved during       ovarian clear cell,  │
│                         processing)            adrenal cortical     │
│                                                                      │
│  Keratin pearls         Concentric layers of    Squamous cell       │
│  (pink, lamellated      keratin → well-        carcinoma            │
│   eosinophilic          differentiated                              │
│   structures)           squamous                                    │
│                                                                      │
│  Rosettes               Radial arrangement of   Neuroblastoma,      │
│  (Homer Wright/         neuroblasts around      medulloblastoma,    │
│   Flexner-Wintersteiner) central neuropil/      retinoblastoma      │
│                         lumen                                        │
│                                                                      │
│  Starry sky            Macrophages with         Burkitt lymphoma,   │
│  (large pale           phagocytosed debris     high-grade           │
│   macrophages          among dark blue         lymphomas           │
│   against dark          lymphocytes)                                │
│   background of                                                       
│
│   lymphocytes)                                                        
│
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

### 14.4 Tumor Grading Systems

```
NOTTINGHAM (BLOOM-RICHARDSON) GRADE — Breast Cancer
═══════════════════════════════════════════════════

  Three components, each scored 1-3:

  1. TUBULE FORMATION (glandular differentiation)
     Score 1: >75% of tumor forms tubules
     Score 2: 10-75% forms tubules
     Score 3: <10% forms tubules (mostly solid sheets)

  2. NUCLEAR PLEOMORPHISM
     Score 1: Small, uniform, regular nuclei
     Score 2: Moderate variation in size and shape
     Score 3: Marked variation, large irregular nuclei, prominent 
nucleoli

  3. MITOTIC COUNT (per 10 HPF at 40x, field diameter varies)
     Score 1: Low mitotic count
     Score 2: Intermediate
     Score 3: High (depends on field area)

  Total: 3-5 = Grade 1 (well-differentiated)
         6-7 = Grade 2 (moderately differentiated)
         8-9 = Grade 3 (poorly differentiated)

GLEASON GRADE — Prostate Cancer
═══════════════════════════════

  Pattern 1: Very well-differentiated, rare
  Pattern 2: Well-differentiated, still fairly organized glands
  Pattern 3: Most common, variably sized glands, cribriform
  Pattern 4: Fused glands, poorly formed glands, cribriform
  Pattern 5: No gland formation, solid sheets, single cells

  Grade = Most common pattern + Worst pattern
  Example: 3+4=7 (Gleason 7, favorable) vs. 4+3=7 (Gleason 7, 
unfavorable)

WHO GRADING — Various CNS Tumors
═════════════════════════════════
  Now incorporates molecular features (e.g., IDH status for glioma)

FUHRMAN GRADE — Renal Cell Carcinoma (historical, being replaced)
═════════════════════════════════════════════════════════════════

NOTE FOR YOUR RESEARCH:
  Grading is PARTIALLY QUANTIFIABLE by computational methods:
  • Nuclear pleomorphism → nuclear size/shape feature extraction
  • Tubule formation → architectural pattern recognition
  • Mitotic count → mitosis detection (AMARA challenge, etc.)
  • All of these require good cell segmentation
```

---

## 15. Molecular Classification of Cancer

### 15.1 Beyond Histology: Molecular Subtypes

```
BREAST CANCER MOLECULAR SUBTYPES (Perou/Sørlie classification):
═══════════════════════════════════════════════════════════════

  ┌──────────────────┬─────────────┬─────────────┬─────────────┬─────────┌──────────────────┬─────────────┬─────────────┬─────────────┬─────────────┐
  │                   │ Luminal A   │ Luminal B   │ HER2-       │ 
Basal-like  │
  │                   │             │             │ enriched    │ (TNBC) 
     │
  │  ──────────────  │ ──────────  │ ──────────  │ ──────────  │ 
──────────  │
  │  ER/PR           │ ER+/PR+     │ ER+/PR±     │ ER-/PR-     │ ER-/PR- 
    │
  │  HER2            │ HER2-       │ HER2±       │ HER2+       │ HER2-   
    │
  │  Ki-67           │ Low (<14%)  │ High (≥14%) │ Variable    │ High    
    │
  │  Grade           │ Low         │ High        │ High        │ High    
    │
  │  Prognosis       │ Best        │ Intermediate│ Poor (pre-  │ Worst   
    │
  │                  │             │             │ trastuzumab)│         
    │
  │  Common          │ PIK3CA mut  │ PIK3CA mut  │ ERBB2 amp   │ TP53 
mut    │
  │  mutations       │             │             │             │ BRCA1 
mut   │
  │                  │             │             │             │ RB1 
loss    │
  │  H&E features    │ Well-diff   │ Mod-poor    │ May have    │ Poorly 
diff │
  │                  │ tubules     │ diff        │ micropapillary│ solid 
sheets│
  │                  │             │             │ features    │ 
high-grade  │
  │                  │             │             │             │ nuclei  
    │
  └──────────────────┴─────────────┴─────────────┴─────────────┴─────────└──────────────────┴─────────────┴─────────────┴─────────────┴─────────────┘

  TNBC further subdivided (Lehmann/Burstein subtypes):
  • Basal-like 1 (BL1): DNA damage response, cell cycle genes
  • Basal-like 2 (BL2): Growth factor, metabolic pathways
  • Mesenchymal (M): EMT, motility, ECM interaction
  • Mesenchymal stem-like (MSL): Similar to M + stem cell features
  • Immunomodulatory (IM): Immune signaling, best prognosis
  • Luminal androgen receptor (LAR): AR-driven, distinct from others

COLORECTAL CANCER — Consensus Molecular Subtypes (CMS):
═══════════════════════════════════════════════════════════

  CMS1 (MSI-Immune): 14%
    • MSI-high, hypermutated, BRAF mutations
    • Strong immune activation (Cytotoxic T cells)
    • Best prognosis in early stage
    • Responds to immunotherapy

  CMS2 (Canonical): 37%
    • Chromosomal instability (CIN), WNT/MYC activation
    • Epithelial, well-differentiated
    • Moderate prognosis

  CMS3 (Metabolic): 13%
    • KRAS mutations, metabolic dysregulation
    • Eosinophilic cytoplasm, mucinous features may be present

  CMS4 (Mesenchymal): 38%
    • TGF-β activation, stromal infiltration
    • Worst prognosis
    • EMT, angiogenesis, CAF-rich
    • H&E: Prominent desmoplastic stroma, infiltrative borders

GLIOMA — WHO 2021 Classification (now integrates molecular):
═══════════════════════════════════════════════════════

  IDH-wildtype glioblastoma (worst prognosis, ~15 months)
    + TERT promoter mutation
    + EGFR amplification
    + +7/-10 copy number changes

  IDH-mutant astrocytoma (better prognosis)
    + ATRX mutation (in most)
    + TP53 mutation
    + Grades 2-4 based on specific markers

  IDH-mutant, 1p/19q-codeleted oligodendroglioma (best prognosis)
    + CIC, FUBP1 mutations
    + TERT promoter mutation
    + Sensitive to PCV chemotherapy

  Key insight: Same histological grade can have very different outcomes
  based on molecular features → molecular testing is essential
```

---

## 16. Spatial Biology and the TME

### 16.1 Spatial Transcriptomics Technologies

```
SPATIAL TRANSCRIPTOMICS TECHNOLOGY COMPARISON:
═════════════════════════════════════════════

┌─────────────────┬──────────────┬───────────────┬───────────────┬───────┌─────────────────┬──────────────┬───────────────┬───────────────┬──────────────────┐
│  Technology     │  Resolution  │  Genes/Panel  │  Tissue area  │  
Method          │
│  ─────────────  │  ──────────  │  ───────────  │  ───────────  │  
──────────────  │
│  10x Visium     │  55μm spots  │  Whole        │  6.5×6.5mm   │  
Barcoded spots  │
│                 │  (1-10 cells)│  transcriptome│  per capture  │  on 
glass slide  │
│                 │              │               │  area         │       
           │
│  10x Visium HD  │  2μm bins    │  Whole        │  6.5×6.5mm   │  
Continuous grid │
│                 │  (subcellular│  transcriptome│               │  of 
barcoded     │
│                 │   in theory) │               │               │  
spots           │
│  10x Xenium     │  Subcellular │  300-5000    │  ~1cm²        │  In 
situ         │
│                 │  (~100nm)    │  genes (panel)│               │  
hybridization   │
│                 │              │               │               │  + 
rolling       │
│                 │              │               │               │  
circle amplif.  │
│  MERFISH        │  Subcellular │  100-10,000  │  ~1-5mm²      │  
Combinatorial   │
│  (Vizgen)       │  (~100nm)    │  genes        │               │  FISH 
barcoding  │
│                 │              │               │               │  + 
imaging       │
│  CosMx SMI      │  Subcellular │  1000+ genes │  Multiple FOV │  ISH 
with       │
│  (NanoString)   │              │  (panel)      │               │  
fluorescent     │
│                 │              │               │               │  
readout         │
│  Stereo-seq     │  Subcellular │  Whole        │  Up to 13×13cm│  DNA 
nanoball   │
│  (BGI)          │  (500nm bins)│  transcriptome│  (whole organ!)│  
grid + capture │
│                 │              │               │               │  
sequencing      │
│  Slide-seq V2   │  10μm        │  Whole        │  3mm diameter │  
Bead-based      │
│                 │              │  transcriptome│               │  
barcoding       │
│  Seq-Scope      │  Submicron   │  Whole        │  ~2mm²        │  
Illumina        │
│                 │              │  transcriptome│               │  flow 
cell grid │
└─────────────────┴──────────────┴───────────────┴───────────────┴───────└─────────────────┴──────────────┴───────────────┴───────────────┴──────────────────┘

KEY DISTINCTIONS:

  SEQUENCING-BASED (Visium, Slide-seq, Stereo-seq):
  • Unbiased (whole transcriptome)
  • Lower spatial resolution
  • Tissue is consumed (cannot re-stain)
  • Good for discovery

  IMAGING-BASED (MERFISH, Xenium, CosMx):
  • Targeted (pre-selected gene panel)
  • Subcellular resolution
  • Tissue preserved (can re-stain with H&E, IHC)
  • Good for cell-type mapping and your research
  • Subcellular transcript locations → natural cell boundary definition

  H&E + SPATIAL TRANSCRIPTOMICS INTEGRATION:
  • Imaging-based platforms preserve tissue → H&E on same slide
  • Visium: H&E on adjacent section or same slide before 
permeabilization
  • This co-registration is exactly what enables your 
research
```

### 16.2 Computational Analysis of Spatial Transcriptomics

```
ANALYSIS PIPELINE (simplified):

1. PREPROCESSING
   • Raw data → gene expression matrix + spatial coordinates
   • Quality control (low-quality spots/cells, ambient RNA)
   • Normalization (library size, gene length)
   • Log transformation / SCTransform

2. CELL SEGMENTATION (if subcellular resolution)
   ┌──────────────────────────────────────────────────────────────┐
   │  THIS IS WHERE YOUR RESEARCH FITS                            │
   │                                                              │
   │  Approaches to defining cells from subcellular ST data:      │
   │                                                              │
   │  a) Nuclei-based:                                            │
   │     Segment nuclei → expand by fixed radius → cell boundary │
   │     Problem: arbitrary, doesn't account for cell shape        │
   │                                                              │
   │  b) Membrane staining:                                       │
   │     Use membrane stain (if available) → segment boundaries   │
   │     Problem: not always available, may be poor quality       │
   │                                                              │
   │  c) Transcript-based:                                        │
   │     Cluster transcripts → define cells by expression         │
   │     (Baysor, ComSeg, CellAssign)                            │
   │     Problem: requires sufficient transcripts per cell         │
   │                                                              │
   │  d) H&E-informed (YOUR APPROACH):                            │
   │     Use H&E morphology to guide cell boundary definition     │
   │     → Nuclei from H&E provide seeds                         │
   │     → Cytoplasmic boundaries from H&E provide constraints   │
   │     → ST data provides cell type identity                   │
   │     → Combined: accurate whole-cell segmentation            │
   │       + cell type assignment                                 │
   │                                                              │
   │  e) Multi-modal (YOUR APPROACH - advanced):                 │
   │     Simultaneously process H&E and ST data                   │
   │     → Joint model that leverages both modalities             │
   │     → H&E provides morphology features                       │
   │     → ST provides molecular features                         │
   │     → Cross-attention between modalities                    │
   └──────────────────────────────────────────────────────────────┘

3. CELL TYPE ANNOTATION
   • Reference-based: compare expression to scRNA-seq references
     (SingleR, CellTypist, Azimuth)
   • Marker-based: use known gene markers for cell types
   • De novo: unsupervised clustering + manual annotation
   • Spatially-informed: consider spatial coherence of labels

4. SPATIAL ANALYSIS
   • Neighborhood analysis: which cell types are near each other?
   • Spatial co-occurrence: cell type co-localization patterns
   • Ligand-receptor analysis: which cells are signaling to each other?
     (CellChat, NicheNet, COMMOT)
   • Spatial domains: identify tissue regions with distinct composition
     (BayesSpace, SpaGCN, STAGATE)
   • Spatial trajectory: pseudo-time analysis along spatial gradients
   • TME classification: inflamed/excluded/desert regions

5. INTEGRATION WITH H&E
   • Morphological features + expression patterns → predict cell types
   • Train on ST data → predict on H&E-only slides
   • This is the "virtual staining" or "virtual transcriptomics" concept
     → Huge clinical value: H&E is cheap and universal,
       ST is expensive and limited
```

---

## 17. Clinical Relevance for Computational Pathology

### 17.1 Why Your Research Matters Clinically

```
CLINICAL WORKFLOW WHERE YOUR RESEARCH FITS:

  Current clinical workflow:
  ┌──────────┐    ┌───────────┐    ┌──────────────┐    ┌──────────┐
  │ Biopsy   │───►│ H&E slide │───►│ Pathologist  │───►│ Report   │
  │ /surgery│    │           │    │ interpretation│    │ grade,   │
  └──────────┘    └───────────┘    └──────────────┘    │ stage,   │
                                                       │ IHC if   │
                                                       │ needed    │
                                                       └──────────┘

  Future workflow with your technology:
  ┌──────────┐    ┌───────────┐    ┌──────────────────────┐
  │ Biopsy   │───►│ H&E slide │───►│ AI-powered analysis   │
  │ /surgery│    │ + ST data │    │ • Whole-cell segment. │
  └──────────┘    └───────────┘    │ • Cell type classif.  │
                                   │ • TME characterization│
                                   │ • Immune phenotype    │
                                   │ • Spatial patterns    │
                                   └──────────┬───────────┘
                                              │
                                   ┌──────────▼───────────┐
                                   │ Integrated report     │
                                   │ • Grade + molecular  │
                                   │ • Immune phenotype   │
                                   │ • Treatment suggest. │
                                   │ • Prognosis predict. │
                                   └──────────────────────┘
```

### 17.2 Specific Clinical Applications

```
1. TUMOR GRADING AUTOMATION
   • Current: subjective, inter-observer variability
   • Your contribution: quantitative nuclear features, mitotic counting,
     architecture assessment → objective, reproducible grading

2. IMMUNE PHENOTYPING
   • Current: manual TIL assessment, semi-quantitative, variable
   • Your contribution: automated whole-cell segmentation →
     precise TIL counting, spatial distribution → 
inflamed/excluded/desert

3. TREATMENT SELECTION
   • Checkpoint inhibitors: need to know immune phenotype
   • Anti-angiogenic: need to assess microvessel density
   • Targeted therapy: need molecular subtyping
   • Your contribution: TME characterization from H+E+ST → 
     guide treatment decisions

4. PROGNOSIS PREDICTION
   • Current: stage + grade + limited biomarkers
   • Your contribution: spatial TME features → novel prognostic 
signatures
   • Immunoscore concept (Galon): CD8+ density at core + margin
     → may outperform TNM staging
   • Need whole-cell segmentation to compute this accurately

5. TREATMENT RESPONSE MONITORING
   • Pre- and post-treatment biopsies → compare TME changes
   • Spatial transcriptomics → track immune cell changes
   • Your contribution: standardized, reproducible cell-level analysis

6. CLINICAL TRIAL STRATIFICATION
   • Select patients likely to respond to specific therapies
   • Immune-hot tumors → checkpoint inhibitors
   • Immune-excluded → combination with TGF-β inhibitor
   • Immune-cold → vaccines + adoptive cell therapy
   • Your contribution: automated immune phenotyping from routine H&E
```

---

## 18. Glossary

| Term | Definition |
|---|---|
| **Adenocarcinoma** | Cancer of glandular epithelial origin |
| **Aneuploidy** | Abnormal number of chromosomes |
| **Angiogenesis** | Formation of new blood vessels |
| **Anoikis** | Apoptosis induced by loss of attachment to ECM |
| **Apoptosis** | Programmed cell death |
| **Basophilic** | Stains blue/purple with hematoxylin |
| **Carcinoma** | Cancer of epithelial origin |
| **CIN** | Chromosomal instability |
| **Clone** | Population of cells derived from a single progenitor |
| **CpG island** | Region of DNA with high frequency of CG dinucleotides 
|
| **Desmoplasia** | Fibrotic stromal reaction around tumor |
| **Differentiation** | Process of cell specialization |
| **Driver mutation** | Mutation that confers selective advantage to 
cancer cells |
| **EMT** | Epithelial-mesenchymal transition |
| **Eosinophilic** | Stains pink/red with eosin |
| **Epigenetics** | Heritable changes in gene expression without DNA 
sequence change |
| **Euchromatin** | Open, transcriptionally active chromatin |
| **Heterochromatin** | Condensed, transcriptionally silent chromatin |
| **Hyperplasia** | Increased number of cells, still normal appearance |
| **Hypoxia** | Low oxygen conditions |
| **In situ** | Cancer confined to original location (not invasive) |
| **Invasive** | Cancer that has broken through basement membrane |
| **LOH** | Loss of heterozygosity |
| **Lymphovascular invasion** | Tumor cells within blood or lymphatic 
vessels |
| **Metastasis** | Spread of cancer to distant sites |
| **MSI** | Microsatellite instability |
| **Necrosis** | Uncontrolled cell death (distinct from apoptosis) |
| **Neoantigen** | Novel antigen from tumor-specific mutations |
| **Oncogene** | Gene whose activation promotes cancer |
| **Passenger mutation** | Mutation that does not drive cancer growth |
| **Pleomorphism** | Variation in cell/nuclear size and shape |
| **Proliferative index** | Fraction of cells actively dividing (Ki-67) 
|
| **Sarcoma** | Cancer of mesenchymal origin |
| **Senescence** | Permanent cell cycle arrest |
| **TIL** | Tumor-infiltrating lymphocyte |
| **Translocation** | Chromosomal rearrangement |
| **TME** | Tumor microenvironment |
| **Tumor suppressor** | Gene whose inactivation promotes cancer |
| **WGD** | Whole genome duplication |

---

## 19. References

### Foundational Texts
1. Hanahan D, Weinberg RA. Hallmarks of cancer: the next generation. 
*Cell*. 2011;144(5):646-674.
2. Vogelstein B, Kinzler KW. Cancer genes and the pathways they control. 
*Nature Medicine*. 2004;10(8):789-799.
3. Weinberg RA. *The Biology of Cancer*. 2nd ed. Garland Science; 2013.
4. Alberts B et al. *Molecular Biology of the Cell*. 7th ed. W.W. 
Norton; 2022.
5. Kumar V et al. *Robbins & Cotran Pathologic Basis of Disease*. 10th 
ed. Elsevier; 2020.

### Key Reviews
6. Hanahan D, Weinberg RA. The hallmarks of cancer. *Cell*. 
2000;100(1):57-70.
7. Hanahan D. Hallmarks of cancer: new dimensions. *Cancer Discovery*. 
2022;12(1):31-46.
8. Tlsty TD, Coussens LM. Tumor stroma and regulation of cancer 
initiation and progression. *Cell*. 2006;125(6):1113-1118.
9. Joyce JA, Fearon DT. T cell exclusion, immune privilege, and the 
tumor microenvironment. *Science*. 2015;348(6230):74-80.
10. McGranahan N, Swanton C. Clonal heterogeneity and tumor evolution. 
*Cell*. 2017;168(4):613-628.

### Spatial Transcriptomics
11. Marx V. Method of the year: spatially resolved transcriptomics. 
*Nature Methods*. 2021;18(1):9-14.
12. He S et al. High-plex imaging of RNA and proteins at subcellular 
resolution. *Science*. 2022;375(6582):eabo3400.
13. Petukhov V et al. Cell segmentation in imaging-based spatial 
transcriptomics. *Nature Biotechnology*. 2022;40(3):345-354.
14. Biancalani T et al. Spatial mapping of tissue architecture at 
single-cell resolution (Slide-seq). *Nature Methods*. 
2022;19(2):181-192.

### Computational Pathology
15. Dimitriou N et al. A systematic review of computational cancer 
pathology. *Artificial Intelligence in Medicine*. 2023;142:102593.
16. Graham S et al. HoverNet: Simultaneous segmentation and 
classification of nuclei in multi-tissue histology images. *Medical 
Image Analysis*. 2019;60:101563.
17. Ho Q et al. CellViT: Vision transformers for precise cell 
segmentation and classification. *Medical Image Analysis*. 
2024;92:103048.
18. Rozman J et al. CellSAM: The cell segment anything model. *bioRxiv*. 
2024.

### Immune Oncology
19. Galon J et al. Type, density, and location of immune cells within 
human colorectal tumors predict clinical outcome. *Science*. 
2006;313(5795):1960-1964.
20. Chen DS, Mellman I. Oncology meets immunology: the cancer-immunity 
cycle. *Immunity*. 2013;39(1):1-10.
21. Binnewies M et al. Understanding the tumor immune microenvironment 
(TIME) for effective therapy. *Nature Medicine*. 2018;24(5):541-550.

---

*This document is a living reference. Update and annotate as your 
understanding deepens through literature reading, dataset exploration, 
and experimental work.*

---

*Last updated: 2025*

---

## Related

- [[Cancer Biology MOC]]
- [[Tumor Microenvironment]]
- [[Digital Pathology MOC]]
- [[Computational Pathology MOC]]
