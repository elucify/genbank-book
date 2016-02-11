
# Common Discrepancy Reports

### Introduction

The Discrepancy Report is an evaluation of a single or multiple ASN.1 files, looking for suspicious annotation or annotation discrepancies that NCBI staff has noticed commonly occur in genome submissions, both complete and incomplete (WGS). A few of the problems that this function was written to find include inconsistent locus_tag prefixes, missing protein_id's, missing gene features, and suspect product names. The function is available in specially configured Sequin, as an argument for tbl2asn, or with the command-line program asndisc.

If you have questions about the Discrepancy Report, please contact us by email at [genomes@ncbi.nlm.nih.gov](mailto:genomes@ncbi.nlm.nih.gov) prior to sending us your submission.

For more information about annotation requirements, be sure to read the appropriate annotation guidelines:

*   [Prokaryotic Genome Guidelines](/~/genomesubmit)
*   [Eukaryotic Genome Guidelines](/~/eukaryotic_genome_submission)

.

You may be interested to know that NCBI has a publicly available [Prokaryotic Genomes Annotation Pipeline](http://www.ncbi.nlm.nih.gov/genomes/static/Pipeline.html) . This pipeline generates files that are ready for submission to GenBank, although the submitter is welcome to edit them before submission to GenBank.

### Common Discrepancy Report Categories

<pre>MISSING_GENES
  -every CDS, rRNA, tRNA and ncRNA must have a gene feature with a locus_tag.  This report 
  may also occur if the gene is present, but the nucleotide spans do not completely 
  contain the corresponding feature.

EXTRA_GENES
  -Looks for genes that do not have corresponding features.  This may be OK if these 
    represent pseudogenes that are not translated. If this is the case, be sure to 
    include a brief note with the gene.  For example "similar to protein X; may 
    contain a frameshift"

BAD_LOCUS_TAG_FORMAT
  -The correct format for a locus_tag is prefix_uniqueID  (i.e. ABC_0001).   For more 
    information about locus_tags, see http://www.ncbi.nlm.nih.gov/genomes/lltp.cgi  
    If you haven't already, register your project and a locus_tag prefix here: 
    http://www.ncbi.nlm.nih.gov/genomes/mpfsubmission.cgi. 

MISSING_LOCUS_TAGS
  -every gene must have a locus_tag

DUPLICATE_LOCUS_TAGS
  -every locus_tag should be unique.  The only exception is if a gene is split across a gap.

INCONSISTENT_LOCUS_TAG_PREFIX
  -All of the locus_tags must have the same prefix, before the underscore. If you would 
    like to differentiate RNA genes or plasmid genes, you could add a letter after the 
    underscore (i.e ABC_r0001 or ABC_p0001).  The only punctuation allowed in a locus_tag 
    is the underscore.

DUPLICATE_GENE_LOCUS
  -more than one gene includes the same biological gene name.  This may be Ok if there 
    are multiple copies of the same gene in the genome

NON_GENE_LOCUS_TAG
  -locus_tags should only be used on gene features

DISC_COUNT_NUCLEOTIDES
  -counts the number of nucleotide sequences

MISSING_PROTEIN_ID
  -every CDS feature (unless they are labeled as pseudo) must have a protein_id.  The basic 
    format is:
        protein_id      gnl|dbname|OBB_0001
    where dbname is an abbreviation for your lab or institute and OBB_0001 is a unique 
    identifier (usually the same as the locus_tag)

INCONSISTENT_PROTEIN_ID
  -all of the protein_ids should include the same dbname

FEATURE_LOCATION_CONFLICT
  -the nucleotide location of the gene feature does not match the nucleotide location of 
    the corresponding rRNA, TRNA, tmRNA, or ncRNA

EC_NUMBER_NOTE
  -EC numbers should be annotated as EC_number qualifiers on the CDS feature, not as notes 
    or product names.  However an EC number may be included in a note if it refers to 
    another protein.

EC_NUMBER_ON_UNKNOWN_PROTEIN
  -We do not expect to see the EC numbers on proteins named "hypothetical protein".  If 
    there is enough information to add an EC number, please use a more informative 
    product name.  Otherwise, remove the EC number.

PSEUDO_MISMATCH
  -a feature includes a pseudo qualifier but the corresponding gene feature is not labeled.  
    The pseudo qualifier is required on the gene feature.

JOINED_FEATURES
  -Joined features are not expected in prokaryotic submissions since introns are rare 
    in bacteria.  This may be OK if the CDS includes an exception (e.g., ribosomal slippage). 
    Joined features are expected in eukaryotic submissions.

OVERLAPPING_CDS
  -indicates that two CDS features overlap and have similar product names, suggesting 
    that they may represent a frameshifted gene that is annotated in two separate genes.  
    [Since ABC-type transporter genes often overlap, they are not reported.] If these 
    genes are not found biologically as two separate proteins, then they should be annotated 
    as a single gene with a /pseudo qualifier to indicate the gene is non-functional. The 
    product name would be entered in the gene_description and a brief note describing the 
    problem ("frameshift") added. For example:
        1       200     gene
                        gene    phoA
                        gene_desc       alkaline phosphatase
                        locus_tag     OBB_0001
                        pseudo
                        note    nonfunctional due to frameshift

   If the situation is unclear and you want to keep the two genes in draft annotation, then 
   a note can be added to each CDS, "overlaps another CDS with the same product name", as a 
   flag to database users. This note can be added automatically when the .sqn files are made, 
   using the "-c b" argument of tbl2asn. 

OVERLAPPING_GENES
  -similar to OVERLAPPING_CDS.  The nucleotide location of one gene overlaps an adjacent 
    gene. This may be OK or it may indicate a gene with a frameshift.  If this is a 
    frameshifted gene, annotate one gene feature across the entire span, include a 
    pseudo qualifier, and include a brief note. 

ADJACENT_PSEUDOGENES
  -adjacent pseudogenes have the same gene name.  This may indicate a frameshifted gene 
    that should be combined into a single gene feature.  This can be ignored if there really 
    are two separate genes.

CONTAINED_CDS
  -One CDS feature completely contains another CDS feature.  This may be OK in a eukaryote   
    If there is a gene inside the intron of a longer gene.  However, this is not expected 
    in a prokaryote.  Often, this indicates short open reading frames that do not encode 
    REAL proteins were annotated as hypothetical proteins.  Please remove any CDS features 
    that do not represent translated proteins.

RNA_CDS_OVERLAP and CDS_TRNA_OVERLAP
  -similar to CONTAINED_CDS.  A CDS feature overlaps an RNA feature.  This is unusual 
    and may indicate a feature(s) needs to be removed.

SHORT_CONTIG and SHORT_SEQUENCES
  -We prefer not to include contigs shorter than 200 nucleotides

INCONSISTENT_BIOSOURCE
  -The organism information is not identical on all of the contigs.

PARTIAL_CDS_COMPLETE_SEQUENCE
  -Every CDS feature in a prokaryotic sequence should be complete unless it abuts the 
    end of the sequence or a gap.

TAX_LOOKUP_MISSING and TAX_LOOKUP_MISMATCH
  -Taxonomy errors can generally be ignored because they will be fixed during processing.

SUSPECT_PHRASES and DISC_SUSPICIOUS_NOTE_TEXT
  -looks for phrases in a note that may indicate a problem.  For example, 'fragment' may 
    indicate this should be a pseudogene.  We also prefer not to include percent similarity 
    information because this information is time sensitive and may change as more data 
    is added/updated.

RNA_NO_PRODUCT
  -every rRNA and tRNA should have a product name.  If you do not know the product, then 
    use "Xxx" or "tRNA-Xxx".  For example:
     100        180     gene
                                locus_tag       ABC_xxxx
     100        180     tRNA
                                product Xxx

DISC_PERCENT_N
  -an unusually large number of ambiguous bases is present.  This may indicate a low quality 
    sequence that should be trimmed or removed.

N_RUNS
  -There should not be any gaps in the individual contigs in your submission.  WGS projects 
    consist of only contigs (overlapping reads), not any supercontigs/scaffolds (assembled 
    contigs separated by gaps).  If these are gaps, you will need to split the sequences at 
    the gaps and submit each contig as a separate record.  We prefer not to include contigs 
    that are shorter than 200 nucleotides unless they are part of multi-component scaffolds.
    If you have super-contig/assembly information, you can send it to us as an AGP file to 
    indicate how the pieces of the WGS submission are assembled together.  We will use the AGP 
    file to create CON records of the scaffolds and/or chromosomes.  
    For more information about AGP files see: http://www.ncbi.nlm.nih.gov/Genbank/wgs.html#AGP 

ZERO_BASECOUNT
  -A sequence does not include a particular nucleotide; may indicate a low quality sequence; 
    could be OK if it's a short repetitive sequence.

NO_ANNOTATION
  -Typos in table headers may lead to lost annotation.  Check to be sure this is the expected 
    number of unannotated sequences.

DISC_SHORT_INTRON
  -Detects introns shorter than 10bp, which are usually not biologically correct, but are 
    present to adjust for a frameshift in the sequence.  If this is a frameshifted gene, 
    then the recommended approach is to annotate one gene feature across the entire span, 
    include a pseudo qualifier, and a brief note.

DISC_CDS_WITHOUT_MRNA
  -In eukaryotic annotation, every CDS feature should have a corresponding mRNA feature. 
    However, mRNAs are not usually included in prokaryotic annotation.

DISC_FEATURE_COUNT 
  -counts the number of each feature type.  Check to be sure this is correct

DISC_GENE_PARTIAL_CONFLICT
  -if a CDS is partial, the corresponding gene feature should also be partial.  [For 
    eukaryotes if there is no UTR information, then the mRNA and gene will agree with 
    the CDS but will be partial at both ends.]

DISC_BAD_GENE_STRAND
  -a gene and its corresponding feature should be annotated on the same strand

SHOW_HYPOTHETICAL_CDS_HAVING_GENE_NAME
   -If there is enough information to assign a gene name, then the CDS needs a 
     more informative product name than "hypothetical protein", so improve the 
     product name or remove the gene name, as appropriate.

TEST_OVERLAPPING_RRNAS
   -rRNA features should not overlap

TEST_UNUSUAL_MISC_RNA
   -misc_RNAs are unusual in a genome, consider using ncRNA, misc_binding, or misc_feature, 
    as appropriate.

DISC_QUALITY_SCORES
  -if you have quality scores, please include them.  

DISC_PARTIAL_PROBLEMS and DISC_BACTERIAL_PARTIAL_NONEXTENDABLE_PROBLEMS
  -In a eukaryotic sequence, internal partial are expected to end at splice consensus sites.  
    However, internal partials should not be present in prokaryotic submissions.  The 
    only partials expected in a prokaryotic sequence are those that abut the end of the 
    sequence or a gap.  If an internal partial is within one or two bases of the end of 
    a sequence (or a gap) it should be extended to end of the sequence (use codon_start 
    to adjust the start codon if extending the 5' end).  However, if extending the CDS 
    introduces internal stop codons, then annotate as a pseudogene or nonfunctional 
    gene with the /pseudo qualifier.

DISC_SUSPECT_RRNA_PRODUCTS and DISC_SHORT_RRNA
  -Most often seen when rRNAs are annotated based on similarity to the 5' domain of 16S rRNA. 
    Please verify the all of the rRNA is annotated.  If only part of the rRNA is present 
    because it extends off the end of a contig, the rRNA should be partial at the end of 
    the contig.  Note that rRNAs should not be partial unless they are at the end of the 
    contig.  If only a fragment of the rRNA is present, do not use an rRNA feature.  Instead, 
    either delete the feature or annotate it as a misc_feature (without a gene or locus_tag)

DISC_TRINOMIAL_SHOULD_HAVE_QUALIFIER
  -When an organism name includes qualifiers (i.e strain, subspecies, serovar. forma), the 
    qualifier should be included in the source information.  The easiest way is to include 
    this information in the fasta header.  For example:

    >ContigID [organism=Salmonella enterica subsp. enterica serovar Choleraesuis str. A50] [subspecies=enterica] [serovar=Chloeraesuis] [strain=A50]

DISC_SEGSETS_PRESENT
  -When creating a submission in Sequin, segmented sequence is an outdated submission 
    format that is no longer accepted.  Instead use the Batch option.

DISC_MISMATCHED_COMMENTS
  -The information in the comments should be identical for all of the sequences in a 
    single submission.

DISC_BAD_BACTERIAL_GENE_NAME
  -The standard format for a bacterial gene name is three lowercase letter followed by a 
    capital letter (eg, abcD)

SHORT_PROT_SEQUENCES
  -Protein sequences should be at least 50 amino acids, unless they are partial.

SUSPECT_PRODUCT_NAMES

Categories:

Remove organism from product name
Organelles not appropriate in prokaryote
Implies evolutionary relationship; change to -like protein (homolog, paralog, ortholog)
Suspicious phrase; should this be nonfunctional?
Consider adding 'protein' to the end of the product name (eg, ends with domain, fold, motif)
May contain database identifier more appropriate in note; remove from product name
Use short product name instead of descriptive phrase
Possible parsing error or incorrect formatting; remove inappropriate symbols (punctuation symbols)
Correct the name or use 'hypothetical protein'
Typo (includes replace predicted, possible, probable, candidate  with 'putative')
Use American spelling
Putative typo
	Use 'protein' instead of 'gene' as appropriate

Details:
  Typos
	-list of commonly seen typos, eg 'proteine'.  Fixed by -c f and -M arguments of tbl2asn

  Use American spelling
  	-list of commonly seen words, eg, 'sulfur' rather than 'sulphur'.  Fixed by -c f and -M arguments of tbl2asn

  Possible parsing error or incorrect formatting; remove inappropriate symbols

  Organelles not appropriate in prokaryote
        -Prokaryotic product name should not include organelle names (i.e. mitochondria, 
          golgi, chloroplast)

  Suspicious phrase may indicate this is a pseudogene
        -if you do not believe a CDS is translated into a functional protein, do not use 
          a CDS feature.  Similarly, if a CDS feature contains a frameshift, do not 
          annotate the N-terminal fragment and the C-terminal fragment as separate features. 
          It would be better to use a single gene feature with pseudo qualifier and a 
          brief note.  
        -If a feature is partial, use the appropriate partial symbol.  Do not include the 
          word partial in the product name.

   May contain database identifier more appropriate in note; remove from product name
        -locus_tags, accession numbers, database identifiers, COG names, EC_number etc 
          should not be included in product names.  Use the appropriate qualifier (eg,  
          EC_number, inference, db_xref) or use a note.

  Implies evolutionary relationship; change to "xyz-like protein"
        -Do not use homolog, paralog, or ortholog in a protein name as this infers an 
          evolutionary relationship that has generally not been determined. Instead of 
          "protein X homolog" use  "protein X-like protein", "putative protein X", or 
          just "protein X" depending on how certain you are of the protein's identity.

  Better as hypothetical protein
        -While we prefer to have biological product names, if you don't have a better 
          name use "hypothetical protein".  However, not EVERY product name in the genome 
          is allowed to be "hypothetical protein"

  Domain name, descriptive phrase or truncated name; need concise product name
        -Product names should be concise protein names, not descriptions or a domain 
          names.  If a domain name is all you have (e.g., zinc finger) then use 
          "zinc finger domain-containing protein". In addition, use protein names instead 
          of gene names (i.e. 'ABC protein' NOT 'ABC gene').

 Brackets or parenthesis [] ()
        -Brackets or parenthesis may be OK if they are part of a protein name, eg,  
          3-oxoacyl-(acyl-carrier-protein) reductase and 
          tRNA (5-methylaminomethyl-2-thiouridylate)-methyltransferase are valid names. 
          However, synonyms or descriptive phrases should not be included in product 
          names.  This information should be moved to a note.

</pre>

</div>

</div>