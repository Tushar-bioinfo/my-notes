---
tags:
  - biology
  - cancer-biology
  - epigenetics
  - chromatin
  - cornell
aliases:
  - DNA Methylation
  - Histone Modifications
  - SWI/SNF
date: 2026-04-14
status: permanent
---
# Epigenetics in Cancer

> [!ABSTRACT] Summary
> Epigenetic alterations — changes in gene expression without DNA sequence change — are as important as mutations in cancer. Three systems drive the cancer epigenome: DNA methylation (global hypomethylation + focal hypermethylation), histone modifications (writers/erasers/readers all mutated), and chromatin remodeling (SWI/SNF complex mutated in >20% of ALL cancers). Unlike mutations, epigenetic changes are reversible, making them attractive therapeutic targets (DNMT inhibitors, EZH2 inhibitors, HDAC inhibitors).

---

## Cue Questions

> [!QUESTION] Key questions for self-testing
> - What is the difference between global hypomethylation and focal hypermethylation in cancer?
> - What are DNMT1, DNMT3A/B, and TET1/2/3? Name one cancer mutation in each.
> - How do IDH1/2 mutations cause epigenetic changes (2-HG → TET2 inhibition → G-CIMP)?
> - Name 3 tumor suppressor genes silenced by promoter methylation.
> - What is the "histone code"? Name 3 active marks and 3 repressive marks.
> - What is a bivalent domain (H3K4me3 + H3K27me3), and why does it matter in cancer?
> - What is the SWI/SNF complex, and why is its mutation (~20% of all cancers) significant?
> - Explain the synthetic lethality between SWI/SNF loss and EZH2.
> - What is the difference between a writer, eraser, and reader of histone marks?

---

## Notes

### 8.1 DNA Methylation

#### The Normal Methylation Landscape

| Feature | Normal State | Cancer State |
|---|---|---|
| **CpG islands at promoters** | Unmethylated → genes ON | Hypermethylated → tumor suppressors silenced |
| **Repetitive elements** | Methylated → silenced | Hypomethylated → genomic instability, retrotransposon reactivation (LINE-1) |
| **Global methylation** | Maintained | Hypomethylated → instability, oncogene activation |

#### The Methylation Machinery

| Role | Enzyme | Function |
|---|---|---|
| **Writer** | DNMT1 | Maintenance methyltransferase (copies pattern after replication) |
| **Writer** | DNMT3A/3B | De novo methyltransferases |
| **Eraser** | TET1/2/3 | Oxidize 5mC → 5hmC → 5fC → 5caC → unmethylated C |
| **Reader** | MBD proteins (MBD1, MeCP2, MBD2/3/4) | Recruit repressive complexes to methylated DNA |

#### Cancer-Specific Examples

| Mutation / Event | Cancer Type | Consequence |
|---|---|---|
| **DNMT3A mutations** | AML (~20%) | Aberrant methylation patterns |
| **TET2 mutations** | Myeloid neoplasms (15–30%) | Impaired demethylation → hypermethylation |
| **IDH1/2 mutations** | Glioma, AML | Produce 2-HG (oncometabolite) → inhibits TET2 + JmjC demethylases → CpG island hypermethylation phenotype (G-CIMP in glioma) |
| **MLH1 promoter methylation** | Colorectal | MMR deficiency → MSI |
| **BRCA1 promoter methylation** | Breast, ovarian | BRCA1 silencing → "BRCAness" → PARP inhibitor response |
| **CDKN2A (p16) methylation** | Various | Cell cycle deregulation |

> [!IMPORTANT] Key Insight
> Promoter methylation is **functionally equivalent to mutation** — it silences genes without altering DNA sequence. But unlike mutations, it is **reversible** (therapeutic target: DNMT inhibitors azacitidine, decitabine).

---

### 8.2 Histone Modifications

The **"histone code"** — combinatorial patterns of modifications control gene expression:

#### Active Marks

| Mark | Location | Significance |
|---|---|---|
| **H3K4me3** | Promoter | Promoter activation |
| **H3K36me3** | Gene body | Active genes |
| **H3K27ac** | Enhancers, promoters | Active regulatory elements |
| **H3K9ac** | Open chromatin | Transcription-associated |
| **H3K4me1** | Enhancers | Poised or active enhancer |

#### Repressive Marks

| Mark | Location | Significance |
|---|---|---|
| **H3K27me3** | Polycomb targets | Polycomb-mediated silencing |
| **H3K9me3** | Heterochromatin | Constitutive silencing |
| **H3K9me2** | Heterochromatin | Facultative heterochromatin |
| **H4K20me3** | Pericentric heterochromatin | Structural silencing |

#### Bivalent Domains

- **H3K4me3 + H3K27me3 simultaneously** → "poised" genes (developmental regulators in stem cells)
- In cancer: resolve to either active or repressed → aberrant activation of developmental programs (EMT genes) or silencing of differentiation genes

---

### 8.3 Histone Writers, Erasers, Readers Mutated in Cancer

| Modification | Enzyme | Role | Cancer Type |
|---|---|---|---|
| **H3K27me3** (write) | EZH2 (mutated) | PRC2 component | Lymphoma (GOF), prostate |
| **H3K27me3** (erase) | UTX/KDM6A (mutated) | Demethylase | Myeloid cancers, bladder |
| **H3K4me3** (write) | MLL1 (translocation) | Methyltransferase | AML, ALL |
| **H3K9me3** (write) | SUV39H1 | Methyltransferase | Various (overexpressed) |
| **H3K27ac** (write) | CBP/p300 (mutated) | Acetyltransferases | Lymphoma, AML |
| **H3K27me3** (read) | EED (mutated) | PRC2 reader | Myeloid malignancies |
| **H3K4me3** (erase) | LSD1/KDM1A | Demethylase | AML, SCLC (overexpressed) |

---

### 8.4 Chromatin Remodeling — SWI/SNF Complex

The SWI/SNF (BAF/PBAF) complex uses ATP to remodel nucleosome positioning:

- **29 genes** encoding subunits
- **Mutated collectively in >20% of ALL human cancers**

| Subunit | Cancer Type |
|---|---|
| **ARID1A** | Ovarian clear cell, endometrial, gastric |
| **SMARCB1 (INI1)** | Rhabdoid tumors (loss is diagnostic!) |
| **SMARCA4** | Small cell carcinoma of ovary, lung |
| **PBRM1** | Renal cell carcinoma (~40%) |

**Mechanism:** Loss of chromatin remodeling → aberrant gene expression

> [!IMPORTANT] Synthetic Lethality: SWI/SNF × EZH2
> SWI/SNF-mutant cancers become dependent on EZH2 for survival → **EZH2 inhibitors** (tazemetostat, FDA-approved for epithelioid sarcoma) exploit this vulnerability.

---

## Summary

> [!TIP] Cornell Summary
> Cancer epigenetics operates through three systems: (1) **DNA methylation** — global hypomethylation causes instability while focal hypermethylation silences tumor suppressors (functionally equivalent to mutation but reversible); (2) **Histone modifications** — active marks (H3K4me3, H3K27ac) and repressive marks (H3K27me3, H3K9me3) are disrupted through mutations in writers (EZH2, MLL1), erasers (UTX, LSD1), and readers (EED); (3) **Chromatin remodeling** — SWI/SNF complex is mutated in >20% of all cancers, with loss creating EZH2 dependency (synthetic lethality). IDH1/2 mutations produce the oncometabolite 2-HG, which inhibits TET2 and creates the G-CIMP phenotype. Unlike mutations, epigenetic changes are reversible → therapeutic targets (DNMT inhibitors, EZH2 inhibitors, HDAC inhibitors).

---

## Related

- [[Cancer Biology Reference Index]]
- [[DNA Genes and Central Dogma]]
- [[Oncogenes and Tumor Suppressors]]
- [[Molecular Classification of Cancer]]
- [[Cancer Biology MOC]]
