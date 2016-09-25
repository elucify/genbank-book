# Using Sequin to Prepare a HTG Submission

This document assumes that you are already familiar with the Sequin program. If you are not, please visit the Sequin home page at [www.ncbi.nlm.nih.gov/Sequin](//www.ncbi.nlm.nih.gov/Sequin).

## Configuring Sequin for HTG Submissions

In order to create HTG records in Sequin, you must add some information to the active Sequin configuration file, which is not the configuration file that may be included when you download Sequin. The config files in the config directory in the Sequin archive are copies that need to be moved to the right place in order to work. In Unix, the active configuration file is called .sequinrc, on the Macintosh it is called sequin.cnf, and on the PC it is called sequin.ini. To the active config file, add the lines

<pre><tt>[SETTINGS]</tt>
<tt>GENOMECENTER=genome_center_abbreviation</tt></pre>

where genome_center_abbreviation is usually your FTP login name. If there is already a section called [SETTINGS] in the configuration file, add the GENOMECENTER to the list.

For the PC, the only active config file is in the "Windows" directory. This file can have different names, such as WINNT, depending upon which version of Microsoft Windows is being used. The easiest way to find the active config file is to download the Sequin archive, extract it, run sequin.exe, choose Misc->Net Configure, click on Normal, press Accept, and then Quit Program. This should save a sequin.ini file in the correct place. You should then search for sequin.ini. Once you find the right sequin.ini file, you should edit that one.

If you are using a MAC, then the active config file is the sequin.cnf file in the "System Folder:Preferences" folder, not the one in the "Sequin Folder:config" folder. Furthermore, any config file in the "System Folder" itself will override the normal one, so you need to edit the one in "System Folder:Preferences". If there isn't a file there already, you can move the one from the "Sequin Folder:contig" folder, even if you have already edited this file.

Be sure to do the editing while Sequin isn't running so that your changes are not overwritten when you quit Sequin. When you restart Sequin, there will be a new button on the first Welcome to Sequin form called "New FA2HTGS Submission". If you have previously set up the configuration file with the GENOMETAG setting and you see this button in Sequin, there is no need to change anything.

## Creating a Sequin Submission Template File

Before you create your first HTG submission, you need to make a Sequin submission template that contains contact, citation, and organism information. You can then use this template for subsequent submissions.

To create the template, click on the "Start New Submission" button on the first Welcome to Sequin form. All of the information from the subsequent Submitting Authors form will be used for the HTG record. Fill out the Submission, Contact, Authors, and Affiliation pages carefully. Instructions are provided in the Sequin [help](http://www.ncbi.nlm.nih.gov/Sequin/sequin.hlp.html#SubmittingAuthorsForm) documentation. On the Sequence Format form, select Single sequence and FASTA format. On the next form, Organism and Sequences, the only information that will be read into the HTG record is the name of the organism. Select the scientific name on the Organism page, and import a dummy nucleotide sequence on the Nucleotide page. This sequence will not be included in any submissions, therefore, any sequence, even just one nucleotide, is sufficient. There is no need to provide any Protein information. When you reach the record viewer (the GenBank flatfile view), save the file and close the window.

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

It is possible to submit sequences containing **known length gaps** or a **mix of known and unknown length gaps**, however you must modify the fasta file to correctly format this. The fasta file should be set up to contain runs of internal N's to represent the gaps. Use a run of exactly 100 N's to represent each unknown length gap. For known length gaps use a run of N's that corresponds to the exact length of the gap. For example if you know the gaps is 16 bp long, you would insert 16 N's. Sequin will mark runs of N's great than 10 and not equal to 100 as estimated length gaps and runs of 100 N's will be represented as unknown length gaps.

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

## Formatting Ace Sequences from Phrap

You can also import sequence files in the .ace file format, which is an output of Phrap. This format is not described here.

## Creating the HTG Record

On the Welcome to Sequin form, select "New FA2HTGS Submission" if you are submitting sequences in FASTA format, and "New PHRAP Submission" if you are submitting sequences in PHRAP .ace format. On the next page, click on "Read Seq-submit template" to import the Sequin submission template file. Next, read in the FASTA or PHRAP-formatted sequence file. On the final page, enter details about the record.

*   Phase

    HTGS-0: Single-pass or a few-pass reads of a single clone. A phase 0 record, in general, does not have contigs.

    HTGS-1: A collection of unordered contigs with gaps of unknown length. A phase 1 record must at the very least have two segments with one gap.

    HTGS-2: A series of ordered contigs whose relative orientation is known. The gap lengths may or may not be known. This could even be a single sequence without gaps if the sequence has ambiguities that will be resolved.

    HTGS-3: A single contiguous sequence with no gaps. This sequence is finished, although it may or may not be annotated.

*   Draft

    Check this box if the sequence is a DRAFT-quality sequence.

*   Organism

    This field was read in from the Sequin submission template.

*   Sequence name

    The sequence must have a name that is unique within the genome center. The NCBI uses the combination of the genome center name and the sequence name to track this sequence and to talk to you about it. The name can have any form you like but must be unique within your center. The name can be the same as the clone name, but does not have to be, as the sequence name is an internal identifier that does not appear in the GenBank view in Entrez.

*   Update

    Check this box if the sequence is an update to an existing accession number, and type the number in the box. Do not check this box if you are preparing a new submission.

*   Chromosome

    The chromosome number will appear as a /chromosome qualifier in the source feature.

*   Clone

    The clone name will appear as a /clone qualifier in the source feature. This name may be the same as the sequence name.

*   Secondary Accessions

    In some cases, a large segment will supercede another group of shorter segments with different accession numbers. These shorter records are then no longer needed as independent entries in GenBank and should be made secondary. Use this spreadsheet field to list the accession numbers, one per line, which should be made secondary to the sequence in the record (the primary sequence). The NCBI will then remove the records containing those accession number(s) from GenBank, and they will no longer be part of the GenBank release. They will nonetheless be available from Entrez, as secondary accession numbers are listed in the Accession field of the GenBank flatfile after the primary accession number.

    Please take great care when using this field!!! The NCBI does not check that the sequence of the primary and secondary accession numbers overlaps. A mistake on your part will result in the wrong sequence being withdrawn from GenBank, EMBL, and DDBJ. We provide this parameter as a convenience to submitting centers, but this parameter will be removed if it is not used carefully.

*   Title

    Use this box to enter the title of the sequence for Phase 3 sequences. This text will appear in the definition line of the GenBank flatfile. If there was a title on the first line of the FASTA-formatted sequence, that title will be automatically entered into this box where it can be edited if necessary. However, it will be overwritten by the entry's source information in the case of Phase 0, 1, and 2 submissions. For these unfinished HTGs, the organism, chromosome, map, and clone information that has been entered into the correct fields, together with the phase and number of pieces, will automatically be used to generate the definition line during processing of the submission. Sample DEFINITION lines are shown in the HTG [FAQ](/~/htgs/faq).

*   Remark

    Any text entered into this box will become a Comment descriptor on the record. For Phase 1 and 2 HTGs, information about the Phase, gaps, and order of contigs will be automatically added to the Comment descriptor.

## After Using Sequin

When you are finished with the submission, deposit it on your [FTP account](/genbank/htgs/ftp) under the "SEQSUBMIT" directory. Our software will look for it there every day, validate the center and sequence_name id's, check if the record is an update, and write a report that you can pick up the next day. Further information about how HTG records are processed is available from [www.ncbi.nlm.nih.gov/HTGS/processing.html](/~/htgs/processing).





