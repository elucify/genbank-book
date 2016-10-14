
# WGS Frequently Asked Questions

*   [Can I submit annotation as a GenBank flatfile?](#q1)
*   [I want all of the WGS contigs in my assembly available to users. Should I put unlink WGS contigs into the AGP?](#q2)
*   [Can I submit an assembly and have it held back until I publish my paper?](#q3)
*   [I'm using second generation sequencing technology. Can I still submit an assembly?](#q4)
*   [Do I need to split the sequences at the Ns that were inserted by the assembler, eg Velvet or Abyss?](#q5)
*   [What should I use for the gap sizes?](#q6)
*   [I concatenated the sequences into the correct order with Ns between each sequence and annotated this pseudomolecule. Can I submit this annotated pseudomolecule?](#q7)
*   [I concatenated the sequences in a random order with Ns between each sequence and annotated the pseudomolecule. Can I submit the annotated pseudomolecule?](#q8)
*   [Can I annotate across gaps?](#q9)
*   [Do I need to submit my genome assembly with annotation?](#q10)
*   [Does NCBI have an annotation pipeline that can be used to annotate my assembly?](#q11)
*   [If I do have my own annotation, in what format should I provide this data?](#q12)
*   [My genome assembly has contigs and scaffolds. Should I submit the annotation on the contigs or the scaffolds?](#q13)
*   [Do I have to register a separate BioProject for each genome I am sequencing?](#multi)
*   [Can I submit RAST annotation?](#rast)

## 1\. Can I submit annotation as a GenBank flatfile?

In general, we cannot accept annotation a GenBank, EMBL or DDBJ flat file. To submit annotation, follow the instructions given for [Prokaryotic annotation](/~/genomesubmit.html) or [Eukaryotic annotation](/~/eukaryotic_genome_submission.html). However, you can use the [RAST conversion scripts](#rast) to make the correct file for submission from a .gb file, although there may still be problems that need to be fixed to create a GenBank submission.

## 2\. I want all of the WGS contigs in my assembly available to users. Should I put singleton WGS contigs into the AGP?

The AGP file defines the assembly, so typically we do want all of the WGS contigs in the AGP file. However, contigs that are not considered to be part of the assembly, perhaps because they are degenerate or duplicates, should not be included in the AGP file. In addition, remove from the submission any sequences that are <200 bp and are not part of multi-component scaffolds.

## 3\. Can I submit an assembly and have it held back until I publish my paper?

Yes, you may submit your assembly and have it held until publication.

## 4\. I'm using second generation sequencing technology. Can I still submit an assembly?

Yes, you may submit assemblies using second generation sequencing technology. The process is analogous to using Sanger technology. The primary second generation reads should be submitted to the [Sequencing Read Archive](http://www.ncbi.nlm.nih.gov/sra). The reads should be assembled into WGS contigs and submitted as described in the [submission instructions](/~/wgs.submit). These WGS contigs can be used to assemble higher order molecules and submitted using an AGP file, as described in the [submission instructions](/~/wgs.submit).

## 5\. Do I need to split the sequences at the Ns that were inserted by the assembler, eg Velvet or Abyss?

No, you now have the option to submit the sequences that represent biological molecules (chromosomes or scaffolds) as a [Gapped submission](/~/wgs_gapped) with the Ns representing gaps presented as assembly_gap features with the appropriate linkage evidence. However, sequences concatenated in unknown order are not allowed. The original submission format, of splitting the sequences at the runs of Ns into contigs and rebuilding the scaffolds with an AGP file, remains an option.

## 6\. What should I use for the gap sizes?

If you have estimates of the gap sizes, then use those values for the gaps. We prefer that you use 10 as the minimum gap size, to be more of a signal to database users. If you do not have an estimate of the gap size, then the preference is to use 100 as the value and the 'U' in column five of the [AGP](http://www.ncbi.nlm.nih.gov/projects/genome/assembly/agp/AGP_Specification.shtml) file, indicating that the gap size is unknown. For a Gapped submission, use 100 Ns and -a r#u (with the appropriate number in place of #; case 2 or 3 in the [Gapped submission](/~/wgs_gapped) examples).

## 7\. I concatenated the sequences into the correct order with the Ns between each sequence and annotated the pseudomolecule. Can I submit this annotated pseudomolecule?

Yes, now that gapped submissions are allowed; however, you will need to include the correct gap and linkage evidence for each run of Ns that represent a gap. If all the gaps have the same linkage evidence, then you can make the appropriate submissions simply with tbl2asn, as [described](/~/wgs_gapped).

## 8\. I concatentated the sequences in a random order with Ns between each sequence and annotated this pseudomolecule. Can I submit the annotated pseudomolecule?

Since the annotated sequence does not correspond to a biological molecule, you need to split the pseudomolecule into the contig sequences and submit those as the pieces of a wgs project. You will need to map the annotation down to the contig level, but can use the offset in the .tbl file to avoid recalculating if desired, as shown [here](http://www.ncbi.nlm.nih.gov/Sequin/table.html).

## 9\. Can I annotate across gaps?

Annotation is allowed to cross gaps of estimated size, but not those of unknown sizes. However, annotation across gaps is discouraged unless there is evidence that the translation on the other side of the gap is in the correct frame. In addition, if >50% of the translation is Xs (i.e. in the gap) then the CDS should be made partial at the gap, or split into two partial CDSs, as described for [genes split across two contigs](/~/eukaryotic_genome_submission_annotation.html#Splitgenesontwocontigs), depending upon the confidence of the translation on both sides of the gap.

## 10\. Do I need to submit my genome assembly with annotation?

No, you can submit the genome without any annotation. However, you may request that a prokaryotic genome assembly be annotated by NCBI's [Prokaryotic Genome Annotation Pipeline](#q11) before its release into GenBank.

## 11\. Does NCBI have an annotation pipeline that can be used to annotate my assembly?

You can request that NCBI annotate complete or incomplete prokaryotic genomes using our [Prokaryotic Genome Annotation Pipeline](http://www.ncbi.nlm.nih.gov/genome/annotation_prok/) during the [submission process](http://www.ncbi.nlm.nih.gov/genbank/wgs.submit#pgaap). The NCBI [Eukaryotic Genome Annotation pipeline](http://www.ncbi.nlm.nih.gov/genome/annotation_euk/) is not generally available as a GenBank submitter resource.

## 12\. If I do have my own annotation, in what format should I provide this data?

Annotation must be in the 5-column feature table described in [tbl2asn](http://www.ncbi.nlm.nih.gov/genbank/tbl2asn2.html) and the [Eukaryotic](http://www.ncbi.nlm.nih.gov/genbank/eukaryotic_genome_submission_annotation.html) and [Prokaryotic](http://www.ncbi.nlm.nih.gov/genbank/genomesubmit_annotation.html) annotation instructions.  
The 5-column feature table is saved as a file with the suffix .tbl, and that file is used in conjunction with the template, fasta, and optional quality score files to create the annotated genome file for submission to GenBank, as described on the [tbl2asn](http://www.ncbi.nlm.nih.gov/genbank/tbl2asn2.html) page. The .sqn file(s) that is the output of running tbl2asn and the .tbl file (for eukaryotes) are submitted to GenBank.

However, the [RAST conversion scripts](#rast) are able to convert some flatfile formats into a GenBank submission.

## 13\. My genome assembly has contigs and scaffolds. Should I submit the annotation on the contigs or the scaffolds?

Eukaryotic genomes, which usually have thousands of contigs and hundreds or thousands of scaffolds, should be annotated at the scaffold level. Small genomes, eg prokaryotic, can be annotated at either level. However, processing of those small genomes will be quicker if the annotation is on the contigs.

## 14\. Do I have to register a separate BioProject for each genome I am sequencing?

If multiple cultured genomes are part of the same research effort, then they can belong to the same BioProject. However, each culture must be registered as a separate BioSample.

Metagenomic assemblies, where multiple genomes are assembled with high confidence from a single metagenomic sample, are handled differently. In those cases use the same BioSample for every genome that is assembled from that sample, and register a separate BioProject for each. The reason for this is because a unique locus_tag prefix is assigned to a BioSample/BioProject pair, and it is important to keep the same BioSample to help users more easily recognize that the genomes were assembled from the same sample.

## 15\. Can I submit RAST annotation?

We are currently working on a prototype that will convert flatfile formats created by outside programs into a 5 column feature table. Part of the problem is that GenBank type files from other sources often contain qualifiers that are not recognized by GenBank so they can't be converted. Conversely, features or qualifiers that are required by GenBank may be missing. In addition, there may be errors such as internal N's representing gaps, invalid translations or unacceptable protein names that need to be addressed.

We are working to make a simpler conversion system, but for now to convert the flatfile (.gb) file from RAST to a .sqn file for GenBank submission, get the scripts from the scripts directory on the NCBI ftp site: [ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/converters/scripts/](ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/converters/scripts/)

*   gbf2tbl.pl
*   rast2sqn.sh
*   rastbatch.sh
*   tblfix.pl

In addition, provide the following:

*   a template file (created at [http://www.ncbi.nlm.nih.gov/WebSub/template.cgi](http://www.ncbi.nlm.nih.gov/WebSub/template.cgi))
*   flatfile from RAST (*gb)
*   locus tag prefix (whatever is registered in BioProject for this genome)
*   protein_id prefix (an abbreviation of your lab name that you think will be unique)

usage:

*  ``./rast2sqn.sh template flatfile locus_tag_prefix protein_id_prefix``

for example:

input:

*   flatfile = TEST.gb
*   template file = template.sbt
*   locus_tag prefix = AAA
*   protein_id_prefix = xx

command line:

*   ```./rast2sqn.sh template.sbt TEST.gb AAA xx```

output:

*   TEST.sqn
*   TEST.fsa
*   TEST.tbl
*   TEST.val = validation
*   errorsummary.val = summary of validation
*   TEST.dsc = discrepancy report
*   TEST.err = qualifiers that couldn't be converted
*   TEST.ecn = EC_numbers that are not found at ftp://ftp.expasy.org/databases/enzyme/enzyme.dat
*   TEST.fixedproducts = product names found by the discrepancy report typo, hypothetical protein, and American spelling categories that are automatically corrected

You will need to [review the validation and discrepancy reports](/~/wgs.submit#Fix) and make any necessary corrections to the .sqn file. Some of the product names will probably need to be improved. See the [Prokaryotic Genome Guidelines](/~/genomesubmit) for more information about NCBI protein naming conventions. [Submit](/~/wgs.submit#Submit) the .sqn file, as described.
