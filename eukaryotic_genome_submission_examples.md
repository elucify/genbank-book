
## Eukaryotic Genome Submission Examples

#### Figure 1: Sample FASTA-formatted sequence

<pre>>HTE831 [organism=Drosophila yakuba] [strain=HTE831]
tagagcaaaaaatagacattttaatggcgctaatcatacaaggaaggaataataacactg
acatggatacatccacttaatctacatttgcttattcctatcttgactatatctatatcc
[etc.]
</pre>

#### Figure 2: Feature table format

This mock example of a feature table file includes:

*   Genes whose 5' and 3' UTRs are known (eg, [Ngs_17131](#Ngs_17131) and [Ngs_3038](#Ngs_3038) ).
*   Gene with no UTR information ( [Ngs_2945](#Ngs_2945) ).
*   Features on the complementary strand (eg, [Ngs_3038](#Ngs_3038) and [Ngs_11232](#Ngs_11232) ).
*   Pseudogene ( [Ngs_10112](#Ngs_10112) ).
*   Gene that is alternatively spliced ( [Ngs_3038](#Ngs_3038) ).
*   Gene for a bifunctional protein ( [Ngs_2945](#Ngs_2945) ).
*   RNAs (eg, [Ngs_10111](#Ngs_10111) and [Ngs_11232](#Ngs_11232) )
*   Transposable elements and AT-rich sequences ( [repeat_region features](#repeat_region) )
*   Features that are partial (eg, [Ngs_2945](#Ngs_2945) ).
*   A [misc_feature](#misc_feature) .
*   Experiment and inference evidence qualifiers (CDS of [Ngs_17131](#Ngs_17131) and [Ngs_2945](#Ngs_2945) )

Note that the relative order of the features in the file does not matter, and that the misc_feature and repeat_region features do not have a corresponding gene feature, and so do not have a locus_tag.

See the flatfile view of this file in [Figure 3](#fig3) .

<pre>>Feature HTE831
<span class="gene"><a class="gene" id="Ngs_17131">63574	87173	gene
			locus_tag		Ngs_17131</a></span> 
<span class="mrna">63574	63907	mRNA
75690	75730
84396	85536
85598	85773
85836	86109
86173	86467
86555	86670
86731	87173
			product  hypothetical protein
			protein_id	gnl|ncbi|Ngs_17131
			transcript_id	gnl|ncbi|Ngs_mrna17131</span>
<span class="annot">84402	85536	CDS
85598	85773
85836	86109
86173	86467
86555	86670
86731	86882
			product	hypothetical protein
			protein_id	gnl|ncbi|Ngs_17131
			transcript_id	gnl|ncbi|Ngs_mrna17131
			inference	similar to RNA sequence, mRNA:INSD:AY123455.2</span> 
<span class="gene"><a class="gene" id="Ngs_3038">102664	100872	gene
			locus_tag		Ngs_3038</a>
			gene	TpnI</span> 
<span class="mrna">102664	102502	mRNA
102400	102234
102168	100872
			product	troponin isoform B
			protein_id	gnl|ncbi|Ngs_3038B
			transcript_id	gnl|ncbi|Ngs_mrna3038B
			note	transcript variant B; alternatively spliced</span>
<span class="mrna">102655	102234	mRNA
102168	100872
			product	troponin isoform A
			protein_id	gnl|ncbi|Ngs_3038A
			transcript_id	gnl|ncbi|Ngs_mrna3038A
			note	transcript variant A; alternatively spliced</span>
<span class="annot">102503	102502	CDS
102400	102234
102168	101261
			product	troponin isoform B
			protein_id	gnl|ncbi|Ngs_3038B 
			transcript_id	gnl|ncbi|Ngs_mrna3038B
			note	encoded by transcript variant B; alternatively spliced</span>
<span class="annot">102492	102234	CDS
102168	101261
			product	troponin isoform A
			protein_id	gnl|ncbi|Ngs_3038A
			transcript_id	gnl|ncbi|Ngs_mrna3038A
			note	encoded by transcript variant A; alternatively spliced</span>
<span class="gene"><a class="gene" id="Ngs_2945"><112616	>115107	gene	
			locus_tag		Ngs_2945</a></span> 
<span class="mrna"><112616	112646	mRNA
112703	113463
113584	113762
113821	114249
114302	114464
114804	114902
114964	>115107
			product	bifunctional methylenetetrahydrofolate dehydrogenase (NADP+)/methenyltetrahydrofolate cyclohydrolase
			protein_id	gnl|ncbi|Ngs_2945
			transcript_id	gnl|ncbi|Ngs_mrna2945</span>
<span class="annot">112616	112646	CDS
112703	113463
113584	113762
113821	114249
114302	114464
114804	114902
114964	115107
			product	bifunctional methylenetetrahydrofolate dehydrogenase (NADP+)/methenyltetrahydrofolate cyclohydrolase
			EC_number		1.5.1.5
			EC_number		3.5.4.9
			note	bifunctional
			experiment	Western blot
			protein_id	gnl|ncbi|Ngs_2945
			transcript_id	gnl|ncbi|Ngs_mrna2945</span>
<span class="gene"><a class="gene" id="Ngs_10111">101	180	gene
			locus_tag		Ngs_10111</a>
			gene	trnL</span> 
<span class="trna">101	180	tRNA
			product	Leu</span> 
<span class="gene"><a class="gene" id="Ngs_10112">45111	45190	gene
			locus_tag		Ngs_10112</a>
			pseudo</span> 
<span class="trna">45111	45190	tRNA
			product	Xxx</span> 
<span class="gene"><a class="gene" id="Ngs_11232">2103	400	gene
			locus_tag		Ngs_11232</a></span> 
<span class="rrna">2103	400	rRNA
			product	18S ribosomal RNA</span> 
<span class="misc">60101	60567	<a class="misc" id="misc_feature">misc_feature</a>
			note	similar to ABC transporters</span> 
43027	43136	<a class="repeat_region" id="repeat_region">repeat_region</a>
			mobile_element	retrotransposon:mini-me-Dpse-like{}4773
56408	56558	repeat_region
			mobile_element	retrotransposon:INE-1{}4674
62077	62147	repeat_region
			mobile_element	retrotransposon:P-T-Damb-like{}4769
63111	63154	repeat_region
			note	at-rich

 </pre>

#### Figure 3: GenBank flatfile

This is part of the flatfile view of the .sqn file made from the .fsa file ( [Fig. 1](#fig1) ) and .tbl file ( [Fig. 2](#fig2) ).

<pre>source          1..116100
                     /organism="Drosophila yakuba"
                     /mol_type="genomic DNA"
                     /strain="HTE831"
                     /db_xref="taxon:7245"
 <span class="gene">gene            101..180
                     /gene="trnL"
                     /locus_tag="Ngs_10111"</span> 
 <span class="trna">tRNA            101..180
                     /gene="trnL"
                     /locus_tag="Ngs_10111"
                     /product="tRNA-Leu"</span> 
 <span class="gene">gene            complement(400..2103)
                     /locus_tag="Ngs_11232"</span> 
 <span class="rrna">rRNA            complement(400..2103)
                     /locus_tag="Ngs_11232"
                     /product="18S ribosomal RNA"</span> 
     repeat_region   43027..43136
                     /mobile_element="retrotransposon:mini-me-Dpse-like{}4773"
 <span class="gene">gene            45111..45190
                     /locus_tag="Ngs_10112"
                     /pseudo</span> 
 <span class="trna">tRNA            45111..45190
                     /locus_tag="Ngs_10112"
                     /product="tRNA-OTHER" 
                     /pseudo</span> 
     repeat_region   56408..56558
                     /mobile_element="retrotransposon:INE-1{}4674"
 <span class="misc">misc_feature    60101..60567
                     /note="similar to ABC transporters"</span> 
     repeat_region   62077..62147
                     /mobile_element="retrotransposon:P-T-Damb-like{}4769"
     repeat_region   63111..63154
                     /note="at-rich"
 <span class="gene">gene            63574..87173
                     /locus_tag="Ngs_17131"</span> 
 <span class="mrna">mRNA            join(63574..63907,75690..75730,84396..85536,85598..85773,
                     85836..86109,86173..86467,86555..86670,86731..87173)
                     /locus_tag="Ngs_17131"
                     /product="hypothetical protein"</span> 
 <span class="annot">CDS             join(84402..85536,85598..85773,85836..86109,86173..86467,
                     86555..86670,86731..86882)
                     /locus_tag="Ngs_17131"
                     /inference="similar to RNA sequence, mRNA:INSD:AY123455.2"
                     /codon_start=1
                     /product="hypothetical protein"
                     /translation="MQSTQSKSDRSSMHRGPLLLCAVMVVLVTLPEQINARMAFEKLT
                     DFDFPGNTYYSVKNLSLYECQGWCREEADCQAAAFSFVVNPLSPSQETHCQLQNDSSA
                     ANPSAAPQRSANMYYMIKLQLRSENVCHRPWSFERVPNKVIRGLDNALIYTSTKEACL
                     SACLNERRFVCRSVEYDYNNMKCVLSDSDRRSSGQFVQLVDAQGTDYFENLCLKPAQA
                     CKNNRSFGNSQKMGVSEEKVAQYVGLHYYTDKELQVTSESACRLACEIESEFLCRSFL
                     YLGQPQGSQYNCRLYHLDHKTLPDGPSTYLNHERPLIDHGEPIGQYFENQCEKAAGLG
                     AGSPPGTLDKIDTLPVSLDTIEDPNLTNLTRNDVNCDKTGTCYDVSVHCKDTRIAVQV
                     RTNKPFNGRIYALGRSETCNIDVINSDAFRLDLTMAGQDCNTQSVTGVYSNTVVLQHH
                     SVVMTKADKIYKVKCTYDMSSKNITFGMMPIRDPEMIHINSSPEAPPPRIRILDTRQR
                     EVETVRIGDRLNFRIEIPEDTPYGIFARSCVAMAKDARTSFKIIDDDGCPTDPTIFPG
                     FTADGNALQSTYEAFRFTESYGVIFQCNVKYCLGPCEPAVCEWNMDSFESLGRRRRRS
                     IESNDTKSEDDMNISQEILVLDFGDEKREFFKADPSTDFAKDKTVTIIEPCPTKTSVL
                     ALAVTCALMILLYISTLFCYYMKKWMQPHKIVA"</span> 
 <span class="gene">gene            complement(100872..102664)
                     /gene="TpnI"
                     /locus_tag="Ngs_3038"</span> 
 <span class="mrna">mRNA            complement(join(100872..102168,102234..102400,
                     102502..102664))
                     /gene="TpnI"
                     /locus_tag="Ngs_3038"
                     /product="troponin isoform B"
                     /note="transcript variant B; alternatively spliced"</span> 
 <span class="mrna">mRNA            complement(join(100872..102168,102234..102655))
                     /gene="TpnI"
                     /locus_tag="Ngs_3038"
                     /product="troponin isoform A"
                     /note="transcript variant A; alternatively spliced"</span> 
 <span class="annot">CDS             complement(join(101261..102168,102234..102400,
                     102502..102503))
                     /gene="TpnI"
                     /locus_tag="Ngs_3038"
                     /note="encoded by transcript variant B; alternatively spliced"
                     /codon_start=1
                     /product="troponin isoform B"
                     /translation="MDSSQSRKNGFLLHLPLETKRNPSNPNTPLSNLLNLTDFHYLLA
                     SNVCRKAKRELLAVLIVTSYAGHDALRSAHRQAIPQSKLEEMGLRRVFLLAALPSREH
                     FISQDQLASEQNRFGDLLQGNFIEDYRNLSYKHVMGLKWVSEECKKQAKFIIKLDDDI
                     IYDVFHLRRYLETLEVREPGLATSSTLLSGYVLDAKPPIRLRANKWYVSKKEYPQALY
                     PAYLSGWLYVTNVPTAERIVAEAERMSFFWIDDTWLTGVVRTRLGIPLERHNDWFSAN
                     AEFIDCCVRDLKKHNYECEYSVGPNGGDDRLLVEFLHNVEKCYFDECVKRPVGKSLKE
                     TCLAAAKSRPPKHGFPEIKALRLR"</span> 
 <span class="annot">CDS             complement(join(101261..102168,102234..102492))
                     /gene="TpnI"
                     /locus_tag="Ngs_3038"
                     /note="encoded by transcript variant A; alternatively spliced"
                     /codon_start=1
                     /product="troponin isoform A"
                     /translation="MRMRGRRLLPIILSLLLIVLLSLCYFSNHLRDSSQSRKNGFLLH
                     LPLETKRNPSNPNTPLSNLLNLTDFHYLLASNVCRKAKRELLAVLIVTSYAGHDALRS
                     AHRQAIPQSKLEEMGLRRVFLLAALPSREHFISQDQLASEQNRFGDLLQGNFIEDYRN
                     LSYKHVMGLKWVSEECKKQAKFIIKLDDDIIYDVFHLRRYLETLEVREPGLATSSTLL
                     SGYVLDAKPPIRLRANKWYVSKKEYPQALYPAYLSGWLYVTNVPTAERIVAEAERMSF
                     FWIDDTWLTGVVRTRLGIPLERHNDWFSANAEFIDCCVRDLKKHNYECEYSVGPNGGD
                     DRLLVEFLHNVEKCYFDECVKRPVGKSLKETCLAAAKSRPPKHGFPEIKALRLR"</span> 
 <span class="gene">gene            <112616..>115107
                     /locus_tag="Ngs_2945"</span> 
 <span class="mrna">mRNA            join(<112616..112646,112703..113463,113584..113762,
                     113821..114249,114302..114464,114804..114902,
                     114964..>115107)
                     /locus_tag="Ngs_2945"
                     /product="bifunctional methylenetetrahydrofolate dehydrogenase (NADP+)/methenyltetrahydrofolate cyclohydrolase"</span> 
 <span class="annot">CDS             join(112616..112646,112703..113463,113584..113762,
                     113821..114249,114302..114464,114804..114902,
                     114964..115107)
                     /locus_tag="Ngs_2945"
                     /EC_number="3.5.4.9"
                     /EC_number="1.5.1.5"
                     /experiment="Western blot"
                     /codon_start=1
                     /product="bifunctional methylenetetrahydrofolate dehydrogenase (NADP+)/methenyltetrahydrofolate cyclohydrolase"
                     /translation="MESITFGVLTISDTCWQEPEKDTSGPILRQLIGETFANTQVIGN
                     IVPDEKDIIQQELRKWIDREELRVILTTGGTGFAPRDVTPEATRQLLEKECPQLSMYI
                     TLESIKQTQYAALSRGLCGIAGNTLILNLPGSEKAVKECFQTISALLPHAVHLIGDDV
                     SLVRKTHAEVQGSAQKSHICPHKTGTGTDSDRNSPYPMLPVQEVLSIIFNTVQKTANL
                     NKILLEMNAPVNIPPFRASIKDGYAMKSTGFSGTKRVLGCIAAGDSPNSLPLAEDECY
                     KINTGAPLPLEADCVVQVEDTKLLQLDKNGQESLVDILVEPQAGLDVRPVGYDLSTND
                     RIFPALDPSPVVVKSLLASVGNRLILSKPKVAIVSTGSELCSPRNQLTPGKIFDSNTT
                     MLTELLVYFGFNCMHTCVLSDSFQRTKESLLELFEVVDFVICSGGVSMGDKDFVKSVL
                     EDLQFRIHCGRVNIKPGKPMTFASRKDKYFFGLPGNPVSAFVTFHLFALPAIRFAAGW
                     DRCKCSLSVLNVKLLNDFSLDSRPEFVRASVISKSGELYASVNGNQISSRLQSIVGAD
                     VLINLPARTSDRPLAKAGEIFPASVLRFDFISKYE"</span> 
ORIGIN
        1 tagagcaaaa aatagacatt ttaatggcgc taatcataca aggaaggaat aataacactg
       61 acatggatac atccacttaa tctacatttg cttattccta tcttgactat atctatatcc
       [etc.]
</pre>

</div>

</div>