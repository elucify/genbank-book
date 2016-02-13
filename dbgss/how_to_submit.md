# Submitting Sequences to dbGSS

Please ensure that your submissions follow these sequence quality and file formatting guidelines:

**Sequence Quality and Content:**

[1] Please submit only single-pass sequences (no next-gen sequences, raw or assembled)

[2] Remove: vector, linker, adaptor, mitochondrial, ribosomal, and contaminant sequences

[3] Use VecScreen to identify any vector, linker, or adaptors (accepts multiple sequences in fasta format)

[http://www.ncbi.nlm.nih.gov/tools/vecscreen/](http://www.ncbi.nlm.nih.gov/tools/vecscreen/)

[4] Trim terminal N's from 5' or 3' ends.  Sequences should not begin or end with N.

[5] Remove any low quality sequences.  These have high number of N's and/or long stretches of polynucleotides throughout. 

Examples of low quality sequences:

SEQUENCE:

AAAAAAAAAAAAAAAATTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCGGGGGGGGGGGGG

SEQUENCE:

CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCTCCCCCCCCCCCCTCCCCCCCCCCCCCC

SEQUENCE:

TNNCANNNNGNNNGGNNCNNANNNNNTGCNNNNNNTTNNAANNGCAANNNNTG

**File Formatting:**

[6] Please send your submission as two text files:

     plc.txt   contains publication, library, and contact files

     gss.txt   contains all GSS submissions

[7] Ensure that all GSS# are unique

[8] GSS file CITATION must exactly match Pub file TITLE

[9] GSS file LIBRARY must exactly match Lib file NAME

[10] GSS file CONT_NAME must exactly match Cont file NAME

[11] Use only standard 26 letters of the English alphabet (no accent marks, umlauts, etc.)

[12] PUT_ID field should not contain organism, hypothetical protein, unknown, or similar info

[13] The following represent the most common fields for each file:

TYPE: Pub

TITLE:

AUTHORS: Lastname,I.I.; Lastname,I.; Lastname,I.I.; etc…

YEAR:

STATUS:

||

TYPE: Lib

NAME:

ORGANISM:

DESCR:

||

TYPE: Cont

NAME:

EMAIL:

LAB:

INST:

ADDR:

||

TYPE: GSS

STATUS: New

CONT_NAME:

CITATION:

LIBRARY:

CLASS:

PUBLIC:

SEQUENCE:

||

GSSs by nature are usually submitted to GenBank and dbGSS as batches of dozens to thousands of entries, with a great deal of redundancy in the citation, submittor and library information. To improve the efficiency of the submission process for this type of data, we have designed a separate streamlined submission process and data format.

NOTE: Beginning in 2009 Sequences derived from "next generation" sequencing platforms, including Roche 454, Illumina, Applied Biosystems SOLiD, and Helicos Biosciences HeliScope, should be submitted to the [Short Read Archive (SRA)](http://www.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?) (For information contact sra@ncbi.nlm.nih.gov.)

## Data submission file types

The batch submission process for [GSS sequence data](#Submission Format for GSS Sequence Data) involves the completion of four file types:

 1.  [Publication](#Publication Files)  
 2.  [Library](#Library Files)  
 3.  [Contact](#Contact Files)  
 4.  [GSS sequence file](#GSS Files)

The format for each file is described below.

If all the GSSs share the same Publication, Library, and Contact information, you only need to prepare one of each of those files. Then complete a separate GSS file (file type d) for each sequence.

If any of the GSS files have different Publication, Library, or Contact information, you must complete a new set of file types 1-3.

Once we have entered particular Publication, Library, or Contact information into the database, you do not need to resend the data input files.

## Mailing files to dbGSS

Send the completed files to: [batch-sub@ncbi.nlm.nih.gov](mailto:batch-sub@ncbi.nlm.nih.gov)

You can attach all the files to a single email message, or you can include them in the body of the email message. Please be sure that they are in plain text (ASCII) format.

We prefer to have the individual GSS batched together as much as possible.

You can submit Publication, Library, and Contact data together in one file. You can also send them in the same file as the GSS entries - the TYPE field will differentiate them for the parsing software.

## Assignment of GenBank Accession numbers and release of data

You will receive a list of dbGSS IDs and GenBank Accession numbers from a dbGSS curator via email.

If you would like your sequences held confidential until publication, you can indicate that by putting the release date in the PUBLIC field of the GSS files. Your sequences will be released on that date, or when the Accession numbers or sequence data are published, whichever comes first.

Once your sequences are released into the public database, they will be available from the GSS division of GenBank (accessible through the [Entrez Nucleotide](http://www.ncbi.nlm.nih.gov:80/entrez/query.fcgi?db=Nucleotide) division).

## Updating your dbGSS data

Updates to GSS entries are done basically in the same way as new entries. Changes to any item in the GSS input file (other than GSS# or CONT_NAME) are made by completing an input file with new data in the fields that need to be changed. For the STATUS field, enter "Update" instead of "New".

In addition to the fields to be changed Updates need to include TYPE, STATUS, GSS#, and CONT_NAME fields.

For changes in Publication, Contact, or Source data, or for changes in GSS#'s or CONT_NAME, send an email message describing the change that is needed.

Send the update files to: [batch-sub@ncbi.nlm.nih.gov](mailto:batch-sub@ncbi.nlm.nih.gov)

## Questions and Comments

If you have questions about the GSS submission format, please contact [info@ncbi.nlm.nih.gov](mailto:info@ncbi.nlm.nih.gov)

* * *

## <a name="Submission Format for GSS Sequence Data"></a>Submission Format for GSS Sequence Data

The following is a specification for flat file formats for delivering GSS and related data to the NCBI GSS database.

*   The format consists of colon delineated capitalized field tags, followed by data.
*   The data fields should appear on the same line as the tag, with no line wrapping.  Exceptions to this are the TITLE and AUTHORS fields of the Publication file; Description (DESCR:) field of the Library file; and the CITATION, COMMENT, and SEQUENCE fields of the GSS file. In these fields, the data text begins on the same line as the tag or on the line following the field tag, and the text can cover several lines.
*   Note that some fields are obligatory.
*   The TYPE field is obligatory at the beginning of each entry, even if there are multiple entries of a given type in a file.
*   If data are not available for a non-obligatory field, the field can either be omitted entirely, or the tag may be included with an empty data field.  Please do not put "*", "-", etc. to indicate missing data.
*   Each record (including the last record in the file) should end with a double-bar tag (||) to indicate the end of the record.
*   Please also see the bulleted tips at the end of each file format for important notes about that file type.

* * *

### File Types

There are four types of deliverable files:  
1\. [Publication](#Publication Files)  
2\. [Library](#Library Files)  
3\. [Contact](#Contact Files)  
4\. [GSS sequence file](#GSS Files)

Each GSS file needs to reference the Publication, Library, and Contact data.  Therefore the Publication, Library, and Contact files must be in the database when the GSS file is entered. Once these files have been submitted and entered, they do not need to be re-submitted for additional GSS files that have the same Publication, Library, or Contact.

* * *

### 1. <a name="Publication Files"></a>Publication Files

The following is an example of the valid tags and some illustrative data:

<pre>TYPE:    Entry type - must be "Pub" for publication entries. 
         **Obligatory field**.
MEDUID:  Medline unique identifier. 
	 Not obligatory, include if you know it.
TITLE:   Title of article. 
         **Obligatory field**.
	 Begin on tag line or on line below tag, use multiple lines if needed
AUTHORS: Author name, format:  Name,I.I.; Name2,I.I.; Name3,I.I.
         **Obligatory field**.
	 Begin on tag line or on line below tag, use multiple lines if needed
JOURNAL: Journal name
VOLUME:  Volume number
SUPPL:   Supplement number
ISSUE:   Issue number
I_SUPPL: Issue supplement number
PAGES:   Page, format:   123-9
YEAR:    Year of publication.
         **Obligatory field**.
STATUS:  Status field. Use 1, 2, 3, or 4.
         1=unpublished, 2=submitted, 3=in press, 4=published
         **Obligatory field**.
||
</pre>

Examples:

<pre>TYPE: Pub
MEDUID: 92347897
TITLE: 
Genomic sequences from a subtracted retinal pigment epithelium 
library
AUTHORS: 
Gieser,L.; Swaroop,A.
JOURNAL: Genomics
VOLUME: 13
ISSUE: 2
PAGES: 873-6
YEAR:  1992
STATUS: 4
||
</pre>

*   The TYPE field is obligatory at the beginning of each entry, even if there are multiple entries of a given type in a file.
*   The MEDUID field is a MEDLINE record unique identifier. We do not normally expect you to supply this. We try to retrieve this from our relational version of MEDLINE database.
*   The STATUS field is 1=unpublished, 2=submitted, 3=in press, 4=published
*   The TITLE field is a free format string. The only requirement is that you put an identical string in the CITATION field of the GSS files, because we will be matching that field automatically against the publications in the publication table and replacing the string with the publication identity number in the GSS table.

* * *

### 2. <a name="Library Files"></a>Library Files

The following is an example of the valid tags and some illustrative data:

<pre>TYPE:      Entry type - must be "Lib" for library entries. 
           **Obligatory field**.
NAME:      Name of library. 
           **Obligatory field**.
ORGANISM:  Organism from which library prepared.
STRAIN:    Organism strain
CULTIVAR:  Plant cultivar
ISOLATE:   Individual isolate from which the sequence was obtained
SEX:       Sex of organism (female, male, hermaphrodite)
ORGAN:     Organ name 
TISSUE:    Tissue type
CELL_TYPE: Cell type
CELL_LINE: Name of cell line
STAGE:     Developmental stage
HOST:      Laboratory host
VECTOR:    Name of vector
V_TYPE:    Type of vector (Cosmid, Phage, Plasmid, YAC, other)
RE_1:      Restriction enzyme at site1 of vector
RE_2:      Restriction enzyme at site2 of vector
DESCR:     Description of library preparation methods, 
	   vector, etc. 
           This field starts on the same line or on the line below the DESCR: tag.
||
</pre>

Examples:

<pre>TYPE: Lib
NAME:  Rat Lambda Zap Express Library
ORGANISM: Rattus norvegicus
STRAIN: Sprague-Dawley
SEX: male
STAGE: embryonic day 17 post-fertilization
TISSUE: aorta
CELL_TYPE: vascular smooth muscle
DESCR: 
Put description here.
||
</pre>

*   The TYPE field is obligatory at the beginning of each entry, even if there are multiple entries of a given type in a file.
*   Try to keep the library NAME field to <= 48 characters. We can accept up to 255 characters, but it will be truncated to 48 characters in the identification line of the FASTA file created for BLAST searching.
*   When you enter the library NAME in the Library Files, please note that the identical string must be used in the LIBRARY field of the GSS files.
*   The DESCR field should contain as much detail about the library as seems appropriate.

* * *

### 3. <a name="Contact Files"></a>Contact Files

The following is an example of the valid tags and some illustrative data:

<pre>TYPE:   Entry type - must be "Cont" for contact entries. 
        **Obligatory field**.
NAME:   Name of person providing the GSS sequence 
        **Obligatory field**.
FAX:    Fax number as string of digits.
TEL:    Telephone number as string of digits.
EMAIL:  E-mail address
LAB:    Laboratory
INST:   Institution name
ADDR:   Address string
||
</pre>

Examples:

<pre>TYPE: Cont
NAME: Sikela JM
FAX: 303 270 7097
TEL: 303 270 
EMAIL: tjs@tally.hsc.colorado.edu
LAB: Department of Pharmacology
INST: University of Colorado Health Sciences Center
ADDR: Box C236, 4200 E. 9th Ave., Denver, CO 80262-0236, USA
||
</pre>

*   The TYPE field is obligatory at the beginning of each entry, even if there are multiple entries of a given type in a file.
*   None of the other fields are obligatory, but we require at least the name of a contact person.
*   We would like as many of the fields filled in as possible to provide complete information to the user for contacting a source for the GSS or further information about it.
*   The contact name field (CONT_NAME) in the GSS files must contain an identical string to the string used in the NAME field of the Contact file, for automatic matching.

* * *

### 4. <a name="GSS Files"></a>GSS Files

The following is an example of the valid tags and some illustrative data:

<pre>TYPE:          Entry type - must be "GSS" for GSS entries. 
               **Obligatory field**
STATUS:        Status of GSS entry - "New" or "Update". 
               **Obligatory field**
CONT_NAME:     Name of contact 
               Must be identical string to the contact entry
	       **Obligatory field**
CITATION:      Journal citation 
	       Must be identical string to the publication title
               Begins on line below tag.
               Use continuation lines if needed.
	       **Obligatory field**
LIBRARY:       Library name
               Must be identical string to library name entry.
	       **Obligatory field**
GSS#:          GSS name or number assigned by contact lab. For GSS entry 
               updates, this is the string we match on.
	       **Obligatory field**
GDB#:          Genome Database accession number
GDB_DSEG:      Genome Database Dsegment number
CLONE:         Clone number/name
SOURCE:        Source providing clone, e.g., ATCC
SOURCE_DNA:    Source identity number for the clone as pure DNA
SOURCE_INHOST: Source identity number for the clone stored in the host
OTHER_GSS:     Other GSSs on this clone.
DBNAME:        Database name for cross-reference to another 
	       database
DBXREF:        Database cross-reference accession
PCR_F:         Forward PCR primer sequence
PCR_B:         Backward PCR primer sequence
INSERT:        Insert length (in bases)
ERROR:         Estimated error in insert length (bases)
PLATE:         Plate number or code
ROW:           Row number or letter
COLUMN:        Column number or letter
SEQ_PRIMER:    Sequencing primer description or sequence
P_END:         Which end sequenced, e.g., 5'
HIQUAL_START:  Base position of start of high-quality sequence 
               (default = 1)
HIQUAL_STOP:   Base position of last base of high-quality 
	       sequence
DNA_TYPE:      Genomic (default), cDNA, Viral, Synthetic, Other
CLASS:         Class of sequencing method, e.g., BAC ends, 
	       YAC ends, exon-trapped
	       **Obligatory field**
PUBLIC:        Date of public release
	       Leave blank for immediate release. 
	       **Obligatory field**
               Format:   MM/DD/YYYY
PUT_ID:        Putative identification of sequence by submitter
COMMENT:       Comments about GSS. 
               Text starts on same line or on the line below COMMENT: tag.
SEQUENCE:      Sequence string. 
               Text starts on same line or on the line below SEQUENCE: tag. 
	       **Obligatory field**
||		
</pre>

Examples:

<pre>TYPE: GSS
STATUS:  New
CONT_NAME: Sikela JM
GSS#: Ayh00001
CLONE: HHC189
SOURCE: ATCC
SOURCE_INHOST: 65128
OTHER_GSS:  GSS00093, GSS000101
CITATION: 
Genomic sequences from Human 
brain tissue
SEQ_PRIMER: M13 Forward
P_END: 5'
HIQUAL_START: 1
HIQUAL_STOP: 285
DNA_TYPE: Genomic
CLASS: shotgun
LIBRARY: Hippocampus, Stratagene (cat. #936205)
PUBLIC: 
PUT_ID: Actin, gamma, skeletal
COMMENT:
SEQUENCE:
AATCAGCCTGCAAGCAAAAGATAGGAATATTCACCTACAGTGGGCACCTCCTTAAGAAGCTG
ATAGCTTGTTACACAGTAATTAGATTGAAGATAATGGACACGAAACATATTCCGGGATTAAA
CATTCTTGTCAAGAAAGGGGGAGAGAAGTCTGTTGTGCAAGTTTCAAAGAAAAAGGGTACCA
GCAAAAGTGATAATGATTTGAGGATTTCTGTCTCTAATTGGAGGATGATTCTCATGTAAGGT
GCAAAAGTGATAATGATTTGAGGATTTCTGTCTCTAATTGGAGGATGATTCTCATGTAAGGT
TGTTAGGAAATGGCAAAGTATTGATGATTGTGTGCTATGTGATTGGTGCTAGATACTTTAAC
TGAGTATACGAGTGAAATACTTGAGACTCGTGTCACTT
||
</pre>

*   The TYPE field is obligatory at the beginning of each entry, even if there are multiple entries of a given type in a file.
*   Valid data values for the GSS STATUS field are New (new entry) or Update (change existing GSS entry).
*   When updating a GSS, only the fields present in the GSS file will be changed.
*   The DNA_TYPE is assumed to be Genomic, so this field may be omitted unless the DNA type differs from this.
*   Sequences can start on the same line or on the line below the SEQUENCE field tag.

<pre>AFLP fragment
Alu-PCR
B1-PCR
BAC ends
BAC sequence gap
BAC subclone
BAC subclone end
BAC/YAC ends
CAPS
CoT 5E-3 hydroxyapatite-fractioned DNA
Concatamer T-DNA junction
DArT clone
Ds tagged
Ds/TDNA launch pad
ERIC-PCR
EcoRI fragments
Gene Trap
Genomic PCR
High-Cot
HindIII fragments
HpaII fragments
HpaII/MspI fragment
Hydroxyapatite-fractionated DNA
ISSR
Intron Spanning
Low-Cot
MboI fragments
MuTAIL-PCR
NdeI/DraI fragments
NotI site
P1 ends
PAC end
PAC nested deletions
PAC subclone
PCR fragment
PCR from cDNA
PCR product
PCR product with degenerate primers
PCR with nonspecific primers
PCR with specific primers
PCR-based subtractive hybridization
PSTI fragment
RAPD
REP-PCR
RFLP clone
RFLP probe
RLGS
Random amplified microsatellites
Random complexity-reduced genomic representation
Random sheared small inserts
SCAR
SRAP
SSR-containing BAC subclone
SSR-containing genome clone
Subtraction library
TAC ends
TAIL-PCR
TDNA tagged
Targeting vectors
Telomere Associated Sequences
U3NeoSV1-trapped
U3NeoSV2-trapped
XbaI fragments
YAC ends
cosmid ends
cosmid sequence
deletion endpoint
enhancer trap
exon-trapped
fosmid ends
internal BAC sequence
methylation filtered
microarray
microsatellite
paralogous sequence variant
partial digestion
plasmid
plasmid ends
plasmid insert
plasmid insertion site
primer walking
random plasmid subclone
repeat-enriched
representational difference analysis
sheared ends
shotgun
subtractive hybridization
transposon insertion site
transposon-tagged
viral insertion site
viral tagged
virtual transcript
</pre>

*   The CLASS field is a controlled vocabulary field. Currently (May 2009) accepted values are:

*   It is important that the strings in the following fields be completely identical:



