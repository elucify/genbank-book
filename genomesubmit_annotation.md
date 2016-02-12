# Prokaryotic Genome Annotation Guide

### Annotation

Sequin and tbl2asn use a simple five-column tab-delimited table of feature locations and qualifiers in order to generate annotation.

The format of this feature table allows diferent kinds of features (e.g. gene, coding region, tRNA, repeat_region) and qualifiers (e.g. /product, /note) to be indicated. The validator will check for errors such as internal stops in coding regions.

Guidelines for [eukaryotic genome submissions](/~/eukaryotic_genome_submission) .

If you do not understand any of the instructions presented here or you have questions, please contact us by email at [genomes@ncbi.nlm.nih.gov](mailto:genomes@ncbi.nlm.nih.gov) prior to creating your submission. This will save us both a lot of time.

### Table of Contents

1.  [Prepare annotation table](#prepare_table)
    *   [Gene features](#Gene_features)
    *   [locus_tag is required](#locus_tag)
    *   [protein_id](#protein_id)
    *   [CDS (coding region) features and protein names](#CDS)
    *   [Intein containing coding region](#intein)
    *   [Partial coding regions in incomplete genomes](#partial_CDS)
    *   [Gene fragments](#disrupted_genes)
    *   [Intron Containing Genes](#introns)
    *   [Transpliced Genes](#transpliced)
    *   [Split genes on two contigs](#Split_genes)
    *   [Ribosomal RNA, tRNA and other RNA features](#RNA)
    *   [Evidence Qualifiers](#Evidence_Qualifiers)
    *   [Functional bacteriophage](#bacteriophage)
    *   [Insertion sequences and transposons](#transposons)
    *   [Data base cross references](#db_xref)
    *   [Gene Ontology](#GOterms)
    *   [Variation](#variation)
    *   [Other Annotation](#Other)

### Prepare annotation table

The features must be in a simple five-column tab-delimited table, called the feature table. The feature table specifies the location and type of each feature for tbl2asn or Sequin to include in the GenBank submission that is created. The first line of the table contains the following basic information:

```
>Features SeqId table_name
```

The SeqId must be the same as that used on the sequence. The table_name is optional. Subsequent lines of the table list the features. Columns are separated by tabs.

*   Column 1: Start location of feature
*   Column 2: Stop location of feature
*   Column 3: Feature key
*   Column 4: Qualifier key
*   Column 5: Qualifier value

[Figure 2](/~/genomesubmit-Examples#fig2) shows a sample feature table and illustrates a number of points about the feature table format. The GenBank flatfile corresponding to this table is shown in [Figure 3](/~/genomesubmit-Examples#fig3)

Features that are on the complementary strand (such as the gene abrB in the examples below) and its corresponding CDS, are indicated by reversing the interval locations. Please avoid unnecessary capitalization in all text entered in your table.

#### Gene features

Gene features are usually a single interval, and their location should cover the intervals of all the relevant features such as promoters and operator binding sites. Gene names must follow the standard bacterial nomenclature rules of three lower case letters. Different loci are distinguished by a suffix of uppercase letters.

#### Example

```
correct cytB
  incorrect CYTB
  incorrect cytochrome B
  incorrect orf1
  incorrect putative gene fragment
```

If a gene is a pseudogene, please do not add the word "pseudo" to the gene name or protein name. Instead use the /pseudo qualifier on the gene feature. Please see [Gene fragments](#disrupted_genes) for more details.

#### locus_tag

All genes must be assigned a systematic gene identifier which must receive the locus_tag qualifier on the gene feature in the annotation table. Genes may also have functional names as assigned in the scientific literature. In this example, OBB_0001 is the systematic gene identifier, while abcD is the functional gene name. We recommend having the BioProject registration process auto-assign a locus_tag prefix, as they are not meant to confer meaning. The locus_tag prefix must be 3-12 alphanumeric characters and the first character may not be a digit. Additionally locus_tag prefixes are case sensitive. All chromosomes and plasmids of an individual genome must use the exactly same locus_tag prefix followed by an underscore and then an alphanumeric identification number that is unique within the given genome. Other than the single underscore used to separate the prefix from the identification number no other special characters can be used in the locus_tag. Locus_tags must only be used in combination with a gene feature. Read more about [locus_tags](//www.ncbi.nlm.nih.gov/genomes/locustag/Proposal.pdf) and their intended usage.

The use of locus_tag is supported in Sequin version 4.35 or newer. If you have an older version of Sequin please download the [current version](//www.ncbi.nlm.nih.gov/Sequin/) .

#### Table view of gene with both biological name and locus_tag

```
1 1575   gene
                gene    abcD
                locus_tag     OBB_0001
```

#### Flatfile view

```
gene     1..1575
        /gene="abcD"
        /locus_tag="OBB_0001"
```

#### Table view of gene with only locus_tag:

```
1 1575   gene
                locus_tag     OBB_0001
```

#### Flatfile view:

```
gene     1..157
        /locus_tag="OBB_0001"
```

#### protein_id

The submitter must assign an identification number to all proteins. NCBI uses this number to track proteins when sequences are updated. This number is indicated in the table by the CDS qualifier protein_id, and must have the format gnl|dbname|string, where dbname is a version of your lab name that you think will be unique (eg SmithUCSD), and string is the unique protein SeqID assigned by the submitter.

#### Example

The protein_id for abcD is `gnl|dbname|OBB_0001`. This identifier is saved with the record (in ASN.1 format), but it is not visible in the flatfile. We recommend using the locus_tag number as the protein identification number.

```
1  1575    gene
                        gene    abcD
                        locus_tag     OBB_0001
1       1575    CDS
                        product AbcD
                        protein_id      gnl|SmithUCSD|OBB_0001
```

The protein_id is used for internal tracking in our database, it is important that the complete protein_id (dbname + string) not be duplicated by a genome center. Note that when WGS submissions are processed, the dbname in the protein_id is automatically changed to 'WGS:XXXX', where XXXX is the project's accession number prefix. After your genome is released into GenBank, the proteins are assigned accession numbers. We will provide a table of the protein SeqIDs and accession numbers for you to use in future [updates](/~/genomesubmit#updating) .

#### protein names

All CDS features must have a product qualifier (protein name). NCBI protein naming conventions are adopted in part from the [UniProt-Swiss-Prot Protein Knowledgebase](//www.uniprot.org/docs/proknameprot)

Consistent nomenclature is indispensable for communication, literature searching and data retrieval. Many species-specific communities have established gene nomenclature committees that try to assign consistent and, if possible, meaningful gene symbols. Other scientific communities have established protein nomenclatures for a set of proteins based on sequence similarity and/or function. But there is no established organization involved in the standardization of protein names, nor are there any efforts to establish naming rules that are valid across the largest spectrum of species possible.

Ambiguities regarding gene/protein names are a major problem in the literature and it is even worse in the sequence databases which tend to propagate the confusion. For this reason, we ask that you follow some basic guidelines in naming your proteins. The protein naming guidelines are based on the premise that a good and stable recommended name for a protein is a name that is as neutral as possible.

Guidelines for naming proteins:

*   If it exists, use the approved nomenclature.
*   Use a concise name, not a description or phrase.
*   Ideally the name should be unique and attributed to all orthologs.
*   The protein name should not contain specific characteristics of the protein, and it should not reflect the function of the protein, its subcellular location, its domain structure, its molecular weight or its species of origin. This information can be included in the note.
*   In cases where the protein name is not known use "unknown" or "hypothetical protein" as the product name. We recommend the use of "hypothetical protein" as this will allow the locus_tag identifier to be appended to the product name in BLAST and Entrez summary lines.
*   Protein names may be denoted by the same symbol as the corresponding gene, but the symbol begins with a capital letter.
*   Avoid the use of molecular weights in protein names "unicornase subunit A" is preferred to "unicornase 52 kDa subunit"
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

Here are some examples of good protein names. These names all concisely describe the function of the protein, where known, and avoid references to structure, homology and species:

* ``cytochrome b``
* ``CytB``
* ``aconitate hydrase B``
* ``hypothetical protein``
* ``cytochrome b-like protein``
* ``4Fe-4S cluster binding protein``
* ``adenylyltransferase/ADP-heptose synthase``
* ``2-hydroxyhepta-2,4-diene-1,7-dioate isomerase``
* ``short-chain specific acyl-CoA dehydrogenase``
* ``formylmethanofuran--tetrahydromethanopterin formyltransferase``
* ``serine/threonine-protein kinase``
* ``translation initiation factor 1``
* ``triphosphoribosyl-dephospho-CoA synthetase``
* ``thiamine biosynthesis protein ThiC``
* ``PAS domain-containing protein 5``
* ``ABC transporter ATP-binding protein AlbC``
* ``stage 0 sporulation protein J``

Here are some examples of bad protein names:

* ``required for the efficient incorporation of molybdate into molybdoproteins``
    * _This describes the protein's role in a biosynthetic process but is not a protein name._

 
* ``chaperone Hsp70; DNA biosynthesis; autoregulated heat shock proteins``
    * _The name "chaperone Hsp70" is fine however the remaining comments would be best fielded as a note or in the function qualifier._

 
* ``putative carbonic anhdrase (EC 4.2.1.1)``
    * _The EC number should not be part of the protein name but instead fielded in the EC_number qualifier_

 
* ``similar to aconitrate hydrase B``
    * _This statement is fine as a note, however as a protein name aconitrate hydrase B-like protein is preferred_

 
* ``related to protein of unknown function``
    * _uninformative name_

 
* ``cytochrome b-like``
    * _cytochrome b-like protein is preferred_

 
* ``ABC transporter related``
    * _vague name, there are many ABC transporters and subunits, be more specific_

 
* ``pirin, N-terminal:pirin, C-terminal``
    * _uniformative name noting similarity in N and C terminus_

 
* ``helix-turn-helix motif``
    * _Describes a motif or structural domain but is not an appropriate protein name._

 
* ``PP-loop``
    * _Describes a motif or structural domain but is not an appropriate protein name._

 
* ``alpha/beta hydrolast fold``
    * _Describes a motif or structural domain but is not an appropriate protein name._

 
* ``pentapeptide repeat``
    * _Describes a motif or structural domain but is not an appropriate protein name._

 
* ``phosphopantetheine-binding domain``
    * _Describes a motif or structural domain but is not an appropriate protein name._

 
* ``protein of unknown function:conserved``
    * _uninformative name_

 
* ``hypothetical 32.5 kDa protein homologous to phytoene and squalene synthethases``
    * _Hypothetical protein alone is appropriate. The remaining comments should be fielded as a note._

 
* ``ribosomal protein L3 (E. coli)``
    * _Protein names should not contain references to organism names. Ribosomal protein L3 is an appropriate name by itself._

 
* ``saccharopine dehydrogenase or related protein``
    * _"saccharopine dehydrogenase" or "saccharopine dehydrogenase-like protein" would be more appropriate_

 
* ``tyrosine-protein kinase (capsular polysaccharide biosynthesis)``
    * _tyrosine-protein kinase is fine as a protein name but capsular polysaccharide biosynthesis would be more appropriate as a function._

 
* ``RimM protein, required for 16S rRNA processing``
    * _RimM is fine as a protein name but descriptive comments should be placed in the note._

 
* ``involved in flagellar biosynthesis``
    * _This is a functional comment and not a protein name._



#### Notes

Please avoid including notes indicating a specific percentage of similarity to other entries in the database, since the corresponding record that you have pointed to may change and make your current note inaccurate, incorrect and obsolete. Descriptions, notes describing similarity to other proteins, and functional comments must be placed in the appropriate CDS qualifiers such as `note`, or `prot_desc`, as they are descriptors of the product. E.C. numbers must be fielded in an `EC_number` qualifier.

```
start    stop    CDS
                        product DNA gyrase subunit B
                        EC_number     5.99.1.3
                        note    required for the gyration of DNA
```

Qualifiers that can be used on the CDS feature are:

```
start   stop    CDS
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

#### Bifunctional Proteins

If a protein contains two separate and distinct functions or if it has more than one name, it can be annotated in several ways as outlined below.

Table view:

```
start  stop    CDS
                        product adenylyltransferase/ADP-heptose synthase
                        note    bifunctional
                        EC_number     2.7.7.2
                        EC_number     1.4.1.13
```

or

```
start    stop    CDS
                        product bifunctional adenylyltransferase/ADP-heptose synthase cyclohydrolase
                        EC_number     2.7.7.2
                        EC_number     1.4.1.13
```

or

```
start    stop    CDS
                        product FolD 
                        function        adenylyltransferase
                        function        ADP-heptose synthase cyclohydrolase
                        note    bifunctional
                        EC_number     2.7.7.2
                        EC_number     1.4.1.13
```

#### Intein-containing coding regions

Intein-containing coding regions must be represented as follows:

```
946506  950039  gene
                        gene    recA
                        locus_tag     OBB_0010
946506  950039  CDS
                        product DNA recombination protein precursor
                        protein_id      gnl|dbname|OBB_0010
946506  946790  misc_feature
948057  950036
                        note    DNA recombination protein
946791  948056  misc_feature
                        note    intein  

```

Inteins should be annotated with two `mat_peptide` features, one for the intein and one for the final protein. We also add `precursor` to the product name on the CDS feature. Unfortunately, you can not add a mat_peptide feature in a table. Instead, you can add a misc_feature and we can convert them for you. Please see accession number [AY847267](//www.ncbi.nlm.nih.gov/nuccore/AY847267) for an example of an intein-containing protein.

#### Partial coding regions in incomplete genomes

Annotate a partial coding region using the `<` or `>` in your feature table to designate the feature as either 5' or 3' partial. Although coding region must begin at the first nucleotide present, the translation starts at the first complete codon.

#### Example

In the first example below, the `<` designates this coding region as 5' partial and `codon_start 3` tells the software to start translation with the third nucleotide of the CDS. Note that if the `codon_start` is not specified, then the software assumes a `codon_start` of `1`. The second coding region below is partial at the 3' end so `>` is used to indicate a 3' partial feature. The third example is of a 3' partial coding region on the complementary or minus strand.

```
<1   497     gene
                        gene    abcD
                        locus_tag     OBB_0001
<1   497     CDS
                        product AbcD
                        note    similar to Bacillus subtilis aldolase
                        codon_start     3
                        protein_id      gnl|dbname|OBB_0001
200     >1575        gene
                        gene    xyzA
                        locus_tag     OBB_0002
200     >1575        CDS
                        product actin-like protein
                        protein_id      gnl|dbname|OBB_0002
436     >1   gene
                        gene    nirK
                        locus_tag     OBB_0003
436     >1   CDS
                        product NirK
                        protein_id      gnl|dbname|OBB_0003
```

Here are [more examples of formatting partial CDS features](/~/examples.wgs#partialcds) .

Partial coding regions may be used for incomplete genomes only. All coding regions annotated on finished genomes must be complete at both the 5' and 3' ends.

#### Disrupted genes and gene fragments

Sometimes a genome will have adjacent or nearby genes that seem to be only part of a protein. In many cases these indicate a possible problem with the sequence and/or annotation. A related issue is the presence of internal stop codons in the conceptual translation of a CDS that looks like it should be a real CDS. These problems may be due to a variety of reasons, including mutations or sequencing artifacts. They can be annotated in a number of ways:

1.  _Annotate the gene as a pseudogene._ If multiple gene fragments were present initially, then add a single gene feature which covers all of the potential coding regions and add the pseudo qualifier indicating this is a pseudogene. If known, a note qualifier may be added indicating why this gene is disrupted.

    ```
1        200     gene
                            gene    phoA
                            gene_desc     alkaline phosphatase
                            locus_tag     OBB_0001
                            pseudo
                            note    frameshift
    ```

2.  _Alternatively, if you are not sure if the disrupted gene is a "pseudogene" you can just use a gene feature without the `/pseudo`._ Please use the complete nucleotide spans of the frameshifted gene. A note can be added to indicate the reason for the incomplete translation.

    ```
1    200     gene
                            gene    phoA
                            gene_desc     alkaline phosphatase
                            locus_tag     OBB_0001
                            note    nonfunctional due to frameshift
    ```

3.  _A coding region containing a frameshift that is thought to be corrected by ribosomal slippage can be annotated using joined feature spans._ Joined spans on a feature are used to combine two non-contiguous regions of sequence that are joined together to encode a protein, for example. This is typically used to combine eukaryotic exons to translate the coding region. To create a join CDS you must specify the spans of each contiguous region of sequence that encodes the protein. The use of the joined feature spans is rare in bacteria.

    ```
333255  333181  CDS
    333179  332157
                            product AbcD
                            protein_id     gnl|dbname|OBB_0001
                            exception      ribosomal slippage
```

    In this case the CDS must also include an exception qualifier with the exact text "ribosomal slippage". If you include a join feature for a different reason, please include a note qualifier indicating why the two nucleotide spans are joined.

4.  _If a gene is localized but the translation is unknown, it is possible to simply annotate the gene feature without a corresponding coding region._ The `gene_desc` qualifier can be used to annotate both the gene symbol and the gene description.

    ```
1   200     gene
                            gene    phoA
                            gene_desc     alkaline phosphatase
                            locus_tag     OBB_0001

    ```

5.  _A gene containing an authentic frameshift induced by phase variation can be represented by a gene feature with a `note`._

    ```
1    200     gene
                            gene    phoA
                            gene_desc     alkaline phosphatase
                            locus_tag     OBB_0001
                            note    authentic frameshift induced by phase variation; This region contains 
                            an authentic frameshift or in-frame stop in the coding sequence and is not the 
                            result of a sequencing error
                     ```

#### Intron-Containing Genes

While rare, there are some examples of bacterial genes containing introns. Annotate the gene feature of any intron-containing gene such that the gene feature spans are a single span covering all exons and introns. The actual feature (CDS, tRNA, etc.) should then be annotated with sets of nucleotide spans showing how the exons are joined to create the correct product. In this example there are two exons transcribed to create a tRNA. The first exon is from 1456 to 1419 and the second is from 1400 to 1361\. Note how the gene feature spans encompass both exons and the intron.

```
1456    1361    gene
                        locus_tag     APO_t01
1456    1419    tRNA
1400    1361
                        product tRNA-Cys
```

#### Transpliced Genes

Transpliced genes are the exception to the rule for annotating gene feature spans. Transpliced genes are similar to intron containing genes except the two pieces of the gene are found on different regions of the chromosome. These genes are transcribed as two or more separate RNA products that are transpliced into a single mRNA or tRNA. To annotate this using a table, enter the nucleotide spans so that the complementary (minus strand) spans are arranged from high to low and vice versa for the plus strand.

```
36700   36618   gene
86988   87064
                        locus_tag    NEQ_t38
                        exception    trans-splicing
36631   36618   misc_feature
                        note    sequence cleaved during processing of trans-spliced tRNAs
36673   36635
87030   87064   tRNA
                        product tRNA-Glu
                        exception    trans-splicing
                        note    this trans-spliced tRNA consists of two halves on mixed strands; it shares a 3' half with another tRNA
```

Flatfile view:

```
gene            join(complement(36618..36700),86988..87064)
                     /locus_tag="NEQ_t38"
                     /trans_splicing
     misc_feature    complement(36618..36631)
                     /locus_tag="NEQ_t38"
                     /note="sequence cleaved during processing of trans-spliced tRNAs"
     tRNA            join(complement(36635..36673),87030..87064)
                     /locus_tag="NEQ_t38"
                     /product="tRNA-Glu"
                     /trans_splicing
                     /note="this trans-spliced tRNA consists of two halves on
                     mixed strands; it shares a 3' half with another tRNA"
```

#### Split genes on two contigs

NEW (Sept 2012): Sometimes in incomplete genomes the ends of a gene may be on different contigs. When certain that the two pieces are part of the same gene, annotate these as separate genes with unique locus_tags, plus separate CDS with different protein_id's. In addition, link the features together with notes that refer to the other part of the gene. However, do not create extremely short features, for example if one end is only the start methinione or only a few amino acids before the stop codon.

#### Example

```
>Feature Cont01.00111
5000    >7500        gene
                        locus_tag     KCS_2223A
5488    5500    CDS
6000    >7200
                        product enolase
                        protein_id    gnl|dbname|KCS_2223A
                        note    5' end; 3' end is gene KCS_2223B on contig Cont01.00224
```

```
>Feature Cont01.00224
<1   1000    gene    
                        locus_tag     KCS_2223B
<100 876     CDS
                        product enolase
                        protein_id    gnl|dbname|KCS_2223B
                        note    3' end; 5' end is gene KCS_2223A on contig Cont01.00111
```

#### Ribosomal RNA, tRNA and other RNA features

RNA features (rRNA, tRNA, ncRNA) must include a corresponding gene feature with a locus_tag qualifier. Please be sure to specify which amino acid the tRNA gene corresponds to. If the amino acid of a tRNA is unknown, use tRNA-Xxx as the product, as in the example. Many submitters like to label the tRNAs such as tRNA-Gly1, etc. If you wish to do this please include "tRNA-Gly1" as a note and not in /gene. The use of /gene is reserved for the actual biological gene symbol such as "trnG". If a tRNA is a pseudogene, please use the /pseudo qualifier.

Annotate ncRNAs that belong to one of the INSDC [ncRNA_class](//www.insdc.org/documents/ncrna-vocabulary) as an ncRNA feature, with the appropriate value in the required /ncRNA_class qualifier. Regions of an RNA should be annotated as a misc_feature (eg, leader sequences), or a misc_binding feature if they bind a known molecule (eg, riboswitches). See [Other Annotation](#Other) for examples of regions of RNAs.

Some rRNA, tRNA, ncRNA examples:

```
<1      400     gene
                        locus_tag     OBB_0001
<1      400     rRNA
                        product 16S ribosomal RNA
401     500     gene
                        gene    trnG
                        note    tRNA-Gly1
                        locus_tag     OBB_0002
401     500     tRNA
                        product tRNA-Gly
501     600     gene
                        locus_tag     OBB_0003
501     600     tmRNA
                        product tmRNA
601     700     gene
                        locus_tag     OBB_0004
601     700     tRNA
                        product tRNA-Xxx
701     800     gene
                        locus_tag     OBB_0005
                        pseudo
701     800     tRNA    
                        product tRNA-Phe
                        pseudo
801     900     gene
                        locus_tag       OBB_0006
801     900     ncRNA
                        ncRNA_class     SRP_RNA
                        product RNA component of signal recognition particle
```

#### Evidence Qualifiers

At the 2005 annual meeting of the International Nucleotide Sequence Databases (INSD), DDBJ, EMBL and GenBank agreed to adopt two qualifiers to describe the evidence for features in sequence records. These are "/experimental=text" and "/inference=TYPE:text", where 'TYPE' is from a select list and 'text' is structured text. These new qualifiers replace "evidence=experimental" and "evidence=non-experimental", respectively, which are no longer supported. Read more about [Evidence Qualifiers](/~/evidence)

```
1     100   gene  
                locus_tag   Test_0001
1     100   CDS
                product     RecA
                protein_id  gnl|center_name|Test_0001
                inference   ab initio prediction:Genscan:2.0
200   300   gene
                locus_tag   Test_0002
200   300   CDS
                product     SecA
                protein_id  gnl|center_name|Test_0002
                inference   similar to DNA sequence, (same species):INSD:DQ060639.1
400   500   gene  
                locus_tag   Test_0003
400   500   CDS
                product     ribonuclease R
                protein_id  gnl|center_name|Test_0003
                inference   protein motif:InterPro:IPR001900
                db_xref InterPro:IPR001900
600   700   gene  
                locus_tag   Test_0004
600   700   CDS
                product     nitroreductase A
                protein_id  gnl|center_name|Test_0004
                experiment  expression of GST fusion protein    
```

#### Functional bacteriophage

If a bacterial genome contains a functional phage, an additional source feature must be included with the spans covering the complete phage sequence. However, if the phage is not functional or if you are not sure, annotate it as a misc_feature.

#### Example

```
361      4200    source
                        organism        Bacteriophage xyz
```

#### Insertion sequences and transposons

Insertion sequences and transposons must be annotated as repeat_region features. The name of the insertion sequence or transposon must be added in a insertion_seq or transposon qualifier. Note that transposons and insertion sequences should not be given locus_tags.

```
1     100     repeat_region
                        mobile_element  insertion sequence:IS1363

500   600     repeat_region
                        mobile_element  transposon:Athena-Av1
```

#### Data base cross references

A variety of data base cross references can be added to a feature. These appear as /db_xref on the features. This qualifier serves as a vehicle for linking of sequence records to other external databases. See the full list of [db_xref](/~/collab/db_xref) .

```
1     100   gene  
                locus_tag   Test_0001
1     100   CDS
                product     RecA
                protein_id  gnl|center_name|Test_0001
                db_xref InterPro:IPR000111

180     210   misc_feature
                note     yybP-ykoY element
                db_xref RFAM:RF00080
```

#### Gene Ontology

GO (Gene Ontology) terms can be included in genomes in order to describe protein functionality. Gene Ontology (GO) terms can be indicated with the following qualifiers

```
1       100     CDS
                        product AbcD
                        go_component    exocyst|0000145
                        go_process      regulation of transcription, DNA-dependent|0006355
                        go_process      exocytosis|0006887
                        go_function     DNA binding|0003677
```

The value field is separated by vertical bars '|' into a descriptive string, the GO identifier (leading zeroes are retained), and optionally a PubMed ID and one or more evidence codes. The evidence code is the fourth token, so include blank fields, as necessary (eg the last qualifier has no PubMed ID so the third field is blank). See examples on the [detailed eukaryotic annotation](/~/eukaryotic_genome_submission_annotation#GOterms) page.  

#### Variation

Polymorphisms in the sequence can be shown with variation features. Include one of the polymorphisms in the sequence (usually, this is the most commonly seen sequence), and then add a variation feature in the .tbl file for each of the other possibilities.

*   The `variation` feature requires a `replace` qualifier, whose value is the sequence of the polymorphism that is NOT in the submitted sequence. For example, if `CCC` is most common at position 100-102 but there is also `CC` (a substitution), `CCCCC` (an insertion), and nothing (a deletion) then the sequence will have `CCC` at that location and you would include three variation features, one for each polymorphism.
*   For an insertion polymorphism, a carat (`^`) is part of the start location.
*   When the polymorphism is a complete deletion, then the replace value is just two double-quotes.
*   You can also include optional qualifiers: `note`, and the `frequency` with which the other sequence is found.

Here is an example with all of those options:

```
100	102	variation
			replace	cc
			note	polymorphism
100^	102	variation
			replace	ccccc
			frequency	0.1
100	102	variation
			replace	""
			note	deletion
```

Those features will appear like this in the GenBank view:

```
variation       100..102
                     /note="polymorphism"
                     /replace="cc"
     variation       100^102
                     /frequency="0.1"
                     /replace="ccccc"
     variation       100..102
                     /note="deletion"
                     /replace=""
```

#### Other Annotation

Riboswitches should be annotated using the `misc_binding` feature if the bound moiety is known, for example:

```
1     100    misc_binding
                        note cobalamin riboswitch
                        bound_moiety adenosylcobalamin
```

If the bound moiety is unknown or if the sequence is a leader sequence, annotate as a misc_feature, for example:

```
1     100    misc_feature
                        note yybP-ykoY element
```

`misc_feature` and `misc_binding` features do not have an associated gene feature. If it is desired to tag these features with a locus_tag-like identifier, then include that value in the note, separated from other information by a semi-colon and space.

