
# Discrepancy Report

### Introduction

The Discrepancy Report is an evaluation of a single or multiple ASN.1 files, looking for suspicious annotation or annotation discrepancies that NCBI staff has noticed commonly occur in genome submissions, both complete and incomplete (WGS). A few of the problems that this function was written to find include inconsistent locus_tag prefixes, missing protein_id's, missing gene features, and suspect product names. The function is available in specially configured Sequin, as an argument for tbl2asn, or with the command-line program asndisc.

If you have questions about the Discrepancy Report, please contact us by email at [genomes@ncbi.nlm.nih.gov](mailto:genomes@ncbi.nlm.nih.gov) prior to sending us your submission.

NEW To have the FATAL problems tagged, use asndisc version 2.0 or later and include the argument -P t (or use v19.2 or later of [tbl2asn](/~/tbl2asn2) and include '-M n -Z discrep'). The FATAL categories are issues that must be fixed, to allow processing of your submission. Reports that are not flagged as fatal need to be evaluated to determine if they represent annotation artifacts that need to be corrected or if they are acceptable due to the biology of the genome.

### Table of Contents

1.  [Using Sequin](#UsingSequin)
2.  [Using tbl2asn](#Usingtbl2asn)
3.  [Using asndisc](#Usingasndisc)
4.  [Evaluating the output](#Evaluatingtheoutput)
    *   [Fatal reports](#fatal)

### Using Sequin

Sequin can be configured to have the Discrepancy Report function available by following the "Configuring Sequin for HTG Submissions" directions in the [HTG](/HTGS/sequininfo) section. "Discrepancy Report" will then be present as an option in the Special menu.

When you run the Discrepancy Report within Sequin, a box will pop up with the results. In the lefthand frame are the problems, and in the righthand frame are the features with the selected problem. Selecting a feature in the righthand frame will cause Sequin to jump to the feature in the standard display. Double-clicking on a feature in the righthand frame will open that feature's editor, so that changes can be made to it. After making all the changes, click the "Recheck" button to have the Discrepancy Report run again. And be sure to save your changes to the file with File-Save or File-Save as.

See [Evaluating the output](#Evaluatingtheoutput) for information about the output and which kinds of reports need to be fixed and which are just informative.

### Using tbl2asn

To run the discrepancy report using ``tbl2asn``, include the argument ``-Z`` with the name of the output file. For example, a typical command would look like this:

```tbl2asn -p path_to_fsa_files -t template -M n -Z discrep```

```
    -p    Path to Files [String] 
    -t    Template File [File In] 
    -M n  Combines flags for genomes submissions (replaces -a s -V v; invokes FATAL calls when 
          -Z discrep is included). 
    -Z    Discrepancy Report Output File [File Out]
```

For more information, see the [tbl2asn instructions](/~/tbl2asn2) . Examine the contents of the output file, discrep: [Evaluating the output](#Evaluatingtheoutput)</dt>


### Using asndisc

The commandline program asndisc is available by anonymous [FTP](ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/converters/by_program/asndisc/) . Copy the right version for your platform, then uncompress the file, rename it to "asndisc", and set the permissions, as necessary for the platform.

asndisc examines all the files with a common suffix in a directory and collates all the discrepancies into an output file. The standard usage runs all of the tests, but specific tests can be enabled or disabled. In addition, expanded reports of particular tests can be generated. Running "asndisc -" provides the list of arguments and tests. We are actively updating asndisc to reflect what we see in submitted annotation. Please download the most recent version to be sure all of the latest tests are included.

This is the recommended usage for files created using tbl2asn or Sequin:

<div>asndisc -p path_to_files -x .file_suffix -o output_file -X ALL -P t</div>

<dl>

<dd>

<pre>-p    Path to Files [String] 
        -x    File Selection Substring [String] 
        -o    Single Output File [File Out]
        -X    Expand Report Categories (comma-delimited list of test names or ALL)
        -P t  Include FATAL tags in output
</pre>


For example the following commandline will run asndisc with expanded reports on all of the .sqn files in the directory named DIR and will put the output in a file named discrep:

```asndisc -p DIR/ -x .sqn -o discrep -X ALL -P t```

NOTE: this command will produce the same discrep output file as the tbl2asn commandline "tbl2asn -p path_to_fsa_files -t template -M n -Z discrep "

Examine the contents of the output file, ``discrep``: [Evaluating the output](#Evaluatingtheoutput)

### Evaluating the output

In the output file, each type of error is sorted by category and begins with the word "DiscRep". The top level reports begin with "DiscRep_ALL". These will be listed in the summary at the top of the file. Some of the reports also have subcategories that contain more descriptive information. These begin with DiscRep_SUB.

The Discrepancy Report is something of a blunt instrument that reports everything that fails its tests; it does not consider whether those failures are real problems or just a reflection of the biology. Look at the problematic features in the output file and examine those features in the .sqn files to determine whether the problems are real and need to be corrected, or can be ignored because the situation reflects the biology.

#### Fatal reports

LIST of FATAL categories in asndisc v2.0:

*   BAD_LOCUS_TAG_FORMAT
*   DISC_BACTERIA_SHOULD_NOT_HAVE_MRNA
*   DISC_CITSUBAFFIL_CONFLICT
*   DISC_INCONSISTENT_MOLTYPES
*   DISC_MAP_CHROMOSOME_CONFLICT
*   DISC_MICROSATELLITE_REPEAT_TYPE
*   DISC_MISSING_AFFIL
*   DISC_NONWGS_SETS_PRESENT
*   DISC_QUALITY_SCORES
*   DISC_RBS_WITHOUT_GENE
*   DISC_SHORT_RRNA
*   DISC_SEGSETS_PRESENT
*   DISC_SOURCE_QUALS_ASNDISC, when taxname differs
*   DISC_SUBMITBLOCK_CONFLICT
*   DISC_SUSPECT_RRNA_PRODUCTS
*   DISC_TITLE_AUTHOR_CONFLICT
*   DISC_UNPUB_PUB_WITHOUT_TITLE
*   DISC_USA_STATE
*   EC_NUMBER_ON_UNKNOWN_PROTEIN
*   INCONSISTENT_LOCUS_TAG_PREFIX
*   INCONSISTENT_PROTEIN_ID
*   MISSING_GENES
*   MISSING_LOCUS_TAGS
*   MISSING_PROTEIN_ID
*   ONCALLER_ORDERED_LOCATION
*   PARTIAL_CDS_COMPLETE_SEQUENCE
*   PSEUDO_MISMATCH
*   RNA_CDS_OVERLAP, when coding regions are completely contained in RNAs
*   RNA_NO_PRODUCT
*   SHOW_HYPOTHETICAL_CDS_HAVING_GENE_NAME
*   SUSPECT_PRODUCT_NAMES, "Remove organism from product name" category
*   SUSPECT_PRODUCT_NAMES, "Possible parsing error or incorrect formatting; remove inappropriate symbols" category
*   TEST_OVERLAPPING_RRNAS
*   DISC_BACTERIAL_PARTIAL_NONEXTENDABLE_PROBLEMS*
*   MISSING_GENOMEASSEMBLY_COMMENTS**

* Only FATAL for prokaryotes. However, the report appears with the FATAL tag when the files don't include the full taxonomy lookup (which often doesn't happen until processing here), so we've kept it as FATAL so that submitters see the error and can decide whether it's relevant for that particular submission or not.

** Only FATAL with the -P s asndisc argument (or tbl2asn -M p -Z discrep).

These three categories are suspicious but weren't marked as FATAL because the situation is sometimes valid. They will always require confirmation from the submitter that they are biologically correct. These are categories that find CDS and/or RNAs overlapping or contained within each other:

*   OVERLAPPING_CDS
*   CONTAINED_CDS
*   RNA_CDS_OVERLAP

See explanations of some [common discrepancy report categories](/~/asndisc.examples).

Here is a summary of the analysis of a submission, performed with the default settings of asndisc:

Summary

*   DISC_SOURCE_QUALS_ASNDISC:strain (all present, all same)
*   DISC_SOURCE_QUALS_ASNDISC:taxname (all present, all same)
*   DISC_FEATURE_COUNT:gene: 15712 present
*   DISC_FEATURE_COUNT:CDS: 15708 present
*   DISC_FEATURE_COUNT:mRNA: 15708 present
*   DISC_FEATURE_COUNT:misc_RNA: 1 present
*   DISC_FEATURE_COUNT:rRNA: 3 present
*   JOINED_FEATURES:14502 features have joined locations
*   DISC_COUNT_NUCLEOTIDES:209 nucleotide Bioseqs are present
*   EC_NUMBER_NOTE:2 features have EC numbers in notes or products.
*   OVERLAPPING_CDS:10 coding regions overlap another coding region with a similar or identical name.
*   FEATURE_LOCATION_CONFLICT:13007 features have inconsistent gene locations.
*   CONTAINED_CDS:3 coding regions are completely contained in another coding region.
*   SUSPECT_PRODUCT_NAMES:25 product_names contain 'suspect phrase or characters'
    *   6 product names contain 'Brackets or parenthesis [] ()'
    *   4 product names contain 'Mitochondrial'
    *   4 product names contain 'N-term'
    *   2 product names contain 'Related to'
    *   2 product names contain 'Similar to'
    *   2 product names contain 'gene'
    *   2 product names contain 'partial'
    *   2 product names contain 'similar'
    *   1 product names end with like
*   DISC_SHORT_INTRON:221 introns are shorter than 10 nt
*   NO_ANNOTATION:12 bioseqs have no features
*   TEST_UNUSUAL_MISC_RNA:1 unexpected misc_RNA features found.
*   FATAL: TEST_OVERLAPPING_RRNAS:3 rRNA features overlap another rRNA feature.
*   FATAL: SHOW_HYPOTHETICAL_CDS_HAVING_GENE_NAME:1 hypothetical coding regions have a gene name
*   DISC_QUALITY_SCORES:Quality scores are missing on all sequences.

Since this was a eukaryotic organism with introns, the "features have joined locations" is expected. Similarly, since the submitters have UTR information for some mRNAs, those mRNAs (and, therefore, their genes) will extend beyond their CDS, generating "features have inconsistent gene locations" reports. However, the other reports need to be investigated to determine whether they indicate a real problem with the annotation. For example, EC numbers need to be fielded in the EC_number qualifier, unless they are within a note about similarity to another protein. However, since that function looks for #.#.#.# in product names and notes, non-EC numbers that have that format will appear in that report. Similarly, short introns may be an indication that artificial introns were inserted to correct a frameshift, which is not biologically valid.

OVERLAPPING_CDS indicates that two CDS overlap and have similar product names, suggesting that they may represent a frameshifted gene that is annotated in two separate genes. [Since ABC-type transporter genes often overlap, they are not reported.] If these genes are not translated as two separate proteins, then they should be annotated as a single gene with a /pseudo qualifier to indicate the gene is non-functional. The product name would be entered in the gene_description and a brief note describing the problem ("frameshift") added. If the situation is unclear and you want to keep the two genes in draft annotation, then a note can be added to each CDS, "overlaps another CDS with the same product name", as a flag to database users. This note can be added automatically when the .sqn files are made, using the "-c b" argument of tbl2asn.

The discrepancy report also looks for common errors in product names. Review the names and fix those that are incorrect. Since this is a eukaryote, it is possible that some of these are nuclear genes encoding organellar proteins, so perhaps the mitochondrial reports should be ignored. In contrast, no product name should contain the word 'partial'. Keep in mind that the discrepancy report will not catch every bad product name. See the product name guidelines in the [Prokaryotic](/~/genomesubmit_annotation#CDS) and [Eukaryotic](/~/eukaryotic_genome_submission_annotation#CDS) annotation guidelines for recommended and inappropriate product name formats.

If a subset of the submission is not annotated, as in this sample (reported as "NO_ANNOTATION:12 bioseqs have no features"), please let us know when you submit. We occasionally find sequences with missing annotation caused by incorrectly formatted table headers. Therefore, we will ask you to verify that unannotated records are expected, particularly if they are large sequences.

With regards to the DISC_QUALITY_SCORES output, we encourage all submitters to provide quality scores for contig sequences, when possible, for example when all the sequencing was done by Sanger-style sequencing on an ABI machine. We realize that for NextGen sequencing technologies (eg, 454 or Illumina) the normalization of quality scores across different platforms is still being discussed, so we are not currently expecting quality scores on those submissions. In addition, scaffold objects do not contain quality scores. For more information on how to include quality scores, see the [WGS submission instructions](/~/wgs) .

After you've run the Discrepancy Report and fixed the problem annotation, let us know when you submit your genome about reports that you think can be ignored and why. If you are not certain whether a particular test is important for your genome, please ask us.

</dd>

</dl>

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