
# Whole Genome Shotgun Submissions

### What is Whole Genome Shotgun (WGS)?

Whole Genome Shotgun (WGS) projects are genome assemblies of incomplete genomes or incomplete chromosomes of prokaryotes or eukaryotes that are generally being sequenced by a whole genome shotgun strategy.   WGS projects may be annotated, but annotation is not required. NCBI has a [Prokaryotic Genomes Annotation Pipeline](http://www.ncbi.nlm.nih.gov/genomes/static/Pipeline.html) that may be requested at the time the genome files are submitted to GenBank. This pipeline generates a submission-ready annotated file that the submitter could edit prior to data release.

**New**: We are accepting two formats for WGS submissions, Split or Gapped:

*   Split format (standard WGS submission format):  The pieces of a WGS project are the contigs (overlapping reads with no gaps).   An optional [AGP file](http://www.ncbi.nlm.nih.gov/genbank/wgs.submit#agp) can be submitted to indicate how the wgs-sequences are assembled together into scaffolds or chromosomes.
*   Gapped format (new): the pieces of a WGS project are the scaffolds that contain runs of Ns that represent gaps. An agp file is not required for the gapped format See [Gapped Genome Submission](/~/wgs_gapped) for details. Sequences that are simply concatenated and joined by Ns are not allowed.

**New**: Assignment of strain-level taxids is ending in January 2014 and registration of a BioSample is required.

The public WGS projects are at the [list of WGS projects](http://www.ncbi.nlm.nih.gov/Traces/wgs/)[.](http://www.ncbi.nlm.nih.gov/Traces/wgs/)

Each WGS project is assigned a stable 4-letter WGS accession prefix, which does not change as the project is updated. In addition to the WGS accession prefix, the contig identifiers have a version number corresponding to a particular WGS project update. Finally, each individual contig within the assembly is assigned a unique accession number prefixed by the WGS accession prefix and version number. For instance, if a WGS project's assigned accession number is XXXX00000000, then that project's first assembly version would be XXXX01000000, and the first contig of that version would be XXXX01000001\. (The last six digits of this ID identify each individual contig). When there is more sequencing and the genome is reassembled, the contigs are submitted as the 02 version of the WGS project. No linkage or relationship is expected between the old and new contigs, and the new contigs are given new accession numbers beginning with XXXX02000001\. The 01 contigs are suppressed when the 02 contigs are released.  

In addition, each genome is part of a [BioProject](http://www.ncbi.nlm.nih.gov/bioproject/) that describes the research effort, and is from a [BioSample](http://www.ncbi.nlm.nih.gov/biosample/)  which presents details of the source of the DNA. Furthermore, each public genome is loaded into the [Assembly](http://www.ncbi.nlm.nih.gov/assembly/) database, where it is assigned an Assembly accession. When a genome is updated, the Assembly accession is incremented to the next version, but the BioProject and BioSample accessions remain the same.

The nucleotide data from all WGS projects go into the BLAST wgs database since the fall of 2011.  Proteins from most WGS projects go into the BLAST nr database.  Proteins from environmental projects are present in either the BLAST nr or env_nr database, depending upon whether that sequence has been identified as a particular organism (nr), or if the organism is not yet known (env_nr).

See the [Metagenome Submission Guide](/~/metagenome) for information about how to submit the various elements of a metagenome project.

Information about the requirements for more complex assemblies, such as those with PARs or alternate loci, is in the [Assembly Submission](http://www.ncbi.nlm.nih.gov/projects/genome/assembly/submission/index.shtml) pages.

### Some Examples

The table below shows a few examples of WGS projects:

1.  unannotated contigs and scaffolds
2.  annotated contigs with unannotated scaffolds
3.  unannotated contigs with annotated scaffolds.

The accession number of each WGS project is included in the table and will link to the live record for viewing. For accession AZCS00000000, notice that the annotation on contigs is displayed up on the corresponding scaffold. However, annotation that is submitted on a scaffold or chromosome CON record is not displayed on the underlying components, as seen in ABXC00000000\. To be able to see the annotation on large records, use the GenBank(full) Display setting and/or the Customize options to ’show sequence’.

<table border="1">

<tbody>

<tr>

<td>Annotated Contigs</td>

<td>Annotated Scaffolds</td>

<td>No Annotation</td>

</tr>

<tr>

<td>ACZS00000000</td>

<td>ABXC00000000</td>

<td>AAGU00000000</td>

</tr>

<tr>

<td>[WGS contig](http://www.ncbi.nlm.nih.gov/nuccore/260636527?report=gbwithparts&log$=seqview)</td>

<td>[WGS contig](http://www.ncbi.nlm.nih.gov/nuccore/237891334?report=gbwithparts&log$=seqview)</td>

<td>[WGS contig](http://www.ncbi.nlm.nih.gov/nuccore/253587594?report=gbwithparts&log$=seqview)</td>

</tr>

<tr>

<td>[Scaffold CON](http://www.ncbi.nlm.nih.gov/nuccore/260871327?report=gbwithparts&log$)</td>

<td>[Scaffold CON](http://www.ncbi.nlm.nih.gov/nuccore/239785565?report=gbwithparts&log$=seqview)</td>

<td>[Scaffold CON](http://www.ncbi.nlm.nih.gov/nuccore/253994985)</td>

</tr>

</tbody>

</table>

### Nucleotide sequences must conform to the following standards:

*   Submitted sequences must be assembled from data experimentally determined by the submitter.
*   Screened for vector contamination and any vector/linker sequence removed. This includes the removal of NextGen sequencing primers.
*   Sequences should be greater than 200 bp in length, if they are not part of multi-component scaffolds
*   Sequence gaps may be present and annotated with the assembly_gap feature; however, sequences cannot be randomly concatenated for submission. See the [Gapped Genome Submissions](/~/wgs_gapped) page  for more information about adding assembly_gap features.
*   Sequences cannot begin or end with Ns

WGS genomes without annotation or with PGAP annotation require at least two weeks to be processed. Genomes with annotation require at least one month for processing. Please submit your genome assembly with enough lead time.

### Requirements:

*   Register the source information for each genome in the [BioSample](https://submit.ncbi.nlm.nih.gov/subs/biosample) database. If the same sample is used for two different genome assemblies, then use the same BioSample for both. Registering a new BioSample can be done during the WGS submission process for unannotated (or PGAP-annotated) genomes; however, genomes submitted with annotation will need to be [pre-registered](https://submit.ncbi.nlm.nih.gov/subs/biosample/) to get a locus_tag prefix.
*   Each genome must belong to a BioProject. Genomes sequenced as part of the same research effort can belong to a single BioProject.  Registering a new BioProject can be done during the WGS submission process for unannotated (or PGAP-annotated) genomes; however, genomes submitted with annotation will need to be [pre-registered](https://submit.ncbi.nlm.nih.gov/subs/bioproject/).
*   Raw reads should be submitted to [SRA](http://www.ncbi.nlm.nih.gov/books/NBK47529/)
*   Genome-Assembly-Data Structured Comment. This can be supplied in the submission web page during the genome submission. Alternatively, it can be created using the [Structured Comment Template](https://submit.ncbi.nlm.nih.gov/structcomment/genomes/) and then included in the genome file that is submitted. Additional information is in the [WGS Submission Guide](http://www.ncbi.nlm.nih.gov/genbank/wgs.submit.html)
*   If annotation is provided, the product names should follow the [UniProt-Protein Naming Guidelines](http://www.uniprot.org/docs/nameprot).
*   Annotation must be biologically valid (and error-free).

### How to Submit to WGS

Submission details can be found in the [WGS Submission Guide](/~/wgs.submit).

See the [Metagenome Submission Guide](/~/metagenome) for information about how to submit the various elements of a metagenome project.

WGS projects without annotation require at least two weeks to be processed. Projects with annotation require at least one month for processing. Please submit your project with enough lead time.

We recommend sending us a test file if you have a large annotated genome to see if there are problems before committing to generating the entire project.

### How to Update an Existing WGS Submission

See [Update Genome Resources](http://www.ncbi.nlm.nih.gov/genbank/wgs_update)

### Should not be submitted to WGS

*   Assemblies from sequences not directly sequenced by the submitter.
*   A single assembly from multiple organisms.
*   Complete organellar and viral genomes. They should be submitted as regular GenBank records.  See [GenBank Submissions](http://www.ncbi.nlm.nih.gov/genbank/) for more information on how to submit these types if sequences. If the organelle belongs to an already submitted WGS genome, then include the WGS accession and BioProject and BioSample identifiers (PRJNAxxxxxx and SAMNxxxxxx, respectively) in the Comments box during submission.
*   [Complete genomes](/~/genomesubmit), with each of the chromosomes in single sequences should be submitted to GenBank as a complete genome via [GenomesMacroSend](http://www.ncbi.nlm.nih.gov/projects/GenomeSubmit/genome_submit.cgi). The most common complete genomes are bacteria, archaea and fungi. Complete genomes are defined for GenBank as the chromosomes, although any plasmids that are isolated with the chromosomes should be submitted too. As of July 2013, these sequences are allowed to contain gaps and are not required to include annotation. However, submitters need to know what kinds of gaps and linkage evidence are present, as described in [Gapped Format for Genome Submissions](/~/wgs_gapped). For information about annotating genomes, see the [prokaryotic annotation guide](/~/genomesubmit_annotation) or [eukaryotic annotation guide](/~/eukaryotic_genome_submission).





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



