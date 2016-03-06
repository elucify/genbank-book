
# Evidence Qualifiers

The evidence qualifiers /experiment and /inference can be used to provide more detail about the support for the annotation. These qualifiers replaced "evidence=experimental" and "evidence=non-experimental", respectively, which are no longer supported.

### **/experiment**

Definition: a brief description of the nature of the experimental evidence that supports the feature identification or assignment.

Value format: `[CATEGORY:]text`

CATEGORY is optional, and is one of these:

*   COORDINATES; support for the annotated coordinates
*   DESCRIPTION; support for a broad concept of function such as that based on phenotype, genetic approach, biochemical function, pathway information, etc.
*   EXISTENCE; support for the known or inferred existence of the product

A PubMedID or doi can be included within brackets in the text.

<dl>
<dt>Examples:</dt>
<dd>/experiment="EXISTENCE:Northern blot"</dd>
<dd>/experiment="heterologous expression system of Xenopus laevis oocytes [PMID: 12345678, 10101010, 987654]"</dd>
</dl>

Comment: detailed experimental details should not be included, and would normally be found in the cited publications.

### **/inference**

Definition: a structured description of non-experimental evidence that supports the feature identification or assignment.

Value format: ["CATEGORY:]TYPE[ (same species)][:EVIDENCE_BASIS]"

CATEGORY is optional, and is one of these:

*   COORDINATES; support for the annotated coordinates
*   DESCRIPTION; support for a broad concept of function such as that based on phenotype, genetic approach, biochemical function, pathway information, etc.
*   EXISTENCE; support for the known or inferred existence of the product  

TYPE is required and is one of these:

*   /inference="similar to AA sequence"
*   /inference="similar to DNA sequence"
*   /inference="similar to RNA sequence"
*   /inference="similar to RNA sequence, mRNA"
*   /inference="similar to RNA sequence, EST"
*   /inference="similar to RNA sequence, other RNA"
*   /inference="profile"
*   /inference="nucleotide motif"
*   /inference="protein motif"
*   /inference="ab initio prediction"
*   /inference="alignment"

The optional text "(same species)" can be included when the inference comes from the same species as the entry.

EVIDENCE_BASIS provides reference to a database entry (including accession and version) or an algorithm (including version). The accession.version number of a database record and the version number of an algorithm are separated from the database or algorithm name by a colon, as seen in the examples. 

Examples:

<dl>

<dd>/inference="similar to DNA sequence:INSD:AY411252.1"  
/inference="similar to RNA sequence, mRNA:RefSeq:NM_000041.2"  
/inference="similar to DNA sequence (same species):INSD:AACN010222672.1"  
/inference="profile:tRNAscan:2.1"  
/inference="protein motif:InterPro:IPR001900"  
/inference="ab initio prediction:Genscan:2.0"  
/inference="alignment:Splign:1.0"  
/inference="alignment:Splign:1.26p:RefSeq:NM_000041.2,INSD:BC003557.1"</dd>

</dl>

Several things to note about /inference are:

*   When citing a GenBank record, use INSD (International Sequence Database).
*   When citing a RefSeq record (recognized by the underscore between the letters and the digits), use RefSeq.
*   Include the version of the algorithm that was used, and separate the version from the algorithm name with a colon, eg Genscan:2.0.
*   The EVIDENCE_BASIS can include the accession.version of the records that support the analysis.  The format is [ALGORITHM][:EVIDENCE_DBREF[,EVIDENCE_DBREF]*[,...]], as in the example "alignment:Splign:1.26p:RefSeq:NM_000041.2,INSD:BC003557.1"

**How to add the qualifiers to your genome submissions**

Example .tbl file:

In this example the first CDS is predicted by Genscan 2.0, the second CDS was identified by its similarity to EST H22345.1 from the same species, the third CDS was identified because it's similar to GenBank (INSD) record JQ340893.1 and by its InterPro domain IPR001900, and the fourth CDS has experimental expression evidence.

<pre>>Feature  ExampleSeq

1     100   gene  
                  locus_tag   Test_0001
1     100   CDS
                  product     hypothetical protein
                  protein_id  gnl|center_name|Test_0001
                  inference   ab initio prediction:Genscan:2.0
200   300   gene
                  locus_tag   Test_0002
200   300   CDS
                  product     putative helicase
                  protein_id  gnl|center_name|Test_0002
                  inference   similar to RNA sequence, EST (same species):INSD:H22345.1
400   500   gene  
                  locus_tag   Test_0003
400   500   CDS
                  product     ribonuclease
                  protein_id  gnl|center_name|Test_0003
                  inference   similar to RNA sequence, mRNA:INSD:JQ340893.1
                  inference   protein motif:InterPro:IPR001900
600   700   gene  
                  locus_tag   Test_0004
600   700   CDS
                  product     alcohol dehydrogenase
                  protein_id  gnl|center_name|Test_0004
                  experiment  expression of GST fusion protein   
</pre>

The resulting flatfile looks like this:

<pre>gene            1..100
                     /locus_tag="Test_0001"
     CDS             1..100
                     /locus_tag="Test_0001"
                     /inference="ab initio prediction:Genscan:2.0"
                     /codon_start=1
                     /product="hypothetical protein"
                     /translation="M...."
     gene            200..300
                     /locus_tag="Test_0002"
     CDS             200..300
                     /locus_tag="Test_0002"
                     /inference="similar to RNA sequence, EST (same
                     species):INSD:H223456.1"
                     /codon_start=1
                     /product="putative helicase"
                     /translation="M...."
     gene            400..500
                     /locus_tag="Test_0003"
     CDS             400..500
                     /locus_tag="Test_0003"
                     /inference="protein motif:InterPro:IPR001900"
                     /inference="similar to RNA sequence, mRNA:INSD:JQ340893.1"
                     /codon_start=1
                     /product="ribonuclease"
                     /translation="M...."
     gene            600..700
                     /locus_tag="Test_0004"
     CDS             600..700
                     /locus_tag="Test_0004"
                     /experiment="expression of GST fusion protein"
                     /codon_start=1
                     /product="alcohol dehydrogenase"
                     /translation="M...."
 </pre>





<div id="shared-content-1" nid="1469">

<div class="rightnav">

## Genome Resources

*   [BioProject](http://www.ncbi.nlm.nih.gov/bioproject)
*   [Prokaryotic Genome Annotation Guide](/~/genomesubmit_annotation)
*   [tbl2asn](/~/tbl2asn2)
*   [GenomesMacroSend](http://www.ncbi.nlm.nih.gov/projects/GenomeSubmit/genome_submit.cgi)
*   [NCBI Prokaryotic Genome Annotation Pipeline](http://www.ncbi.nlm.nih.gov/genome/annotation_prok/)
