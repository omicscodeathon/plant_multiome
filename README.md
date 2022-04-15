# Mining Omics features in Plants and Animals
## Introduction
Eukaryotic cells are known to have several genomes, including nuclear genomes and organelle genomes, the latter of which are thought to be derived from prokaryotic origin via endosymbiosis, making them behave more like prokaryotic cells than eukaryotes(1). Genome communication via conjugation, transformation, and transduction is one of the recognized prokaryotic behaviors, so symbiosis is recognized to have played a significant role in eukaryote evolution, favoring host adaptation in changing environmental conditions..(2) In this study, we hope to uncover the communication between various eukaryotic genomes and discover how it manifests itself in diverse living groups. We want to achieve our goal by mining diverse data from the NCBI genome database using several genome parameters (Size, Number of genes, GC count) and examining the frequency of horizontal gene transfer (HGT) for each species.
## Datasets
We scrap the NCBI Genomes database and collect all genomes and organelles genomes that belong to plants and animals and fit the following criteria:
* Genomes are in completed, chromosomes, or scaffolds level
* Genomes are annotated
* Organelles are published
Then bind them to their organelle genomes using Bioproject as a binding parameter, by the end, only datasets that gather the chromosome and extra chromosomes will be selected.
## Analysis pipeline
![Présentation sans titre](https://user-images.githubusercontent.com/85350037/163555673-e5751795-36d7-4ee6-8e94-4420d1f16812.jpg)
## How to use
## Citation
(1) Zimorski, V., Ku, C., Martin, W. F., & Gould, S. B. (2014). Endosymbiotic theory for organelle origins. Current Opinion in Microbiology, 22, 38–48. doi:10.1016/j.mib.2014.09.008

(2) Garuglieri E, Booth JM, Fusi M, Yang X, Marasco R, Mbobo T, Clementi E, Sacchi L, Daffonchio D. Morphological characteristics and abundance of prokaryotes associated with gills in mangrove brachyuran crabs living along a tidal gradient. PLoS One. 2022 Apr 14;17(4):e0266977. doi: 10.1371/journal.pone.0266977. PMID: 35421185.
## Team
* Abdellah IDRISSI AZAMI: PhD Student in Plant Genomics | University Mohammed VI for health Sciences Morocco | Project Leader
* Mustapha LEMSYAH: Engineer in Softwares and BI | University of Lyon France | Tech co-Lead
* Zainab EL OUAFI: PhD Student in Molecular Modeling | University Mohammed VI for health Sciences Morocco | Writer
* Douae EL GHOUBALI: PhD Student in Insect Genomics | University Mohammed VI for health Sciences Morocco | Writer
