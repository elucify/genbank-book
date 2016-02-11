<meta http-equiv="Content-Type" content="text/html; charset=utf-8">  <meta name="node-id" content="3349"> <meta name="revision-id" content="18516"> <meta name="cms-base-url" content="http://cms.ncbi.nlm.nih.gov"> <meta name="cms-view-url" content="http://cms.ncbi.nlm.nih.gov/genbank/wgs_gapped"> <meta name="cms-edit-url" content="http://cms.ncbi.nlm.nih.gov/node/3349/edit"> <meta name="created" content="2014-01-01T13:48:26-05:00"> <meta name="modified" content="2014-01-02T14:28:10-05:00"> <meta name="publication-date" content="2014-01-01T12:39:00-05:00"> <meta name="author" content="kclark"> <meta name="subsite" content="genbank"> <meta name="path" content="genbank/wgs_gapped"> <meta name="node-type" content="page"> <meta name="jira-ticket" content=""> <meta name="cms-tags" content="">  <meta name="" content=""> <title>Gapped Genome Submission</title>

<div class="node clear-block">

<div class="content">

# Gapped Format for Genome Submissions

If your contig sequences include runs of N's that represent gaps, you will need to include assembly_gap features with the appropriate linkage evidence.  If the sequences meet certain requirements, then you can generate a gapped submission with tbl2asn (v 22.9 or higher, available from [FTP](ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/converters/by_program/tbl2asn/)) using the arguments -l (to add linkage evidence) and -a (to add assembly_gaps), as described below.  If you have multiple linkage types in a single sequence or if any of the gaps are between scaffolds, please [contact us](mailto:genomes@ncbi.nlm.nih.gov) for additional instructions, as these simple instructions are not sufficient for those more complex cases.

## Requirements

*   Each record must represent a sequence that occurs biologically in the organism. Do NOT manually use N's to randomly combine the contigs to create a single sequence; you must know the order and orientation of the contigs. 
*   Do not include any artificial sequences, such as linkers with multiple stop codons in the submitted genome.
*   Do not add assembly_gaps for Ns that represent ambiguous base calls, so you may need to check the parameters of the assembler that was used to determine what the N's represent. To convert the runs of Ns to assembly_gaps, you need to know:
    *   the linkage evidence for each gap
    *   the minimum number of N's in a row (ie 'run of Ns') that represents a gap
    *   if any runs of Ns represent gaps of unknown size
    *   if the sequences also include N's that are ambiguous base calls, then what is the length of the longest run of ambiguous bases. To use these simple instructions, the maximum number of Ns in a row that are ambiguous bases must be less than the minimum number of N's in a row that represents a gap. 
*   For these simple instructions, all the gaps must be within scaffolds and have the same linkage evidence; gaps of unknown size must be represented by 100 Ns; and all runs of "ambiguous base Ns" must be shorter than any run of Ns that  represents a gap. More complex cases such as those will require more detailed instructions, so [contact us](mailto:genomes@ncbi.nlm.nih.gov) if the genome assembly is more complicated.

## Gap Details

There are two types of gap lengths:

*   Estimated length: The approximate gap size is known.  This is also used if the gap is known to be small  (e. g. gap could be between 10-50 N's).
*   Unknown length:  The gap size is not known (e.g. gap could be 50 or 50000 N's) but the order and orientation of the contigs are known.  We suggest using 100 N's to represent gaps of unknown length rather than a  random number because it will allow you to add assembly_gap features using tbl2asn.

Use the -l argument (lowercase 'l' as in 'linkage') followed by the type of evidence used to assert linkage across the gaps.  These are the available options (they correspond to the options for column 9 of an [AGP file](http://www.ncbi.nlm.nih.gov/projects/genome/assembly/agp/AGP_Specification.shtml)):

*   paired-ends (ie, for paired ends or mate pairs)
*   align-genus
*   align-xgenus
*   align-trnscpt (ie, the evidence is a transcript)
*   within-clone
*   clone-contig
*   map
*   strobe (ie, from PacBio)

Use the argument -a followed by r#k or r#u to define how to interpret the runs of Ns in the sequences.

*   r# indicates the size of the minimum run of Ns to convert to a gap
*   k/u indicates whether all the gaps are of estimated length (=k) or if runs of 100 Ns represent gaps of unknown length (=u)

## Common Cases

1.  [All the gaps are of estimated lengths](#all_estimated)
2.  [ALL of the gaps are 100bp and are of unknown length](#all_unknown)
3.  [There are both estimated length and unknown length gaps](#both)
4.  [Complex cases](#complex)

### 1\. All the gaps are of estimated lengths, use -a r#k

The # indicates the size of the minimum run of N's to convert to an estimated length gap. For example, if all of the gaps are estimated length (there are no unknown length gaps) and runs of 5 or more N's are estimated gaps and shorter runs of N's are ambiguous bases, then use -a r5k.  Similarly, if every N represents an estimated length gap, use -a r1k. 

Example: Every run of 5 or more Ns represents a gap of estimated length, and the linkage evidence is paired-ends:

*   tbl2asn -p path_to_fsa_files -t template -M n  -Z discrep -a r5k -l paired-ends

Note that you should only include an assembly_gap for runs of N's that represent gaps.  Do not add assembly_gaps for single or short runs of N's that represent ambiguous bases. You will need to check your assembly parameters to determine what the N's represent.

### 2\. ALL of the gaps are 100bp and are of unknown length, use -a r100u

Note that all of the unknown length gaps must be 100 N's. An assembly_gap will be added for every run of 100 N's.  All other N's will be ignored.  Please contact us for additional instructions if there are unknown length gaps of other sizes.

Example: all gaps are 100 Ns and are of unknown length, and the linkage evidence is by alignment to another genome of the same genus:

*   tbl2asn -p path_to_fsa_files -t template -M n  -Z discrep -a r100u -l align-genus

Note that you must know the order and orientation of the contigs.  You cannot randomly link contigs using unknown (or known) length gaps.  If you do not have linkage evidence, submit the sequences as individual contigs.

### 3\. There are both estimated length and unknown length gaps, use -a r#u. 

Note that all of the unknown length gaps must be 100 N's.  The # indicates the size of the minimum number of N's to convert to an estimated length gap. If some run's of 100 N's are unknown length and others are estimated length, please contact us for more information.

Example: if runs of 10 or more N's are estimated gaps, and shorter runs of N's are just ambiguous bases, and all runs of exactly 100 N's are unknown gaps, and the linkage evidence is paired-ends:

*   tbl2asn -p path_to_fsa_files -t template -M n  -Z discrep -a r10u -l paired-ends

### 4\. Complex cases

There may be complex assemblies that cannot be appropriately represented by the above examples, eg the sequences are chromosomes and some of the gaps are between scaffolds, or there are different kinds of linkage evidences for the gaps within a sequence, or some runs of Ns of particular lengths within a sequence represent gaps but others of those lengths are ambiguous base calls. In these cases, please [contact us](mailto:genomes@ncbi.nlm.nih.gov) for additional instructions.

## Annotation FYI

Annotation is not required.  However, if you would like to annotate the gapped sequences, you need to be careful about crossing gaps. 

A CDS may not cross the gap if the gap size is unknown.  Instead, you could have two partial CDS features (and mRNAs in eukaryoties) that abut the gap, with a single gene over the whole locus.  Alternatively, one of the partial CDS/mRNA features may be deleted if it is very short and there is little or no supporting evidence.  If you have a single gene and two partial CDS/mRNA features, you should: (1) add a note to each CDS referencing the other half of the gene, (2) add a note to the gene and CDS features stating, "gap found within coding sequence."

A CDS can cross the gap if the gap size is estimated; however, a CDS (or mRNA) should not cross a gap such that over 50% of the translation is X (ie, in the gap).  This situation will generate an error.  Again, the CDS/mRNA should either be partial up to the gap or split into two partial CDS/mRNA features on either side of the gap, depending upon your confidence in the translation on each side of the gap. 

In addition, no feature should begin or end inside a gap.  Instead, the feature should abut the gap and be partial.

For more information about splitting CDS features, see either the [eukaryotic annotation guidelines](/~/eukaryotic_genome_submission_annotation#Splitgenesontwocontigs) or the [prokaryotic annotation guidelines](/~/genomesubmit_annotation#Split_genes).

## tbl2asn arguments:

  -p    Path to Files [String]  Optional

  -t    Template File [File In]  Optional

  -M n  Genome Flags Normal

  -Z    Discrepancy Report Output File [File Out]  Optional see [http://www.ncbi.nlm.nih.gov/Genbank/asndisc.html](http://www.ncbi.nlm.nih.gov/Genbank/asndisc.html)

  -l  (lowercase 'l', as in 'linkage') Add type of evidence used to assert linkage across assembly_gaps. Must be one of the following:

      paired-ends

      align-genus

      align-xgenus

      align-trnscpt

      within-clone

      clone-contig

      map

      strobe

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