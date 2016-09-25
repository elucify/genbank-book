# What is a Third Party Annotation (TPA) Sequence?

TPA: A database designed to capture experimental or inferential results that support submitter-provided annotation for sequence data that the submitter did not directly determine but derived from GenBank primary data.

TPA records are divided into two categories:

*   [TPA:experimental:](/~/TPA-Exp) Annotation of sequence data is supported by peer-reviewed wet-lab experimental evidence.
*   [TPA:inferential:](/~/TPA-Inf) Annotation of sequence data by inference (where the source molecule or its product(s) have not been the subject of direct experimentation)

TPA database records differ from GenBank and RefSeq records:

*   [GenBank:](/~/) An archival database of [primary](#prim) nucleotide sequences that were directly sequenced by the submitter.
*   [RefSeq:](/RefSeq/) A curated, non-redundant database that includes genomic DNA, transcript (RNA), and protein products, for major organisms. The sequence data are derived from GenBank primary data, and the annotation is computational, from published literature, or from domain experts.

A TPA sequence is derived or assembled from primary sequence data currently found in the DDBJ/EMBL/GenBank International Nucleotide Sequence Database. It can be genomic or mRNA sequence and can be assembled or derived from primary genomic and/or mRNA sequences. TPA sequences are submitted to DDBJ/EMBL/GenBank as part of the process of publishing biological experiments that include the annotation of existing, primary nucleotide sequences.

Examples of TPA sequences are:

*   mRNA assembled from overlapping EST sequences.
*   mRNA derived from an unannotated section of genomic sequence by comparison with another known mRNA from a different organism.
*   mRNA assembled from overlapping EST sequences, other partial mRNAs, and/or genomic sequences.
*   previously unannotated genomic sequence now described with the exons, introns, and coding region information (CDS) of a new gene.

Note: It is required that all new annotations will be experimentally determined to exist, directly or indirectly.

## What is a primary sequence?

'Primary' sequences used to assemble a TPA sequence are those that have been experimentally determined and are now publicly available in the GenBank/EMBL/DDBJ databases. These may also be trace data sequences and Whole Genome Shotgun (WGS) sequences. They may not be from a proprietary database. Each primary sequence used to assemble a TPA sequence must be identified by an Accession Number in the submission of the TPA sequence.

[Reference sequences](/refseq/about/) may not be cited as data used to build TPA sequences since RefSeqs are not primary data. For example, sequences with Accession Numbers such as NT_112233 or NW_123456 represent contig sequences; the sequences used to assemble these contigs, which can be found at the bottom of contig records, should be cited in a TPA sequence submission. Sequences with Accession Numbers such as XM_345678 or NM_123456 are RefSeqs representing mRNAs that are not experimentally determined and therefore cannot be cited as primary data.

## How Do TPA Sequence Records Differ from Other GenBank/EMBL/DDBJ Records?

The display of a TPA sequence is similar to other Collaboration records, but includes the following:

*   Keywords: TPA;THIRD PARTY ANNOTATION; TPA:experimental TPA;THIRD PARTY ANNOTATION; TPA:inferential
*   The label 'TPA_exp: or TPA_inf:' at the beginning of each Definition Line.
*   PRIMARY field providing the base pair spans of the primary sequences that contribute to the TPA sequence.

Other Features and References are similar to those displayed in other GenBank/EMBL/DDBJ records.

An example of a TPA:experimental is [BK000016](http://www.ncbi.nlm.nih.gov/sites/entrez?cmd=Retrieve&db=nucleotide&dopt=GenBank&list_uids=20043254)

An example of a TPA:inferential is [BK000554](http://www.ncbi.nlm.nih.gov/sites/entrez?cmd=Retrieve&db=nucleotide&dopt=GenBank&list_uids=32880373)

TPA sequence records are shared by all three Collaboration databases and can be found using typical search methods in EntrezNuc and EntrezProt (ie, submitter name, gene/protein name, Accession Number, etc)

## How to Submit TPA Sequence Data

Sequence can be submitted to the TPA database through either BankIt or Sequin:

*   [BankIt](http://www.ncbi.nlm.nih.gov/WebSub/?tool=genbank)
    *   On the 'Submission type' input page, under Submission Category, choose 'Third Party Annotation'.
    *   After the 'Nucleotide' input page, you will be directed to a 'Third Party Annotation' input page.
    *   In the appropriate boxes, enter the GenBank accession number(s) of the primary sequence(s) used to assemble or derive your TPA sequence and a brief explanation of the evidence you have to support the new annotation you are presenting.
    *   Continue with the standard submission process. Be sure to add all new annotation for your TPA sequence on the 'Features' input page.
    *   The submission will be labeled as a TPA sequence and processed accordingly after it is successfully submitted.
*   [Sequin](http://www.ncbi.nlm.nih.gov/Sequin/)
    *   Follow standard procedure for Sequin submission.
    *   Choose Third Party Annotation from the Sequence Format window under Submission category
    *   The Assembly Tracking box will appear with the flatfile display. The primary Accession Number(s) used to assemble/derive the TPA sequence should be entered into this box.
    *   Click on Accept; new COMMENT field will appear in the flatfile, which will list the primary sequence Accession Numbers.
    *   It is recommended that the submitter note in the email that contains the sequence submission that this is intended for TPA.
*   General Information

    *   The entire submitted sequence must be covered by primary sequence data.
    *   There is no limit on the number of overlapping/adjoining primary sequences that can be cited for a TPA submission.
    *   If sections of a sequence submitted to TPA have been newly determined by the submitter, those sequences (if they are more than 50 nt) must first be submitted to GenBank, processed, and released to the public before they can be cited as primary sequences
    *   TPA sequences must cite the same organism as the primary sequence data.

    ## When are TPA sequences released?

    *   TPA sequences are held confidential until their Accession Numbers or sequence data and/or annotation appear in a peer-reviewed publication in a biological journal.
    *   No sequence accepted for the TPA database will be released to the public until the submitter notifies us of its publication or we determine independently that such information was published.

    ## What should not be submitted to TPA

    *   Synthetic constructs such as cloning vectors that use well characterized, publicly available genes, promoters, or terminators; these should be submitted as synthetic sequences for [GenBank](/Genbank/submit) .
    *   Microsatellites and related types of repeat regions
    *   New sequence that updates or changes existing sequence data from another submitter; these should be submitted as new sequences for [GenBank](/Genbank/submit) .
    *   Annotation that has arisen from an automated tool, such as GeneMark, tRNA scan or ORF finder, where no further evidence, experimental or otherwise, is presented for the annotation.
    *   Annotation from in vivo, in vitro, or in silico experimentation that will not be submitted for publication in a peer-reviewed journal.





