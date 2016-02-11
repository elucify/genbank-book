
## What is a Third Party Annotation:experimental (TPA:experimental) Sequence?

**TPA:experimental** A database designed to capture experimental results that support submitter-provided annotation for sequence data that the submitter did not directly determine but derived from GenBank primary data.

A TPA sequence is derived or assembled from primary sequence data currently found in the DDBJ/EMBL/GenBank databases. It can be genomic or mRNA sequence, and can be assembled or derived from primary genomic and/or mRNA sequences. TPA sequences are submitted as part of the process of publishing biological experiments that include the annotation of existing nucleotide sequences in the primary sequence database.

Published wet bench experiments are the most critical and valuable data to validate, add, or correct annotation on records in GenBank, particularly for those annotations on genome records that are largely computational results. The TPA:experimental database was established specifically to capture these experimental results in a familiar format. In addition, a publicly accessible TPA record will be linked to a publication that documents that the data are supported by biological experimentation.

## Examples of TPA:experimental

*   CDS and related annotation applied to a sequence derived from existing genomic and/or mRNA primary data with wet-lab experimental evidence for existence of all or part of the transcript. (For example, RT-PCR, Northern blot experiments)
*   CDS and related annotation applied to a sequence derived from existing genomic and/or mRNA primary data with novel sequencing and wet-lab experimental evidence for existence of all or part of the transcript. (For example, RT-PCR, Northern blot experiments)
*   CDS and related annotation applied to a sequence derived from existing genomic and/or mRNA primary data with experimental evidence for the presence of the product. (For example, antibody staining or biochemical assays.)
*   CDS and related annotation applied to a sequence derived from existing genomic and/or mRNA primary data, with novel sequencing and experimental evidence for the presence of the product. (For example antibody staining or biochemical assays.)
*   Confirmation of a new product name and/or function for a coding gene where there is no change to existing annotated exon, mRNA and CDS locations and wet-lab experimental evidence is presented.
*   Annotation of non-coding transcripts, such as antisense regulators, with wet-lab experimental evidence for their existence and/or function.
*   Annotation of repeat features in association with transposon, retrotransposon, integron, iteron, and insertion sequences with wet-lab experimental evidence.
*   Annotation of functional RNA genes, such as tRNAs, scRNAs, etc. with wet-lab experimental evidence.
*   Sequences that are part of a collection of annotated members of a gene family, where wet-lab experimental evidence exists for the annotation.

Note: It is required that all predicted annotations will be experimentally supported.

## How Do TPA:experimental Sequence Records Differ from TPA:inferential and Other GenBank/EMBL/DDBJ Records?

The display of a TPA record is similar to other Collaboration records, but includes the following:

*   Keywords: TPA;THIRD PARTY ANNOTATION; TPA:experimental.
*   The label 'TPA_exp:' at the beginning of each Definition Line.
*   PRIMARY field providing the base pair spans of the primary sequences that contribute to the TPA sequence.

Other Features and References are similar to those displayed in other GenBank/EMBL/DDBJ records.

An example of a TPA:experimental submission is [BK000016](http://www.ncbi.nlm.nih.gov/sites/entrez?cmd=Retrieve&db=nucleotide&dopt=GenBank&list_uids=20043254)

TPA sequence records are shared by all three Collaboration databases and can be found using typical search methods in EntrezNuc and EntrezProt (ie, submitter name, gene/protein name, Accession Number, etc)

## How to Submit TPA Sequence Data

Sequence can be submitted to the TPA database through either BankIt or Sequin:

*   [BankIt](http://www.ncbi.nlm.nih.gov/WebSub/?tool=genbank)
    *   Check 'No' to answer the question 'Is This Primary Sequence Data?'.
    *   Input list of Accession Numbers of all the primary sequences used to assemble or derive the submitted sequence.
    *   Provide explanation of all experimental evidence.
    *   Complete standard submission process, being sure to annotate all new descriptive information (CDS, protein name, gene name, etc) for the TPA sequence.
    *   Sequence submission will be labeled as a TPA sequence and will be processed accordingly.
*   [Sequin](http://www.ncbi.nlm.nih.gov/Sequin/)
    *   Follow standard procedure for Sequin submission.
    *   Choose Third Party Annotation from the Sequence Format window under Submission category
    *   The Assembly Tracking box will appear with the flatfile display. The primary Accession Number(s) used to assemble/derive the TPA sequence should be entered into this box.
    *   Click on Accept; new COMMENT field will appear in the flatfile, which will list the primary sequence Accession Numbers.
    *   It is recommended that the submitter note in the email that contains the sequence submission that this is intended for TPA.

## What should not be submitted as TPA:experimental

*   Sequences with annotation not supported by experimental evidence.
*   Synthetic constructs such as cloning vectors that use well characterized, publicly available genes, promoters, or terminators; these should be submitted as synthetic sequences for [GenBank](/Genbank/submit) .
*   Microsatellites and related types of repeat regions
*   New sequences that updates or changes existing sequence data from another submitter; these should be submitted as new sequences for [GenBank](/Genbank/submit) .
*   Annotation that has arisen from an automated tool, such as GeneMark, tRNA scan or ORF finder, where no further evidence, experimental or otherwise, is presented for the annotation.
*   Annotation from in vivo, in vitro, or in silico experimentation that will not be submitted for publication in a peer-reviewed journal.





<div id="shared-content-1" nid="1308">

<div class="rightnav">

## TPA Resources

*   [About TPA](/~/TPA)
*   [FAQ](/~/tpafaq)
*   [TPA-Experimental](/~/TPA-Exp)
*   [TPA-Inferential](/~/TPA-Inf)



