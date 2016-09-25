
# Eukaryotic Annotation Submission Guide

Submitting eukaryotic genomes to GenBank includes registering the metadata and submitting the appropriate data files. The steps include:

*   Registering the research project
*   Registering the sample sources
*   Preparing data files
*   Submitting the data

# Data submission table

Submission scenarios and data files (required or optional) are summarized in the table  
below, followed by additional explanations.

<table border="1" cellpadding="1" cellspacing="1" height="319" width="596">

<tbody>

<tr>

<th rowspan="2">Submission Scenario</th>

<th rowspan="2">BioProject & BioSample</th>

<th colspan="3">SRA</th>

<th>TSA</th>

<th colspan="3">WGS/Genome</th>

</tr>

<tr>

<th>Reads</th>

<th>BAM</th>

<th>.vcf</th>

<th>.sqn</th>

<th>FASTA</th>

<th>.sqn</th>

<th>AGP</th>

</tr>

<tr>

<td>No Assembly</td>

<td>X</td>

<td>X</td>

<td>R</td>

<td>R</td>

</tr>

<tr>

<td>Transcriptome</td>

<td>X</td>

<td>O<sup>2</sup></td>

<td>X</td>

<td>R</td>

<td>O<sup>2</sup></td>

</tr>

<tr>

<td>

Multiple related genomes (eg multiple strains)

</td>

<td>X</td>

<td>X</td>

<td>R</td>

</tr>

<tr>

<th>Genome Assembly</th>

</tr>

<tr>

<td>Traditional contigs</td>

<td>X</td>

<td>R</td>

<td>X</td>

<td>O</td>

</tr>

<tr>

<td>Traditional contigs + annotation</td>

<td>X</td>

<td>R</td>

<td>X</td>

<td>X*</td>

<td>X</td>

</tr>

<tr>

<td>Gapped submission</td>

<td>X</td>

<td>R</td>

<td>X</td>

</tr>

<tr>

<td>

Gapped submission + annotation

</td>

<td>X</td>

<td>R</td>

<td>X</td>

<td>O<sup>1</sup></td>

</tr>

</tbody>

</table>

NOTE:  
X = submit  
R = strongly recommended  
O = optional  
X* = .sqn file of annotated scaffolds  
1 = required only if scaffolds are assembled into chromosomes  
2 = submit either a BAM file, or the reads plus .sqn files of the assembled sequences

# Registering the BioProject

The BioProject records the description of the research effort of the registering researcher or laboratory and ties together the discrete datasets generated from that research effort. A BioProject entry can be used for a single experiment or for multiple experiments, e.g., comparison of multiple strains of the same species or analyzing the genome and transcriptome assemblies  
of the same organism.

There are three ways to register a BioProject:

*   individually at [https://submit.ncbi.nlm.nih.gov/subs/bioproject/](https://submit.ncbi.nlm.nih.gov/subs/bioproject/)
*   during a BioSample registration (see section below) at [https://submit.ncbi.nlm.nih.gov/subs/biosample/](https://submit.ncbi.nlm.nih.gov/subs/biosample/), or
*   during a WGS genome submission at [https://submit.ncbi.nlm.nih.gov/subs/wgs/](https://submit.ncbi.nlm.nih.gov/subs/wgs/)

The BioProject identifier, PRJNA######, is included with each set of data that is submitted, e.g. raw reads, BAM file, vcf file, TSA assembly, and genome assembly.

# Registering details of the source of nucleotide in BioSample

This registration provides the metadata about the source of the RNA or DNA, e.g., the location where the animal lived  
when the sample was collected, the sex of the animal, and the breed of the animal or the cultivar of the plant.  
Basic guidelines for BioSample registration are:

*   Register a separate BioSample for each unique source, e.g., RNA from wings is a separate BioSample than RNA from legs if those two sources were sequenced independently
*   A genome assembly can have only one BioSample. For a genome assembled from reads of multiple BioSamples, register a new BioSample and indicate which other BioSamples were used to generate the assembly. For example, if the reads from a male and from a female were submitted to SRA separately but the reads were combined to assemble the genome, register a new BioSample for the male plus the female, providing the identifiers of the male and the female reads in the new BioSample registration.
*   Endosymbionts: Because sequences are annotated by genome, register a separate BioProject/BioSample pair for an insect and its endosymbiont. In this case, we recommend indicating that the endosymbiont’s BioSample is separate and references the insect BioSample.

*   Different aliquots of the same sample can be registered either as a single BioSample or as multiple BioSamples, depending upon the research focus.

BioSample can be registered either

*   individually or using a batch template through the BioSample portal [https://submit.ncbi.nlm.nih.gov/subs/biosample/](https://submit.ncbi.nlm.nih.gov/subs/biosample/)
*   individually during a WGS genome submission [https://submit.ncbi.nlm.nih.gov/subs/wgs/](https://submit.ncbi.nlm.nih.gov/subs/wgs/)

The BioSample identifier, SAMN######, must be included with each set of data that is submitted, e.g., reads, BAM file, vcf file, TSA assembly, and genome assembly

# Submission scenarios for different data types

## No assembly

DNA or RNA-seq reads (NOT the processed FASTA) should be submitted to Sequence Read Archive (SRA). If possible,  
BAM is preferred over FASTQ, and vcf files are strongly recommended. For details, see:  
[http://www.ncbi.nlm.nih.gov/books/NBK47529/](http://www.ncbi.nlm.nih.gov/books/NBK47529/) and [http://www.ncbi.nlm.nih.gov/books/NBK47537/#File_Format_Guide_B.BAM_Binary_Sequence](http://www.ncbi.nlm.nih.gov/books/NBK47537/#File_Format_Guide_B.BAM_Binary_Sequence)

## Quantitative gene expression and epigenomic data

Submit project and sample metadata, raw data files and processed data files to GEO, according to the instructions at [http://www.ncbi.nlm.nih.gov/geo/info/seq.html](http://www.ncbi.nlm.nih.gov/geo/info/seq.html).  Note that the BioProject and BioSample will be created by GEO during processing of the submission.

## Transcriptome options

*   BAM file should be submitted to SRA.
*   Assembled sequences should be in Sequin format (.sqn) with reference to SRA runs (SRR# that had been submitted to SRA) and submitted to TSA. More information is available at: [http://www.ncbi.nlm.nih.gov/genbank/tsaguide](/~/tsaguide).

Details on BAM format is at: [http://www.ncbi.nlm.nih.gov/books/NBK47537/#File_Format_Guide_B.BAM_Binary_Sequence](http://www.ncbi.nlm.nih.gov/books/NBK47537/#File_Format_Guide_B.BAM_Binary_Sequence)  
Common errors to avoid in TSA submission:

*   Sequences are less than 200 bp in length
*   Sequences with vector screening hits for Next-Gen sequencing primers, i.e. not properly trimmed
*   Sequences with more than 10% N's or 14 consecutive N’s not in assembly_gap features format
*   Files that are incorrectly formatted or have biologically invalid annotation

## Multiple related genomes, reference-guided assemblies of multiple strains

BAM file plus optional vcf file of SNPs should be submitted to SRA. For more information on .vcf format, see:  
[http://www.ncbi.nlm.nih.gov/SNP/docs/dbSNP_VCF_Submission.pdf](http://www.ncbi.nlm.nih.gov/SNP/docs/dbSNP_VCF_Submission.pdf ) and [http://www.1000genomes.org/node/101](http://www.1000genomes.org/node/101)

## Genome assembly options

There are two basic types of assemblies, and either can be submitted with or without annotation:

*   Traditional, submitted as contigs plus an optional AGP file to assemble scaffolds or chromosomes
*   Gapped, submitted as scaffolds with Ns that represent gaps converted to assembly_gap features

As described in the instructions, [http://www.ncbi.nlm.nih.gov/genbank/wgs.submit](/~/wgs.submit), genome assemblies and their genome assembly metadata are submitted via the WGS submission portal ([https://submit.ncbi.nlm.nih.gov/subs/wgs/](https://submit.ncbi.nlm.nih.gov/subs/wgs/)). The metadata includes the assembly method, date or version of the program, the approximate genome coverage, and the relevant sequencing technology used. For genomes with complex annotation, it is useful to submit the fasta sequences first and request that they be run through the foreign contamination screen, to ensure that any contamination is removed before the submission files are created and annotated.

### Traditional submission without annotation:

Submit FASTA files of the contigs, with:

*   10,000 sequences per file maximum
*   contigs lengths are >200bp each
*   no foreign sequence contamination (the results of this screen will be reported back, and you can resubmit corrected files)
*   no Ns at the ends of sequences
*   concise identifiers, e.g. contig00001, contig00002 (avoid overtly long identifiers containing information on coverage or length, and any punctuation except underscores)
*   for sequences representing a chromosome or belonging to a plasmid or to an organelle (ie, location), include that information in the fasta defline, using brackets such as: [chromosome=I] or [plasmid-name=unnamed1] or [location=mitochondrion].

More details are available at: http://www.ncbi.nlm.nih.gov/genbank/wgs.submit

### Gapped submission without annotation:

Create .sqn files and convert runs of Ns that represent gaps in the fasta files to assembly_gap features with the correct linkage evidence. Needed tools and files are:

*   The command line program tbl2asn, v23.0 or higher, available from [ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/converters/by_program/tbl2asn/](ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/converters/by_program/tbl2asn/)
*   FASTA files (specifications are the same as traditional without annotation)
*   Template file with submitter information, made at [http://www.ncbi.nlm.nih.gov/WebSub/template.cgi](http://www.ncbi.nlm.nih.gov/WebSub/template.cgi)
*   Optional Genome-Assembly-Data structured comment, which can also be provided in the WGS submission form [https://submit.ncbi.nlm.nih.gov/structcomment/genomes/](https://submit.ncbi.nlm.nih.gov/structcomment/genomes/)

The Ns that represent gaps can be easily converted to assembly_gap features if all of the following criteria are met:

*   Each sequence represents a sequence that occurs biologically in the organism, such as a chromosome; the contigs were not simply concatenated
*   No artificial sequences, such as linkers with multiple stop codons, are present
*   The linkage evidence for each gap is the same
*   Knowing whether runs of 100 Ns represent gaps of unknown size
*   No other Ns represent gaps of unknown size
*   all runs of "ambiguous base Ns" must be shorter than any run of Ns that represents a gap
*   all the gaps must be ‘within scaffolds’, not ‘between scaffolds’

The "Gapped Format for Genome Submission” ([http://www.ncbi.nlm.nih.gov/genbank/wgs_gapped](/~/wgs_gapped)) provides the tbl2asn command line for several different simple cases. For example, if runs of 10 or more N's are estimated  
gaps, and shorter runs of N's are just ambiguous bases, and all runs of exactly 100 N's are unknown gaps, and the linkage  
evidence is paired-ends, then run:

tbl2asn -p path_to_fsa_files -t template -M n -Z discrep -a r10u -l paired-ends

Additional options for the gap-type and linkage evidence are also listed at [http://www.ncbi.nlm.nih.gov/genbank/wgs_gapped](http://www.ncbi.nlm.nih.gov/genbank/wgs_gapped).

### Gapped submission with annotation (including complex gap cases):

This is like the previous situation, except that the annotation is provided in .tbl files. Instructions and tbl specifications  
are available at [http://www.ncbi.nlm.nih.gov/genbank/eukaryotic_genome_submission_annotation](http://www.ncbi.nlm.nih.gov/genbank/eukaryotic_genome_submission_annotation ) and [http://www.ncbi.nlm.nih.gov/genbank/eukaryotic_genome_submission](http://www.ncbi.nlm.nih.gov/genbank/eukaryotic_genome_submission)

Brief requirements for common features are:

*   each rRNA, tRNA, ncRNA needs a gene;
*   each functional CDS needs an mRNA and a gene;
*   each functional CDS/mRNA pair must share a unique protein_id and transcript_id;
*   each gene must have a locus_tag that has the registered locus_tag prefix; and
*   each locus_tag must be unique across the genome.

It is recommended that the protein_id and transcript_id be based on the gene’s locus_tag.

Alternatively spliced genes are an exception to the above rule: a single gene feature extends from the 5’-most to 3’-most feature. An mRNA and CDS feature are required for each alternatively spliced product even if multiple CDS have the same translation, and each mRNA/CDS pair has unique transcript_id/protein_id pair. See an example at [http://www.ncbi.nlm.nih.gov/genbank/eukaryotic_genome_submission_annotation#Alternativelysplicedgenes](/~/eukaryotic_genome_submission_annotation#Alternativelysplicedgenes).

CDS product names must conform to SwissProt guidelines, as per [http://www.uniprot.org/docs/gennameprot](http://www.uniprot.org/docs/gennameprot ) and [http://www.ncbi.nlm.nih.gov/genbank/eukaryotic_genome_submission_annotation#CDS](http://www.ncbi.nlm.nih.gov/genbank/eukaryotic_genome_submission_annotation#CDS). See the “Annotation FYI” section of the [http://www.ncbi.nlm.nih.gov/genbank/wgs_gapped](http://www.ncbi.nlm.nih.gov/genbank/wgs_gapped ) page for the prohibitions about features crossing gaps.

When the sequences are gapped (i.e., are scaffolds) and the simple cases for using tbl2asn to convert the Ns to assembly_  
gap features do not apply (eg, there are different kinds of linkage evidence), then the assembly_gap features need to be included in the annotation .tbl file. They are set up like this, with the appropriate gap-type and linkage evidence:

<pre>100	201	assembly_gap
			gap_type	within scaffold
			linkage_evidence	align-genus
</pre>

Note that the gap-type “between scaffolds” is allowed only when the sequences are chromosomes. They are not allowed in  
scaffold sequences. The gapped sequnces also must meet these criteria:

*   Each sequence represents a sequence that occurs biologically in the organism, such as a chromosome; the contigs were not simply concatenated
*   No artificial sequences, such as linkers with multiple stop codons, are present

Run tbl2asn:

tbl2asn -p path_to_fsa_files -t template -M n -Z discrep

Before submission, fix any Errors or FATALs in the .val or discrep files that are produced by referencing instructions given  
in this document: [http://www.ncbi.nlm.nih.gov/genbank/wgs.submit#Fix](/~/wgs.submit#Fix)

### Traditional submission with annotation:

The annotation must be at the scaffold level, so submit:

*   fasta files of the contigs
*   an AGP file to assemble the contigs into scaffolds, and
*   .sqn files of the annotated scaffolds.

The annotated scaffolds are created like the Gapped examples described early in this document, either the simple cases  
of using tbl2asn command lines or the complex cases that require including the assembly_gap features in the .tbl files.  
As described by WGS submission document ([http://www.ncbi.nlm.nih.gov/genbank/wgs.submit#agp](/~/wgs.submit#agp)), the AGP file  
should be made according to the AGP2.0 specifications: [http://www.ncbi.nlm.nih.gov/projects/genome/assembly/agp/AGP_Specification.shtml](http://www.ncbi.nlm.nih.gov/projects/genome/assembly/agp/AGP_Specification.shtml)

NOTE: The contig identifiers must match the component IDs in column 6 of the AGP files, and the scaffold/chromosome identifiers  
must match the object IDs in column 1 of the AGP files. The format of AGP files can be validated on this NCBI web  
page: [http://www.ncbi.nlm.nih.gov/projects/genome/assembly/agp/agp_validate.cgi](http://www.ncbi.nlm.nih.gov/projects/genome/assembly/agp/agp_validate.cgi)

For more extensive validation of AGP files locally, a standalone command line program agp_validate is available by  
anonymous FTP, as explained here: [http://www.ncbi.nlm.nih.gov/projects/genome/assembly/agp/AGP_Validation.shtml](http://www.ncbi.nlm.nih.gov/projects/genome/assembly/agp/AGP_Validation.shtml)  
Run the program with the -help to obtain details of the available arguments and their appropriate input format.

## Technical assistance

Technical assistance is available through the following email aliases:

[sra@ncbi.nlm.nih.gov](mailto:sra@ncbi.nlm.nih.gov ) for questions on submission to SRA, including vcf and BAM files  
[biosamplehelp@ncbi.nlm.nih.gov](mailto:biosamplehelp@ncbi.nlm.nih.gov ) for BioSample questions  
[genomeprj@ncbi.nlm.nih.gov](mailto:genomeprj@ncbi.nlm.nih.gov ) for BioProject questions  
[genomes@ncbi.nlm.nih.gov](mailto:genomes@ncbi.nlm.nih.gov ) for questions about transcriptome and genome assemblies  
[info@ncbi.nlm.nih.gov](mailto:info@ncbi.nlm.nih.gov ) for other general questions related to submission



