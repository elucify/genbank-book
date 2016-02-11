
# Complete Genome Submission Guide

### Introduction

This is the submission route for genome assemblies that are essentially the complete genome, eg the complete prokaryotic chromosome with or without any plasmids; or the 16 Saccharomyces cerevisiae chromosomes. If the assembly is still very fragmented with unplaced and/or unlocalized sequences, then submit it as a [WGS genome](//www.ncbi.nlm.nih.gov/genbank/wgs.submit). However, submissions of complete organellar or viral sequences should be submitted as regular records; see [GenBank Submissions](//www.ncbi.nlm.nih.gov/genbank/) for more information on how to submit those types of sequences. [If the organelle belongs to an already submitted WGS genome, then include the WGS accession and BioProject and BioSample identifiers (PRJNAxxxxxx and SAMNxxxxxx, respectively) in the Comments box during submission so that the organelle is linked to the genome assembly.]

If you do not understand any of the instructions presented here or you have questions, please contact us by email at [genomes@ncbi.nlm.nih.gov](mailto:genomes@ncbi.nlm.nih.gov) prior to creating your submission.

### Requirements

*   Your lab must have sequenced the genome or paid to have it sequenced or been part of the collaboration that sequenced it. You cannot submit a genome that you have downloaded from a web site or similar place.
*   The sequence submission must represent a sequence that occurs biologically in the organism. Do not randomly combine the contigs to create a single sequence; you must keep them separate (a traditional WGS submission) or join them with runs of Ns into the correct order and orientation (a gapped WGS submission). If you keep them separate in a traditional submission, you can provide the information to assemble them into scaffolds and/or chromosomes or plasmids with an AGP file (//www.ncbi.nlm.nih.gov/genbank/wgs.submit#agp).
*   Register the source information for each genome in the [BioSample](https://submit.ncbi.nlm.nih.gov/subs/biosample) database. Multiple BioSamples can be pre-registered at once, with the ‘Batch’ option. For isolated unicellular organisms, chose the appropriate Pathogen package (‘Clinical or host-associated pathogen’ OR ‘Environmental, food or other pathogen’) or the Microbe package. If the same sample is used for two different genome assemblies, then use the same BioSample for both.
*   Each genome must belong to a [BioProject](https://submit.ncbi.nlm.nih.gov/subs/bioproject/). Genomes sequenced as part of the same research effort can belong to a single multi-isolate or to a multi-species BioProject.  When more BioSamples are added to a BioProject, the assigned locus_tag prefixes are added to the “locustagprefix.txt” file in the BioProject submission portal, [https://submit.ncbi.nlm.nih.gov/subs/bioproject/](https://submit.ncbi.nlm.nih.gov/subs/bioproject/).
*   Raw reads should be submitted to [SRA](//www.ncbi.nlm.nih.gov/books/NBK47529/). If the genome was sequenced using PacBio sequencing technology, please also submit to SRA the base modification files, eg the motif_summary.csv file. If you have any questions about SRA, contact sra@ncbi.nlm.nih.gov.
*   Annotation is not required, but if annotation is provided it must be biologically valid and the product names should follow the [UniProt-Protein Naming Guidelines](//www.uniprot.org/docs/nameprot).
*   NCBI’s [Prokaryotic Genomes Annotation Pipeline](//www.ncbi.nlm.nih.gov/genome/annotation_prok/)  (NCBI_PGAP) is used to annotate prokaryotic RefSeq genomes and is available for GenBank submissions, by request. No changes by the submitter are needed to make this annotation ready for GenBank submission. Note that all complete prokaryotic genomes will be run through NCBI_PGAP for a basic integrity check, to see that the genome contains some required elements like RNAs and has low levels of pseudogenes/frameshifted genes.  The genome will not be released with this annotation unless you ask us to include it.
*   Provide relevant chromosome, plasmid or organellar assignment information for any sequences in the fasta definition line, as described below.

### Data files:

1\. Fasta file

*   put the sequences into [fasta format](//www.ncbi.nlm.nih.gov/genbank/tbl2asn2#fsa) of the sequences. These files have the suffix .fsa. Each sequence has a definition line beginning with a '>' and a unique identifier, eg contig001, contig002, etc.
    *   The source information can be included in the defline of each contig or in the tbl2asn commandline. It is included in the same format, in either place. At a minimum the source information is the organism and the relevant strain, breed, cultivar or isolate, if one exists for the sequenced organism. The additional source qualifiers will be obtained from the registered BioSample.
    *   Annotated bacterial assemblies should also include the genetic code, [gcode=11], to reduce the number of false errors.
    *   Contigs that are part of a plasmid, or an organellar chromosome, or specific nuclear chromosomes need to have that information included in the fasta definition line, in these formats:
        *   [plasmid-name=pBR322]
        *   [plasmid-name=unnamed] (when the plasmid name is not known. However, be sure that each plasmid has a unique name, eg unnamed1 and unnamed2\. )
        *   [location=mitochondrion]
        *   [location=chloroplast]
        *   [chromosome=2]
    *   Sequences that are a complete circular chromosome or circular plasmid need to have that topology and completeness included by adding this to the fasta definition line:
        *   [topology=circular] [completeness=complete]
    *   Here is an example of the definition line for the complete plasmid of a bacterial submission:

>contig02  [organism=Clostridium difficile] [strain=ABDC] [gcode=11] [plasmid-name=pABDC1] [topology=circular] [completeness=complete]

Another example of a FASTA-formatted sequence is shown in [Figure 1](/~/genomesubmit-examples#fig1)

2.      a [template](//www.ncbi.nlm.nih.gov/WebSub/template.cgi) file with submitter, publication, BioProject and BioSample information.

3.       The Genome-Assembly-Data Structured Comment which includes the assembly method and version, the genome coverage and the sequencing technologies can be created on the [Structured Comment Template](https://submit.ncbi.nlm.nih.gov/structcomment/genomes/) page.

4\. annotation files, if appropriate. These correspond to and have the same basenames as the .fsa files, but have the suffix .tbl. The .tbl files have a 5-column tab-delimited format, as described in the annotation instruction pages. Be sure to read the annotation requirements in the appropriate annotation guidelines:

*   [Prokaryotic Genome Annotation Guide](//www.ncbi.nlm.nih.gov/genbank/genomesubmit_annotation)
*   [Eukaryotic Genome Annotation Guide](//www.ncbi.nlm.nih.gov/genbank/eukaryotic_genome_submission_annotation)

[5\. quality scores](//www.ncbi.nlm.nih.gov/genbank/tbl2asn2#QualityScores) of the sequences. These files correspond to and have the same basenames as the .fsa files, but have the suffix .qvl. The quality scores are optional, but desired.

### Create your submission

Put all the files in the same directory, and run [tbl2asn](//www.ncbi.nlm.nih.gov/genbank/tbl2asn2) (version 22.9 or higher; available by anonymous [FTP](ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/converters/by_program/tbl2asn/)). The basic command line when the sequences are contigs (overlapping reads with no Ns representing gaps) is:

*   **tbl2asn -p path_to_files -t template -M n -Z discrep**

**If the sequences contain Ns that represent gaps**, then run the appropriate tbl2asn commandline with the –l and –a arguments, as described in the [Gapped Genome Submission](//www.ncbi.nlm.nih.gov/genbank/wgs_gapped) page.

For either case:               

*   if you put the template file in a different directory, then include the full path to that file
*   if you want to use a particular file, then use -i file_name, instead of -p path_to_files
*   including "-Z discrep" runs the [discrepancy report](//www.ncbi.nlm.nih.gov/Genbank/asndisc) , which looks for inconsistencies or other suspicious problems, so is most appropriate for annotated submissions.
*   You can include the source information in the definition line of each contig, as described in the [source info above](//www.ncbi.nlm.nih.gov/genbank/wgs.submit#source). Alternatively, all of the common source information, can be included with -j in the tbl2asn commandline. The additional source qualifiers will be obtained from the registered BioSample. In addition, if the submission is an annnotated prokaryotic genome, then include the genetic code with -j in the commandline:
    *   tbl2asn -p path_to_files -t template -M n -Z discrep -j "[organism=Clostridium difficile] [strain=ABDC]  [gcode=11]"
*   To include the structured comment in the output .sqn file, add –w strcmt_file to the commandline, eg
    *   tbl2asn -p path_to_files -t template -M n -Z discrep –w genasm.cmt
    *   This is optional, but can be helpful when there are multiple genomes, because there will be less correspondence about the missing information

Additional command line arguments can be seen on the [tbl2asn](/Genbank/tbl2asn2) page.

In the directory specified by '-p', the program looks for corresponding pairs of *.fsa and *.tbl files, and builds ASN.1 records named *.sqn for these pairs. The results of the validation (error checking) will be in *.val files. Note that if there are no .tbl files in the directory, then tbl2asn will still generate .sqn files from the .fsa files that are present.

### Check and fix problems

Check the errorsummary.val file for the number, severity and type of errors that are present in the .val files. All Errors and Rejects need to be fixed. The presence of errors will slow processing.  Contact genomes@ncbi.nlm.nih.gov with any questions about the validation output. 

Check the file named 'discrep' for the results of the discrepancy report. Categories prefaced with FATAL are always unacceptable and must be fixed.  Some of the categories are informational. See the [discrepancy report examples and explanations](//www.ncbi.nlm.nih.gov/genbank/asndisc#Evaluating%20the%20output) for guidance. Write to genomes@ncbi.nlm.nih.gov and send the discrep file with questions about this report.

Make any necessary fixes to the input .fsa and/or .tbl files and run tbl2asn again. Or make the necessary fixes directly to the .sqn file by opening it in [Sequin](//www.ncbi.nlm.nih.gov/Sequin/index.html) and editing the features there. Additional tips on using Sequin are found in the [Sequin Guide](//www.ncbi.nlm.nih.gov/Sequin/QuickGuide/sequin.htm) .

In addition, NCBI offers a [Genome Submission Check Tool](//www.ncbi.nlm.nih.gov/genomes/frameshifts/frameshifts.cgi) to check your submission file before sending it to us. This tool performs another validation check on your submission files. It takes neighboring pairs of proteins and does a BLASTP analysis on them and notes which neighbors hit the same longer protein. Finding pairs of proteins that hit the same longer protein suggests that the pair may represent a single gene that has gained a frameshift or other mutation. We ask that you do your own analysis to decide whether the pair should remain two proteins, or be combined into a single pseudogene. This validation check also looks for and reports tRNAs and rRNAs that may have escaped your detection or were annotated on the wrong strand.

Once the errors have been fixed, the .sqn files can be submitted to GenBank. If either the Discrepancy Report or the Genome Submissions Check tool report errors that you feel are not problems, please send the list of these errors along with some explanation as to why they are OK.

### Submit

Use our [Genomes Submission Tool](//www.ncbi.nlm.nih.gov/projects/GenomeSubmit/genome_submit.cgi) to upload the .sqn files of one or more genome submissions to us. Send us an email at [genomes@ncbi.nlm.nih.gov](mailto:genomes@ncbi.nlm.nih.gov) whenever you submit a new genome, and include the registered BioProject and organism name in the message and the requested release date of the genome. The choices are ‘immediately after processing’ or a specific date. Note that the genome will be released on that date or when the data is published, whichever is first. If either the Discrepancy Report or the Genome Submissions Check tool report errors that you feel are not problems, please include the list of these errors along with some explanation as to why they are OK.

If you want the genome annotated by the [Prokaryotic Genomes Annotation Pipeline](http://www.ncbi.nlm.nih.gov/genome/annotation_prok/) before its release, then include that request in your email: "Please annotate this genome through PGAP".  If you want to preview the annotation files, include that request in the email: "Please annotate this genome through PGAP and provide the files back to me before processing them." You may edit the files before final submission, though this is not required and is generally not recommended, as it will slow processing and may introduce problems that you would need to fix before submitting the edited files.

### What happens next

Once we receive your genome submission, a member of our staff will conduct an initial review of it and will contact you by email. If we do not find any significant issues with your submission, you will be issued an accession number. Once your submission is assigned an accession number it undergoes a thorough review by our staff. This review is critical because we are striving to present genome annotation in an accurate and consistent manner so that database users can make maximum use of the data. If we encounter problems during this review, we will contact you by email.

Once we have completed our review of your submission, we will prepare it for release to the public database. You can choose to have your submission released immediately or to be kept confidential until a certain date or publication of the work, whichever is first. If you wish your genome to be held until publication, we ask that you provide us with the expected publication date and also notify us in a timely manner of the upcoming publication and the relevant citation details. This will allow us to coordinate the release of your genome with the appearance of the paper. Please provide at least two weeks' notice of any upcoming publication.

### Updating a genome

See [Update Genome Resources](//www.ncbi.nlm.nih.gov/genbank/wgs_update)

</div>

</div>

<div id="shared-content-1" nid="1469">

<div class="rightnav">

## Genome Resources

*   [BioProject](http://www.ncbi.nlm.nih.gov/bioproject)
*   [Prokaryotic Genome Annotation Guide](/~/genomesubmit_annotation)
*   [tbl2asn](/~/tbl2asn2)
*   [GenomesMacroSend](http://www.ncbi.nlm.nih.gov/projects/GenomeSubmit/genome_submit.cgi)
*   [NCBI Prokaryotic Genome Annotation Pipeline](http://www.ncbi.nlm.nih.gov/genome/annotation_prok/)

</div>

</div>