
# Metagenome Submission Guide

### Introduction

Microorganisms comprise the majority of the planet's biological diversity. However, due to the varied environments and conditions in which these organisms reside, many of these cannot be cultured by standard techniques. Culture-independent methods are essential for understanding the genetic diversity, population structure, and ecological roles of these uncultured microorganisms.

Metagenomics is the culture-independent genomic analysis of a community of microorganisms. It provides a community-wide assessment of metabolic function and bypasses the need for the isolation and laboratory cultivation of individual species. The analysis of metagenomic data provides a way to identify new organisms and isolate complete genomes from unculturable species that are present within an environmental sample.

Metagenome projects may include raw sequence reads collected from an ecological or organismal source (submitted to the Trace Archive or Sequence Read Archive), assembled contigs and/or scaffolds derived from the raw sequence data, including partial genomes from taxonomically defined organisms (submitted as a WGS project), and in some cases, supporting sequences such as 16S ribosomal RNAs or fosmids (submitted to regular GenBank).

This guide explains how to submit a metagenome project to NCBI, including information for submitting sequences to the Trace Archive, Sequence Read Archive and GenBank, and registering BioProjects and BioSamples.

If you do not understand any of the instructions presented here or you have questions, please contact us by email at [genomes@ncbi.nlm.nih.gov](mailto:genomes@ncbi.nlm.nih.gov) prior to creating your submission.

### Table of Contents

1.  [BioProject and BioSample Registration](#registering)
2.  [Submitting sequences to the Trace Archive or Sequence Read Archive (SRA)](#Submitting_Trace_Archive)
3.  [Submitting assembled metagenomic contigs to WGS](#Submitting_WGS_project)
4.  [Other types of metagenome sequence data (eg, fosmids, 16S rRNA)](#Submitting)
5.  [What happens next](#What_happens_next)

### BioProject and BioSample Registration

Metagenome [BioProjects](/books/NBK169438/) function to link together biological data related to a single initiative, including all of the sequences and descriptive environmental metadata.  [BioSamples](/books/NBK169436/) contain the attributes that detail the biological source materials that were isolated as part of the environmental project.  A single BioProject can link to multiple BioSamples, which can also be included in separate Bioproject initiatives.  BioProject and BioSample IDs are included within sequence data submitted to NCBI and subsequently generate Entrez links.

BioProject and BioSample IDs can be automatically registered and assigned during the submission of sequence data to SRA or WGS within the [NCBI Submission Portal](//submit.ncbi.nlm.nih.gov).  In addition, individual BioProjects and BioSamples can be created for submissions of metagenomic/environmental 16S ribosomal RNA or targeted genes/genomic regions that are submitted to GenBank.  BioProjects can also be set up for large scale initiatives that include links from sequence data to multiple projects. In general, use the same BioProject and BioSample for all the data from that sample, eg the raw reads that are submitted to SRA and the assembled metagenomic sequences that are submitted to WGS.

Creating individual BioProject and BioSamples prior to sequence submission

*   [Register your BioProject](//submit.ncbi.nlm.nih.gov/subs/bioproject/) as an Environmental BioProject prior to preparing your sequence submission to GenBank.  If the project only involves the sequencing of a single gene (eg., 16S ribosomal RNA), it should be described as a Targeted Locus/Loci BioProject.  Please include information about the project, including a detailed description of the isolation source, and the scope of the project.  The assigned BioProject ID should be included in any correspondence regarding the metagenome project as well as within any relevant sequence submissions.  Questions regarding the submission and organization of BioProjects should be sent to genomeprj@ncbi.nlm.nih.gov.
*   BioSamples include descriptive information about the physical specimen from which the sequence data were derived.  Please provide as much metadata and information as possible about the samples in order to provide context for the experimental data.  [BioSample registration](//submit.ncbi.nlm.nih.gov/subs/biosample/) can be completed using web forms or in batch using spreadsheet templates.  The [BioSample packages and attributes](//submit.ncbi.nlm.nih.gov/biosample/template/) along with the submission templates can be reviewed and downloaded prior to submission.  Use either the 'Metagenome or environmental sample' or 'Genome, metagenome or marker sequences (MIxS compliant) - MIMS' BioSample package. Register the metagenomic BioSample using the organism name "xxxx metagenome" (e.g., soil metagenome), and choose the most appropriate name from this list of [metagenome organism names](http://ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Undef&id=408169&lvl=3&p=mapview&p=has_linkout&p=blast_url&p=genome_blast&keep=1&srchmode=3&unlock/) in the taxonomy database. Please use the assigned BioSample ID(s) in any correspondence regarding the metagenome project as well as within any sequence submissions derived from the sample.  Questions regarding the submission of BioSamples should be sent to [biosamplehelp@ncbi.nlm.nih.gov](mailto:biosamplehelp@ncbi.nlm.nih.gov).

### Submitting sequences to the Trace Archive or Sequence Read Archive (SRA)

Unassembled sequence data should be submitted to the [Trace Archive](//Traces/trace.cgi?cmd=show&f=submit&m=doc&s=submit) or [NCBI Sequence Read Archive](//submit.ncbi.nlm.nih.gov/subs/sra/) (SRA).

Traditional gel-capillary reads (including DNA sequence chromatograms, base calls, and quality estimates obtained from sequencing instruments like ABI 3730) should be submitted to the Trace Archive. Sequence reads obtained using next-generation sequencers (eg, 454, Illumina, ABI solid, Helicos) should be deposited in the Sequence Read Archive.  When you submit your data, you will be assigned a BioProject and BioSample ID.  If you have already registered a BioProject and/or BioSample, include these IDs with your SRA submission.

Contact [sra@ncbi.nlm.nih.gov](mailto:trace@ncbi.nlm.nih.gov) for questions about submitting to the Trace Archive and NCBI Sequence Read Archive.

### Submitting assembled metagenomic contigs to WGS

Contigs that have been assembled from raw reads can be submitted as a [WGS project](/~/wgs).  WGS accepts both draft assemblies that have been identified as a particular organism and assembled sequences from a metagenomic source that have not been assigned organism names.  Sequences shorter than 200bp should not be included unless they are part of multi-component scaffolds.

Please see the [WGS](/~/wgs/) pages for instructions about how to generate a WGS submission.  In addition, review either the [prokaryotic](/~/genomesubmit_annotation) or the [eukaryotic](/~/eukaryotic_genome_submission_annotation/) annotation guidelines, if you decide to include annotation. Note that annotation is not required for genome or metagenome submissions.

[1] Both a BioProject and BioSample ID are required for WGS submissions.  You can either register the BioProject and BioSample separately, or you can create them when you submit your sequence data using the [Genomes (WGS) Submission Portal](//submit.ncbi.nlm.nih.gov/subs/wgs/). However, if you have already registered a BioProject and BioSample for submission of the corresponding raw reads to SRA, then, in general, you would use those when you submit the assembled data to WGS.

If you haven't already created a BioProject, register the metagenomic study ahead of time or create one during the WGS submission.  The BioProject ID will be included with all of the data that is part of the metagenomic study.  Be sure to include a brief description that distinguishes each BioProject from similar studies.

If you haven't already created a BioSample, register the metagenomic BioSample or create one during the WGS submission using the organism name "xxxx metagenome" (e.g., soil metagenome). Choose the most appropriate name from this list of [metagenome organism names](//ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Undef&id=408169&lvl=3&p=mapview&p=has_linkout&p=blast_url&p=genome_blast&keep=1&srchmode=3&unlock/) in the taxonomy database. Use either the 'Metagenome or environmental sample' or 'Genome, metagenome or marker sequences (MIxS compliant) - MIMS' BioSample package.

If you want to indicate the organism identification of particular sequences, then email [genomes@ncbi.nlm.nih.gov](mailto:genomes@ncbi.nlm.nih.gov) so that NCBI staff can help with your submission. Provide the following information:

*   A brief explanation of how you identified the sequences.
*   Describe whether a set of sequences represents a presumed genome assembly.
*   The list of proposed organism names. If you have assemblies that represent a single organism, you will need to provide a unique identifier for each organism (eg., Acidilobus sp. OSP8 or Acidobacteria bacterium A11)
*   Once the organism names have been approved, you will be contacted with instructions as to how to register your BioSamples.

Note that if there are only a few short contigs for each organism, if the organisms were binned based only on BLAST similarity, or if there is no organism information, the assembled contigs should be submitted as a single WGS submission using the metagenomic organism name (eg., marine metagenome).  The organism bin information should be added as source notes.

If your data is complex or if you are uncertain what organism names to use, please send a message to [genomes@ncbi.nlm.nih.gov](mailto:genomes@ncbi.nlm.nih.gov) and we will help you determine the best way to set up the data before you begin registration.

* * *

* * *

While you can create the Biosamples individually in the WGS submission portal, it may be easier to register multiple BioSamples using a tab-delimited table within the batch option in the BioSample registration wizard  The BioProject ID can be included within the batch template.  If you have questions about your BioSample submission, contact biosamplehelp@ncbi.nlm.nih.gov.

If you choose to register the BioProject and BioSamples separately, provide the registered BioProject and BioSample IDs in the WGS submission portal when you create your WGS submission.  Do not create duplicate BioProjects and BioSamples.

* * *

* * *

[2] Upload either the fasta files or the .sqn files to GenBank in the [Genomes (WGS) Submission Portal](//submit.ncbi.nlm.nih.gov/subs/wgs/) described in the [WGS submission](/~/wgs.submit) instructions.

[3] Annotation is not required for a WGS submission.  If you choose to provide your own annotation, you must submit annotated .sqn files as described in the prokaryotic or eukaryotic annotation guidelines.  If you are not providing annotation, please submit fasta files.

[4] Supercontig or assembly information can be submitted in one of two formats:

*   Split format - The pieces of a WGS project are the contigs (overlapping reads with no gaps).  An optional [AGP](/~/wgs.submit#agp) file can be submitted to indicate how the WGS sequences are assembled together into scaffolds or chromosomes.
*   Gapped format - The pieces of a WGS project are the scaffolds that contain runs of Ns that represent gaps.  An AGP file is not required for the gapped format.  You can provide either fasta files and answer the gap questions in the submission portal or you can include assembly_gap features in a .sqn file as described in the [Gapped Genome Submission](/~/wgs_gapped) instructions.  Unordered sequences that are simply concatenated and joined by Ns are not allowed.

### Other types of metagenome sequence data (eg., fosmids, 16S rRNA)

Metagenome projects can include other types of sequence data such as assembled 16S ribosomal RNA, fosmid sequences, and/or transcriptome data. The organism names for these sequences will be "uncultured xxx" (eg., uncultured bacterium) for ribosomal RNA and fosmid sequences whereas the transcriptome may use a "xxx metagenome" name as appropriate.  If BioProjects and BioSamples have been registered for the sequence data, please include the IDs within your submission correspondence.

These types of data should be submitted to GenBank as follows:

*   16S ribosomal RNA
    *   Assembled 16S ribosomal RNA from uncultured or cultured bacteria/archaea can be submitted using the [GenBank component](//submit.ncbi.nlm.nih.gov/subs/genbank/) of the Submission Portal
    *   Assembled 16S ribosomal RNA from eukaryotes should be prepared using the sequence submissions tools [Sequin](//ncbi.nlm.nih.gov/Sequin/index.html) or [tbl2asn](/~/tbl2asn2).  These submissions should be emailed to [gb-sub@ncbi.nlm.nih.gov](mailto:gb-sub@ncbi.nlm.nih.gov) or uploaded via [SequinMacroSend](//ncbi.nlm.nih.gov/LargeDirSubs/dir_submit.cgi).
*   Fosmid end sequences and GSS data can be submitted to the [GSS division](//ncbi.nlm.nih.gov/dbGSS/how_to_submit.html) of GenBank. These sequences must not be annotated. Please contact [batch-sub@ncbi.nlm.nih.gov](mailto:batch-sub@ncbi.nlm.nih.gov) with any questions you have regarding this type of submission.
*   Fosmids, BACs, other genomic fragments assembled from raw reads, and/or annotated sequences should be submitted to [GenBank](/~/submit) using the sequence submission tools Sequin or tbl2asn.  Prepared submissions should be emailed to [gb-sub@ncbi.nlm.nih.gov](mailto:gb-sub@ncbi.nlm.nih.gov) or uploaded via SequinMacroSend. 
*   Metagenomic transcriptomes can be submitted to GenBank as outlined in the [TSA Submission Guide](/~/tsaguide).

Please contact [gb-admin@ncbi.nlm.nih.gov](mailto:gb-admin@ncbi.nlm.nih.gov) with any questions you have regarding these types of submissions as well as for instructions regarding their format.

### What happens next

Once we receive your metagenome submission(s), a member of our staff will conduct an initial review and will contact you by email if there are any questions.  Once the data passes the initial review, we will assign Accession Numbers to the sequence records associated with your metagenome project.  The submission will then be placed in the processing queue where it will be manually reviewed by our indexing staff.  We will contact you if we find any additional problems or errors as we prepare your data to be released to the public database.  . Once we have assigned Accession Numbers to the sequence records associated with your metagenome project and contacted you with any issues, we will prepare it for release to the public database.

You can choose to have your metagenome project and sequence submission(s) released immediately or to be kept confidential until a certain date or publication of the work, whichever is first. If you wish your metagenome project to be held until publication, we ask that you provide us with the expected publication date and also notify us in a timely manner of the upcoming publication and the relevant citation details. This will allow us to coordinate the release of your metagenome project and sequence submission(s) with the appearance of the paper. Please provide at least two weeks notice of any upcoming publication.





<div id="shared-content-1" nid="1402">

<div class="rightnav">

## Metagenome Resources

*   [BioProject](http://www.ncbi.nlm.nih.gov/bioproject)
*   [BioSample](http://www.ncbi.nlm.nih.gov/biosample)
*   [Sequence Read Archive](http://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi)
*   [Genomes](/~/genomesubmit)
*   [WGS](/~/wgs)
*   [Metagenome Submission Guide](/~/metagenome)
*   [Structured Comment Guide](/~/structuredcomment)
*   [Genomic Standards Consortium](http://gensc.org/)



