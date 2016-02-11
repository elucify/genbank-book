
# HTG FAQs

Compiling this list of frequently asked questions is an ongoing project. Please send any additional questions to [htg-admin@ncbi.nlm.nih.gov](mailto:info@ncbi.nlm.nih.gov), and we will include them if they are appropriate.

*   [What Phase should my HTG submission be?](#phase)
*   [Will the accession number change when the Phase changes?](#accchange)
*   [What do the different KEYWORDS mean?](#keywords)
*   [What information should be included in the DEFINITION line of an HTG record?](#defline)
*   [Where do I send an HTG update?](#whereupdate)
*   [If my HTG record replaces a record(s) already present in the database, how do I include this information in my HTG submission?](#replace)
*   [What are some common annotation errors to avoid?](#errors)

## What Phase should my HTG submission be?

If the HTG record is unfinished, it should be designated Phase 1 or Phase 2\. Phase 1 indicates an unfinished sequence containing gaps, in which the order and relative orientation of the pieces are not known. Phase 2 is also an unfinished sequence, but the order and orientation of the pieces are known, however, the length of the gaps between these pieces may or may not be known. By definition, an unfinished sequence of only one piece is Phase 2\. Phase 3 submissions are one contiguous piece of DNA of finished quality.

![htgs_orient](/core/assets/genbank/images/orient.gif)

## Will the accession number change when the Phase changes?

No. The accession number you receive when you first submit an HTG record remains with that record throughout its existence, that is, through its various phases and any updates of its sequence and/or annotations.

## What do the different KEYWORDS mean?

*   HTGS_DRAFT

    Clones that are sequenced to draft status. These should be, on average over all draft depositions, at least 4X coverage (but can be more) and are Phase 1 or Phase 2.

*   HTGS_FULLTOP

    An HTGS_DRAFT clone where all shotgun reads are done. At this point, the project is ready to hand off to finishers. A deposition should be made at this stage. Note that the precise coverage will vary depending on center operating procedure, but usually the coverage is between 6X and 10X. These projects are almost always ordered and oriented (Phase 2).

*   HTGS_PREFIN

    After the HTGS_FULLTOP stage, when the clone has undergone 2 rounds of prefinishing (two iterative computational determinations of low coverage/low quality regions and addition of directed sequencing reads, including primer walks, covering those areas followed by re-assembly, in an attempt to improve contiguity and quality).

*   HTGS_IMPROVED

    After the HTGS_FULLTOP stage, when one or more regions of the BAC are of finished quality.

*   HTGS_ACTIVEFIN

    The fulltop project has been passed to the finishing team. Often this happens very rapidly after HTGS_fulltop is reached.

*   HTGS_ENRICHED

    The BAC assembly is enriched by inclusion of both BAC generated reads and overlapping WGS reads.

*   HTGS_POOLED_MULTICLONE

    The assembly consists of reads from multiple BAC clone reads that have not yet been deconvoluted from an array of pooled clones. The keyword is valid for Phase 0, 1, and 2 HTGS records, but not Phase 3\. The clone names must be present in the /clone qualifier, separated by a semi-colon.

*   HTGS_POOLED_CLONE

    The assembly consists of a specific BAC clone's reads that were deconvoluted from an array of pooled clones; contains overlapping reads from WGS sequencing if used in conjunction with HTGS_ENRICHED.

*   HTGS_CANCELLED

    Sequencing of the clone has stopped, and this clone will not be finished.

*   HTGS_LIMITED_ORDER

     A clone in which the order and orientation is known for some of the contigs, but not all of them. This can be used for Phase 1 clones.

*   GAP_CLOSURE

    Used for non-HTG records whose sequences close gaps in HTG records

*   PCR_CORRECTION

    Used for non-HTG records that are PCR sequences of genomic DNA that were generated to correct small errors in HTG or other sequences of a genome assembly.

## What information should be included in the DEFINITION line of an HTG record?

For phase 3 entries, the DEFINITION line should contain the scientific name of the organism and the clone name and if available, the chromosome or map location. For phase 0, 1, and 2 HTGs, the definition line is generated automatically from the phase and the number of pieces present, plus all of the source information that is included in the source feature (the organism, clone, chromosome, etc.). Examples of definition lines are:

<dl>

<dd>Homo sapiens chromosome 17 clone 297N7, *** SEQUENCING IN PROGRESS ***, 9 unordered pieces.

for an entry with 9 pieces and this source information:

<pre>source          1..125768
                     /organism="Homo sapiens"
                     /chromosome="17"
                     /clone="297N7"

                  </pre>

</dd>

<dd>Arabidopsis thaliana clone BAC T5I7 map near marker CIC10A06, *** SEQUENCING IN PROGRESS ***, 2 unordered pieces.

for an entry with 2 pieces and this source information:

<pre>source          1..125768
                     /organism="Arabidopsis thaliana"
                     /clone="BAC T517"
                     /map="near marker CIC10A06"

                  </pre>

</dd>

<dd>Arabidopsis thaliana chromosome II BAC T28M21, genomic sequence.</dd>

<dd>Homo sapiens chromosome 17 clone 104H12, complete sequence.</dd>

<dd>Arabidopsis thaliana clone BAC T5I7 map near marker CIC10A06, *** SEQUENCING IN PROGRESS ***, 2 unordered pieces.

for an entry with 2 pieces and this source information:

<pre>source          1..125768
                     /organism="Arabidopsis thaliana"
                     /clone="BAC T517"
                     /map="near marker CIC10A06"

                  </pre>

</dd>

<dd>Arabidopsis thaliana chromosome II BAC T28M21, genomic sequence.</dd>

</dl>

## Where do I send an HTG update?

This depends on how the record was initially submitted.  
HTG records can be submitted through two different routes:

*   HTGS FTP site
*   email to [gb-sub@ncbi.nlm.nih.gov](mailto:gb-sub@ncbi.nlm.nih.gov)

If your HTG record was originally submitted through the HTGS FTP site, then all updates to that record should be sent to that site. However, if your HTG record was originally submitted to [gb-sub@ncbi.nlm.nih.gov](mailto:gb-sub@ncbi.nlm.nih.gov), all updates should be sent by email to [gb-admin@ncbi.nlm.nih.gov](mailto:gb-admin@ncbi.nlm.nih.gov) per these [instructions](http://www.ncbi.nlm.nih.gov/genbank/update/).

## If my HTG record replaces a record(s) already present in the database, how do I include this information in my HTG submission?

If you need to change the sequence or annotations in a record, we prefer that you update that record. However, in some special cases, you may need to completely replace one or more records with a new record. In this case (in consultation with the database staff at NCBI), you can make the old accession number(s) secondary to the new one.

If you are using Sequin, you can make a previous record secondary to another submission by listing the secondary accession number(s) on the Secondary Accessions spreadsheet of the HTGS submission form.

If you are using the tbl2asn tool, add the following argument to the end of the tbl2asn command line (directly after the accession number):

<dl>

<dd>-x Secondary accession number(s), separated by commas if multiple, e.g., U10000, L10000</dd>

</dl>

Please verify the accuracy of the secondary accession number(s) before submitting this information. Once a record is made secondary to another, it is withdrawn from the databases, and it is very complicated for the database staff to reinstall a withdrawn record. The only check that the database staff will do for these HTG records is to ensure that the CENTER owns the record that is being withdrawn (made secondary). The staff does not verify that the sequence that is being withdrawn is actually contained within the sequence of the primary accession number.

## What are some common annotation errors to avoid?

It should be noted that annotations (apart from the biosource of the sequence (i.e., Homo sapiens, Arabidopsis thalania)) are not mandatory in an HTG record, and submitters should not feel obligated to add them. Listings of computer-generated repeats add little to the record because it is fairly easy to find these repeats on a DNA sequence. However, if you want to add experimentally or computationally derived annotations to the sequence, we welcome them. Please be aware that [Sequin](//www.ncbi.nlm.nih.gov/Sequin) has extensive tools to validate annotations, and we suggest that you run annotated records through the validator before you submit them. If you have any questions about the warning messages presented to you by Sequin, please feel free to contact the NCBI staff ([info@ncbi.nlm.nih.gov](mailto:info@ncbi.nlm.nih.gov)).

All annotations present in an HTG record use and apply the same rules that are present in any DDBJ/EMBL/GenBank record. The complete [Feature table](//www.ncbi.nlm.nih.gov/collab/FT/) documentation that explains all of these rules and regulations is available.

1.  Human instead of Homo sapiens on the DEFINITION line

    DEFINITION lines should start with the scientific name (Genus species) of the organism from which the sequence originates.

    Examples of DEFINITION lines are shown [above](#defline).

2.  /chromosome vs. /map

    The /chromosome qualifier should contain only the chromosome number. (i.e., /chromosome ="X" or "22" )

    The /map qualifier should be used to represent the chromosomal location of the sequence. (i.e. /map="22q11" )

    For example, a final source descriptor might read:

    <pre>source          1..125768
                         /organism="Homo sapiens"
                         /chromosome="22"
                         /clone="58b8"
                         /map="22q12"

                      </pre>

3.  No product name or description

    All annotated coding regions must have a product name. If similarity to a known protein is present, such information should be included as a /note qualifier. If no similarity exists, please include "unknown" or "hypothetical protein" as a product name.

4.  Incorrect STS feature

    The /evidence qualifer is not legal on an STS feature. Please annotate STS features per this example:

    <pre>STS             6792..7095
                             /db_xref="dbSTS:05783"
            </pre>





<div id="shared-content-1" nid="1331">

<div class="rightnav">

## HTGs Resources

*   [About HTGs](/~/htgs)
*   [Submitting HTGs](/~/htgs/subinfo)
*   [Processing HTGs](/~/htgs/processing)
*   [](/~/htgs/processing)[HTGs FAQ](/~/htgs/faq)



