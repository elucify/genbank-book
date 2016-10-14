# Using tbl2asn to Prepare an HTG Submission

This document assumes that you are already familiar with the Sequin program. If you are not, please visit the Sequin home page at [www.ncbi.nlm.nih.gov/Sequin](//www.ncbi.nlm.nih.gov/Sequin).

## Setting Up tbl2asn

Basic information about the commandline program tbl2asn is described on the [tbl2asn](/~/tbl2asn2) home page. tbl2asn is available by anonymous FTP from [ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/converters/by_program/tbl2asn/](ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/converters/by_program/tbl2asn/).

Copy the right version for your platform, then uncompress the file, rename it to "tbl2asn", and set the permissions (as necessary for the platform)

## Creating a Sequin Submission Template File

Before you create your first HTG submission, you need to make a Sequin submission template that contains contact and citation information. You can then use this template for subsequent submissions.

To create the template, follow the instructions on the [tbl2asn](/~/tbl2asn2#Template) page:

*   Go to [Create Submission Template](//www.ncbi.nlm.nih.gov/WebSub/template.cgi) page
*   Fill in the boxes
*   Click on "Create Template"
*   SAVE the file as template.sbt

OR

*   Choose start a new submission with [Sequin](/~/htgs/sequininfo)
*   Enter manuscript title if desired.
*   Enter contact, authors and affiliation information.
*   Return to submission tab and use File->Export Submitter Info.
*   Save as template.sbt.

## Formatting Sequences in FASTA Format

Single, unsegmented (i.e. no gaps) sequences should be in standard FASTA format. Segmented sequences containing **unknown length** gaps for phase 0, 1, or 2 HTGS should be in a modified FASTA format such as this:

<pre>>P74A8 [chromosome=2] [clone=ABC12345]
gatcagcccaaagcattgattaggggaacttacctgtagagggctgcagcaatggggaac
acctggctgggtcacagagtggtcaatgcactccatgacttttgggtcaggacacagaaa
gaaagagcggggaaccggggggccctacagtgatgaattatactaactgattttagaatg
>segment2
ttaaacaaacattgcatttccagaataaaccccatttagtaacgcatagtgtgcttgtat
ctcagcctcccaaagtgctgggattatagacatgagccagcgcacctggctttgttagcc
>segment3
ttttcaaataactttttgaactttgttaattttttaattgcacgttttctccttcattta
ctaattccattcaaaagtagcatcaatgagaataaattacttaggaatacatttaattaa
aaagtgctagacttgtacactgaaaattacaaagtactctggagatatattc</pre>

The first line has the Sequence Id (=SeqID or sequence name), P74A8, and source information. Each segment is separated by-

>segmentx

This line must be unique among all the lines of FASTA-formatted sequence being processed (e.g., ">segment2", ">segment3", etc).

The basic tbl2asn command for unknown length gaps is:

tbl2asn -a di -i gap.fa -t template.sbt -C center_name -j "[tech=htgs2] [organism=Triticum aestivum] [cultivar=Chinese Spring]" -Y comment_file -o output_file.ss 

It is possible to submit sequences containing **known length gaps** or a **mix of known and unknown length gaps**, however you must modify the fasta file and the tbl2asn command to correctly format this. The fasta file should be set up to contain runs of internal N's to represent the gaps. Use a run of exactly 100 N's to represent each unknown length gap. For known length gaps use a run of N's that corresponds to the exact length of the gap. For example if you know the gaps is 16 bp long, you would insert 16 N's. The tbl2asn tool will mark runs of N's great than 10 and not equal to 100 as estimated length gaps and runs of 100 N's will be represented as unknown length gaps.

<pre>>P74A8 [chromosome=2] [clone=ABC12345]
gatcagcccaaagcattgattaggggaacttacctgtagagggctgcagcaatggggaac
acctggctgggtcacagagtggtcaatgcactccatgacttttgggtcaggacacagaaa
gaaagagcggggaaccggggggccctacagtgatgaattatactaactgattttagaatg
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnttaaacaaacattgcatttc
cagaataaaccccatttagtaacgcatagtgtgcttgtatctcagcctcccaaagtgctgg
gattatagacatgagccagcgcacctggctttgttagccnnnnnnnnnnnnnnnnttttca
aataactttttgaactttgttaattttttaattgcacgttttctccttcatttactaattc
cattcaaaagtagcatcaatgagaataaattacttaggaatacatttaattaaaaagtgct
gacttgtacactgaaaattacaaagtactctggagatatattc</pre>

The tbl2asn command line for this is modified such that -a di is now -a r10u. For example

tbl2asn -a r10u -i gap.fa -t template.sbt -C center_name -j "[tech=htgs2] [organism=Triticum aestivum] [cultivar=Chinese Spring]" -Y comment_file -o output_file.ss

see below for more details on tbl2asn

## Formatting Quality Scores in FASTA Format

Because the information is useful to database users, please include the quality scores of unfinished (phase 0, 1 or 2) HTG records in the submission. If you are using .fsa files to include the sequences, then tbl2asn will include the associated CONSED/PHRAP quality scores in the output file if they are in a file named and formatted as described on the [tbl2asn](/~/tbl2asn2#QualityScores) page. The instructions are:

Put the scores in a .qvl file whose basename matches the fasta (.fsa) file's basename, and whose definition line has the same identifier (SeqID) as the corresponding .fsa file. Put this file in the same directory as the .fsa file.

To account for gaps of unknown size (the default), include 100 zeroes between the contigs' scores.

## Formatting Ace Sequences from Phrap

Alternatively, you can import sequence and quality scores in the .ace file format, which is an output of Phrap. This format is not described here.

## Including Source Information

The source information must be included in the FASTA file definition line and/or the tbl2asn commandline. All of the source information, including the HTG phase, can be included in the FASTA file definition line. Alternatively, common information such as the organism name can be included in the commandline, and only unique information included in the FASTA file definition line, if desired. If the same qualifiers are present both places, the information in the FASTA definition line will be used. The source qualifiers are described on the [tbl2asn](/~/tbl2asn2#fsa) page.

The HTG phase is included as:

*   [tech=htgs 0]
*   [tech=htgs 1]
*   [tech=htgs 2]
*   [tech=htgs 3]

Keywords, such as HTGS_DRAFT, are included as:

*   [keyword=HTGS_DRAFT]

## Creating the HTG Record

A basic commandline for a new phase 2 submission with unknown length gaps is:

*   tbl2asn -a di -i gap.fsa -t template.sbt -C center_name -j "[tech=htgs 2] [organism=Solanum lycopersicum] [cultivar=Heinz 1706]" -Y comment_file -o gap.ss

A commandline for an update must include the accession number:

*   tbl2asn -a di -i gap.fsa -t template.sbt -C center_name -A accession_number -j "[tech=htgs 2] [organism=Solanum lycopersicum] [cultivar=Heinz 1706]" -Y comment_file -o gap.ss

In both cases the chromosome and clone names would be included in the definition line of the .fsa file.

Type "tbl2asn -" to see the program's command line arguments. Note that several command line arguments were changed in version 10.0 of tbl2asn, to make it more flexible and expandable. Below, we list some arguments along with additional comments.

tbl2asn 10.1 arguments:

**-i** Filename for .fsa FASTA input [File In]

**-t** Filename for Seq-submit template [File In]

**-p** Path to Files [String] Optional

> To run tbl2asn on all the files with a common suffix in a directory.

**-x** Suffix [String] Optional

> default = .fsa

**-o** Filename for ASN.1 output [File Out] Optional

> default = basename.sqn  
> The convention until now has been to name the output file as clone_name.ss (e.g., P74A8.ss), but using tbl2asn's default name is fine. Our scripts/code report with the same file name convention used in the submission. Note that because we are working in Unix space, "case" of letter is important. Also avoid "meta-characters" (such as ^*/\ etc.).

**-C** Genome Center tag [String]

> This is the same as the login name on the NCBI FTP server.

**-j** Source Qualifiers [String] Optional

> Include multiple qualifiers between double quotes. The source qualifiers can be included in the FASTA definition line instead of or in addition to using -j. If the same qualifier is in the FASTA definition line and the -j argument, tbl2asn will use the information in the FASTA file.

**-n** Organism name [String] Optional

> This can be included in the FASTA definition line or with the -j argument instead.

**-Y** Filename for the comment: [File In] Optional

> Will read the comment from a given file. Maximum 100 characters per line. New lines can be incorporated with "~"; if you actually want to include the "~" in your text, you need to escape it with "`". Please ensure that the correct format is obtained by viewing your comment in Sequin.

**-y** Comment [String] Optional

> Will read a short comment from the commandline.

**-V** Verification (combine any of the following letters) Optional

> **v** Validate. Will generate a file basename.val for each record. This is especially important for phase 3 records where many annotations may be added, as described on the [tbl2asn](//www.ncbi.nlm.nih.gov/Genbank/tbl2asn2.html#tbl) page, or for DRAFT entries that include quality scores. Taxonomy-related errors can generally be ignored.

> **b** Will generate GenBank flatfile.

**-a** Specifies the File type.

> **di** Will read FASTA file as delta sequences, with implicit gaps (=unknown size represented by 100 Ns) between contigs. Use this argument when the input is a FASTA file.
> 
> **r10u** Will read FASTA file as a delta sequence containing a mix of known and unknown length gaps (unknown size represented by 100 Ns, known size represented by runs of Ns corresponding to the actual gap size) between contigs. Use this argument when the input is a FASTA file.

> **e** Filename for Phrap/ACE input. Using this argument implies that you are NOT using the -i above.

**-A** Accession [String] Optional

## After Using tbl2asn

When you are finished with the submission, deposit it on your [FTP account](/~/htgs/ftp) under the "SEQSUBMIT" directory. Our software will look for it there every day, validate the center and sequence name ids, check whether the record is an update, and write a report that you can pick up the next day. Further information about how HTG records are processed is available from [www.ncbi.nlm.nih.gov/HTGS/processing.html](/~/htgs/processing) .





<div id="shared-content-1" nid="1331">

<div class="rightnav">

## HTGs Resources

*   [About HTGs](/~/htgs)
*   [Submitting HTGs](/~/htgs/subinfo)
*   [Processing HTGs](/~/htgs/processing)
*   [](/~/htgs/processing)[HTGs FAQ](/~/htgs/faq)



