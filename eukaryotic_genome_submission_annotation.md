# Eukaryotic Genome Annotation Guide

## Annotation

`Sequin` and `tbl2asn` use a simple, five-column, tab-delimited table of feature locations and qualifiers to generate annotation.

The format of this feature table allows different kinds of features (e.g. `gene`, `CDS` (coding region), `tRNA`, `repeat_region`) and qualifiers (e.g. `/product`, `/note`) to be indicated. The validator will check for errors such as internal stops in coding regions.

## Guidelines for [prokaryotic genome submissions](/genbank/genomesubmit) .

If you do not understand any of the instructions presented here or you have questions, please contact us by email at [genomes@ncbi.nlm.nih.gov](mailto:genomes@ncbi.nlm.nih.gov) prior to creating your submission. This will save us both a lot of time.

## Table of Contents

1.  [Prepare annotation table](#prepare_table)
    *   [Gene features](#Genes)
    *   [`locus_tag`](#`locus_tag`)
    *   [`protein_id`](#`protein_id`)
    *   [`transcript_id`](#`transcript_id`)
    *   [CDS (coding region) features](#CDS)
    *   [Partial coding regions in incomplete genomes](#Partialcodingregionsinincompletegenomes)
    *   [Gene fragments](#Gene_fragments)
    *   [Transpliced Genes](#transpliced)
    *   [Split genes on two contigs](#Splitgenesontwocontigs)
    *   [Ribosomal RNA, tRNA and other RNA features](#rRNA)
    *   [mRNA features](#mRNA)
    *   [Alternatively spliced genes](#Alternativelysplicedgenes)
    *   [Evidence Qualifiers](#Evidence_Qualifiers)
    *   [Data base cross references](#db_xref)
    *   [Gene Ontology](#GOterms)

## Prepare annotation table

The features must be in a simple five-column tab-delimited table, called the feature table. The feature table specifies the location and type of each feature for tbl2asn or Sequin to include in the GenBank submission that is created. The first line of the table contains the following basic information:

```
>Features SeqID table_name
```

The SeqID must be the same as the sequence's SeqID in the FASTA file. The table_name is optional. Subsequent lines of the table list the features. Columns are separated by tabs.

*   Column 1: Start location of feature
*   Column 2: Stop location of feature
*   Column 3: Feature key
*   Column 4: Qualifier key
*   Column 5: Qualifier value

[Figure 2](/~/eukaryotic_genome_submission_Examples#fig2) shows a sample feature table and illustrates a number of points about the feature table format. The GenBank flatfile corresponding to this table is shown in [Figure 3](/~/eukaryotic_genome_submission_Examples#fig3) . The allowed features and their qualifiers are listed in the Feature Table [documentation](/~/collab/FT/index#7.3.2) .

Features that are on the complementary strand, such as the genes Ngs_3038 and Ngs_11232 and their corresponding features shown in [Figure 2](/~/eukaryotic_genome_submission_Examples#fig2) , are indicated by reversing the interval locations.

Please avoid unnecessary capitalization in all text entered in your table.

Additional requirements, as well as suggestions for various types of annotation, are included in the following sections.

### Gene features

Gene features are always a single interval, and their location should cover the intervals of all the relevant features such as promoters and polyA binding sites.

Gene names should follow the standard nomenclature rules of the particular organism. For example, mouse gene names begin with an uppercase letter, and the remaining letters are lowercase.

Coding regions (CDS) and RNAs, such as tRNAs and rRNAs, must have a corresponding gene feature. However, other features such as repeat_regions and misc_features do not have a corresponding gene or `locus_tag`.

### `locus_tag`

All genes should be assigned a systematic gene identifier which should receive the `locus_tag` qualifier on the gene feature in the table. Genes may also have functional names as assigned in the scientific literature. In this example, KCS_0001 is the systematic gene identifier, while Abc5 is the functional gene name.

### Table view of gene with both biological name and `locus_tag`

```
1       1575    gene
                        gene    Abc5
                        `locus_tag`        KCS_0001
```

### Flatfile view

```
gene       1..1575
                     /gene="Abc5"
                     /`locus_tag`="KCS_0001"
```

### Table view of gene with only `locus_tag`

```
1 1575    gene
                        `locus_tag`     KCS_0001
```

### Flatfile view

```
gene       1..1575
                     /`locus_tag`="KCS_0001"
```

For consistency the same `locus_tag` prefix must be used throughout the entire genome. Therefore, all the chromosomes of a genome should have the same `locus_tag` prefix.

To improve the use of `locus_tag`s we are now requiring that all `locus_tag` prefixes be registered and that they be unique. We recommend having the BioProject registration process auto-assign a `locus_tag` prefix, as they are not meant to convey meaning. The `locus_tag` prefix should be 3-12 alphanumeric characters and the first character may not be a digit. The `locus_tag` prefix is followed by an underscore and then an alphanumeric identification number that is unique within the given genome. Other than the single underscore used to separate the prefix from the identification number, no special characters can be used in the `locus_tag`.

The chromosome number can be embedded in the `locus_tag`, if desired, in the format `Prefix\_`_#g#####_, where the first `#` is the chromosome number and `#####` is the unique number of the gene. For example, `Ajs_4g00123` for a gene on chromosome 4.

Read more about [`locus_tag`s](http://www.ncbi.nlm.nih.gov/genomes/locustag/Proposal.pdf) and their intended usage.

Please register your genome project and proposed `locus_tag` prefix on the [BioProject registration](https://submit.ncbi.nlm.nih.gov/subs/bioproject/) page prior to preparing your submission to GenBank. Each project that is registered here is assigned a project_id, and in the future we intend that the project_id will appear on all entries associated with a particular genome project.

The use of `locus_tag` is supported in Sequin version 4.35 or later. If you have an older version of Sequin please download the [current version](http://www.ncbi.nlm.nih.gov/Sequin/) . The latest version of tbl2asn is available from the [tbl2asn](/~/tbl2asn2) page.

### `protein_id`

All proteins in a WGS or complete genome must be assigned an identification number by the submitter. We use this number to track proteins when sequences are updated. This number is indicated in the table by the CDS qualifier `protein_id`, and should have the format gnl|dbname|string, where dbname is a version of your lab name that you think will be unique (eg SmithUCSD), and string is the unique protein SeqID assigned by the submitter. This identifier is saved with the record (in ASN.1 format), but it is not visible in the flatfile. We recommend using the `locus_tag` as the protein SeqID. In this example, the `protein_id` for `ABC5` is `gnl|SmithUCSD|KCS_0001`.

#### Example:

```
<1      >1575        gene
                        gene    Abc5
                        locus_tag    KCS_0001
1       1575    CDS
                        product      ABC5
                        protein_id   gnl|SmithUCSD|KCS_0001
```

Since the `protein_id` is used for internal tracking in our database, it is important that the complete `protein_id` (dbname + SeqID) not be duplicated by a genome center. Thus, if your genome center is submitting more than one complete genome, please be sure to use unique `protein_id`'s for all of the genomes.

The `protein_id` is also included as a qualifier on the corresponding mRNA feature, to allow the CDS and mRNA to be paired during processing.

Note that when WGS submissions are processed, the dbname in the `protein_id` is automatically changed to 'WGS:XXXX', where XXXX is the project's accession number prefix.

After your genome is released into GenBank, the proteins are assigned accession numbers. We will provide a table of the protein SeqIDs and accession numbers for you to use in future [updates](/~/eukaryotic_genome_submission#updating) .

### `transcript_id`

The `transcript_id` is included as a qualifier for both the CDS and its corresponding mRNA. It has the same format as the `protein_id`, gnl|dbname|identifier. Because each `transcript_id` and `protein_id` must be unique, we suggest adding 'mrna' or 't' to the `protein_id` identifier as a simple way to create the corresponding (unique) `transcript_id`. However, you can use whatever naming convention you choose, as long as all of the identifiers are unique.

```
63574        87173   gene
                        `locus_tag`     Ngs_17131
63574   63907   mRNA
75690   75730
84396   85536
85598   85773
85836   86109
86173   86467
86555   86670
86731   87173
                        product     hypothetical protein
                        protein_id  gnl|ncbi|Ngs_17131
                        transcript_id     gnl|ncbi|mrna.Ngs_17131
84402   85536   CDS
85598   85773
85836   86109
86173   86467
86555   86670
86731   86882
                        product     hypothetical protein
                        protein_id  gnl|ncbi|Ngs_17131
                        transcript_id     gnl|ncbi|mrna.Ngs_17131
```

### `CDS` (coding region) features

All CDS features must have a product qualifier (protein name). NCBI protein naming conventions are adopted in part from the [UniProt-Swiss-Prot Protein Knowledgebase](http://www.uniprot.org/docs/gennameprot)

Consistent nomenclature is indispensable for communication, literature searching and data retrieval. Many species-specific communities have established gene nomenclature committees that try to assign consistent and, if possible, meaningful gene symbols. Other scientific communities have established protein nomenclatures for a set of proteins based on sequence similarity and/or function. But there is no established organization involved in the standardization of protein names, nor are there any efforts to establish naming rules that are valid across the largest spectrum of species possible.

Ambiguities regarding gene/protein names are a major problem in the literature and it is even worse in the sequence databases which tend to propagate the confusion. For this reason, we ask that you follow some basic guidelines in naming your proteins. The protein naming guidelines are based on the premise that a good and stable recommended name for a protein is a name that is as neutral as possible.

#### Guidelines for naming proteins:

*   If it exists, use the approved nomenclature.
*   Use a concise name, not a description or phrase.
*   Ideally the name should be unique and attributed to all orthologs.
*   The protein name should not contain specific characteristics of the protein, and it should not reflect the function of the protein, its subcellular location, its domain structure, its molecular weight or its species of origin. This information can be included in the note.
*   In cases where the protein name is not known use "unknown" or "hypothetical protein" as the product name. We recommend the use of "hypothetical protein" as this will allow the `locus_tag` identifier to be appended to the product name in BLAST and Entrez summary lines.
*   Protein names may be denoted by the same symbol as the corresponding gene, but in the correct format for the organism. For example, mouse proteins have the same symbol as the gene name, but the protein name has all capital letters.
*   Avoid the use of molecular weights in protein names; "unicornase subunit A" is preferred to "unicornase 52 kDa subunit"
*   Do not use the term "homolog" in a protein as this infers an evolutionary relationship that has generally not been determined.
*   Where possible, avoid the use of commas in protein names
*   Use lowercase letters, except when uppercase are required (for example, in acronyms such as DNA or ATP).
*   Wherever appropriate, the name should use American spelling conventions.
*   Avoid the use of Roman numerals where possible. Use instead Arabic numbers.
*   Do not build molecular weights into abbreviations
*   For proteins that belong to a multigene family, it is recommended that you choose a coherent nomenclature with numbers to specify the different members of the family.
*   When naming proteins which can be grouped into a family based on homology or according to a notion of shared function, the different members should be enumerated with a dash "-" followed by an Arabic number. e.g. "desmoglein-1", "desmoglein-2", etc.
*   Greek letters must be written in full e.g. "alpha", and written entirely in lower case with the exception of "Delta" in the context of steroid/fatty acid metabolism nomenclature. Additionally the Greek letters that are followed by a number should be preceded or followed by a dash "-" e.g. "unicornase alpha-1".
*   Do not use diacritics, such as accents, umlauts. Many computer sytems (ours included) can only understand ASCII characters.
*   Do not use plurals in a protein name. e.g. "ankyrin repeats-containing protein 8" is wrong.
*   Proteins of unknown function which contain a defined domain or motif, can be named according to the domain present. The name should be of the following type: "<domain|repeat>-containing protein". e.g. "PAS domain-containing protein 5".

Here are some examples of good protein names:

<dl class="goodbad">

<dt>**cytochrome b**</dt>

<dt>**CytB**</dt>

<dt>**aconitate hydrase B**</dt>

<dt>**hypothetical protein**</dt>

<dt>**cytochrome b-like protein**</dt>

<dt>**4Fe-4S cluster binding protein**</dt>

<dt>**adenylyltransferase/ADP-heptose synthase**</dt>

<dt>**2-hydroxyhepta-2,4-diene-1,7-dioate isomerase**</dt>

<dt>**short-chain specific acyl-CoA dehydrogenase**</dt>

<dt>**formylmethanofuran--tetrahydromethanopterin formyltransferase**</dt>

<dt>**serine/threonine-protein kinase**</dt>

<dt>**translation initiation factor 1**</dt>

<dt>**triphosphoribosyl-dephospho-CoA synthetase**</dt>

<dt>**thiamine biosynthesis protein ThiC**</dt>

<dt>**PAS domain-containing protein 5**</dt>

<dt>**ABC transporter ATP-binding protein AlbC**</dt>

<dt>**stage 0 sporulation protein J**</dt>

<dd>_These names all concisely describe the function of the protein, where known, and avoid references to structure, homology and species._</dd>

</dl>

Here are some examples of bad protein names:

<dl class="goodbad">

<dt>**required for the efficient incorporation of molybdate into molybdoproteins**</dt>

<dd>_This describes the protein's role in a biosynthetic process but is not a protein name._</dd>

<dt>**chaperone Hsp70; DNA biosynthesis; autoregulated heat shock proteins**</dt>

<dd>_The name "chaperone Hsp70" is fine however the remaining comments would be best fielded as a note or in the function qualifier._</dd>

<dt>**putative carbonic anhdrase (EC 4.2.1.1)**</dt>

<dd>_The EC number should not be part of the protein name but instead fielded in the EC_number qualifier_</dd>

<dt>**similar to aconitrate hydrase B**</dt>

<dd>_This statement is fine as a note, however as a protein name aconitrate hydrase B-like protein is preferred_</dd>

<dt>**related to protein of unknown function**</dt>

<dd>_uninformative name_</dd>

<dt>**cytochrome b-like**</dt>

<dd>_cytochrome b-like protein is preferred_</dd>

<dt>**ABC transporter related**</dt>

<dd>_vague name, there are many ABC transporters and subunits, be more specific_</dd>

<dt>**pirin, N-terminal:pirin, C-terminal**</dt>

<dd>_uniformative name noting similarity in N and C terminus_</dd>

<dt>**helix-turn-helix motif**</dt>

<dd>_Describes a motif or structural domain but is not an appropriate protein name._</dd>

<dt>**PP-loop**</dt>

<dd>_Describes a motif or structural domain but is not an appropriate protein name._</dd>

<dt>**alpha/beta hydrolast fold**</dt>

<dd>_Describes a motif or structural domain but is not an appropriate protein name._</dd>

<dt>**pentapeptide repeat**</dt>

<dd>_Describes a motif or structural domain but is not an appropriate protein name._</dd>

<dt>**phosphopantetheine-binding domain**</dt>

<dd>_Describes a motif or structural domain but is not an appropriate protein name._</dd>

<dt>**protein of unknown function:conserved**</dt>

<dd>_uninformative name_</dd>

<dt>**hypothetical 32.5 kDa protein homologous to phytoene and squalene synthethases**</dt>

<dd>_Hypothetical protein alone is appropriate. The remaining comments should be fielded as a note._</dd>

<dt>**ribosomal protein L3 (E. coli)**</dt>

<dd>_Protein names should not contain references to organism names. Ribosomal protein L3 is an appropriate name by itself._</dd>

<dt>**saccharopine dehydrogenase or related protein**</dt>

<dd>_"saccharopine dehydrogenase" or "saccharopine dehydrogenase-like protein" would be more appropriate_</dd>

<dt>**tyrosine-protein kinase (capsular polysaccharide biosynthesis)**</dt>

<dd>_tyrosine-protein kinase is fine as a protein name but capsular polysaccharide biosynthesis would be more appropriate as a function._</dd>

<dt>**RimM protein, required for 16S rRNA processing**</dt>

<dd>_RimM is fine as a protein name but descriptive comments should be placed in the note._</dd>

<dt>**involved in flagellar biosynthesis**</dt>

<dd>_This is a functional comment and not a protein name._</dd>

</dl>

#### Notes

Please avoid including notes indicating a specific percentage of similarity to other entries in the database, since the corresponding record that you have pointed to may change and make your current note inaccurate, incorrect and obsolete. Descriptions, notes describing similarity to other proteins, and functional comments must be placed in the appropriate CDS qualifiers such as note, or prot_desc, as they are descriptors of the product. E.C. numbers must be fielded in an EC_number qualifier.

```
start      stop    CDS
                        product     DNA gyrase subunit B
                        EC_number   5.99.1.3
```

Qualifiers that can be used on the CDS feature are:

```
start    stop    CDS
                        product
                        prot_desc
                        function
                        EC_number
                        note
                        experiment
                        inference
                        go_component
                        go_process
                        go_function
                        db_xref
                        pseudo
                        exception
                        transl_except
```

Multiple `note` qualifiers are supported. tbl2asn or Sequin concatenate multiple `note` qualifiers into a single `note` with semicolons as separators.

#### Bifunctional proteins:

If a protein contains two separate and distinct functions or if it has more than one name, these can be annotated in several ways, as outlined below. Table view:

```
start  stop    CDS
                        product     adenylyltransferase/ADP-heptose synthase
                        note   bifunctional

```

or

```
start    stop    CDS
                        product     bifunctional adenylyltransferase/ADP-heptose synthase cyclohydrolase

```

or

```
start    stop    CDS
                        product     FolD 
                        function    adenylyltransferase
                        function    ADP-heptose synthase cyclohydrolase
                        note   bifunctional

```

### Partial coding regions in incomplete genomes

To annotate an partial coding region, you should use the "<" or ">" in your feature table to designate the feature as either 5' or 3' partial. The coding region should begin at the first nucleotide present, however the translation will start at the first complete codon.

#### Example

In the first example below, the "<" designates this coding region as 5' partial and "codon_start 3" tells the software to start translation with the third nucleotide of the CDS. Note that if the codon_start is not specified, then the software assumes a codon_start of 1\. The second coding region below is partial at the 3' end so ">" is used to indicate a 3' partial feature.

```
<1  497     CDS
                        product       ABC5
                        note   similar to Bacillus subtilis aldolase
                        codon_start  3
                        protein_id   gnl|dbname|KCS_0001
                        transcript_id   gnl|dbname|KCS_mrna0001

600     >1575        CDS
                        product         actin-like protein
                        protein_id      gnl|dbname|KCS_0002
                        transcript_id   gnl|dbname|KCS_mrna0002

```

Here are [more examples of formatting partial CDS features](/~/examples.wgs#partialcds) .

Partial genes within a sequence should begin or end at consensus splice sites.

The use of partial coding regions is reserved for incomplete genomes only. All coding regions annotated on finished genomes should be complete at both the 5' and 3' ends.

#### Gene fragments

Sometimes a genome will have adjacent or nearby genes that seem to be only part of a protein. In many cases these indicate a possible problem with the sequence and/or annotation. A related issue is the presence of internal stop codons in the conceptual translation of a CDS that looks like it should be a real CDS. These problems may be due to a variety of reasons, including mutations or sequencing artifacts. They can be annotated in a number of ways:

1.  Annotate the gene as a pseudogene. If multiple gene fragments were present initially, then add a single gene feature which covers all of the potential coding regions and add the pseudo qualifier indicating that this is a pseudogene. If known, a note qualifier may be added indicating why this gene is disrupted.

```
1    200     gene
                            gene    Abc5
                            `locus_tag`        KCS_0001
                            gene_desc       alkaline phosphatase
                            pseudo
                            note    frameshift

    
```

2.  Alternatively, if you are not sure if the disrupted gene is a "pseudogene" you can just use a gene feature without the /pseudo. Please use the complete nucleotide spans of the frameshifted gene. If known, the reason for the incomplete translation can be included in a note.

```
1  200     gene
                            gene    Abc5
                            `locus_tag`        KCS_0001
                            gene_desc       alkaline phosphatase
                            note    nonfunctional due to frameshift

    
```

3.  If the feature is just noting a similarity to genes in the database and is probably not translated, then it should be annotated as a misc_feature without a corresponding gene feature.

```
1  200     misc_feature
                            note    similar to Abc5

    
```

#### Transpliced Genes

Transpliced genes are the exception to the rule for annotating gene feature spans. Transpliced genes are similar to intron-containing genes, except that the two pieces of the gene occur on different regions of the chromosome. These genes are transcribed as two or more separate RNA products that are transpliced into a single mRNA or tRNA. To annotate this using a table, enter the nucleotide spans so that the complementary (minus strand) spans are arranged from high to low, and vice-versa for the plus strand.

```
36700   36618   gene
86988   87064
                        `locus_tag`    NEQ_t38
                        exception    trans-splicing
36631   36618   misc_feature
                        note    sequence cleaved during processing of trans-spliced tRNAs
36673   36635
87030   87064   tRNA
                        product tRNA-Glu
                        exception    trans-splicing
                        note    this trans-spliced tRNA consists of two halves on mixed strands; it shares a 3' half with another tRNA
```

```
gene            join(complement(36618..36700),86988..87064)
                     /`locus_tag`="NEQ_t38"
                     /trans_splicing
     misc_feature    complement(36618..36631)
                     /`locus_tag`="NEQ_t38"
                     /note="sequence cleaved during processing of trans-spliced tRNAs"
     tRNA            join(complement(36635..36673),87030..87064)
                     /`locus_tag`="NEQ_t38"
                     /product="tRNA-Glu"
                     /trans_splicing
                     /note="this trans-spliced tRNA consists of two halves on
                     mixed strands; it shares a 3' half with another tRNA"
```

#### Split genes on two contigs

Sometimes, in incomplete genomes, the ends of a gene may be on different contigs. When you are certain that the two pieces are part of the same gene, annotate these as separate genes with unique `locus_tag` features, plus separate `CDS`/`mRNA` features with different `protein_id` and `transcript_id` qualifiers. In addition, link the features together with `note` qualifiers that refer to the other part of the gene. However, do not create extremely short features; for example, if one end is only the start methionine, or only a few amino acids before the stop codon.

#### Example

```
>Feature Cont01.00111
5000    >7500        gene
                        `locus_tag`     KCS_2223A
5000    5500    mRNA
6000    >7200
                        product       enolase
                        protein_id    gnl|dbname|KCS_2223A
                        transcript_id    gnl|dbname|KCS_mrna2223A
5488    5500    CDS
6000    >7200
                        product       enolase
                        protein_id    gnl|dbname|KCS_2223A
                        transcript_id    gnl|dbname|KCS_mrna2223A
                        note   5' end; 3' end is gene KCS_2223B on contig Cont01.00224
```

```
>Feature Cont01.00224
<1   1000    gene    
                        `locus_tag`    KCS_2223B
<100 1000    mRNA
                        product      enolase
                        protein_id   gnl|dbname|KCS_2223B
                        transcript_id    gnl|dbname|KCS_mrna2223B
<100 876     CDS
                        product      enolase
                        protein_id   gnl|dbname|KCS_2223B
                        transcript_id    gnl|dbname|KCS_mrna2223B
                        note   3' end; 5' end is gene KCS_2223A on contig Cont01.00111

```

#### Ribosomal RNA, tRNA and other RNA features

RNA features (rRNA, tRNA, ncRNA) need a corresponding gene feature with a `locus_tag` qualifier. If the amino acid of a tRNA is unknown, use tRNA-Xxx as the product, as in the example. Many submitters like to label the tRNAs such as tRNA-Gly1, etc. If you wish to do this please include "tRNA-Gly1" as a note and not in /gene. The use of /gene is reserved for the actual biological gene symbol such as "trnG". If a tRNA is a pseudogene, please use the /pseudo qualifier.

Annotate ncRNAs that belong to one of the INSDC [nRNA_class](http://www.insdc.org/documents/ncrna-vocabulary) as an ncRNA feature, with the appropriate value in the required /ncRNA_class qualifier. Regions of an RNA should be annotated as a misc_feature (eg, leader sequences), or a misc_binding feature if they bind a known molecule (eg, riboswitches). If the RFAM identifier is known, it can be included as a [db_xref](#db_xref).

Some rRNA, tRNA and ncRNA examples:

```
<1      400     gene
                        `locus_tag`       KCS_00011
<1      400     rRNA
                        product 16S ribosomal RNA
488     560     gene
                        `locus_tag`       KCS_00012
488     560     tRNA
                        product tRNA-Lys
570     601     gene
                        `locus_tag`       KCS_00020
                        pseudo
570     601     tRNA
                        product tRNA-Phe
                        pseudo
700     780     gene
                        `locus_tag`       KCS_00013
700     780     tRNA
                        product tRNA-Xxx
900     923     gene
                        `locus_tag`       KCS_00014
900     923     ncRNA
                        ncRNA_class     miRNA
                        product mir-9c
950     1000    gene
                        `locus_tag`       KCS_00015
950     1000    tmRNA
                        product tmRNA

```

`misc_feature` and `misc_binding` features do not have an associated `gene` feature. To tag these features with a `locus_tag`-like identifier, include that value in the `note`, separated from other information by a semicolon and space.

Riboswitches should be annotated using the `misc_binding` feature if the bound moiety is known; for example:

```
1     100    misc_binding
                        note cobalamin riboswitch
                        bound_moiety adenosylcobalamin
```

If the bound moiety is unknown or if the sequence is a leader sequence, annotate as a `misc_feature, for example:

```
1     100    misc_feature
                        note yybP-ykoY element
```

#### mRNA features

Include an mRNA feature for each translated CDS. Several things to note are:

*   Use the same product name for the mRNA and its corresponding CDS.
*   If there is no UTR information, then the mRNA's location will agree with its CDS's location, but the mRNA will be partial at its 5' and 3' ends.
*   Extend the gene feature to include the entire mRNA.
*   If the mRNA is partial, then make the gene partial.

#### Example

The first example is a complete `CDS` whose 5' and 3' UTRs are known.

```
>Feature Cont54
10400   12512   gene
                        locus_tag    CCC_03116
10400   10462   mRNA
10533   10577   
10651   11098   
11182   11642   
11716   12512   
                        product     hypothetical protein
                        protein_id  gnl|dbname|CCC_03116
                        transcript_id    gnl|dbname|CCC_mrna03116
10450   10462   CDS
10533   10577   
10651   11098   
11182   11642   
11716   12233   
                        product     hypothetical protein
                        protein_id  gnl|dbname|CCC_03116
                        transcript_id    gnl|dbname|CCC_mrna03116

```

The second example is a `CDS` that is partial at the 5' end and lacks any 3' UTR information.

```
>Feature Cont3
<1   >497 gene             
                        locus_tag CCC_111011
<1   497     CDS             
                        note    similar to Bacillus subtilis aldolase
                        product   aldolase-like protein
                        codon_start     3
                        protein_id   gnl|dbname|CCC_111011
                        transcript_id    gnl|dbname|CCC_mrna111011
<1   >497 mRNA             
                        product   aldolase-like protein
                        protein_id   gnl|dbname|CCC_111011
                        transcript_id    gnl|dbname|CCC_mrna111011

```

### Alternatively spliced genes

In many cases a gene can be alternatively spliced, yielding alternative transcripts. These transcripts may differ in the coding region and produce different products, or they may differ in the non-translated 5' or 3' UTR and produce the same protein. To annotate alternatively spliced genes, include one `mRNA` and `CDS` for each transcript, and include only one gene over all of the features. Give the corresponding `mRNA` and `CDS` the same name, and include a `note` with the value `alternatively spliced` on each. If there are multiple `CDS` with the same name, then add a `note` to each `mRNA` and `CDS` to refer to each other; e.g., `transcript variant A` and `encoded by transcript variant A` for one `mRNA`/`CDS` pair. If the `CDS` have different translations, then they should have different product names. Make sure that all the proteins have unique `protein_id` values.

#### Examples

Example 1 (different products):

```
>Feature Cont01.00055
10      5000    gene    
                        locus_tag    CCC_04562
10      500     mRNA
722     1555
2548    3901
4400    5000
                        product     CCC_04562 isoform A
                        note alternatively spliced
                        protein_id  gnl|dbname|CCC_04562A
                        transcript_id   gnl|dbname|CCC_mrna04562A
102     500     CDS
722     1555
2548    3901
4400    4566
                        product    CCC_04562 isoform A
                        note alternatively spliced
                        protein_id  gnl|dbname|CCC_04562A
                        transcript_id   gnl|dbname|CCC_mrna04562A
10      500     mRNA
2548    3901
4400    5000
                        product     CCC_04562 isoform B
                        note alternatively spliced
                        protein_id  gnl|dbname|CCC_04562B
                        transcript_id   gnl|dbname|CCC_mrna04562B
102     500     CDS
2548    3901
4400    4566
                        product     CCC_04562 isoform B
                        note alternatively spliced
                        protein_id  gnl|dbname|CCC_04562B
                        transcript_id   gnl|dbname|CCC_mrna04562B
```

Example 2 (same product):

```
>Feature Cont01.00056
100     1000    gene
                        locus_tag    CCC_03222
100     333     mRNA
444     678
800     1000
                        product     hypothetical protein
                        note    transcript variant A; alternatively spliced
                        protein_id  gnl|dbname|CCC_03222A
                        transcript_id   gnl|dbname|CCC_mrna03222A
456     678     CDS
800     865
                        product     hypothetical protein
                        note    encoded by transcript variant A; alternatively spliced
                        protein_id  gnl|dbname|CCC_03222A
                        transcript_id   gnl|dbname|CCC_mrna03222A
100     360     mRNA
444     678
800     1000
                        product     hypothetical protein
                        note    transcript variant B; alternatively spliced
                        protein_id  gnl|dbname|CCC_03222B
                        transcript_id   gnl|dbname|CCC_mrna03222B
456     678     CDS
800     865
                        product     hypothetical protein
                        note    encoded by transcript variant B; alternatively spliced
                        protein_id  gnl|dbname|CCC_03222B       
                        transcript_id   gnl|dbname|CCC_mrna03222B       
```

### Evidence Qualifiers

The International Nucleotide Sequence Database Collaboration, DDBJ, EMBL and GenBank has adopted a set of new qualifiers to describe the evidence for feature annotation in GenBank records. These are:

/experimental="text" /inference="TYPE:text", where 'TYPE' is from a select list and 'text' is structured text.

The use of the new evidence qualifiers is supported in Sequin version 6.0 or later, and tbl2asn version 5.1 or later. If you have an older version, please download the current version of [Sequin](http://www.ncbi.nlm.nih.gov/Sequin/) or [tbl2asn](/~/tbl2asn2) .

These new qualifiers replace /evidence=experimental and /evidence=non-experimental, respectively, which will no longer be supported.

See more information about the [Evidence Qualifiers](/~/evidence) .

#### Database cross references

A variety of database cross references can be added to a feature. These appear as /db_xref on the features. This qualifier serves as a vehicle for linking of sequence records to other external databases. See the full list of [db_xref](/~/collab/db_xref) databases.

```
1     100   CDS
                product     RecA
                protein_id  gnl|center_name|Test_0001
                db_xref InterPro:IPR000111

180     210    misc_feature
                        note yybP-ykoY element
                        db_xref RFAM:RF00080
```

#### Gene Ontology

GO (Gene Ontology) terms can be included in genomes in order to describe protein functionality. Gene Ontology (GO) terms can be indicated with the following qualifiers

```
1       100     CDS
                        product helicase
                        go_process      chromatin assembly or disassembly|0006333||IEA
                        go_process      antimicrobial humoral response|0019730|16163390|IMP
                        go_component    nucleus|0005634|14668392|IDA
                        go_component    chromatin|0000785||IEA
                        go_function     ATP-dependent helicase activity|0008026||ISS
                        go_function     nucleic acid binding|0003676||IEA
                        go_function     ATP binding|0005524||IEA

```

The value field is separated by vertical bars '|' into a descriptive string, the GO identifier (leading zeroes are retained), and optionally a PubMed ID and one or more evidence codes. The evidence code is the fourth token, so include blank fields, as necessary (eg the last qualifier has no PubMed ID so the third field is blank).
