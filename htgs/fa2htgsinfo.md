
## Using fa2htgs to Prepare an HTG Submission

This document assumes that you are already familiar with the Sequin program. If you are not, please visit the Sequin home page at [www.ncbi.nlm.nih.gov/Sequin](//www.ncbi.nlm.nih.gov/Sequin).

## Setting Up fa2htgs

fa2htgs is available by anonymous FTP from [ftp://ftp.ncbi.nih.gov/fa2htgs](ftp://ftp.ncbi.nih.gov/fa2htgs).

Presently, we have built fa2htgs for the following platforms:

> alphaOSF1.tar.Z  
> linux.tar.Z  
> sgi.tar.Z  
> solaris.tar.Z  
> sun.tar.Z  
> win32/fa2htgs.exe (win95/NT)

If fa2htgs is required for a platform not present here, please [tell](mailto:info@ncbi.nlm.nih.gov) us and we will be happy to try to provide it.

fa2htgs does depend on the presence of some external configuration files. These are provided with Sequin, therefore, if a networked version of Sequin is already installed, all the default files that need to be present will be there and allow fa2htgs to run.

## Creating a Sequin Submission Template File

Before you create your first HTG submission, you need to make a Sequin submission template that contains contact, citation, and organism information. You can then use this template for subsequent submissions.

To create the template, click on the "Start New Submission" button on the first Welcome to Sequin form. All of the information from the subsequent Submitting Authors form will be used for the HTG record. Fill out the Submission, Contact, Authors, and Affiliation pages carefully. Instructions are provided in the Sequin [help](//www.ncbi.nlm.nih.gov/Sequin/sequin.hlp.html#SubmittingAuthorsForm) documentation. On the Sequence Format form, select Single sequence and FASTA format. On the next form, Organism and Sequences, the only information that will be read into the HTG record is the name of the organism. Select the scientific name on the Organism page and import a dummy nucleotide sequence on the Nucleotide page. This sequence will not be included in any submissions, therefore, any sequence, even just one nucleotide, is sufficient. There is no need to provide any Protein information. When you reach the record viewer (the GenBank flatfile view), save the file and close the window.

## Formatting Sequences in FASTA Format

Single, unsegmented sequences should be in standard FASTA format. Segmented sequences for phase 0, 1, or 2 HTGS should be in a modified FASTA format such as this:

<pre>>P74A8 pcr product joining p130c12 and p91c10
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

The first line has the Sequence Id (P74A8) and a title. Each segment is separated by

>segmentx

This line must be unique among all the lines of FASTA-formatted sequence being processed (e.g., ">segment2").

## Formatting Ace Sequences from Phrap

You can also import sequence files in the .ace file format, which is an output of Phrap. This format is not described here.

## Creating the HTG Record

Type "fa2htgs -" to see the program's command line arguments. Below, we list the arguments along with additional comments.

fa2htgs 2.0 arguments:

-i Filename for FASTA input [File In]

> default = stdin

-t Filename for Seq-submit template [File In]

> default = template.sub

-o Filename for ASN.1 output [File Out] Optional

> default = stdout  
> The convention until now has been to name the output file as clone_name.ss (e.g., P74A8.ss). "ss" is a seq-submit, or sequence submission. We then have our scripts/code report with the same file name convention. Also note that because we are working in Unix space, "case" of letter is important, and try to avoid "metacharacters" (such as ^*/\ etc.).

-e Log errors to file named: [File Out] Optional

-n Organism name? [String] Optional

> default = Homo sapiens

-s Sequence name? [String]

> The sequence must have a name that is unique within the genome center. The NCBI uses a combination of the genome center name (-g argument) and the sequence name (-s) to track this sequence and to talk to you about it. The name can have any form you like but must be unique within your center.

-l length of sequence in bp? [Integer]

> This argument should contain the putative full length of the BAC or cosmid clone. The length entered here is checked against the actual number of bases we get. For phase 1 and 2 HTGs, the length is also used to estimate gap lengths. Thus, for phase 1 and 2 records, it is important to use a number GREATER than the number of nucleotides in the FASTA file to avoid generating false "gaps". The final record should contain at least 20 to 30 "N's" between the segments to ensure proper behavior when the record is used with BLAST. If the segments are not separated, BLAST may bring together unrelated segment neighbors. You can check that these N's are present by loading the final ASN.1 into Sequin.

-g Genome Center tag? [String]

> This is probably the same as your login name on the NCBI FTP server.

-p HTGS phase? [Integer]

> default = 1  
> range from 1 to 3  
> Phase 1 - A collection of unordered contigs with gaps of unknown length. A Phase 1 record must at the very least have two segments with one gap.  
> Phase 2 - A series of ordered contigs whose relative orientation is known. Gap lengths may be known. This could be a single sequence, without gaps if the sequence has ambiguities that will be resolved.  
> Phase 3 - A single contiguous sequence. This sequence is finished, although it may or may not be annotated.

-a GenBank accession (if an update) [String] Optional

> This argument is required if this is an update. Do not use it if you are preparing a new submission.

-r Remark for update? [String] Optional

> If this is an update, you can add a brief comment (within "") describing the nature of the update ("new sequence", "new citation", "updated features").

-c Clone name? [String] Optional

> Will appear as /clone in the source feature. This could be the same as the -s argument (sequence name), but this one will appear in the /clone qualifier.

-h Chromosome? [String] Optional

> Will appear as /chromsome in the source feature.

-d Title for sequence? [String] Optional

> The text that will appear in the DEFINITION line of the GenBank flatfile for Phase 3 submissions. Deflines for Phase 0, 1, and 2 submissions are automatically generated from the organism, clone, chromosome, and phase information that is entered. Sample DEFINITION lines are shown in the HTG [FAQ](faq.html#defline).

-m Take comment from template ? [T/F] Optional

> default = F

-u Take biosource from template ? [T/F] Optional

> default = F

-x Secondary accession number, separate by commas if multiple, e.g., U10000, L11000 [String] Optional

> In some cases, a large segment will supercede another group of shorter segments with different accession numbers. These shorter records are then no longer needed as independent entries in GenBank and should be made secondary. Use this field to list the accession numbers that should be made secondary to the sequence in the record (the primary sequence). The NCBI will then remove the records containing those accession number(s) from GenBank, and they will no longer be part of the GenBank release. They will nonetheless be available from Entrez, as secondary accession numbers are listed in the Accession field of the GenBank flatfile following the primary accesion number.
> 
> Please take great care when using this field!!! The NCBI does not check that the sequence of the primary and secondary accession numbers overlaps. A mistake on your part will result in the wrong sequence being withdrawn from GenBank, EMBL, and DDBJ. We provide this parameter as a convenience to submitting centers, but this parameter will be removed if it is not used carefully.

-C Clone library name? [String] Optional

> Will appear as /clone-lib="string" on the source feature.

-M Map? [String] Optional

> Will appear as /map="string" on the source feature.

-O Filename for the comment: [File In] Optional

> Will read the comment from a given file. Maximum 100 characters per line. New lines can be incorporated with "~"; if you actually want to include the "~" in your text, you need to escape it with "`". Please ensure that the correct format is obtained by viewing your comment in Sequin.

-T Filename for Phrap input [File In] Optional

> Using this argument implies that you are NOT using the -i above.

-P Contigs to use, separate by commas if multiple [String] Optional

> If -P is not indicated with the -T option, then the fragments will go in in the order that they are in the ace file that is appropriate for a phase 1 record but not for a phase 2 or 3\. If you need to set the order of the segments of the ace file, you need to set it with the -P flag, like this:
> 
> -P "Contig1,Contig4,Contig3,Contig2,Contig5"

-D HTGS_DRAFT sequence? [T/F] Optional

> default = F

-S Strain name? [String] Optional

-b Gap length [Integer]

> default = 100
> 
> range from 0 to 1000000000, but do not use 0

-N Annotate assembly_fragments [T/F] Optional, but required when using the -6 and -7 arguments

> default = F

-6 SP6 clone (e.g., Contig1,left) [String] Optional

> Using this argument requires that you also use the -N T argument.

-7 T7 clone (e.g., Contig2,right) [String] Optional

> Using this argument requires that you also use the -N T argument.

-f htgs_fulltop keyword [T/F] Optional

> default = F

-v htgs_activefin keyword [T/F] Optional

> default = F

-L Filename for Phrap contig order [File In] Optional

> This is a tab-delimited file that can be used to drive the order of contigs (normally specified by -P), as well as indicating the SP6 and T7 ends. It can also be used when contigs are known to be in opposite orientation. For example:
> 
> <pre>Contig2     +       1       SP6     left
>   Contig3     +       1 
>   Contig1     -               T7      right
>   </pre>
> 
> The first column is the contig name, the second is the orientation, the third is the fragment group, the fourth indicates the SP6 or T7 end, and the fifth says which side of SP6 or T7 end had vector removed.

## After Using fa2htgs

It is good to load the output of fa2htgs into Sequin and validate the record. This is especially important for phase 3 records where many annotations may be present (added with the help of Sequin), or for DRAFT entries that include quality scores. Sequin has a very good built-in validation tool (look under Search -> Validate).

When you are finished with the submission, deposit it on your FTP account under the "SEQSUBMIT" directory. Our software will look for it there every day, validate the center and sequence name ids, check whether the record is an update, and write a report that you can pick up the next day. Further information about how HTG records are processed is available from [www.ncbi.nlm.nih.gov/HTGS/processing.html](processing.html).

</div>

</div>