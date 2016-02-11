
# Adding a Structured Comment to GenBank Submissions

## Introduction

Public database sequence records consist primarily of nucleotide sequence data, source organism information, and sequence features. The organism and feature description are based on a controlled list of organism modifiers (such as isolate, strain, clone, and specimen voucher) and features (such as CDS, rRNA, and gene).

However, many sequence submitters also have additional organism metadata that cannot easily fit into the controlled list but that is significant for the complete description of a sequences source and allows for comparisons of sequences isolated from similar locations.

To collect and display such additional metadata in sequence records, GenBank has developed a Structured Comment. The comment consists of tag-value pairs that are contained within START and END tags that function as delimiters for easy parsing. These comments can be incorporated from a tab-delimited table into submission files using either Sequin or tbl2asn. An example of a GenBank record that includes a structured comment is [GU949562](/nuccore/291609868).

This guide explains how to include structured comments with your sequence submission.

If you do not understand any of the instructions presented here or you have questions, please contact GenBank User Services at [info@ncbi.nlm.nih.gov](mailto:info@ncbi.nlm.nih.gov) prior to creating your submission.

## Table of Contents

1.  [Including Structured Comments Within GenBank Submissions](#IncludingStructuredCommentsWithinGenBankSubmissions)

*   [Adding the same structured comment to all sequences in your submission](#SameStructuredComment)
*   [Adding a unique structured comment to each sequence in your submission](#UniqueStructuredComment)

2.  [Specialized Structured Comments](#Specializedcomments)

*   [MIGS/MIMS/MIMARKS](#MIGS)
*   [Genome Submissions](#Genome)
*   [Transcriptome Shotgun Assembly Submissions](#TSA)
*   [GenBank Assembly-Data](#GenBank)
*   [HIV](#HIV)

3.  [Retrieval in Entrez](#Retrieval)

### <a name="IncludingStructuredCommentsWithinGenBankSubmissions"></a>Including Structured Comments Within GenBank Submissions

In order to include unique metadata within the structured comment, you need to create a tab-delimited table in one of two ways depending on how the data should be applied to the sequences in your submission. Any scientific unit of measurement (eg, deg C or km) should be included with the value.

#### <a name="SameStructuredComment"></a>[1] Adding the same structured comment to all sequences in your submission

This requires a single tab-delimited table that includes the tag-value pairs that are to be applied to all of the sequences in your submission, for example:

<table border="1">

<tbody>

<tr>

<td>oxygen_content</td>

<td>32 ppm</td>

</tr>

<tr>

<td>habitat</td>

<td>Black Lake</td>

</tr>

<tr>

<td>temperature</td>

<td>27 deg C</td>

</tr>

<tr>

<td>sample size</td>

<td>150 mL</td>

</tr>

<tr>

<td>depth</td>

<td>10 m</td>

</tr>

</tbody>

</table>

Once the metadata table is created and saved as plain text, the structured comment can be included using either Sequin or tbl2asn.

*   **Sequin**

    From the Sequin Menu, choose annotate > descriptors > structured comment. This brings up a two-column table that can be completed manually - the first column is the tag and the second the value - or you can import a single-tab-delimited table using file > import.

*   **tbl2asn**

    The tab-delimited table needs to be saved as a .cmt file and included in the same directory as your fasta and table file. The file name should include the same prefix as your fasta file (for example, fasta1.txt and fasta1.cmt).  Including the argument -X C within the tbl2asn commandline, will apply the tab-delimited table as a structured comment to all of the sequences in your file.  Alternatively, you can use any file name for the structured comment file and call it with the argument -w within the tbl2asn commandline.

#### <a name="UniqueStructuredComment"></a>[2] Adding a unique structured comment to each sequence in your submission

The format for this type of table is a tab-delimited, multi-column table, where the first column must be the Sequence Identifier used in the .fsa files. The first row in each column is the metadata tag that appears in the left side of the structured comment, for example:

<table border="1">

<tbody>

<tr>

<td>SeqID</td>

<td>investigation_type</td>

<td>project_name</td>

<td>collection_date</td>

<td>depth</td>

</tr>

<tr>

<td>A</td>

<td>metagenome</td>

<td>aquatic study</td>

<td>2007-03-04</td>

<td>10 m</td>

</tr>

<tr>

<td>B</td>

<td>metagenome</td>

<td>aquatic study</td>

<td>5 m</td>

</tr>

<tr>

<td>C</td>

<td>eukaryote</td>

<td>Analysis of fish</td>

<td>2008-08-09</td>

<td>25 m</td>

</tr>

</tbody>

</table>

Each sequence in this submission will include a structured comment with unique tag-value pairs.  Once the metadata table is created and saved as plain text, the tag-value pairs can be included using either Sequin or tbl2asn.

*   **Sequin**

    Within the Sequin Menu, the option Annotate > advanced table readers > load structured comments from table will upload the tab-delimited table as a structured comment.

*   **tbl2asn**

    The tab-delimited table needs to be saved as a .cmt file and included in the same directory as your fasta and table file. The file name should include the same prefix as your fasta file (for example, fasta1.txt and fasta1.cmt).  The .cmt file will be automatically included as a structured comment when using tbl2asn.

### <a name="Specializedcomments"></a>Specialized Structured Comments

#### **<a name="MIGS"></a>[1] MIGS/MIMS/MIMARKS**

Minimum information checklists have been developed by the [Genomic Standards Consortium](http://gensc.org/) (GSC) as a means of reporting core descriptive information about the environment from which an organism(s) was collected. Core descriptors include information about the origins of the nucleic acid sequence (genome), its environment (eg, latitude and longitude, date and time of sampling, habitat) and sequence processing (sequencing and assembly methods).

Three different metadata lists have been developed to describe genomic, metagenomic, and marker sequences:

*   **MIGS** - Minimum Information About a Genome Sequence
*   **MIMS** - Minimum Information About a Metagenome Sequence
*   **MIMARKS** - Minimum Information About a Marker Sequence

The tag-value pairs that are included for each submission type can be validated for compliance with the GSC recommended list. The recommended lists of core descriptors that should be included for each of these sequence types can be found [here](http://wiki.gensc.org/index.php?title=MIxS).

Validation tools within Sequin and tbl2asn will report if structured comments include all of the GSC recommended compliant core descriptors. Submissions that include of all the compliant tags will have a Keyword included within the GenBank flatfile:

KEYWORD GSC:MIMARKS:3.0

Structured comments that are not compliant based on the GSC guidelines can still be included within GenBank submissions - they just will not include the keyword.

In order for this validation to occur, you will need to include within the first column in your table a tag that defines the prefix and suffix for the start and end tags within the structured comment, for example:

<table border="1">

<tbody>

<tr>

<td>StructuredCommentPrefix</td>

<td>[one of the following - MIGS:3.0-Data / MIMS:3.0-Data / MIMARKS:3.0-Data]</td>

</tr>

<tr>

<td>investigation_type</td>

<td>[value determined by organism type as defined within [GSC spreadsheet](http://wiki.gensc.org/index.php?title=MIxS)]</td>

</tr>

<tr>

<td>project_name</td>

<td>Analysis of soil bacteria</td>

</tr>

<tr>

<td>collection_date</td>

<td>2008-08-09</td>

</tr>

<tr>

<td>lat_lon</td>

<td>35.64N 56E</td>

</tr>

<tr>

<td>geo_loc_name</td>

<td>France</td>

</tr>

<tr>

<td>biome</td>

<td>

grassland

</td>

</tr>

<tr>

<td>feature</td>

<td>

field

</td>

</tr>

<tr>

<td>material</td>

<td>

soil

</td>

</tr>

<tr>

<td>env_package</td>

<td>

[env_package types are listed within the [GSC spreadsheet](http://wiki.gensc.org/index.php?title=MIxS)] - can include the term "missing"

</td>

</tr>

<tr>

<td>num_replicons</td>

<td>14</td>

</tr>

<tr>

<td>ref_biomaterial</td>

<td>PMID</td>

</tr>

<tr>

<td>biotic_relationship</td>

<td>free living</td>

</tr>

<tr>

<td>trophic_level</td>

<td>autotroph</td>

</tr>

<tr>

<td>rel_to_oxygen</td>

<td>aerobe</td>

</tr>

<tr>

<td>isol_growth_condt</td>

<td>PMID</td>

</tr>

<tr>

<td>seq_meth</td>

<td>pyrosequencing</td>

</tr>

<tr>

<td>assembly</td>

<td>Velvet; error rate 1/45</td>

</tr>

<tr>

<td>finishing_strategy</td>

<td>complete; 4X coverage; 2500 contigs</td>

</tr>

</tbody>

</table>

An example of a sequence that includes a structured comment that meets GSC compliance is [GU949561](/nuccore/291609867).

#### **<a name="Genome"></a>[2] Genome Submissions**

[WGS Genome submissions](http://www.ncbi.nlm.nih.gov/genbank/wgs) require assembly information to be included within the Genome Assembly-Data structured comment.  This structured comment includes the following required metadata:

    **Assembly Name**: a short name suitable for display eg, LoxAfr_3.0 for a Loxodonta africana assembly, version 3.0  
    **Assembly Method** (with version or date the program was run): eg, Newbler v. 2.3 OR Celera Assembly v. May 2010  
    **Genome Coverage**: eg, 12x  
    **Sequencing Technology**: eg, ABI 3730; 454 GS-FLX Titanium; Illumina GAIIx

Note that the Assembly Name is optional, and that Assembly Method requires 'v. ' between the algorithm name and its version (or the month and year it was run).  If more than one sequencing technology was used, separate them with a semi-colon, e.g. "Sanger; Illumina GAIIx".  Info-level warnings will report the goal and the current status are missing, but these can be ignored.

When using the [WGS Submission Portal](https://submit.ncbi.nlm.nih.gov/subs/wgs/) to submit a WGS project, you will be prompted for this information, which will then automatically be included within your submission.   You can also include this structured comment within your .sqn file using Sequin or tbl2asn as described above.  The prefix and suffix for the start and end tags are:

*   StructuredCommentPrefix   GenomeAssembly-Data
*   StructuredCommentSuffix   GenomeAssembly-Data

An example of a genome with the required structured comment is [AMVS01000000](http://www.ncbi.nlm.nih.gov/nuccore/amvs00000000.1).

#### **<a name="TSA"></a>[3] Transcriptome Shotgun Assembly Submissions**

An Assembly-Data structured comment is required for [Transcriptome Shotgun Assembly](http://www.ncbi.nlm.nih.gov/genbank/tsa) (TSA) sequences.  Users will be prompted for this information when using the TSA Sequin Wizard.  If submitting using tbl2asn, this file can be made using the [Structured Comment template](https://submit.ncbi.nlm.nih.gov/structcomment/nongenomes/) (non-genomes) page or as described above.

The TSA structured comment includes the following required values:

    **Assembly Method** (with version or date the program was run): eg, Velvet v.1.1.05, Oases v.0.1.22, Trinity r2012-01-25  
    **Sequencing Technology**: eg, ABI 3730; 454 GS-FLX Titanium; Illumina GAIIx

 Coverage and Assembly Name may be added but these are optional. 

    **Assembly Name**: a short name suitable for display eg, LoxAfr_3.0 for a Loxodonta africana assembly, version 3.0  
    **Coverage**: eg, 12x

The prefix and suffix for the start and end tags to include within this structured comment are:

*   StructuredCommentPrefix   Assembly-Data
*   StructuredCommentSuffix   Assembly-Data

An example of a TSA submission with the required structured comment is [JU497302.](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=nucleotide&list_uids=383446918&dopt=GenBank)

#### **<a name="GenBank"></a>[4] GenBank Assembly-Data**

Submission to [GenBank](http://www.ncbi.nlm.nih.gov/genbank/) can include an Assembly-Data structured comment that is displayed within the GenBank flatfile and provides users with information regarding the sequencing and assembly details.

This structured comment includes the following values:

    **Assembly Method** (with version or date the program was run): eg, Newbler v. 2.3 OR Celera Assembly v. May 2010  
    **Coverage**: eg, 12x  
    **Sequencing Technology**: eg, ABI 3730; 454 GS-FLX Titanium; Illumina GAIIx (required)

The prefix and suffix for the start and end tags to include within this structured comment are:

*   StructuredCommentPrefix   Assembly-Data
*   StructuredCommentSuffix   Assembly-Data

An example of a GenBank record with an Assembly-Data structured comment is [JQ307843](http://www.ncbi.nlm.nih.gov/nuccore/JQ307843.1).

#### **<a name="HIV"></a>[5] HIV**

A specialized structured comment can be included with HIV sequence submissions to describe additional metadata that cannot be easily included within the source descriptor. This includes specific tags that provide more information regarding the source of the virus.

For HIV-specific structured comments, you need to include two additional columns in your table that define the prefix and suffix for the start and end tags on either side of the structured comment:

*   StructuredCommentPrefix   HIV-DataBaseData
*   StructuredCommentSuffix   HIV-DataBaseData

Example Table

<table border="1">

<tbody>

<tr>

<td>SeqID</td>

<td>sequence name</td>

<td>Patient cohort</td>

<td>Sample tissue</td>

<td>viral load</td>

<td>StructuredCommentPrefix</td>

<td>StructuredCommentSuffix</td>

</tr>

<tr>

<td>SeqA</td>

<td>mysample_1</td>

<td>CHAVI001</td>

<td>plasma</td>

<td>3565728</td>

<td>HIV-DataBaseData</td>

<td>HIV-DataBaseData</td>

</tr>

<tr>

<td>SeqB</td>

<td>mysample_2</td>

<td>CHAVI002</td>

<td>plasma</td>

<td>3565730</td>

<td>HIV-DataBaseData</td>

<td>HIV-DataBaseData</td>

</tr>

<tr>

<td>SeqC</td>

<td>mysample_3</td>

<td>CHAVI003</td>

<td>plasma</td>

<td>3565755</td>

<td>HIV-DataBaseData</td>

<td>HIV-DataBaseData</td>

</tr>

</tbody>

</table>

An example record that includes a properly formatted HIV structured comment is [EU579019.](/nuccore/238915380)

## <a name="Retrieval"></a>Retrieval in Entrez

Sequences with structured comments can be retrieved in Entrez by specifying the tag-value pair in double quotes, eg, “investigation_type bacteria_archaea”. This search in Entrez retrieves GenBank records with this tag-value pair in the structured comment. You can also search for each tag as a property in Entrez (eg, depth[prop]) in order to retrieve all records that have this indexed within the structured comment.





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



