# Submitting sequences to dbEST

Please ensure that your submissions follow these sequence quality and file formatting guidelines:


## Sequence Quality and Content

1. Please submit only single-pass sequences (no next-gen sequences, raw or assembled)

2. Remove: vector, linker, adaptor, mitochondrial, ribosomal, and contaminant sequences

3. Use VecScreen ([http://www.ncbi.nlm.nih.gov/tools/vecscreen/](http://www.ncbi.nlm.nih.gov/tools/vecscreen/)) to identify any vector, linker, or adaptors (accepts multiple sequences in fasta format)

5. . Trim terminal N's from 5' or 3' ends.  Sequences should not begin or end with N.

5. Remove any low quality sequences.  These have high number of N's and/or long stretches of polynucleotides throughout. 

### Examples of low quality sequences

SEQUENCE:
```
AAAAAAAAAAAAAAAAAAAAACCCCCCCCCCCCCCCCCCCCCCTTTTTTGGGGGG
```
SEQUENCE:
```
TNNCANNNNGNNNGGNNCNNANNNNNTGCNNNNNNTTNNAANNGCAANNNNTG
```

## File Formatting

1. Please send your submission as two text files:

     plc.txt   contains publication, library, and contact files

     est.txt   contains all EST submissions

2. Ensure that all EST# are unique

8. EST file CITATION must exactly match Pub file TITLE

9. EST file LIBRARY must exactly match Lib file NAME

10. EST file CONT_NAME must exactly match Cont file NAME

11. PUT_ID field should not contain organism, hypothetical protein, unknown, or similar information

12. Use only standard 26 letters of the English alphabet (no accent marks, umlauts, etc.)

13. The following represents the basic structure for each file:

```
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

TYPE: EST

STATUS: New

CONT_NAME:

CITATION:

LIBRARY:

PUBLIC:

SEQUENCE:

||
```

## Data submission file types

The batch submission process for [EST sequence data](#SubmissionFormatforESTSequenceData) involves the completion of four file types:

a. [Publication](#PublicationFiles)  
b. [Library](#LibraryFiles)  
c. [Contact](#ContactFiles)  
d. [EST](#ESTFiles)

The format for each file is described below.

If all the ESTs share the same Publication, Library, and Contact
information, you only need to prepare one of each of those files.
Then complete a separate EST file (file type d) for each sequence.

If any of the EST files have different Publication, Library, or Contact information, you must complete a new file of type a, b, or c.

Once we have entered particular Publication, Library, or Contact information into the database, you do not need to resend the data input files.

### Mailing files to dbEST

Send the completed files to: [batch-sub@ncbi.nlm.nih.gov](mailto:batch-sub@ncbi.nlm.nih.gov)

You can attach all the files to a single email message, or you can include them in the body of the email message. Please be sure that they are in plain text (ASCII) format.

We prefer to have the individual EST data files batched together as much as possible.

You can submit library, publication, and contact data together in one file. You can also send them in the same file as the EST entries - the TYPE field will differentiate them for the parsing software.

### Assignment of GenBank Accession Numbers and release of data

You will receive a list of dbEST IDs and GenBank accession numbers from a dbEST curator via email.

If you would like your sequences held confidential until publication, you can indicate that by putting the release date in the PUBLIC field of the EST files. Your sequences will be released on that date, or when the accession numbers or sequence data are published, whichever comes first.

Once your sequences are released into the public database, they will be available from GenBank, accessible through [Entrez Nucleotides](http://www.ncbi.nlm.nih.gov/sites/entrez?db=nucleotide).

### Updating your dbEST data

Updates to EST entries are done basically in the same way as new entries. Changes to any item in the EST input file (other than EST# or CONT_NAME) are made by completing an input file with new data in the fields that need to be changed. For the STATUS field enter "Update" instead of "New".

In addition to the fields to be changed Updates need to include TYPE, STATUS, EST#, and CONT_NAME fields.

For changes in Publication, Contact, or Source data, or for changes in EST#'s or CONT_NAME, send an email message describing the change that is needed.

Send the update files to: [batch-sub@ncbi.nlm.nih.gov](mailto:batch-sub@ncbi.nlm.nih.gov)

### Questions and Comments

If you have questions about the EST submission format, please contact [info@ncbi.nlm.nih.gov](mailto:info@ncbi.nlm.nih.gov).  

## Submission Format for EST Sequence Data

The following is a specification for flat file formats for delivering EST and related data to the NCBI EST database.

*   The format consists of colon delineated capitalized field tags, followed by data.
*   The data fields should appear on the same line as the tag, with no line wrapping. Exceptions to this are the TITLE and AUTHORS fields of the Publication file; Description (DESCR:) field of the Library file; and the CITATION, COMMENT, and SEQUENCE fields of the EST file. In these fields, the data may begin on the same line as the field tag or on the line following the tag and the lines can be wrapped.
*   Note that some fields are obligatory.
*   The TYPE field is obligatory at the beginning of each entry, even if there are multiple entries of a given type in a file.
*   If data is not available for a non-obligatory field, the field can either be omitted entirely, or the tag may be included with an empty data field. Please do not put `*`, `-`, etc., to indicate missing data.
*   Each record (including the last record in the file) should end with a double-bar tag (||) to indicate the end of the record.
*   Please also see the bulletted tips at the end of each file format for important notes about that file type.

* * *

### File Types

There are four types of deliverable files:  
a. [Publication](#PublicationFiles)  
b. [Library](#LibraryFiles)  
c. [Contact](#ContactFiles)  
d. [EST](#ESTFiles)

Each EST file needs to reference the Publication, Library, and Contact data.  Therefore the Publication, Library, and Contact files must be in the database when the EST file is entered. Once these files have been submitted and entered, they do not need to be re-submitted for additional EST files that have the same Publication, Library, or Contact.

* * *

### Publication Files

These are the valid tags and a short description:

```
TYPE:      Entry type - must be "Pub" for publication entries. 
           **Obligatory field**
MEDUID:    Medline unique identifier. 
           Not obligatory, include if you know it.
TITLE:     Title of article. (Begin on same line or the line below tag, 
           use multiple lines if necessary)
           **Obligatory field**
AUTHORS:   Author name, format:  Name,I.I.; Name2,I.I.; 
           Name3,I.I.
           (Begin on the same line or the line below tag, use multiple lines if necessary)
           **Obligatory field**
JOURNAL:   Journal name
VOLUME:    Volume number
SUPPL:     Supplement number
ISSUE:     Issue number
I_SUPPL:   Issue supplement number
PAGES:     Page, format:   123-9
YEAR:      Year of publication.
           **Obligatory field**
STATUS:    Publication status.
           1=unpublished, 2=submitted, 3=in press, 4=published
           **Obligatory field**
||
```

#### Examples

```
TYPE: Pub
MEDUID: 92347897
TITLE: 
Expressed sequence tags and chromosomal localization of 
cDNA clones from a subtracted retinal pigment epithelium library
AUTHORS: 
Gieser,L.; Swaroop,A.
JOURNAL: Genomics
VOLUME: 13
ISSUE: 2
PAGES: 873-6
YEAR: 1992
STATUS: 4
||
```

Pub data template with required and most often used fields:

```
TYPE:      Pub
TITLE:     
title
AUTHORS:   
authors
JOURNAL: 
VOLUME: 
ISSUE:
PAGES: 
YEAR: 
STATUS:    
||
```

*   The TYPE field is obligatory at the beginning of each entry, even if there are multiple entries of a given type in a file.
*   The MEDUID field is a MEDLINE record unique identifier. We do not normally expect you to supply this - we try to retrieve this from our relational version of MEDLINE database.
*   For the Publication STATUS field the values are 1=unpublished, 2=submitted, 3=in press, 4=published
*   The TITLE field is a free format string. The only requirement is that you put an identical string in the CITATION field of the EST files. We match the CITATION in the EST input file automatically against the TITLE for publications in the publication table in order to associate the correct publication with the EST.

* * *

### b. <a name="LibraryFiles"></a>Library Files

These are the valid tags and a short description:

```
TYPE:       Entry type - must be "Lib" for library entries.
            **Obligatory field**
NAME:       Name of library.
            **Obligatory field**
ORGANISM:   Organism from which library prepared.
            Scientific name.
            **Obligatory field**
STRAIN:     Organism strain
CULTIVAR:   Plant cultivar
ISOLATE:    Individual isolate from which the sequence was obtained
SEX:        Sex of organism (female, male, hermaphrodite)
ORGAN:      Organ name 
TISSUE:     Tissue type
CELL_TYPE:  Cell type
CELL_LINE:  Name of cell line
STAGE:      Developmental stage
HOST:       Laboratory host
VECTOR:     Name of vector.
V_TYPE:     Type of vector (Cosmid, Phage,Plasmid,YAC, other)
RE_1:       Restriction enzyme at site1 of vector
RE_2:       Restriction enzyme at site2 of vector
DESCR:      Description of library preparation methods, vector, 
            etc. 
            Text starts on the same line or the line below the DESCR: tag.
||
```

#### Examples

```
TYPE: Lib
NAME:  Rat embryonic day 17 post-fertilization Library
ORGANISM: Rattus norvegicus
STRAIN: Sprague-Dawley
SEX: male
STAGE: embryonic day 17 post-fertilization
TISSUE: aorta
CELL_TYPE: vascular smooth muscle
DESCR: 
||
```

Lib data template with required and most often used fields:

```
TYPE:       Lib
NAME:       
ORGANISM:  
STRAIN:   
CULTIVAR: 
SEX:      
ORGAN:   
TISSUE: 
CELL_TYPE: 
CELL_LINE:
STAGE:   
HOST:   
VECTOR:
V_TYPE:  
RE_1:    
RE_2:   
DESCR:      
description
||
```

*   The TYPE field is obligatory at the beginning of each entry, even if there are multiple entries of a given type in a file.
*   Try to keep the library NAME field to <= 48 characters. We can accept up to 128 characters, but it will be truncated to 48 characters in the identification line of the FASTA file created for BLAST searching.
*   When you enter the library NAME in the Library Files, please note that the identical string must be used in in the LIBRARY field of the EST Files.
*   The purpose of the Library file is to describe the source of the sequence. The most important item is the ORGANISM name. A library NAME is required to link the source information to the individual ESTs. The term 'Library' does not mean that this information strictly applies only to cDNA libraries.
*   The DESCR field should contain as much detail about the derivation of the mRNA/cDNA as seems appropriate.

* * *

### c. <a name="ContactFiles"></a>Contact Files

These are the valid tags and a short description:

```
TYPE:     Entry type - must be "Cont" for contact entries.
          **Obligatory field**
NAME:     Name of person submitting the EST. 
          **Obligatory field**
FAX:      Fax number as string of digits.
TEL:      Telephone number as string of digits.
EMAIL:    E-mail address
LAB:      Laboratory providing EST.
INST:     Institution name
ADDR:     Address string, comma delineation.
||
```

#### Examples

```
TYPE: Cont
NAME: Sikela JM
FAX: 303 270 7097
TEL: 303 270 
EMAIL: tjs@tally.hsc.colorado.edu
LAB: Department of Pharmacology
INST: University of Colorado Health Sciences Center
ADDR: Box C236, 4200 E. 9th Ave., Denver, CO 80262-0236, USA
||
```

Contact data template with required and most often used fields:

```
TYPE: Cont
NAME: 
FAX: 
TEL:
EMAIL: 
LAB: 
INST: 
ADDR: 
||
```

*   The TYPE field is obligatory at the beginning of each entry, even if there are multiple entries of a given type in a file.
*   None of the other fields are obligatory, but we require at least the name of a contact person.
*   We would like as many of the fields filled in as possible, to provide complete information to the user for contacting a source for the EST or further information about it.
*   The contact name field (CONT_NAME) in the EST files must contain an identical string to the string used in the NAME field of the Contact file, for automatic matching.

### d. <a name="ESTFiles"></a>EST Files

These are the valid tags and a short description:

```
TYPE:      Entry type - must be "EST" for EST entries.
           **Obligatory field**
STATUS:    Status of EST entry - "New" or "Update".
           **Obligatory field**
CONT_NAME: Name of contact 
           (must be identical string to the contact entry)
           **Obligatory field**
CITATION:  Journal citation. 
           (Must be identical string to the publication title)
           Begins on the same line or the line below tag - use continuation lines 
           if necessary.
           **Obligatory field**
LIBRARY:   Library name.  
           (Must be identical string to library name entry.)
           **Obligatory field**
EST#:      EST id assigned by contact lab.
           For EST updates, this is the string we match on.
           Length limit: 64 characters.
           **Obligatory field**
GB#:       GenBank accession number
GDB#:      Genome database accession number
GDB_DSEG:  Genome database Dsegment number
CLONE:     Clone id.
SOURCE:    Source providing clone e.g. ATCC
SOURCE_DNA:   Source id number for the clone as pure DNA
SOURCE_INHOST:  Source id number for the clone stored in the host.
OTHER_EST:    Other ESTs on this clone.
DBNAME:    Database name for cross-reference to another database
DBXREF:    Database cross-reference accession
PCR_F:     Forward PCR primer sequence
PCR_B:     Backward PCR primer sequence
INSERT:    Insert length (in bases)
ERROR:     Estimated error in insert length (bases)
PLATE:     Plate number or code
ROW:       Row number or letter
COLUMN:    Column number or letter
SEQ_PRIMER:   Sequencing primer description or sequence.
P_END:     Which end sequenced e.g. 5'
HIQUAL_START:  Base position of start of highest quality sequence 
                (default=1)
HIQUAL_STOP:  Base position of last base of highest quality 
              sequence.
DNA_TYPE:  cDNA (default), Genomic, Viral, Synthetic, Other
PUBLIC:    Date of public release. 
           Leave blank for immediate release.
           Format:  9/11/1994 (MM/DD/YYYY)
            **Obligatory field**
PUT_ID:    Putative identification of sequence by submitter.
TAG_LIB:   Name of library whose tag is found in this sequence.
TAG_TISSUE:  Tissue that was source for the tagged library, if
             a library tag was found.
TAG_SEQ:   The actual sequence of the library tag found in the EST
           read. If the tag was searched for and not found, put
           'Not found' in this field.
POLYA:     Y or N to indicate if a polyA tail was or was not found 
           in the EST sequence.
COMMENT:   Comments about EST. 
           Starts on the same line or the line below COMMENT: tag.
SEQUENCE:  Sequence string. 
           Starts on the same line or the line below SEQUENCE: tag.
           **Obligatory field**
||
```

#### Examples

```
TYPE: EST
STATUS:  New
CONT_NAME: Kerlavage AR
EST#: HHC189f
CLONE: HHC189
SOURCE: ATCC
SOURCE_INHOST: 65128
OTHER_EST:  HHC189r
CITATION: 
Complementary DNA sequencing: expressed sequence tags 
and human genome project
SEQ_PRIMER: M13 Forward
P_END: 5'
HIQUAL_START: 1
HIQUAL_STOP: 285
DNA_TYPE: cDNA
LIBRARY: Hippocampus, Stratagene (cat. #936205)
PUBLIC: 
PUT_ID: Actin, gamma, skeletal
COMMENT:
This is a comment about the sequence.
It may span several lines.
SEQUENCE:
AATCAGCCTGCAAGCAAAAGATAGGAATATTCACCTACAGTGGGCACCTCCTTAAGAAGCTG
ATAGCTTGTTACACAGTAATTAGATTGAAGATAATGGACACGAAACATATTCCGGGATTAAA
CATTCTTGTCAAGAAAGGGGGAGAGAAGTCTGTTGTGCAAGTTTCAAAGAAAAAGGGTACCA
GCAAAAGTGATAATGATTTGAGGATTTCTGTCTCTAATTGGAGGATGATTCTCATGTAAGGT
TGTTAGGAAATGGCAAAGTATTGATGATTGTGTGCTATGTGATTGGTGCTAGATACTTTAAC
TGAGTATACGAGTGAAATACTTGAGACTCGTGTCACTT
||
```

EST data template with required and most often used fields:

```
TYPE:      EST
STATUS:  
CONT_NAME: 
CITATION:  
publication title
LIBRARY:  
EST#:    
CLONE:  
SOURCE:
SOURCE_DNA:   
SOURCE_INHOST:
PCR_F:     
PCR_B:    
INSERT:  
ERROR:  
PLATE: 
ROW:  
COLUMN:   
SEQ_PRIMER: 
P_END:     
HIQUAL_START: 
HIQUAL_STOP: 
DNA_TYPE: 
PUBLIC: 
PUT_ID:  
POLYA:    
COMMENT:   
comments
SEQUENCE: 
sequence
||
```

* The `TYPE` field is obligatory at the beginning of each entry, even if there are multiple entries of a given type in a file.
* Valid data values for the `EST STATUS` field are New (new entry) or Update (change existing `EST` entry).
* When updating an `EST`, only the fields with text present in the `EST` file will be changed. The text in the update file will replace entirely the text for that field in the current version of the file.
* The `DNA_TYPE` is assumed to be c`DNA`, so this field may be omitted unless the `DNA` type differs from this.
* Sequences start on the same line or the line below the `SEQUENCE` field tag.
* It is very important that the strings in the following fields be completely identical, for purposes of automatic matching:
* `POLYA` indicates whether a polyA tail sequence was found in the `EST` read.  
* `TAG_LIB`, `TAG_TISSUE`, `TAG_SEQ`: these were added because some
     researchers pool libraries to
     make subtracted libraries. It's important to many people to know
     which of the libraries in the pooled library a particular
     sequence came from, so short sequence tags are being included in
     the library preps. These tags are specific for each library, so
     if you find that tag in a cDNA read, you know it came from that
     library, even though you found it in a library which was a pool
     of libraries.
* `TAG_LIB`: contains the name of the library whose tag you found in this sequence. e.g. `NCI_CGAP_P`. Leave the field blank if you did not find one. If the library name in this field doesn't match the name of the library the sequence came from, or one of the libraries used to make a subtracted library, this field will alert us that there is a problem.  
* `TAG_TISSUE`: contains the tissue that the tagged library was made from e.g. prostate in the above example.  
* `TAG_SEQ`: contains the actual tag sequence you found in the `EST` read. If you didn't find one, put `None found` in this field,
to distinguish this case from one where the tag hasn't been searched for.



