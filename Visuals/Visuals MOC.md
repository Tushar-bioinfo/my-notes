---
tags:
  - moc
  - visuals
date: 2026-10-10
status: permanent
---
# Visuals MOC

> [!abstract] Map of Content for all visual explanations, interactive models, HTML simulations, and `proff-viz` artifacts.

## Overview
This hub tracks interactive visualizations and visual reference pages across all scientific and quantitative domains. Every visual has a companion note linking it directly into the Obsidian knowledge graph.

## 🧬 Biology & Digital Pathology Visuals

- [[Why some guides came out 19 long - Visual]] — *One read from FASTQ to the count matrix: why G-guides trim to 19 nt and how aligners rescue them...*
- [[Hematoxylin from an H&E image - Visual]] — *Watch light pass through stained tissue. Turn what reaches the camera into optical density...*
- [[MAGeCK RRA, step by step - Visual]] — *A toy knockout screen: 5 genes × 3 guides, day 0 vs day 21. Every number is computed.. Key...*
- [[MAGeCK-MLE, step by step - Visual]] — *One gene, 3 guides, 3 samples. Watch each number get made.. Key stages: Where z falls if G...*
- [[Counts to log-CPM Calculation - Visual]] — *3 genes × 4 samples. Watch each cell change....*
- [[CRISPR Knockout Screen (Standalone) - Visual]] — *A CRISPR knockout screen...*
- [[A CRISPR Knockout Screen - Visual]] — *A CRISPR knockout screen...*
## 🤖 Machine Learning & Deep Learning Visuals

- [[Reading Deep Learning Notation (Opus Edition) - Visual]] — *From one number to nested losses and attention: how the symbols look, what they compute, a...*
- [[Reading Deep Learning Notation - Visual]] — *From x_ij to softmax(QKᵀ/√d)V: what each symbol says and how the numbers move. Key stages:...*
## 📐 Mathematics & Statistics Visuals

- [[Same plants, new ruler - Visual]] — *Five seedlings show why multiplying by c multiplies the SD by |c| and the variance by c²,...*
- [[Prevalence, cumulative incidence, incidence rate - Visual]] — *Three ways to count disease in the same people · PHC6756 lesson 2.3. Key stages: Prevalenc...*
- [[A positive screen is not a diagnosis - Visual]] — *Sensitivity, specificity, PPV and NPV, and why prevalence moves only the last two. Key sta...*
- [[Measures of association from a 2×2 table - Visual]] — *Campsite outbreak, lesson 2.3. Watch each measure come out of four counts.. Key stages: Co...*
- [[The bell curve, piece by piece - Visual]] — *What each part of the normal-density equation does, and what breaks without it.. Key stage...*
- [[Counting sickness in one town - Visual]] — *Public-health measures, each computed from simulated data. Key stages: Every measure start...*
- [[AND multiplies, OR adds - Visual]] — *4 pink + 6 blue balls. Draw 2. Every pair is drawn as its own chip.. Key stages: One outco...*
- [[Counting and chance - Visual]] — *Permutations, combinations, and probability, from zero. Key stages: Choices multiply, Repe...*
- [[Maximum likelihood, from zero - Visual]] — *Start with one coin flip. End with how neural networks learn. Each scene uses only what the...*
- [[Reading the maths in methods sections - Visual]] — *An A–Z course in statistics and deep-learning notation, from the first subscript to KL div...*
- [[Statistical Notation - Visual]] — *Testing a metabolic drug in mice: from raw bench data to statistical proof. Key stages: Be...*
- [[What a t-test Sees - Visual]] — *Two groups of cells, one treated. Is the treated group really higher, or is it noise?. Key...*
- [[Testing 20,000 Genes at Once - Visual]] — *FDR, Bonferroni and Benjamini–Hochberg. Key stages: The BH line on sorted p-values....*
- [[Why Counts Get Logged - Visual]] — *Why counts get logged...*
## 🌐 General & Web Visuals

- [[One equation, three jobs - Visual]] — *β₀ + β₁x as matrices: regression, differential expression, batch removal. Key stages: A li...*
## Ingestion Flow
To add an HTML file, run:
```bash
python scripts/ingest.py path/to/file.html
```
or tell any agent: *"Ingest this HTML file / page."*

## Cross-Topic Bridges
- [[Home]]
- [[Biology MOC]]
- [[Digital Pathology MOC]]
- [[Cancer Biology MOC]]
- [[ML MOC]]
- [[DL MOC]]
- [[Stats MOC]]
