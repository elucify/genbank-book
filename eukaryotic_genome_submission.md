<meta http-equiv="Content-Type" content="text/html; charset=utf-8">  <meta name="node-id" content="1441"> <meta name="revision-id" content="23845"> <meta name="cms-base-url" content="http://cms.ncbi.nlm.nih.gov"> <meta name="cms-view-url" content="http://cms.ncbi.nlm.nih.gov/genbank/eukaryotic_genome_submission"> <meta name="cms-edit-url" content="http://cms.ncbi.nlm.nih.gov/node/1441/edit"> <meta name="created" content="2011-11-10T10:35:44-05:00"> <meta name="modified" content="2014-10-03T08:37:26-04:00"> <meta name="publication-date" content="2011-11-10T10:35:44-05:00"> <meta name="author" content="yankie"> <meta name="subsite" content="genbank"> <meta name="path" content="genbank/eukaryotic_genome_submission"> <meta name="node-type" content="page"> <meta name="jira-ticket" content=""> <meta name="cms-tags" content="">  <meta name="" content=""> <title>Eukaryotic Annotation Guide</title>

<div class="node clear-block">

<div class="content">

# Eukaryotic Genome Submission Guide

### Introduction

This guide explains how to submit or update a eukaryotic genome for GenBank, using the NCBI tools Sequin or tbl2asn. Sequin is a stand-alone program and tbl2asn is a command-line program. Either can be used for creating new or updated GenBank submissions, though tbl2asn is recommended for incomplete genomes with multiple sequences.

Both programs combine a simple five-column tab-delimited table of feature locations and qualifiers with the DNA sequence (in FASTA format) and the submitter information to generate a file for submission to GenBank.

The format of this feature table allows different kinds of features (e.g., gene, mRNA, coding region, tRNA, repeat_region) and qualifiers (e.g., /product, /note) to be indicated. The validator will check for errors such as internal stops in coding regions.

Guidelines for [prokaryotic genome submissions](/~/genomesubmit) .

If you have questions about creating your submission, please contact us by email at [genomes@ncbi.nlm.nih.gov](mailto:genomes@ncbi.nlm.nih.gov) prior to creating your submission, to save time for everyone.

### Table of Contents

1.  [Register your Project](#registering)
2.  [Prepare FASTA-formatted sequence](#FASTA)
3.  [Annotation](#prepare_table)
    *   [Gene features](#Gene_features)
    *   [locus_tag](#locus_tag)
    *   [CDS (coding region) features](#CDS)
    *   [protein_id](#protein_id)
    *   [mRNA features](#mRNA)
    *   [transcript_id](#transcript_id)
4.  [Creating the submission file](#Create_your_submission)
5.  [Submitting](#Submitting)
6.  [What happens next](#What_happens_next)
7.  [Updating existing genome submissions](#updating)
8.  [Examples](/~/eukaryotic_genome_submission_Examples)

### Register your Project

Please register your genome project and locus_tag prefix on the [BioProject registration](https://submit.ncbi.nlm.nih.gov/subs/bioproject/) page prior to preparing your submission to GenBank, you are including annotation in the submission. Each project that is registered here is assigned a project_id, and in the future we intend that the project_id will appear on all entries associated with a particular genome project.

### FASTA-formatted sequence

Nucleotide sequences must be in FASTA format. FASTA format consists of a single definition line, beginning with a '>' and followed by optional text, and subsequent lines of sequence. At minimum, all definition lines must contain an identifier for the sequence, called the SeqID. Other information about the biological source of the organism can also be encoded on the definition line of the sequence and is used to build the record.

A sample definition line is

<pre>>HTE831 [organism=Drosophila yakuba] [strain=HTE831] 
</pre>

Common source [modifiers](http://www.ncbi.nlm.nih.gov/Sequin/modifiers.html) may be incorporated into the definition line e.g. [strain=HTE831]. Alternatively, these modifiers can be included in the tbl2asn command line with -j.

An example of a FASTA-formatted sequence is shown in [Figure 1](/~/eukaryotic_genome_submission_Examples#fig1) .

### Annotation

While annotation is optional for incomplete WGS submissions, complete genome submissions must be annotated. The features listed below are the minimum required annotation, but there are many additional features that can be included. It is our hope that the annotation present on any genome will evolve over time as more is known about the biology. In reviewing eukaryotic genome annotation, NCBI strives to ensure that the annotation is consistent throughout the submission and when compared to other genome submissions. We also strive to present information that is an accurate representation of the known biology. To do this we need your help. Please pay careful attention to the annotation instructions presented here and please review all your annotation before submitting your genome. Many genomes are annotated by automatic prediction programs and since these programs do make mistakes, it is up to all of us to try and ensure the information being presented is as accurate as possible. A summary of the required annotation is presented below, however please also refer to our [detailed annotation instructions](/~/eukaryotic_genome_submission_annotation) for our annotation expectations.

#### Required Annotation

1.  Genes
    *   locus_tag
2.  Coding regions of known proteins
    *   product (protein) names
    *   protein_id
3.  mRNA features
4.  transcript_id

#### Gene features

A gene is defined as a region of biological interest for which a name has been assigned. Gene features are always a single interval, and their location should cover the intervals of all the relevant features such as promoters and polyA binding sites. Gene names should follow the standard nomenclature rules of the particular organism. For example, mouse gene names begin with an uppercase letter, and the remaining letters are lowercase. Please refer to [detailed annotation instructions](/~/eukaryotic_genome_submission_annotation) for more information on genes.

#### locus_tag

The locus_tag is a systematic gene identifier that is assigned to each gene. The locus_tag must be unique for every gene of a genome. Each genome project (i.e. all chromosomes) should have the same unique locus_tag prefix to ensure that a locus_tag is specific for a particular genome project, which is why we require that the locus_tag prefix be registered. In addition, genes may also have functional names as assigned in the scientific literature. For example, KCS_0001 is the systematic gene identifier, while Abc5 is the functional gene name. The locus_tag prefix should be 3-12 alphanumeric characters and the first character may not be a digit. Additionally locus_tag prefixes are case-sensitive. The locus_tag prefix is followed by an underscore and then an alphanumeric identification number that is unique within the given genome. Other than the single underscore used to separate the prefix from the identification number, no special characters can be used in the locus_tag. Read more about [locus_tags](http://www.ncbi.nlm.nih.gov/genomes/locustag/Proposal.pdf) and their intended usage. Please refer to [detailed annotation instructions](/~/eukaryotic_genome_submission_annotation) for how to incorporate locus_tags into your annotation table.

The use of locus_tag is supported in Sequin version 4.35 or later. If you have an older version of Sequin please download the [current version](http://www.ncbi.nlm.nih.gov/Sequin/index.html) . The latest version of tbl2asn is available from the [tbl2asn](/~/tbl2asn2) page.

#### CDS (coding region) features

The CDS feature is used to define a protein coding region. All CDS features must have a product qualifier (protein name), protein_id and transcript_id. For the product, use a concise name, not a description or phrase. Alternatively, protein names may be denoted by the same symbol as the corresponding gene with the appropriate capitalization for the organism. In cases where the protein is not known use "hypothetical protein" as the product name. We recommend the use of "hypothetical protein" as this will allow the locus_tag identifier to be appended to the product name in BLAST and Entrez summary lines. Our [detailed annotation instructions](/~/eukaryotic_genome_submission_annotation) contain instructions and examples on naming your proteins as well as including additional CDS qualifiers such as EC_numbers, protein functions, descriptive and similarity notes.

#### protein_id

The submitter must assign an identification number to all proteins. NCBI uses this number to track proteins when sequences are updated. This number is indicated in the table by the CDS qualifier protein_id, and should have the format gnl|dbname|string, where dbname is a version of your lab name that you think will be unique (eg SmithUCSD), and string is the unique protein SeqID assigned by the submitter.

The protein_id is used for internal tracking in our database, so it is important that the complete protein_id (dbname + SeqID) not be duplicated by a genome center. Note that when WGS submissions are processed, the dbname in the protein_id is automatically changed to 'WGS:XXXX', where XXXX is the project's accession number prefix. Please see [detailed annotation instructions](/~/eukaryotic_genome_submission_annotation) .

#### mRNA features

The submitter must include an mRNA feature for each translated CDS and extend the gene feature to include the entire mRNA. Additionally, the mRNA must have the same product name, protein_id and transcript_id as its corresponding CDS. Each mRNA feature can be either partial or complete. If there is no UTR information, then the mRNA's location will agree with its CDS's location, but the mRNA will be partial at its 5' and 3' ends. If the mRNA is partial, then make the gene partial.

Our [detailed annotation instructions](/~/eukaryotic_genome_submission_annotation) contain examples for including complete and partial mRNA features.

#### transcript_id

The submitter must also include a transcript_id qualifier. The transcript_id is used for internal tracking in our database, so it is important to include a transcript_id as a qualifier for both the CDS and its corresponding mRNA. Each transcript_id must be unique and different from the protein_id. Please see [detailed annotation instructions](/~/eukaryotic_genome_submission_annotation) .

### Creating the submission file

The submission file can be generated using [Sequin](http://www.ncbi.nlm.nih.gov/Sequin/index.html) or [tbl2asn](/~/tbl2asn2) . tbl2asn is a simple command line program that automates parts of the submission process, so is very useful, especially for projects that have multiple sequences. The newest version is available by anonymous [FTP](ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/converters/by_program/tbl2asn/) . The main difference between Sequin and tbl2asn is that Sequin is a menu-driven program with a graphical interface, while tbl2asn is a command line program. Most people find Sequin easier for finished genomes while tbl2asn is useful for unfinished WGS submissions that have many contigs. See the [WGS](/~/wgs) page for specific information on generating a WGS submission.

For both programs the sequence must be in a file or files in FASTA format, and the annotation must be in a file or files in the five column tab-delimited feature table format, as described above.

#### Sequin

If you choose to use Sequin to make your submission file, then follow the directions on the [Sequin](http://www.ncbi.nlm.nih.gov/Sequin/index.html) page. Check the [detailed annotation instructions](/~/eukaryotic_genome_submission_annotation) to ensure that you have included the annotation correctly. Be sure to validate and fix the errors. Run the [Discrepancy Report](/~/asndisc) if your submission has annotation, and fix any problematic annotation detected. Contact [genomes@ncbi.nlm.nih.gov](mailto:genomes@ncbi.nlm.nih.gov) with questions about any errors or discrepancy report output.

#### tbl2asn

If you choose to use tbl2asn, then the basic instructions follow, but more detail is available on the [tbl2asn](/~/tbl2asn2) page.

tbl2asn reads a template along with the sequence and table files, and outputs ASN.1 for submission to GenBank. tbl2asn requires that the sequence and annotation file have specific name conventions. The FASTA-formatted sequence file has ".fsa" as an extension, and the five column tab-delimited table file has ".tbl" as an extension. The base name of the .tbl file must be identical to that of the .fsa file for tbl2asn to recognize it and to include the annotation in the output ".sqn" file that it generates.

The template file is created at http://www.ncbi.nlm.nih.gov/WebSub/template.cgi.

<pre>As described in the [general instructions](/~/wgs.submit#Run), run

</pre>

*   **tbl2asn -p path_to_files -t template -M n -Z discrep**

**If the sequences contain Ns that represent gaps**, then run the appropriate tbl2asn commandline with the –l and –a arguments, as described in the [Gapped Genome Submission](http://www.ncbi.nlm.nih.gov/genbank/wgs_gapped) page.

Additional command line arguments can be seen on the [tbl2asn](/~/tbl2asn2) page.

In the directory specified by '-p', the program looks for corresponding pairs of *.fsa and *.tbl files, and builds ASN.1 records named *.sqn for these pairs. The results of the validation (error checking) will be in *.val files. Note that if there are no .tbl files in the directory, then tbl2asn will still generate .sqn files from the .fsa files that are present.

Go to the [WGS](/~/wgs) page for specific information about generating a WGS submission, and to the [detailed annotation instructions](/~/eukaryotic_genome_submission_annotation) to ensure that you have included the annotation correctly.

You can open a .sqn file in Sequin to fix validation errors and make any editing changes. Additional tips on using Sequin are found in the [Sequin Guide](http://www.ncbi.nlm.nih.gov/Sequin/QuickGuide/sequin.htm) .

[Check the output of the validation and discrepancy report and fix problems](/~/wgs.submit#Fix)  

Once the errors have been fixed, the .sqn files can be submitted to GenBank.

### Submitting

Genomes are generally submitted to us by FTP or with our Genomes Submission Tool. Generally, you can use our [Genomes Submission Tool](http://www.ncbi.nlm.nih.gov/projects/GenomeSubmit/genome_submit.cgi) to upload genome submission files to us directly without using your email system, which can sometimes lead to delivery or file corruption problems. If you are going to be submitting frequently, we can establish an FTP account for you here at NCBI. In this case please send us an email, requesting an ftp account and describing your project. Regardless of the method you use, we ask that you send us an email at [genomes@ncbi.nlm.nih.gov](mailto:genomes@ncbi.nlm.nih.gov) whenever you submit a new genome, and include the registered ProjectID and organism name in the message.

### What happens next

Once we receive your genome submission, a member of our staff will conduct an initial review of it and will contact you by email. If we do not find any significant issues with your submission, you will be issued an accession number. Once your submission is assigned an accession number it undergoes a thorough review by our staff. This review is critical because we are striving to present genome annotation in an accurate and consistent manner so that database users can make maximum use of the data. If we encounter problems during this review, we will contact you by email.

Once we have completed our review of your submission, we will prepare it for release to the public database. You can choose to have your submission released immediately or to be kept confidential until a certain date or publication of the work, whichever is first. If you wish your genome to be held until publication, we ask that you provide us with the expected publication date and also notify us in a timely manner of the upcoming publication and the relevant citation details. This will allow us to coordinate the release of your genome with the appearance of the paper. Please provide at least two weeks notice of any upcoming publication.

### Updating a genome

When a complete genome or chromosome is updated, the proteins should be tracked to the update. To do this, proteins from the original submission that are present in the update must have the same identifiers that were used in the original submission, plus the accession numbers that were assigned when the submission was loaded into GenBank. These identifiers are included in the protein_id of the update in this format:

<pre>gnl|dbname|SeqID|gb|accession_number
</pre>

where the dbname and SeqID are the values used in the original submission, and the accession number was assigned by GenBank.

When your genome is released, we will supply you with a table that has each protein SeqID and protein accession number, so that you can use those in future updates. If you did not receive this table and need to update your genome, contact us at [genomes@ncbi.nlm.nih.gov](mailto:genomes@ncbi.nlm.nih.gov) prior to the preparation of your submission.

See the [WGS](/~/wgs#update) page for information about updating a WGS project.

</div>

</div>

<div id="shared-content-1" nid="1465">

<div class="rightnav">

## WGS Resources

*   [About WGS](/~/wgs)
*   [WGS Project List](http://www.ncbi.nlm.nih.gov/Traces/wgs)
*   [WGS Submission Guide](/~/wgs.submit)
*   [Update Genome Records](/~/wgs_update)
*   [FAQ](/~/wgsfaq)
*   [tbl2asn](/~/tbl2asn2)
*   [Create Submission Template](http://www.ncbi.nlm.nih.gov/WebSub/template.cgi)
*   [BioProject](http://www.ncbi.nlm.nih.gov/bioproject)
*   [Eukaryotic Annotation Guide](/~/eukaryotic_genome_submission)
*   [Prokaryotic Annotation Guide](/~/genomesubmit)
*   [Discrepancy Report](/~/asndisc)
*   [WGS Example Files](/~/examples.wgs)
*   [Assembly Submission Guide](http://www.ncbi.nlm.nih.gov/assembly/docs/submission/)
*   [AGP Format](http://www.ncbi.nlm.nih.gov/assembly/agp/AGP_Specification/)
*   [WGS Submission Portal](https://submit.ncbi.nlm.nih.gov/subs/wgs/)
*   [NCBI Prokaryotic Genome Annotation Pipeline](http://www.ncbi.nlm.nih.gov/genome/annotation_prok/)
*   [Metagenome Submission Guide](/~/metagenome)
*   [Structured Comment](/~/structuredcomment)

</div>

</div>