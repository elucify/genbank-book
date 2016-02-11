<meta http-equiv="Content-Type" content="text/html; charset=utf-8">  <meta name="node-id" content="3133"> <meta name="revision-id" content="16551"> <meta name="cms-base-url" content="http://cms.ncbi.nlm.nih.gov"> <meta name="cms-view-url" content="http://cms.ncbi.nlm.nih.gov/genbank/wgs_update"> <meta name="cms-edit-url" content="http://cms.ncbi.nlm.nih.gov/node/3133/edit"> <meta name="created" content="2013-08-04T13:31:36-04:00"> <meta name="modified" content="2013-08-04T14:52:35-04:00"> <meta name="publication-date" content="2013-08-04T13:13:00-04:00"> <meta name="author" content="kclark"> <meta name="subsite" content="genbank"> <meta name="path" content="genbank/wgs_update"> <meta name="node-type" content="page"> <meta name="jira-ticket" content=""> <meta name="cms-tags" content="">  <meta name="" content=""> <title>How to Update Genome Records</title>

<div class="node clear-block">

<div class="content">

# Updating Information on GenBank Draft Genome Records

The following information provides the different methods to submit updates for draft genomes in order to ensure that your update is processed quickly and correctly. Updates provided in an incorrect format will delay processing. All update files should be saved as plain text.  If you are updating multiple records, please send a list of all accessions to be updated at the top of your request.

### Update Formats

*   [Author Information](#author)
*   [Add a Publication](#pub)
*   [Source Information](#source)
*   [A new assembly of the genome (sequence update)](#newasm)
*   [Changing text or adding new qualifiers for existing features](#text)
*   [Adding or removing a few features](#fewfeats)
*   [Re-annotating existing records (adding or removing or moving many features)](#manyfeats)

### Author Information

Replace any non-ASCII characters (for example, characters with accents and umlauts) with the appropriate English letters, and send a 2-column table with the accession number in column 1 and the author names listed as " given_name middle_initial surname" in column 2, where the middle_initial is optional. For example:

<pre>ARTP00000000    Thomas Smith, Robert T. Jones, Susan Zhu, Michael N. Boone
AMQC00000000    Robert T. Jones, Martin M.J. Roberts, Henry P. Allen
</pre>

### Add a Publication

To add a publication, provide the PubMedID, if one has been assigned. Otherwise, replace any non-ASCII characters (for example, characters with accents and umlauts) with the appropriate English letters and provide the journal name and paper title. Provide the authors in a 2-column table with the accession number in column 1 and the author names listed as " given_name middle_initial surname" in column 2, where the middle_initial is optional. For example:

<pre>ARTP00000000    Thomas Smith, Robert T. Jones, Susan Zhu, Michael N. Boone
Nature Genetics. Genome sequence of the ABCD organism.
</pre>

### Source Information

Send updates to the source information (i.e. strain, cultivar, country, specimen_voucher) in a multi-column tab-delimited table, See http://www.ncbi.nlm.nih.gov/Sequin/modifiers.html for a list of valid qualifiers. For example:

<pre>acc. num.       strain  country
XXXX00000000        82      USA
XXXY00000000        ABC     Canada
</pre>

### A new assembly of the genome (sequence update)

If you have updated the sequence and the chromosomes of the genome are still in multiple pieces, then create a new WGS submission as you did before following the instructions at http://www.ncbi.nlm.nih.gov/genbank/wgs.submit.html. Upload the new files in the submission portal with a note that this is the next version of XXXX00000000\. The pieces will be assigned new accession numbers and the master accession will increment to the next version, eg XXXX01000000 would update to XXXX02000000\. For more information about WGS accession numbers see http://www.ncbi.nlm.nih.gov/genbank/wgs#Intro.

If the chromosomes of the genome are now a single piece each, then submit this as a complete genome. Use [GenomesMacroSend](http://www.ncbi.nlm.nih.gov/projects/GenomeSubmit/genome_submit.cgi) to submit the files and include a note that this is the complete genome, replacing the wgs genome XXXX00000000\. Create prokaryotic files as described at http://www.ncbi.nlm.nih.gov/genbank/genomesubmit. Create annotated eukaryotic genomes as described at http://www.ncbi.nlm.nih.gov/genbank/eukaryotic_genome_submission_annotation.html

### Changing text or adding new qualifiers for existing features

Use a tab-delimited table for simple updates to existing features (eg changing product names or adding EC_numbers to existing CDS features). The first row in the table would be the headers, with subsequent rows for each qualifier being modified or added. The first column is the accession or contig name, the second is locus_tag, and subsequent columns are the qualifiers being changed. For example:

<pre>Accession	Locus_tag	gene_name	CDS_product	CDS note	gene note
XXXX01000001	Abc_xxxx	lacZ	beta-galactosidase		present in multiple copies
XXXX01000010	Abc_xxxy		helicase	required for replication
</pre>

Also indicate whether blank cells mean 'delete what is present' or 'no change'. A blank cell in the CDS_product can never mean 'delete' since that is a required field. You only need to include the features that are changing. New product names will need to follow the protein naming conventions; see the [Prokaryotic](http://www.ncbi.nlm.nih.gov/genbank/genomesubmit_annotation#CDS) and [Eukaryotic Genome Guidelines](http://www.ncbi.nlm.nih.gov/genbank/eukaryotic_genome_submission_annotation/#CDS).

NOTE: You cannot add, remove, or change the locations of new features (eg new CDS or gene) this way. If you want to make those changes, then see the instructions below.

### Adding or removing a few features

If you are only adding a few new features, then you could send a small 5-column Feature Table .tbl file that has only the new features. However, if there are many changes, then follow the [instructions below](#manyfeats) for re-annotating existing records. For more information about this table format see the [Prokaryotic](http://www.ncbi.nlm.nih.gov/Genbank/genomesubmit.html ) or [Eukaryotic Genome Guidelines](http://www.ncbi.nlm.nih.gov/genbank/eukaryotic_genome_submission_annotation.html).

If you are only removing a few features, send us a list of the locus_tags for the features that need to be removed.

We will let you know if we find any issues when the update file is processed, eg if a CDS overlaps an rRNA feature. Email the files to genomes@ncbi.nlm.nih.gov and include the WGS accession in the request.

### Re-annotating existing records (adding or removing or moving features)

If the genome has been released with annotation and you want to update the annotation (but not change the sequences), create a new annotated submission as you did originally, and submit the update via the WGS submission portal https://submit.ncbi.nlm.nih.gov/subs/wgs/. We will replace all of the existing annotation with the annotation in the new file.

The fasta header in the update must include the contig identifier (SeqID) used in the original submission and the accession numbers. The correct format for the identifiers in such an update is:

*   gnl|WGS:XXXX|SeqID|gb|XXXX01xxxxxx

where XXXX is the accession prefix and XXXX01xxxxxx is the contig accession number. You should have received an xxxx.accs file containing the contig identifiers and accession numbers when the genome was released. Let us know if you need a copy of this file.

Please see the WGS page, http://www.ncbi.nlm.nih.gov/genbank/wgs.submit.html, for instructions about how to generate a WGS submission. In addition, be sure to read either the [Prokaryotic](http://www.ncbi.nlm.nih.gov/Genbank/genomesubmit.html ) or [Eukaryotic Genome Guidelines](http://www.ncbi.nlm.nih.gov/genbank/eukaryotic_genome_submission_annotation.html).

In the standard situation, annotation is not tracked from the previous version to the new version. The locus_tag prefix always remains the same; however, the locus_tags would need to be unique in the new annotation, both within the update and compared to the previous annotation. A simple way to ensure uniqueness is to use a different number of digits after the underscore in the locus_tag. For example, if the registered locus_tag prefix is ABC and the previous annotation has 4 digits after the underscore (ABC_0001), then the new annotation could have 5 digits (ABC_00001). Similarly, the protein_ids must be unique compared to the previous assembly. By using the locus_tag in the protein_id, this uniqueness could be maintained, for example:

*   gnl|WGS:xxxx|ABC_00001

where XXXX is the accession number prefix of the project.

Alternatively, you could track the annotation from the previous version to this update. Note that this is not required. Track both the locus_tag's and protein_id's so that they are included when the gene/CDS is retained in the new annotation, even if the nucleotide location is modified slightly (eg, the start codon is being extended upstream). To track the proteins, the protein_id's must have the format:

*   gnl|WGS:xxxx|SeqID|gb|accession_number

where XXXX is the accession number prefix of the project, SeqID is the protein SeqId (column 1 of the p2g file) and accession_number is the protein accession number (column 2 of the p2g file). You should have received a p2g file with the release letter for the genome. We can send this file again if you need it.

If you are adding a new protein, it would not have a protein accession number. You would need to use a new locus_tag that was not in the previous annotation and you would need to give the new protein a unique identifier (usually the same as the new locus_tag). For example, if you used ABC_6000 as the new locus_tag, you could use:

*   gnl|WGS:XXXX|ABC_6000

Please include a summary of the expected protein fates (new proteins, same proteins, changed proteins, removed proteins) so we will know what to expect.

If you are modifying an existing protein (maybe just moving the start codon) then use the same locus_tag and protein_id that is in the previous annotation. The protein will also keep its protein accession number. If you find that two adjacent proteins should be combined into a single protein and part of the translation stays the same, then choose one of the locus_tag/protein_ids/protein_accessions from the previous annotation to use for the new protein (preferably the one that had the similar translation) and remove the other identifiers (or you could add the removed locus_tag to the /old_locus_tag qualifier and include a note explaining twohat t proteins were combined). If you are completely changing a protein (maybe changing the reading frame) such that the new translation is completely different, then it would be a new protein with a new locus_tag, new protein_id, which would be assigned a new accession upon release into GenBank. If you do remove a protein, then do not reuse the locus_tag/protein_id/protein_accession for a different protein. The identifiers are meant to represent a single unique feature and should not be moved to different proteins.

Please contact us at genomes@ncbi.nlm.nih.gov if you have questions about generating the submission files, or about details of annotation.

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