
# Transcriptome Shotgun Assembly Sequence Database

### What is the Transcriptome Shotgun Assembly (TSA) Database?

**TSA** is an archive of computationally assembled sequences from primary data such as ESTs, traces and Next Generation Sequencing Technologies. The overlapping sequence reads from a complete transcriptome are assembled into transcripts by computational methods instead of by traditional cloning and sequencing of cloned cDNAs. The primary sequence data used in the assemblies must have been experimentally determined by the same submitter. TSA sequence records differ from EST and GenBank records because there are no physical counterparts to the assemblies.

### How Do TSA Sequence Records Differ from Other GenBank/EMBL/DDBJ Records?

The display of a TSA sequence is similar to other International Nucleotide Sequence Database Collaboration (INSDC) records, but includes the following:

*   The label 'TSA:' at the beginning of each Definition Line.
*   DBLINK
    *   BioProject
    *   BioSample
    *   Sequence Read Archive
*   Keywords:  TSA; Transcriptome Shotgun Assembly
*   Assembly data
*   Comment describing the assembly if from a multi-step process.

Each TSA project is assigned a stable 4-letter TSA accession prefix, which does not change as the project is updated. In addition to the TSA accession prefix, the transcript identifiers have a version number corresponding to a particular TSA project update. Finally, each individual assembly is assigned a unique accession number prefixed by the TSA accession prefix and version number. For instance, if a TSA project's assigned accession number is XXXX00000000, then that project's first transcript version would be XXXX01000000, and the first assembly of that version would be XXXX01000001\. (The last six digits of this ID identify each individual assembly). When a project is reassembled, the new assemblies are submitted as the 02 version of the TSA project. No linkage or relationship is expected between the old and new assemblies, and the new assemblies are given new accession numbers beginning with XXXX02000001\. The 01 transcripts are suppressed when the 02 transcripts are released.

An example of a TSA master record is [GAAA00000000.](//www.ncbi.nlm.nih.gov:80/entrez/query.fcgi?cmd=Retrieve&db=nucleotide&list_uids=387756559&dopt=GenBank)

TSA sequence records are shared by all three INSDC databases and can be found using typical search methods in Entrez Nucleotide and Entrez Protein.

### Nucleotide sequences must conform to the following standards:

*   Submitted sequences must be assembled from data experimentally determined by the submitter.
*   Screened for vector contamination and any vector/linker sequence removed. This includes the removal of NextGen sequencing primers.
*   Sequences should be greater than 200 bp in length.
*   Ambiguous bases should not be more than total 10% length or more than 14n's in a row.
*   Sequence gaps of known length may be present and annotated with the assembly_gap feature if there is sufficient evidence for the linkage between the sequences.  See the [TSA Submission Guide](/~/tsaguide) for more information about adding assembly_gap features.
*   Gaps cannot be of unknown length.
*   If the submission is a single-step, unannotated assembly and the output is a BAM file(s) these should be submitted as a TSA project to [SRA](https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi).

### Requirements:

*   Register your project in the [BioProject](//submit.ncbi.nlm.nih.gov/subs/bioproject/) database as a Transcriptome Shotgun Assembly project.
*   Register your library information in the [BioSample](//submit.ncbi.nlm.nih.gov/subs/biosample) database.
*   Raw reads should be submitted to [SRA](https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi) and the SRA run accession(s) (SRR) provided.  Do not provide the SRX accession numbers.
*   EST sequences should be submitted to [dbEST](//www.ncbi.nlm.nih.gov/dbEST/index.html) and the accession range provided in the COMMENT section of the submission.
*   Assembly Data Structured Comment. This information can be input through the Submission Portal dialogs or can be created using the [Structured Comment Template](https://submit.ncbi.nlm.nih.gov/structcomment/nongenomes/). Additional information is in the [TSA Submission Guide](/~/tsaguide)
*   Description of the assembly process if a multi-step assembly was performed should be provided in the COMMENT section.
*   If annotation is provided the product names should follow the [UniProt-Protein Naming Guidelines](//www.uniprot.org/docs/nameprot).
*   The keyword 'Targeted' and feature annotation should be included for all targeted subsets of transcriptome data.  See [Targeted vs. Non-targeted TSA Studies](/~/tsaguide#target) for more information.
*   Annotation must be biologically valid.

### How to Submit to TSA

All TSA submissions must be submitted through the TSA [Submission Portal](https://submit.ncbi.nlm.nih.gov/subs/tsa/) . Submission details can be found in the [TSA submission guide](/~/tsaguide). 

### How to Update an Existing TSA Submission

Please contact [gb-admin@ncbi.nlm.nih.gov](mailto:gb-admin@ncbi.nlm.nih.gov) with reason for updating your assemblies and instructions on how to update will be provided.

### How to Search for TSA Sequences:

*   You can search Entrez Nucleotide using the following terms: tsa-master [prop] and 'Genus Species' [orgn].  
    For example: tsa-master [prop] AND  Nitella mirabilis [orgn]
*   The public submissions are available through the [WGS/TSA browser](//www.ncbi.nlm.nih.gov/Traces/wgs/?term=tsa).
*   The sequences can be downloaded from the [NCBI FTP GenBank site](ftp://ftp.ncbi.nlm.nih.gov/genbank/tsa/).

### Should not be submitted to TSA

*   Assemblies from sequences not directly sequenced by the submitter.
*   Clonal based assemblies. These should be submitted to GenBank.
*   A single assembly from multiple organisms.
*   Subsets of a transcriptome study unless it is part of a targeted study.  See the [TSA submission guide](/~/tsaguide) for more information about submitting a targeted study.





