
# How to Submit WGS Genomes

### Introduction

DDBJ/EMBL/GenBank accepts both complete and incomplete genomes. Whole Genome Shotgun (WGS) sequencing projects are incomplete genomes or incomplete chromosomes that are being sequenced by a whole genome shotgun strategy. See the [WGS page](/~/wgs) for details on what is and is not suitable for submission as a WGS project.

**New**: An updated version of the WGS Submission Portal was released on Feb. 3, 2014\. Its URL is the original [https://submit.ncbi.nlm.nih.gov/subs/wgs/](https://submit.ncbi.nlm.nih.gov/subs/wgs/). However, older submissions that were begun before that date are present at this URL- [https://submit.ncbi.nlm.nih.gov/subs/wgs1/](https://submit.ncbi.nlm.nih.gov/subs/wgs1/). If you have already submitted a genome in the original system, then please use that submission and do not create a duplicate submission, as that will cause confusion and slow down processing.

**New**: We are accepting two formats for WGS submissions: Split or Gapped:

*   Split format (standard WGS submission format):  The pieces of a WGS project are the contigs (overlapping reads with no gaps).   An optional [AGP file](http://www.ncbi.nlm.nih.gov/genbank/wgs.submit#agp) can be submitted to indicate how the wgs-sequences are assembled together into scaffolds or chromosomes.
*   Gapped format (new): the pieces of a WGS project are the scaffolds that contain runs of Ns that represent gaps. An agp file is not required for the gapped format See [Gapped Genome Submission](/~/wgs_gapped) for details.

**New**: Assignment of strain-level taxids is ending in February 2014, and registration of a BioSample is required.

Information about the requirements for more complex assemblies, such as those with PARs or alternate loci, is in the [Assembly Submission](http://www.ncbi.nlm.nih.gov/projects/genome/assembly/submission/index.shtml) pages.

WGS genomes without annotation, or with PGAP annotation, require at least two weeks to be processed. Genomes with annotation require at least one month for processing. Please submit your project with enough lead time.

Below are detailed instructions for preparing a simple WGS submission.

### Requirements

*   Register the source information for each genome in the [BioSample](https://submit.ncbi.nlm.nih.gov/subs/biosample) database. If the same sample is used for two different genome assemblies, then use the same BioSample for both. Registering a new BioSample can be done during the WGS submission process for unannotated (or PGAP-annotated) genomes; however, genomes submitted with annotation will need to be [pre-registered](https://submit.ncbi.nlm.nih.gov/subs/biosample/) to get a locus_tag prefix.
*   Each genome must belong to a BioProject. Genomes sequenced as part of the same research effort can belong to a single BioProject.  Registering a new BioProject can be done during the WGS submission process for unannotated (or PGAP-annotated) genomes; however, genomes submitted with annotation will need to be [pre-registered](https://submit.ncbi.nlm.nih.gov/subs/bioproject/).  Write to [genomes@ncbi.nlm.nih.gov](mailto:genomes@ncbi.nlm.nih.gov) if you do not receive a locus_tag prefix with the BioSample/BioProject pair of the genome.
*   Raw reads should be submitted to [SRA](http://www.ncbi.nlm.nih.gov/books/NBK47529/)
*   Genome-Assembly-Data Structured Comment. This can be supplied in the submission web page during the genome submission. Alternatively, it can be created using the [Structured Comment Template](https://submit.ncbi.nlm.nih.gov/structcomment/genomes/) and then included in the genome file that is submitted.
*   If annotation is provided, the product names should follow the [UniProt-Protein Naming Guidelines](http://www.uniprot.org/docs/nameprot).
*   Annotation must be biologically valid (and error-free).

### Submission Details:

#### New:

Genome assemblies without annotation and without any Ns that represent gaps can now be submitted simply with a fasta file in the updated [Genomes (WGS) in the submission portal](https://submit.ncbi.nlm.nih.gov/subs/wgs/), released on Feb. 3, 2014\. The information to generate a genome submission will be collected from:

*   The organism metadata information will be obtained from the indicated BioSample, which can be pre-registered or created during the genome submission
*   The submitter information will be obtained from the submission portal profile.
*   The genome assembly metadata and reference information will be requested in the web pages, as usual
*   Submitters can request PGAP annotation for prokaryotic genomes with the "Annotate this prokaryotic genome in the NCBI Prokaryotic Annotation Pipeline before being released" checkbox in the same submission pages
*   An AGP file to assemble scaffolds and/or chromosomes can also be submitted as part of a fasta-based submission.

Genome assemblies that contain annotation or Ns that represent gaps still need to be submitted as .sqn files. We recommend using tbl2asn to create those files, as described below.

#### Events

1.  If you have annotation, then obtain a locus_tag prefix by pre-registering the genome sequencing project with the [BioProject](https://submit.ncbi.nlm.nih.gov/subs/bioproject/) and BioSample databases, if you have not already done this.  Do not register a duplicate BioProject or BioSample for the same genome. Note that genomes sequenced as part of the same research effort can belong to a single BioProject.
2.  Make the genome assembly [data files](#datafiles)
    1.  [Run](#Run) the commandline program tbl2asn to generate the .sqn file for submission and the validation and discrepancy report files.
    2.  [Fix problems](#Fix) that are indicated in the .val and discrep files. Failure to do this will cause serious delays in processing.
3.  If you have higher-level assembly information, scaffolds and/or chromosomes, then generate an [AGP file](#agp) to build those objects from the wgs-contigs.
4.  [Submit](#Submit) via the new [Genomes (WGS) in the submission portal](https://submit.ncbi.nlm.nih.gov/subs/wgs/)

*   [What happens after submission](#whathappensnext)*   [Submitting PGAP-annotated genomes](#pgaap)

#### Data files:

The specifics of the file formats are presented in the [tbl2asn](/~/tbl2asn2) page.

*   put the sequences into [fasta format](/~/tbl2asn2#fsa) of the sequences. These files have the suffix .fsa. Each sequence has a definition line beginning with a '>' and a unique identifier, eg contig001, contig002, etc. Note that this unique identifier appears in the DEFINITION line in the flatfile view of the record. Please use concise names that do not include length or coverage information. See some [example files](/~/examples.wgs.html). For all types of submissions:
    *   The .fsa files can have up to 10,000 sequences per file. Larger submissions need to be split into multiple files.
    *   Submit only contigs >199nt.
    *   Remove any Ns from the beginning or end of each sequence.
*   The fasta files of submissions that will contain annotation or Ns that represent gaps also need:
    *   The <a name="source">source information</a> can be included in the defline of each contig or in the tbl2asn commandline. It is included in the same format, in either place. At a minimum the source information is the organism and the relevant strain, breed, cultivar or isolate, if one exists for the sequenced organism. **Note that the organism for microbial genomes (prokaryotes and fungi) registered in BioProject or BioSample before Feb. 2014 includes the strain, eg Escherichia coli BCE032-DM-B or Saccharomyces cerevisiae FL100, so the strain name appears in the organism and also in the strain, as seen in the example below**. The additional source qualifiers will be obtained from the registered BioSample.
    *   Annotated bacterial assemblies should also include the genetic code, [gcode=11], to reduce the number of false errors.
    *   Here is an example of the source information for an annotated bacterial submission:

        [organism=Clostridium difficile ABDC] [strain=ABDC] [gcode=11]

    *   Contigs that are part of a plasmid, or an organellar chromosome, or specific nuclear chromosomes need to have that information included in the fasta definition line, in these formats:
        *   [plasmid-name=pBR322]
        *   [plasmid-name=unnamed] (when the plasmid name is not known. However, be sure that each plasmid has a unique name, eg unnamed1 and unnamed2\. )
        *   [location=mitochondrion]
        *   [location=chloroplast]
        *   [chromosome=2] (this is usually included only for smaller genomes when the chromosome assignment is certain; don't do this for large, eg mammalian, genomes when reassembly may result in a contig's assignment to a different chromosome)

Genomes that contain annotation or Ns that represent gaps also need:

*   a [template](http://www.ncbi.nlm.nih.gov/WebSub/template.cgi) file with submitter and publication information.

*   [quality scores](/~/tbl2asn2#QualityScores) of the sequences. These files correspond to and have the same basenames as the .fsa files, but have the suffix .qvl. The quality scores are optional, but desired.
*   Genome-Assembly-Data Structured Comment. This information can be supplied in the submission web page during the genome submission, but if many genomes are being submitted it can be simpler to include this in the file itself. To do that, use the [Structured Comment Template](https://submit.ncbi.nlm.nih.gov/structcomment/genomes/) to create the comment file and then have it included with “-w genasm.cmt” in the [tbl2asn commandline, below](/~/wgs.submit#Run).
*   annotation files, if appropriate. These correspond to and have the same basenames as the .fsa files, but have the suffix .tbl. The .tbl files have a 5-column tab-delimited format, as described in the annotation instruction pages.

    Be sure to read the annotation requirements in the appropriate annotation guidelines:

    You may be interested to know that NCBI has a publicly available [Prokaryotic Genomes Annotation Pipeline](/genome/annotation_prok/). This pipeline generates annotation that is ready for submission to GenBank, although the submitter is welcome to edit the files before final submission to GenBank. Generate files for WGS submission and request PGAAP annotation in the Private Comments box during submission of the genome. See below for [details about PGAAP](#pgaap) submissions to GenBank.

    *   [Prokaryotic Genome Guidelines](/Genbank/genomesubmit)
    *   [Eukaryotic Genome Guidelines](/Genbank/eukaryotic_genome_submission)

#### Run tbl2asn:

Put all the files in the same directory, and run [tbl2asn](/genbank/tbl2asn2) (version 22.9 or higher). The basic commandline when the sequences are contigs (overlapping reads with no Ns representing gaps) is:

*   **tbl2asn -p path_to_files -t template -M n -Z discrep**

**If the sequences contain Ns that represent gaps**, then run the appropriate tbl2asn commandline with the –l and –a arguments, as described in the [Gapped Genome Submission](/~/wgs_gapped) page.

For either case:

*   if you put the template file in a different directory, then include the full path to that file
*   if you want to use a particular file, then use -i file_name, instead of -p path_to_files
*   including "-Z discrep" runs the [discrepancy report](/Genbank/asndisc) , which looks for inconsistencies or other suspicious problems, so is most appropriate for annotated submissions.
*   You can include the source information in the definition line of each contig, as described in the [source info above](#source). Alternatively, all of the common source information, can be included with -j in the tbl2asn commandline. **Note that the organism for microbial genomes (prokaryotes and fungi) still includes the strain, eg Escherichia coli BCE032-DM-B or Saccharomyces cerevisiae FL100, so the strain name appears in the organism and also in the strain, as seen in the example below**. The additional source qualifiers will be obtained from the registered BioSample. In addition, if the submission is an annnotated prokaryotic genome, then include the genetic code with -j in the commandline:
    *   tbl2asn -p path_to_files -t template -M n -Z discrep -j "[organism=Clostridium difficile ABDC] [strain=ABDC]  [gcode=11]"
*   To include the structured comment in the output .sqn file, add –w strcmt_file to the commandline, eg
    *   tbl2asn -p path_to_files -t template -M n -Z discrep –w genasm.cmt
    *   This is optional, but can be helpful when there are multiple genomes, because there will be less information to supply on the web form during submission.

#### Check the Output of the Validation and Discrepancy Report and Fix Problems

*   Check the errorsummary.val file for the number, severity and type of errors that are present in the .val files. All Errors and Rejects need to be fixed (as of March 2012, and v19.6 or higher). The presence of errors will slow processing.  Contact genomes@ncbi.nlm.nih.gov with any questions about the validation output.  During processing there may be some questions about other aspects of the submission.
*   Check the file named 'discrep' for the results of the discrepancy report. Categories prefaced with FATAL are always unacceptable and must be fixed (FATAL tags were added in January 2012 ).  Some of the categories are informational.  Reports that are not flagged as fatal need to be evaluated to determine if they represent annotation artifacts that need to be corrected or if they are acceptable due to the biology of the genome. See the [discrepancy report examples and explanations](/~/asndisc#Evaluating%20the%20output) for guidance. Write to genomes@ncbi.nlm.nih.gov and send the discrep file with questions about this report.
*   Make any necessary fixes to the input .fsa and/or .tbl files and run tbl2asn again. Or make the necessary fixes directly to the .sqn file by opening it in [Sequin](http://www.ncbi.nlm.nih.gov/Sequin/index.html) and editing the features there.

#### AGP file

AGP files provide the ordering and orientation information to construct supercontigs or scaffolds from contigs, or to construct chromosomes from scaffolds and/or contigs.  The AGP file defines these genome assemblies, so include all wgs-contigs that are considered to be part of the genome in the AGP file.

###### <a class="jig-ncbitoggler">see details</a>

See this page for the [AGP format](http://www.ncbi.nlm.nih.gov/projects/genome/assembly/agp/AGP_Specification.shtml) .

Some specific requests are:

*   Encode the type of object in the object names in column 1 like this:
    *   scaffold01, scaffold02, etc for scaffolds
    *   chr (for bacteria) OR chr1, chr2, etc for eukaryotic chromosomes
    *   the plasmid names for plasmids (eg pBR322). If the name is not known, then use 'unnamed'.
    *   MT for the mitochondrial genome. MT_scaf01, MT_scaf02, etc for mitochondrial scaffolds.
*   Use "100" as the length and U as the component-type for gaps of unknown size, as that is the GenBank convention. These will appear as gap(unk100) in the flatfile view of the GenBank record.
*   Use the same contig identifiers in column 6 (the component-id) that you used in the .fsa files. If the components have already been assigned accession numbers, then you need to use the accession.version numbers as the component identifiers; do not use just the accession number.

You can validate the basic format of your AGP file on this web page, [http://www.ncbi.nlm.nih.gov/projects/genome/assembly/agp/agp_validate.cgi](http://www.ncbi.nlm.nih.gov/projects/genome/assembly/agp/agp_validate.cgi).  In addition, the standalone commandline program, [agp_validate](http://www.ncbi.nlm.nih.gov/projects/genome/assembly/agp/AGP_Validation.shtml) is available by anonymous [FTP](ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/converters/by_program/agp_validate/) to validate the AGP file more extensively yourself. The -help option details the arguments and commandline format.



#### Assembly Information Files

Additional information will need to be supplied in the Assignment tab of the updated submission portal if the genome assembly includes chromosomes (or plasmids or linkage-groups) or unlocalized scaffolds (scaffolds known to be part of a particular chromosome/plasmid/linkage-group, but whose location is not known).

Submissions in the original submission portal (before Feb. 3, 2014) will need the files described below, as appropriate.

###### <a class="jig-ncbitoggler">see details</a>



**Contigs only (no AGP file), but some contigs are the complete chromosome or plasmid:** Submit .sqn file(s) from tbl2asn plus a 4-column comma-separated chr/plasmid description file of ContigID,chromosome/plasmid name,Location,Type. The columns of the file are:

*   Column 1 is the contig name that is the id from the fasta file,
*   Column 2 is the official name of the chromosome, plasmid or linkage group. For example, 1, 2, 3 or I, II, III for chromosomes; pBR322 for plasmids; or LG1, LG2 for linkage groups. Use 'chr' for the prokaryotic chromosome name and 'MT' for the mitochondrial chromosome name when there is a single chromosome.
*   Column 3 is the subcellular location of the genomic molecule. Use 'na' for prokaryotes, and either 'nuclear' or the appropriate organelle, eg 'mitochondrion', for eukaryotes.
*   Column 4 is the type of genomic molecule and has a controlled vocabulary: **chromosome, plasmid, linkage group**.

**AGP file and chromosome/plasmid/linkage-group information:** Submit .sqn file(s) from tbl2asn plus the following, depending upon the contents of the genome assembly submission:

*   Separate AGP files for:
    *   unplaced scaffolds. These are scaffolds that have no chromosome information.
    *   unlocalized scaffolds (also known as 'random'). These have a chromosome assignment but the location on the chromosome is unknown. For example, if there were several scaffolds that were mitochondrial but they were not assembled into the mitochondrial chromosome, then these would be unlocalized scaffolds.
    *   chromosomes, plasmids and/or linkage groups.
*   Chromosome Types file when the assembly includes chromosome, plasmid and/or linkage group information. This is a 3-column comma-separated table with these values in the columns:

    pBR322,na,plasmid

    *   Column 1 is the official name of the chromosome/plasmid/linkage-group, eg 1, 2, 3 or I, II, III for chromosomes; pBR322 for plasmids; or LG1, LG2 for linkage groups. Use 'MT' for the mitochondrial chromosome name and 'chr' for the prokaryotic chromosome name when there is only a single chromosome. If the plasmid has not been named, then use 'unnamed'; however, be sure that each plasmid has a unique name. The value in column 1 must match the value in column 2 of the AGP Roles files, below.
    *   Column 2 is the subcellular location of the genomic molecule. Use 'na' for prokaryotes and either 'nuclear' or the appropriate organelle, eg 'mitochondrion', for eukaryotes.
    *   Column 3 is the type of genomic molecule and has a controlled vocabulary: **chromosome, plasmid, linkage group**.
    *   ChromosomeTypes.csv example for eukaryote and prokaryote

1,nuclear,chromosome

2,nuclear,chromosome

MT,mitochondrion,chromosome

chr,na,chromosome

pBR322,na,plasmid

*   AGP Roles, 2-column comma-separated file for unlocalized scaffolds:
    *   Column 1 is the name of the object in column 1 of the corresponding AGP file.
    *   Column 2 is the chromosome/plasmid/linkage-group of that object, using the name from column 1 of the Chromosome Types table. Therefore, use 'MT' for the mitochondrial chromosome name and 'chr' for the prokaryotic chromosome name when there is only a single chromosome.
    *   Example, AGPRoles_unlocalized.csv:

chr2_random0001,2

chr2_random0002,2

chr2_random0035,2

*   AGP Roles, 2-column comma-separated file for chromosomes/plasmids/linkage-groups:
    *   Column 1 is the name of the object in column 1 of the corresponding AGP file.
    *   Column 2 is the chromosome/plasmid/linkage-group of that object, using the name from column 1 of the Chromosome Types table. Therefore, use 'MT' for the mitochondrial chromosome name and 'chr' for the prokaryotic chromosome name when there is only a single chromosome.
    *   Example AGPRoles_chrs.csv:

chr1,1  
chr2,2  
mito,MT  
scf1,chr  
scf10,pBR322



*   #### Submit your files

    Upload the .sqn and .agp files and chromosome/plasmid information files to GenBank in the [Genomes (WGS) submission portal](https://submit.ncbi.nlm.nih.gov/subs/wgs/). A submission whose files total more than 2G will need to use Chrome, Opera or Safari browsers, which do not have a size limit on what they can upload. You can also compress large files to decrease large files for the upload.

    *   To have an unannotated prokaryotic genome submission annotated by NCBI's PGAP pipeline, just click the box with that request on the Source tab of the updated submission portail.  In the original submission portal, include the request in the Private Comments box, "Please annotate this genome through PGAP".

    *   You will be asked to provide additional information,

    ###### <a class="jig-ncbitoggler">including this information:</a>

    

    *   BioProjectID (PRJNAxxxxx) from BioProject DB, or create one during this submission because you have not yet created one
    *   BioSampleID (SAMNxxxxx) from BioSample, or create one during this submission because you have not yet created one
    *   Release date: After Processing OR a specific date
    *   Whether you expect to annotate (or did annotate) this version of the genome assembly. NOTE: this is not the place to request PGAP annotation
    *   Whether this is the final version of the genome. If you don't anticipate updating the assembly, then choose "yes".
    *   Whether this genome is part of a multi-isolate study.
    *   Whether this is a de novo assembly. If it was not, then you'll include the accession.version and/or the assembly name of the genome assembly that was used as the reference guide.
    *   Assembly metadata (unless the Genome assembly structured comment is in the .sqn file, and you check that box) :
        *   Assembly Name: a short name suitable for display eg, LoxAfr_3.0 for a Loxodonta africana assembly, version 3.0
        *   Assembly Method and version (or date the program was run): eg, Newbler v. 2.3 OR Celera Assembly v. May 2010
        *   Genome Coverage: eg, 12x
        *   Sequencing Technologies: eg, ABI 3730; 454 GS-FLX Titanium; Illumina GAIIx

    

    The submission will be given a 'SUB' temporary identifier which you can use in correspondence before an accession number is assigned to the genome submission.

    ### What happens next:

    Once we receive your genome submission, a member of our staff will conduct an initial review of it. If there are problems with the initial submission, the submitted files will be marked in the submission portal as "Processed-error" and you will receive an email with details of the problems. The problems, including those described in the [Fix problems](#Fix) section, could be:

    *   any Error-level errors and some Warning-level errors from the validation. You would see these in the.val file(s) generated by tbl2asn.
    *   any FATAL or problem categories from the discrepancy report (in the discrep file from tbl2asn)
    *   any sequence contamination in the .sqn files
    *   bad format of the AGP file or inconsistencies between the AGP and .sqn files.

    Once you have made the fixes, log back into the [Genomes (WGS) submission portal](https://submit.ncbi.nlm.nih.gov/subs/wgs/), retrieve that submission by its 'SUB' identifier and click "Resubmit" on that submission. You'll be back in the original submission and will need to delete the files that are marked as having errors, and then upload new files in their place. This resubmission will be a replacement of the original and will have a new 'SUB' temporary identifier.

    If the initial review by a member of our staff finds no significant issues with your submission or resubmission, you will be issued an accession number for the genome by email. After your submission is assigned an accession number, it undergoes a thorough review by our staff. This review is critical because we are striving to present genome annotation in an accurate and consistent manner so that database users can make maximum use of the data. If we encounter problems during this review, we will contact you by email.

    Submission statuses in the submission portal:

    *   Queued: the submission is waiting for initial review
    *   Processed-error: some or all files need to be fixed and resubmitted (with a different name)
    *   Processing: the submission has passed the initial review and will be processed by NCBI staff. We will contact you during processing if the submission has issues that require additional information.
    *   Processed-ok: the wgs contigs have been publicly released

    If you elected to hold your genome until a particular date (or publication, whichever is first), we ask that you provide us with the expected publication date and also notify us in a timely manner of the upcoming publication and the relevant citation details. This will allow us to coordinate the release of your genome with the appearance of the paper. Please provide at least two weeks' notice of any upcoming publication.

    *   NOTE that beginning January 2013 genomes will be released on their release date without additional communication, as is the normal GenBank policy.  Be sure to request an extension of the release date if the genome is not yet published and you wish to continue to keep it confidential.

### Submitting PGAP-annotated genomes

Requests for annotation by the [Prokaryotic Genomes Annotation Pipeline](http://www.ncbi.nlm.nih.gov/genome/annotation_prok/) is a step during submission of the genome to GenBank. Prepare a regular GenBank WGS submission and request PGAP annotation during the submission process by clicking on the box "Annotate this prokaryotic genome in the NCBI Prokaryotic Annotation Pipeline before being <label for="id_prokaryote_source-annotate_prokaryotic_genome">released".  </label> A fasta submission in the new updated submission portal would be simplest. You may edit the files before final submission, though this is not required and is generally not recommended, as it will slow processing and may introduce problems that you would need to fix before submitting the edited file.





<div id="shared-content-1" nid="1465">

<div class="rightnav">

## WGS Resources

*   [About WGS](/~/wgs)
*   [WGS Project List](http://www.ncbi.nlm.nih.gov/Traces/wgs)
*   [WGS Submission Guide](/~/wgs.submit)
*   [Update Genome Records](/~/wgs_update)
*   [FAQ](/~/wgsfaq)
*   [tbl2asn](/~/tbl2asn2)
*   [Create Submission Template](http://www.ncbi.nlm.nih.gov/WebSub/template.cgi)
*   [BioProject](http://www.ncbi.nlm.nih.gov/bioproject)
*   [Eukaryotic Annotation Guide](/~/eukaryotic_genome_submission)
*   [Prokaryotic Annotation Guide](/~/genomesubmit)
*   [Discrepancy Report](/~/asndisc)
*   [WGS Example Files](/~/examples.wgs)
*   [Assembly Submission Guide](http://www.ncbi.nlm.nih.gov/assembly/docs/submission/)
*   [AGP Format](http://www.ncbi.nlm.nih.gov/assembly/agp/AGP_Specification/)
*   [WGS Submission Portal](https://submit.ncbi.nlm.nih.gov/subs/wgs/)
*   [NCBI Prokaryotic Genome Annotation Pipeline](http://www.ncbi.nlm.nih.gov/genome/annotation_prok/)
*   [Metagenome Submission Guide](/~/metagenome)
*   [Structured Comment](/~/structuredcomment)



