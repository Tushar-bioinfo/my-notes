---
tags:
  - biology
  - cancer-biology
  - genomics
  - mutations
  - cornell
aliases:
  - Somatic Mutations
  - Mutational Signatures
  - DNA Repair Deficiency
date: 2026-04-14
status: permanent
---
# Mutations and Genomic Alterations

> [!ABSTRACT] Summary
> Cancer arises from accumulated somatic alterations: single nucleotide variants (SNVs), insertions/deletions (INDELs), copy number alterations (CNAs), structural variants (SVs), and whole genome duplication. Each mutational process leaves a characteristic "signature" pattern. Defective DNA repair pathways (MMR, HR, NER, BER, Fanconi) are root causes of genomic instability and create specific therapeutic vulnerabilities — most notably MSI-H tumors responding to immunotherapy and BRCA-deficient tumors responding to PARP inhibitors.

---

## Cue Questions

> [!QUESTION] Key questions for self-testing
> - Name the 5 types of somatic alterations in cancer.
> - What is a mutational signature, and how does it reveal the cause of cancer?
> - What is Signature 7 (UV), Signature 4 (tobacco), and Signature 3 (HR deficiency)?
> - What is microsatellite instability (MSI), and which repair pathway deficiency causes it?
> - Why was anti-PD-1 for MSI-H tumors the first tissue-agnostic FDA approval?
> - Explain synthetic lethality in the context of PARP inhibitors and BRCA mutations.
> - What is chromothripsis, and what is extrachromosomal DNA (ecDNA)?
> - What is the "BRCAness" phenotype?

---

## Notes

### 3.1 Types of Somatic Alterations in Cancer

#### Single Nucleotide Variants (SNVs)
- Most common type of somatic mutation
- **Transition:** purine↔purine (A↔G) or pyrimidine↔pyrimidine (C↔T)
- **Transversion:** purine↔pyrimidine
- C→T transitions at CpG sites = most common mutation in cancer

#### Small Insertions and Deletions (INDELs)
- Frameshift mutations in coding regions → truncated or altered proteins
- **Microsatellite instability (MSI):** frameshifts in repetitive sequences → hallmark of mismatch repair deficiency

#### Copy Number Alterations (CNAs)
- **Amplifications:** oncogenes (MYC, HER2/ERBB2, EGFR, MDM2, CCND1)
- **Deletions:** tumor suppressors (CDKN2A, PTEN, RB1, SMAD4)
- Focal amplifications vs. whole chromosome/arm gains
- **Copy number neutral LOH (CN-LOH):** uniparental disomy → both copies carry mutant allele

#### Structural Variants (SVs)

| Type | Example | Cancer |
|---|---|---|
| **Translocation** | t(9;22) BCR-ABL | CML |
| **Translocation** | t(14;18) BCL2 | Follicular lymphoma |
| **Translocation** | t(11;14) CCND1 | Mantle cell lymphoma |
| **Chromothripsis** | Catastrophic shattering of one chromosome | Dozens of rearrangements in one event |
| **Chromoplexy** | Coordinated rearrangements across multiple chromosomes | Complex cancers |
| **BFB cycles** | Breakage-fusion-bridge → gene amplification | Various |
| **ecDNA** | Circular extrachromosomal DNA carrying oncogenes | Rapid evolution, uneven segregation |

#### Whole Genome Duplication (WGD)
- Occurs in ~30% of cancers
- Tetraploidy → subsequent chromosome loss → aneuploidy
- Promotes genomic instability

---

### 3.2 Mutational Processes and Signatures

Each mutational process leaves a characteristic pattern (~50+ signatures catalogued in COSMIC database):

| Signature | Pattern | Etiology | Cancer Types |
|---|---|---|---|
| **Sig 1** | C>T at CpG | Aging / spontaneous deamination | All (age-related) |
| **Sig 2** | C>T at TpC | APOBEC activity | Bladder, breast, head/neck, lung |
| **Sig 4** | C>A | Tobacco smoking | Lung |
| **Sig 7** | C>T at dipyrimidine + CC>TT tandems | UV exposure (pathognomonic) | Melanoma, skin SCC |
| **Sig 3** | Broad pattern | HR deficiency (BRCA1/2 mutations) | Breast, ovarian |
| **Sig 13** | C>G at TpC | APOBEC (paired with Sig 2) | Same as Sig 2 |

> [!EXAMPLE] APOBEC Mutagenesis (Signatures 2 & 13)
> APOBEC cytidine deaminases are normally antiviral defense. In cancer, off-target activity on genomic DNA causes C>T and C>G at TCA/T motifs. Creates **kataegis** (localized hypermutation clusters) — an active, ongoing mutational process.

---

### 3.3 DNA Repair Pathways and Their Deficiencies

| Repair Pathway | Type of Damage | Key Genes | Cancer Association |
|---|---|---|---|
| **Mismatch Repair (MMR)** | Base-base mismatches, insertion/deletion loops | MLH1, MSH2, MSH6, PMS2 | Lynch syndrome, MSI-high tumors, ~15% CRC |
| **Homologous Recombination (HR)** | Double-strand breaks, interstrand crosslinks | BRCA1, BRCA2, PALB2, RAD51, ATM, CHEK2 | Hereditary breast/ovarian, pancreatic; PARP inhibitor sensitivity |
| **Non-Homologous End Joining (NHEJ)** | Double-strand breaks | KU70/80, DNA-PKcs, XRCC4, LIG4 | Lymphoid malignancies |
| **Nucleotide Excision Repair (NER)** | Bulky adducts, UV-induced pyrimidine dimers | XPA-XPG, ERCC1-6 | Xeroderma pigmentosum → skin cancers |
| **Base Excision Repair (BER)** | Oxidized, alkylated, deaminated bases | OGG1, MUTYH, APE1, XRCC1 | MUTYH-associated polyposis |
| **Fanconi Anemia Pathway** | Interstrand crosslinks | FANCA-FANCW (22 genes) | Fanconi anemia → AML, SCC |
| **Translesion Synthesis (TLS)** | Replication past damage | POLη, POLι, REV1, REV3L | XP-variant |

#### Clinical Significance

> [!IMPORTANT] MMR Deficiency / MSI-High
> - Pembrolizumab (anti-PD-1) FDA-approved for **ANY MSI-H solid tumor** — first tissue-agnostic FDA approval
> - High mutational burden → neoantigens → immune recognition
> - Detection methods: IHC for MMR proteins, PCR for microsatellites, or NGS-based MSI scoring

> [!IMPORTANT] HR Deficiency (BRCA1/2 Mutations)
> - **PARP inhibitors** (olaparib, rucaparib, niraparib, talazoparib) exploit **synthetic lethality**
> - HR-deficient cells depend on PARP for repair → PARP inhibition → DNA damage accumulation → cell death
> - Normal HR-proficient cells survive PARP inhibition
> - **"BRCAness"** phenotype: HR deficiency without BRCA mutation → may also respond
> - HR deficiency score: Myriad myChoice, FoundationFocus

---

## Summary

> [!TIP] Cornell Summary
> Cancer genomes accumulate SNVs, INDELs, CNAs, structural variants, and sometimes WGD. Each mutational process leaves a signature that reveals its cause (UV, tobacco, APOBEC, aging, DNA repair deficiency). The most clinically impactful DNA repair deficiencies are MMR deficiency (MSI-H → immunotherapy response, first tissue-agnostic approval) and HR deficiency (BRCA → PARP inhibitor synthetic lethality). Understanding these mechanisms is essential for computational pathology because mutational signatures and repair deficiencies shape tumor morphology, immune infiltration patterns, and treatment response.

---

## Related

- [[Cancer Biology Reference Index]]
- [[DNA Genes and Central Dogma]]
- [[Oncogenes and Tumor Suppressors]]
- [[Immune Evasion and Immunology]]
- [[Cancer Biology MOC]]
