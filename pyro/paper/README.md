# Images and data for publication

This directory contains figures and tables output by the [PyR<sub>0</sub>
model](https://www.medrxiv.org/content/10.1101/2021.09.07.21263228v1). These
outputs are aggregated to weeks, PANGO lineages, and amino acid changes.

Figures and tables are generated by first running preprocessing and inference,
then postprocessing with the following Jupyter notebooks:
[ `mutrans.ipynb` ](../mutrans.ipynb),
[ `mutrans_gene.ipynb` ](../mutrans_gene.ipynb),
[ `mutrans_prediction.ipynb` ](../mutrans_prediction.ipynb),
[ `mutrans_backtesting.ipynb` ](../mutrans_backtesting.ipynb).

## Data tables

- [Mutation table](mutations.tsv) is ranked by statistical significance.
  The "mean" field denotes the estimated effect on log growth rate of each mutation.
- [Lineage table](strains.tsv) is ranked by growth rate.

## Manhattan plots

![Manhattan plot of entire genome](manhattan.png)
![Manhattan plot of N gene](manhattan_N.png)
![Manhattan plot of S gene](manhattan_S.png)
![Manhattan plot of ORF1a gene](manhattan_ORF1a.png)
![Manhattan plot of ORF1b gene](manhattan_ORF1b.png)
![Manhattan plot of ORF3a gene](manhattan_ORF3a.png)

## Information density plots

![How informative is each gene?](vary_gene_likelihood.png)
![How informative is each NSP?](vary_nsp_likelihood.png)

## Volcano plot

![Volcano plot of mutations](volcano.png)

## Strain characterization plots

![Growth rate versus emergence date](strain_emergence.png)
![Growth rate versus case count](strain_prevalence.png)
![PANGO lineage heterogeneity](lineage_heterogeneity.png)
![Forecast](forecast.png)
![Deep scanning](deep_scanning.png)

## Cross validation plots

The following plots assess robustness via 2-fold crossvalidation, splitting data into Europe versus (World w/o Europe).

![Lineage correlation](lineage_agreement.png)
![Mutation correlation](mutation_agreement.png)
![Lineage box plots](strain_europe_boxplot.png)
![Mutation box plots](mutation_europe_boxplot_rankby_s.png)
![Mutation box plots](mutation_europe_boxplot_rankby_t.png)
![Lineage prediction](lineage_prediction.png)

## Data plots

![Distribution of samples among regions](region_distribution.png)
![Distribution of samples among clades](clade_distribution.png)

## Acknowledgements

The aggregated model outputs in this directory were generated from data inputs
including either GISAID records (https://gisaid.org), an UShER tree placement
of those records
(http://hgdownload.soe.ucsc.edu/goldenPath/wuhCor1/UShER_SARS-CoV-2), PANGO
lineage classifications (https://cov-lineages.org), and case count time series
from Johns-Hopkins University (https://github.com/CSSEGISandData/COVID-19).
Results in this directory can alternatively be generated using GENBANK records
(https://www.ncbi.nlm.nih.gov) instead of GISAID records.

We gratefully acknowledge all data contributors, i.e. the Authors and their Originating laboratories responsible for obtaining the specimens, and their Submitting laboratories for generating the genetic sequence and metadata and sharing via the GISAID initiative [1,2] on which this research is based. A total of 6,466,299 submissions are included in this study. A complete list of the 6,466,299 accession numbers is available in [accession_ids.txt.xz](accession_ids.txt.xz).

1.  GISAID Initiative and global contributors,
    EpiCoV(TM) human coronavirus 2019 database.
    GISAID (2020), (available at https://gisaid.org).
2.  S. Elbe, G. Buckland-Merrett,
    Data, disease and diplomacy: GISAID's innovative contribution to global health.
    Glob Chall. 1, 33-46 (2017).
3.  National Center for Biotechnology Information (NCBI)[Internet].
    Bethesda (MD): National Library of Medicine (US),
    National Center for Biotechnology Information;
    [1988] – [cited 2017 Apr 06].
    Available from: https://www.ncbi.nlm.nih.gov