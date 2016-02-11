
## What is tbl2asn?

Tbl2asn is a command-line program that automates the creation of sequence records for submission to GenBank. It uses many of the same functions as Sequin but is driven generally by data files. Tbl2asn generates .sqn files for submission to GenBank. Additional manual editing is not required before submission.

Tbl2asn is available by anonymous [FTP](ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/converters/by_program/tbl2asn/). Copy the right version for your platform, then uncompress the file, rename it to "tbl2asn", and set the permissions, as necessary for the platform.

Additional details are provided in the GenBank Submission [Handbook](http://www.ncbi.nlm.nih.gov/books/NBK53709/#gbankquickstart.Submission_using_tbl2asn)

## 6 types of input data files

**REQUIRED:**

1.  [Template file](/~/tbl2asn2/#Template) containing a text ASN.1 Submit-block object (suffix .sbt).
2.  [Nucleotide sequence data](#fsa) in [FASTA](http://www.ncbi.nlm.nih.gov/Sequin/sequin.hlp.html#FASTAFormatforNucleotideSequences) format (suffix .fsa).
3.  [Feature Table](#tbl) (suffix .tbl). [Required only if including annotation]

**OPTIONAL:**

1.  [Quality Scores](#QualityScores) (suffix .qvl).
2.  Protein sequence (suffix .pep). (These are rarely needed).
3.  Source Table (suffix .src).

## Generating the .sqn file for submission

*   The minimum requirements to generate a Sequin file using tbl2asn are one .sbt file and one or more .fsa files.
*   The files are placed in a source directory and a series of command-line arguments are used to generate the .sqn files.
*   Tbl2asn will generate a .sqn for every .fsa file in the directory, plus any of the corresponding optional files that may be present. The other files must have the same file name prefix as their corresponding .fsa. (for example helicase.fsa and helicase.tbl).

Command Line Arguments

Typing "tbl2asn -" will give the full list of command line arguments. Here is a partial list of commonly used arguments:

<table border="1" cellpadding="0" cellspacing="0"><caption>tbl2asn command line arguments</caption>

<tbody>

<tr>

<td>-p</td>

<td>Path to the directory. If files are in the current directory -p. should be used.</td>

</tr>

<tr>

<td width="25">-r</td>

<td>Path for the resulting .sqn file(s) (if the -r argument is not used, the .sqn files will be saved in the source directory).</td>

</tr>

<tr>

<td>-t</td>

<td>Specifies the template file (.sbt). If the .sbt file is in a different directory the full path must be specified.</td>

</tr>

<tr>

<td>-i</td>

<td>Creates single submission from indicated .fsa file in a directory of multiple .fsa files.</td>

</tr>

<tr>

<td>-a</td>

<td>Specifies the File type.

Sample command line: -a s</td>

</tr>

<tr>

<td>-j</td>

<td>Allows the addition of [source qualifiers](http://www.ncbi.nlm.nih.gov/Sequin/modifiers.html) that will be the same for each submission. Example: -j "[organism=Saccharomyces cerevisiae] [strain=S288C]".</td>

</tr>

<tr>

<td>-V</td>

<td>

Verification (combine any of the following letters):

*   v :Validates the data records. The output is saved to files with a .val suffix. <a name="command">A summary file named errorlog.val is also created with the number, severity and type of errors found in all the .val files.</a>
*   b :Generates GenBank flatfiles with a .gbf suffix.
*   r :Validates without Country Check

Sample command line: -V vb

</td>

</tr>

<tr>

<td>-k</td>

<td>CDS Flags (combine any of the following letters):

Sample command line: -k c</td>

</tr>

<tr>

<td>-c</td>

<td>Cleanup (combine any of the following letters):

Sample command line: -c fx</td>

</tr>

<tr>

<td>-y</td>

<td>Adds a COMMENT to each submission. Example: -y "Contigs larger than 2kb have been annotated, representing approx. 87% of the total genome".</td>

</tr>

<tr>

<td>-Y</td>

<td>Like -y, but adds a COMMENT to each submission from a file.</td>

</tr>

<tr>

<td>-Z</td>

<td>Runs the Discrepancy Report. Must supply an output file name. Recommended only for annotated genome submissions, complete or WGS. See the [Discrepancy Report page](/~/asndisc) for information about its output.</td>

</tr>

<tr>

<td>-M</td>

<td>Master Genome Flags (combine any of the following letters):

Sample command line: -M n</td>

</tr>

</tbody>

</table>

**Example Command Lines:**

*   Single submission: one sequence per .fsa file
    *   Batch submission: multiple sequences per .fsa file
    *   Single submission: one .fsa file in directory of multiple .fsa files
    *   Genome submission: one or more .fsa files in a directory, with one or more sequences per .fsa file

    **Before submitting your .sqn files to GenBank,** review the .val files and correct any error-level errors. Taxonomy-related errors about missing lineages can generally be ignored. However, if there is annotation and the genetic code is not the standard code, then include the correct code in the .fsa definition line as shown in the [.fsa definition line](#fsa), or with the -j in the command line, to avoid errors.

    ## Creating the template file (.sbt)

    *   Go to [Create Submission Template](http://www.ncbi.nlm.nih.gov/WebSub/template.cgi) page
    *   Fill in the boxes
    *   Click on "Create Template"
    *   SAVE the file as template.sbt

    OR

    *   Choose start a new submission with [Sequin](http://www.ncbi.nlm.nih.gov/Sequin/).
    *   Enter manuscript title if desired.
    *   Enter contact, authors and affiliation information.
    *   Return to submission tab and use File->Export Submitter Info.
    *   Save as template.sbt.

    ## Nucleotide sequence and FASTA defline formats (.fsa)

    *   No size limit on nucleotide sequence.*   FASTA file should consist of a single definition line beginning with a '>'.*   Minimum requirements for the [FASTA defline](http://www.ncbi.nlm.nih.gov/Sequin/sequin.hlp.html#FASTAFormatforNucleotidesequences) are:

*   SeqID (sequence identifier) which is the text between the '>' and the first space.
*   Organism and related information (unless organism information is included with -j at the [command line](/Genbank/tbl2asn2#command) or in a [.src file](/Genbank/tbl2asn2#src) )

*   Optional defline information is in this [list of source modifiers](http://www.ncbi.nlm.nih.gov/Sequin/modifiers.html) and includes:

<div style="margin-left: 2em">Biological

*   strain [strain=S288C]
*   isolate [isolate=CWS1]
*   chromosome [chromosome=XVI]

</div>

<div style="margin-left: 2em">Other elements

*   topology [topology=circular]
*   location [location=mitochondrion]
*   molecule [moltype=mRNA] (DNA is the default)
*   technique [tech=wgs]
*   protein name [protein=helicase] (if using -c)
*   genetic code [gcode=4]

</div>

Here is the [list of source modifiers](http://www.ncbi.nlm.nih.gov/Sequin/modifiers.html) . See the [Tax Browser](/Taxonomy/Utils/wprintgc.cgi?mode=c) for the genetic code values.

Example FASTA:

<pre>>Sc_16 [organism=Saccharomyces cerevisiae]
tataggcgaatcgagtatattattttttctcaacatatgtat
atgaacatgagaatatatttataggaatgtataaaattgtga
cctctcctgctattttagttactgattttatgtatgtagggg
gaataggggctgcctttcttaatgcagttttaattttttctt
ttaattttttcttagtaaaattatttaaagtaaagattaatg
gaataaccattgcgcttttttttacagtttttggtttttcat
tttttggaaaaaatattttaaatattttacctttttatttag
ggggtattttatatagtatctatacttcaacagatttttctg
aacatatagttcctattgctttttcaagtgcattagcccctt
ttgtaagcagtgttgctttttatggagaaatatcctatgaaa
catcatatataaatgcaattttaattggtattttaattggtt
ttatagtggttcctttgtctaaaagtctttatgactttcatg
agggatatgatttatataatttaggttttacagcaggtt
</pre>

## Feature table format (.tbl)

Tbl2asn reads features from a five-column tab-delimited table called a [Feature table](http://www.ncbi.nlm.nih.gov/Sequin/table.html) . The feature table specifies the location and type of each feature. Tbl2asn will process the feature intervals and translate any CDSs into proteins. The first line of the table should contain the following information:

<pre>>Features SeqID table_name
</pre>

The SeqID must match the nucleotide sequence SeqID in the corresponding .fsa file. Example Feature Table:

<pre>>Feature Sc_16 Table1
69      543    gene
                        gene       sde3p
69      543    CDS
                        product SDE3P
                        protein_id     WS1030

</pre>

## Quality scores table format (.qvl)

*   Provides Phrap/Consed quality scores.
*   Has a defline with the corresponding SeqID from the .fsa file.
*   Generates Seq-graph data that will be included with the nucleotide sequence of the .fsa file in the final .sqn file.
*   The quality scores appear below the sequence in the .sqn file, and are shown in the Quality format option when the .sqn file is viewed in Sequin.

<pre>>Sc_16
51 63 70 82 82 82 90 90 90 90 86 86  
86 86 86 86 90 90 90 90 90 86 86 78...
</pre>

## Protein sequence format (.pep)

*   This file is not usually needed because GenBank generally presents on the conceptual translation of the nucleotide sequence, which will be automatically generated by tbl2asn.
*   This file will substitute the automatically translated products of the CDS features with the provided protein sequences, so is only needed in unusual cases.
*   It is FASTA file of the protein sequence, where the SeqID must match protein_id in the .tbl file

Example FASTA:

<pre>>WS1030 [gene=sde3p] [protein=SDE3P]
MYKIVTSPAILVTDFMYVGGIGAAFLNAVLIFSFNFFL
VKLFKVKINGITIAAFFTVFGFSFFGKNILNILPFYLG
GILYSIYTSTDFSEHIVPIAFSSALAPFVSSVAFYGEI
SYETSYINAILIGILIGFIVVPLSKSLYDFHEGYDLYN
LGFTAG
</pre>

## Source table format (.src)

For sets of sequences, especially those with different sources, a tab-delimited [source modifier table](http://www.ncbi.nlm.nih.gov/WebSub/html/help/genbank-source-table.html) file can be created, with a name that has a .src extension. The first column in the file must be the SeqIDs of the sequences. The first row gives the names of the source qualifiers being added, separated by tabs. Any additional rows list the SeqID and source qualifiers for each sequence in the corresponding .fsa file.

<pre>SeqID     organism     strain     isolate
Sc_16     Zea mays     A69Y       JH90.6-2x12
</pre>

## Tbl2asn Update Notification

To receive email notification about updates to tbl2asn, as well as a description of what is included in the update follow these [directions](/~/tbl2asn_announce) .

</div>

</div>