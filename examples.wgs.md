
# WGS Example Files

Remember that the columns in a .tbl file must be tab-delimited. If the samples in which the complete sequence is included do not work, check that tabs separate the columns, not spaces.

*   [Simple file](#simple)
*   [Multiple sequences in a file](#multiples)
*   [Partial coding regions](#partialcds)
*   [Features on the complementary strand](#complementary_strand)

### Simple file

<pre>sample.fsa

>Cont54 [organism=Homo sapiens] [chromosome=5] 
acaagcgctgctgtcgatgcaaactttagcttttaaacaagtgcaaacgcacgctgtctc
acatgataacacacattatcagaatactttccatgcaatatgaaaccatagcaagctacg
....

sample.tbl

>Features Cont54
10400	12512	gene
			locus_tag	CCC_03116
10400	10462	mRNA
10533	10577   
10651	11098   
11182	11642   
11716	12512   
			product	aldolase
			protein_id	gnl|dbname|CCC_03116
			transcript_id	gnl|dbname|mrna.CCC_03116
10450	10462	CDS
10533	10577   
10651	11098   
11182	11642   
11716	12233   
			product	aldolase
			protein_id	gnl|dbname|CCC_03116
			transcript_id	gnl|dbname|mrna.CCC_03116
			inference	profile:Genscan:2.0
15801	17688	gene
			locus_tag	CCC_03118
15801	16607	mRNA
16750	17688
			product	hypothetical protein
			protein_id	gnl|dbname|CCC_03118
			transcript_id	gnl|dbname|mrna.CCC_03118
15840	16607	CDS
16750	17610   
			product	hypothetical protein
			protein_id	gnl|dbname|CCC_03118
			transcript_id	gnl|dbname|mrna.CCC_03118
			inference	similar to RNA sequence, mRNA:INSD:AY123456.2

Here is the definition line of the flatfile view of the final record made
with these files:

DEFINITION  Homo sapiens chromosome 5 Cont54, whole genome shotgun sequence.

</pre>

### Files for multiple sequences

<pre>multiple.fsa

>Cont348.225 [organism=Helicobacter pylori ABC1] [strain=ABC1] [host=Homo sapiens] [isolation-source=blood]
TTGAAGCAAGGCATTAGGCGAACCACTGCCTCTCTTTTACCTTCTTTTTTTTCCACCATTATTACTTTACTTTACATACGTTTAGGATCTGG
CGAGCAGCCCAGGCGAGTGTTTTGTAGTTTTCTCGGGGCTGCCTTTTTTTCTCTCTGTGGATGTGTGTGTGGGTATGGGCTGTATTTTCCTG
>Cont442.125 [organism=Helicobacter pylori ABC1] [strain=ABC1] [host=Homo sapiens] [isolation-source=blood]
TTGAAGCAAGGCATTAGGCGAACCACTGCCTCTCTTTTACCTTCTTTTTTTTCCACCATTATTACTTTACTTTACATACGTTTAGGATCTGG
CGAGCAGCCCAGGCGAGTGTTTTGTAGTTTTCTCGGGGCTGCCTTTTTTTCTCTCTGTGGATGTGTGTGTGGGTATGGGCTGTATTTTCCTG

multiple.tbl

>Features Cont348.225
11	109	gene
			locus_tag	HPC_002564
			gene	cheA
11	109	CDS
			product	CheA 
			protein_id	gnl|dbname|HPC_002564
>Features Cont442.125
15	113	gene
			locus_tag	HPC_003020
15	113	CDS
			product	TPR repeat-containing protein
			protein_id	gnl|dbname|HPC_003020
			experiment	Northern blot
</pre>

### Partial coding region

The first coding region is partial at the 5' end and nucleotide 3 is the beginning of the first complete codon. Therefore, " < " indicates 5' partial, and codon_start "3" indicates the start of the first codon.

The second coding region is partial at the 3' end, so " > " is used to indicate 3' partial.

<pre>partial.fsa

>Cont3  [organism=Mus musculus] [strain=BALB/c] [chromosome=2]
TGcaaagtGGAATTCCAATTTCAACACCAGTTTTTGATGGCGCAAAAGAGCAAGATGTAACAAATATGTTAGAGCTTGCATCATTACCAAAATCTGG
TCAAACAAAATTGTGGGATGGTAGAACAGGTGAAAAATTTGATAGAGAAGTCACAGTTGGCACTATTTATATGTTAAAATTACACCATCTTGTAGAA
GATAAAATACACGCAAGATCTACAGGTCCTTATAGTTTAGTTACACAACAACCTCTTGGTGGTAAGGCTCAATTGGGAGGTCAACGATTTGGAGAAA
TGGAAGTTTGGGCTCTGGAAGCTTATGGGGCTTCTTATACTTTACAAGAAATTTTAACAGTAAAATCTGATGATGTTGCTGGTAGAGTTAAAGTTTA
TGAAACAATAGTAAAAGGTGAAGAGAATTTCGAGTCAGGAATACCTGAGTCATTTAATGTTTTAGTAAAAGAAATCAAAGCGCTAGCTCTTAATGTG
GAGTTAAATTAAAATGAAAAAAGATATTAAAGATTTTTTTAAAGAAACTGCCATATCAGACTCTCAAAATTTTAATAGTATTAAAATTACTTTAGCA
AGCCCTGAAAAGATAAAGTCATGGACTTATGGAGAAATAAAAAAACCCGAAACTATTAATTATAGAACTTTCAGACCTGAAAAAGACGGCCTATTTT
GTGCGAGAATATTTGGTCCAATAAAAGATTACGAATGTTTATGTGGAAAATATAAAAGAATGAAGTTCAGAGGAATTATTTGTGAGAAGTGTGGCGT
AGAGGTTACTAAATCAAATGTTCGTAGAGAAAGAATGGGGCACATCAATTTATCAACCCCAGTTGCACATATTTGGTTTTTAAAATCTTTACCAAGT
AGAATTTCACTAGCTATTGATATGAAGCTTAAAGAGGTTGAAAGAGTTCTATACTTTGAAAGTTTTATTGTTATAGAGCCTGGATTAACTAGTCTTA
AAAAAAATCAACTTTTAAACGAAGATGAATTAAATAAATATCAAGAGGAGTTTGGTGAAGAATCCTTTACTGCAGGAATAGGAGCAGAGGCGATACT
AGAGATTTTAAAATCTATAGACTTGAATAAAGAGAGAGAAATTTTATTAAAAAATATAAATGAGACAAAATCAAAGGTTGCTGAAGAAAGATCTATA
AAAAGATTAAAACTGATCGATTCATTTATTGAAACTGGTAACAAACCAGAATGGATGATTTTAACTACTATACCTGTAATACCACCAGAGTTAAGGC
CACTTGTTCCTCTAGATGGAGGTAGATTTGCAACATCAGATCTAAACGATTTGTATAGAAGAGTTATAAATAGAAATAATAGATTGAAAAGATTAAT
GGATCTTAAAGCTCCAGATATAATTATTAGAAATGAAAAACGAATGTTGCAAGAGTCAGTGGATGCTTTATTCGATAATGGCAGAAGAGGCAGAGTA
ATTACAGGAACTGGTAAACGTCCATTAAAATCTTTGGCTGAAATGCTTAAAGGAaaacaaG

partial.tbl

>Feature Cont3
<1	>497	gene             
			locus_tag KCS_111011
<1	497	CDS             
			note    similar to Bacillus subtilis aldolase
			product aldolase-like protein
			codon_start     3
			protein_id	gnl|dbname|KCS_111011
			transcript_id	gnl|dbname|mrna.KCS_111011
<1	>497	mRNA             
			product aldolase-like protein
			protein_id	gnl|dbname|KCS_111011
			transcript_id	gnl|dbname|mrna.KCS_111011
<499	>1516	gene             
			locus_tag KCS_111012
499	>1516	CDS             
			product actin-like protein
			protein_id	gnl|dbname|KCS_111012
			transcript_id	gnl|dbname|mrna.KCS_111012
<499	>1516	mRNA             
			product actin-like protein
			protein_id	gnl|dbname|KCS_111012
			transcript_id	gnl|dbname|mrna.KCS_111012
</pre>

### Features on the complementary strand

Both genes are on the minus strand. The first CDS begins at nt1018 and is 3' partial. The second CDS is partial at its 5' end, at the end of the sequence at nt1516, and ends at nt1020\. The first complete codon begins at nt1514, so it has codon_start=3.

<pre>complementary.fsa

>AMCont1022  [organism=Burkholderia terrae DEF2] [strain=DEF2] [isolation-source=soil in forest] [country=USA: Maryland]
CTTGTTTTCCTTTAAGCATTTCAGCCAAAGATTTTAATGGACGTTTACCAGTTCCTGTAATTACTCTGCC
TCTTCTGCCATTATCGAATAAAGCATCCACTGACTCTTGCAACATTCGTTTTTCATTTCTAATAATTATA
TCTGGAGCTTTAAGATCCATTAATCTTTTCAATCTATTATTTCTATTTATAACTCTTCTATACAAATCGT
TTAGATCTGATGTTGCAAATCTACCTCCATCTAGAGGAACAAGTGGCCTTAACTCTGGTGGTATTACAGG
TATAGTAGTTAAAATCATCCATTCTGGTTTGTTACCAGTTTCAATAAATGAATCGATCAGTTTTAATCTT
TTTATAGATCTTTCTTCAGCAACCTTTGATTTTGTCTCATTTATATTTTTTAATAAAATTTCTCTCTCTT
TATTCAAGTCTATAGATTTTAAAATCTCTAGTATCGCCTCTGCTCCTATTCCTGCAGTAAAGGATTCTTC
ACCAAACTCCTCTTGATATTTATTTAATTCATCTTCGTTTAAAAGTTGATTTTTTTTAAGACTAGTTAAT
CCAGGCTCTATAACAATAAAACTTTCAAAGTATAGAACTCTTTCAACCTCTTTAAGCTTCATATCAATAG
CTAGTGAAATTCTACTTGGTAAAGATTTTAAAAACCAAATATGTGCAACTGGGGTTGATAAATTGATGTG
CCCCATTCTTTCTCTACGAACATTTGATTTAGTAACCTCTACGCCACACTTCTCACAAATAATTCCTCTG
AACTTCATTCTTTTATATTTTCCACATAAACATTCGTAATCTTTTATTGGACCAAATATTCTCGCACAAA
ATAGGCCGTCTTTTTCAGGTCTGAAAGTTCTATAATTAATAGTTTCGGGTTTTTTTATTTCTCCATAAGT
CCATGACTTTATCTTTTCAGGGCTTGCTAAAGTAATTTTAATACTATTAAAATTTTGAGAGTCTGATATG
GCAGTTTCTTTAAAAAAATCTTTAATATCTTTTTTCATTTTAATTTAACTCCACATTAAGAGCTAGCGCT
TTGATTTCTTTTACTAAAACATTAAATGACTCAGGTATTCCTGACTCGAAATTCTCTTCACCTTTTACTA
TTGTTTCATAAACTTTAACTCTACCAGCAACATCATCAGATTTTACTGTTAAAATTTCTTGTAAAGTATA
AGAAGCCCCATAAGCTTCCAGAGCCCAAACTTCCATTTCTCCAAATCGTTGACCTCCCAATTGAGCCTTA
CCACCAAGAGGTTGTTGTGTAACTAAACTATAAGGACCTGTAGATCTTGCGTGTATTTTATCTTCTACAA
GATGGTGTAATTTTAACATATAAATAGTGCCAACTGTGACTTCTCTATCAAATTTTTCACCTGTTCTACC
ATCCCACAATTTTGTTTGACCAGATTTTGGTAATGATGCAAGCTCTAACATATTTGTTACATCTTGCTCT
TTTGCGCCATCAAAAACTGGTGTTGAAATTGGAATTCCACTTTGCA

complementary.tbl

>Feature AMCont1022 
1018	>1	gene
			locus_tag	AMt_11123
1018	>1	CDS
			product	hypothetical protein
			protein_id	gnl|dbname|AMt_11123
<1516	1020	gene
			locus_tag	AMt_11124
<1516	1020	CDS
			product	oxidase
			codon_start	3
			protein_id	gnl|dbname|AMt_11124

</pre>

</div>

</div>

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

</div>

</div>