Dataset accompanying the research article "Barcoded Bulk QTL mapping reveals highly
polygenic and epistatic architecture of complex traits in yeast" by Alex N. Nguyen Ba,
Katherine R. Lawrence, Artur Rego-Costa, Shreyas Gopalakrishnan, Daniel Temko,
Franziska Michor, and Michael M. Desai (2021).

> Correponding author
Michael M. Desai
Department of Organismic and Evolutionary Biology
Harvard University
mdesai@oeb.harvard.edu

> General information
The dataset contains genotype and phenotype information for a panel of approximately 
100,000 F1 offspring from a cross between strains BY and RM of Saccharomyces cerevisiae.
The genotype is encoded at the approximately 42,000 single-nucleotide polymorphisms
between the two parental strains as an inferred posterior probability of that strain
having the RM allele at that locus. Phenotypic values comprise inferred relative fitness
in liquid fed-batch culture condition under eighteen different growth media. This dataset
was created from raw sequencing data stored in the NCBI SRA repository. See manuscript
for more information on data generation, processing, and access.

> Dataset description
|- SNP_list.txt
|	Table with index, genome position, and sequence information of the approximatelly 42,000
|	single-nucleotide polymorphisms between the two parental strains. The genome reference sequence
|	on which this dataset is based is S288C_reference_genome_R64-3-1_20210421 by the Saccharomyces
|	Genome Database Project. The RM alleles were inferred from sequencing of the parental RM strain.
|- segregant_info.txt
|	Unique indeces, library location (Batch, Set, Plate, Well) and barcode sequence of each of the
|	approximatelly 100,000 F1 strains in our panel.
|- geno_data_*.txt.gz
|	Inferred posterior probability of each strain in our panel having the RM allele at each of the
|	approximatelly 42,000 single-nucleotide polymorphisms considered. Each row contains the genotype
|	of one strain. The first column contains the identifying number of that strain, as in the 'Number'
|	column of segregant_info.txt. Each file contains the genotype of 20,000 strains.
|- pheno_data_*.txt.gz
|	Each file contain the inferred fitness with its associated standard error for each strain in our panel
|	in a given environment, identified in the file name. Missing data from strains for which we could
|	not infer fitness is coded as 'nan'.

> Acknowledgments
We thank the Bauer Core facility at Harvard and the Broad Institute Genomic Services
sequencing core for assistance with sequencing. We thank Alan Moses, Andrew Murray, Hunter Fraser,
Dan Rice, and members of the Desai lab for comments on the manuscript. A.N.N.B. acknowledges
support from the National Science and Engineering Research Council of Canada (NSERC).
K.R.L. acknowledges support from the Fannie & John Hertz Foundation Graduate Fellowship Award,
the National Science Foundation (NSF) Graduate Research Fellowship Program, and fellowship
award #1764269 from the NSF-Simons Center for Mathematical and Statistical Analysis of Biology
at Harvard. M.M.D. acknowledges support from grant PHY-1914916 from the NSF and grant GM104239
from the National Institutes of Health (NIH). The computations in this paper were run on the
Faculty of Arts and Sciences Research Computing (FASRC) Cannon cluster supported by the FAS
Division of Science Research Computing Group at Harvard University.
