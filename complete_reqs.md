<meta http-equiv="Content-Type" content="text/html; charset=utf-8">  <meta name="node-id" content="1442"> <meta name="revision-id" content="10286"> <meta name="cms-base-url" content="http://cms.ncbi.nlm.nih.gov"> <meta name="cms-view-url" content="http://cms.ncbi.nlm.nih.gov/genbank/complete_reqs"> <meta name="cms-edit-url" content="http://cms.ncbi.nlm.nih.gov/node/1442/edit"> <meta name="created" content="2011-11-10T11:22:21-05:00"> <meta name="modified" content="2012-08-27T09:14:46-04:00"> <meta name="publication-date" content="2011-11-10T11:22:21-05:00"> <meta name="author" content="yankie"> <meta name="subsite" content="genbank"> <meta name="path" content="genbank/complete_reqs"> <meta name="node-type" content="page"> <meta name="jira-ticket" content=""> <meta name="cms-tags" content="">  <meta name="" content=""> <title>Complete Eukaryotic Genome Requirements</title>

<div class="node clear-block">

<div class="content">

# Additional Guidelines for Complete Eukaryotic Genome Submissions

### Introduction

Because complete genomes and complete chromosomes are often used as the basis for RefSeq records, there are additional needs for their submissions.

### Requirements

#### Additional qualifiers

All WGS and complete genome submissions require that each CDS have a protein_id, as described in the general eukaryotic [guidelines](/~/eukaryotic_genome_submission). However, complete genomes need a transcript_id qualifier also. In addition, the protein_id and transcript_id are included as a qualifier for both the CDS and its corresponding mRNA, and each protein_id and transcript_id must be unique.

<pre>63574	87173	gene
			locus_tag	Ngs_17131
63574	63907	mRNA
75690	75730
84396	85536
85598	85773
85836	86109
86173	86467
86555	86670
86731	87173
			product	hypothetical protein
			protein_id	gnl|ncbi|Ngs_17131
			transcript_id	gnl|ncbi|Ngs_mrna17131
84402	85536	CDS
85598	85773
85836	86109
86173	86467
86555	86670
86731	86882
			product	hypothetical protein
			protein_id	gnl|ncbi|Ngs_17131
			transcript_id	gnl|ncbi|Ngs_mrna17131

</pre>

### Additional files

Often the submitter has the sequences of the proteins and their transcripts. If these sequences are saved as appropriately named files in the same directory as the .fsa and .tbl files, then tbl2asn will use them to confirm the conceptual translations and the mRNA sequences when it builds the .sqn file.

If the protein and mRNA sequences are known, put the proteins into .pep files, as described on the [tbl2asn](/~/tbl2asn2) page, and put the mRNA sequences into analogous files, named .rna files.

The .pep and .rna files will contain the sequences of all the proteins and transcripts, respectively, of the cognate nucleotide sequence (.fsa) file. The basename of the .pep and .rna files must match the basename of the .fsa file, and each sequence has a definition line, in which the identifier is the protein_id (for the .pep file) or transcript_id (for the .rna file).

<pre>.pep file:

>gnl|ncbi|Ngs_17131
MQSTQSKSDRSSMHRGPLLLCAVMVVLVTLPEQINARMAFEKLT
>gnl|ncbi|Ngs_3038A
MRMRGRRLLPIILSLLLIVLLSLCYFSNHLRDSSQSRKNGFLLH
[etc.]

.rna file:

>gnl|ncbi|Ngs_mrna17131
cgtcaacagcagccattgcgcgtgatgcaattgaagtgctaacacctcgcaccgcccgagttttagc
>gnl|ncbi|Ngs_mrna3038A
aatgcagtcaacccaaagtaagagtgatcgatcttcgatgcacaggggccctctacttctctgcgccgtg
[etc.]

</pre>

### Creating the submission file

If you have .pep and/or .rna files, put them into the same directory as the .fsa and .tbl files. Run the same tbl2asn command line as usual, but include the -g argument so that the submission is created as a genome-product (GenProd) set in the .sqn file. A GenProd set contains the genomic DNA sequence packaged together with all of its mRNA sequences and protein sequences, for ease of display of RefSeq genome resources. Note that the flatfile view of the final processed genome will be the same whether -g was used or not.

Sample command line:

tbl2asn -p path_to_files -t template_file -v -g

When you submit a complete genome or complete chromosome, in addition to the .sqn file, please send us the additional files that you used: .fsa, .tbl, .pep and .rna.

Even if you do not have the additional .pep or .rna files, set up your .tbl file with transcript_id and protein_id qualifiers, and include the -g argument when you run tbl2asn for complete genomes or complete chromosomes.

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