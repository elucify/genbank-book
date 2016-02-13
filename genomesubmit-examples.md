# Bacterial Genome Submission Examples

#### Figure 1: Sample FASTA-formatted sequence

<pre>>HTE831 [organism=Oceanobacillus iheyensis] [strain=HTE831] [topology=circular] [completeness=complete]
actttcaaaaaaatcagcgtaaaaaacatactaatttgggcaaattcccacctgttttta
gggacatttttctttgaattagagcctcagcagctcgtcattgctgaattttcttgaagt
[etc.]

</pre>

#### Figure 2: Sequin table format

<pre>>Feature HTE831
<span class="gene">1830	2966	gene
			gene	dnaN
			locus_tag     OBB_0002</span>
<span class="annot">1830	2966	CDS
			product	DNA-directed DNA polymerase III beta chain
			EC_number	2.7.7.7
			protein_id	gnl|ncbi|OBB_0002</span>
<span class="gene">3219	3440	gene
			locus_tag     OBB_0003</span>
<span class="annot">3219	3440	CDS
			product	hypothetical protein
			protein_id	gnl|ncbi|OBB_0003</span>
<span class="gene">3443	4552	gene
			gene	recF
			locus_tag     OBB_0004</span>
<span class="annot">3443	4552	CDS
			product	RecF
			function	DNA repair and genetic recombination
			protein_id	gnl|ncbi|OBB_0004</span>
<span class="gene">5109	7034	gene
			gene	gyrB
			locus_tag     OBB_0006</span>
<span class="annot">5109	7034	CDS
			product	DNA gyrase subunit B
			EC_number	5.99.1.3
			protein_id	gnl|ncbi|OBB_0006</span>
<span class="gene">45081	44806	gene
			gene	abrB
			locus_tag     OBB_0045</span>
<span class="annot">45081	44806	CDS
			product	AbrB
			protein_id	gnl|ncbi|OBB_0045
			function	transcriptional pleiotropic regulator</span>
<span class="gene">64225	64758	gene
			locus_tag     OBB_0064</span>
<span class="annot">64225	64758	CDS
			product	stage V sporulation protein T
			function	transcriptional regulator
			protein_id	gnl|ncbi|OBB_0064</span>
<span class="gene">84524	85393	gene
			locus_tag     OBB_0082</span>
<span class="annot">84524	85393	CDS
			product	chaperonin
			product	heat shock protein 33
			protein_id	gnl|ncbi|OBB_0082</span>
<span class="gene">89569	91050	gene
			locus_tag     OBB_0088</span>
<span class="annot">89569	91050	CDS
			product	lysine-tRNA ligase
			EC_number	6.1.1.6
			protein_id	gnl|ncbi|OBB_0088</span>
<span class="operon">91493	96462	operon
			operon	rrnA</span>
<span class="gene">91493	93058	gene
			gene	rrsA
			locus_tag     OBB_0089</span>
<span class="rrna">91493	93058	rRNA
			product	16S ribosomal RNA</span>
<span class="gene">93292	96213	gene
			gene	rrlA
			locus_tag     OBB_0090</span>
<span class="rrna">93292	96213	rRNA
			product	23S ribosomal RNA</span>
<span class="gene">96347	96462	gene
			gene	rrfA
			locus_tag     OBB_0091</span>
<span class="rrna">96347	96462	rRNA
			product	5S ribosomal RNA</span>
<span class="operon">96468	96744	operon
			operon	trnC
<span class="gene">96468	96543	gene</span>
			gene	trnV
			locus_tag     OBB_0092</span>
<span class="trna">96468	96543	tRNA
			product	tRNA-Val</span>
<span class="gene">96545	96620	gene
			gene	trnT
			locus_tag     OBB_0093</span>
<span class="trna">96545	96620	tRNA
			product	tRNA-Thr</span>
<span class="gene">96669	96744	gene
			gene	trnK
			locus_tag     OBB_0094</span>
<span class="trna">96669	96744	tRNA
			product	tRNA-Lys</span>
<span class="gene">1914923	1914066	gene
			gene	folD
			locus_tag     OBB_1880</span>
<span class="annot">1914923	1914066	CDS
			product	bifunctional methylenetetrahydrofolate dehydrogenase (NADP+)/methenyltetrahydrofolate cyclohydrolase
			EC_number	1.5.1.5
			EC_number	3.5.4.9
			protein_id	gnl|ncbi|OB1880</span>
</pre>

#### Figure 3: GenBank flatfile

<pre>LOCUS  OB_HTE831       3630528 bp    DNA     circular BCT 11-DEC-2002
DEFINITION  Oceanobacillus iheyensis HTE831, complete genome.
ACCESSION
VERSION
KEYWORDS    .
SOURCE      Oceanobacillus iheyensis HTE831
  ORGANISM  Oceanobacillus iheyensis HTE831
            Bacteria; Firmicutes; Bacillales; Oceanobacillus.
REFERENCE   1  (bases 1 to 3630528)
  AUTHORS   Takami,H., Takaki,Y. and Uchiyama,I.
  TITLE     Genome sequence of Oceanobacillus iheyensis isolated from the Iheya
            Ridge and its unexpected adaptive capabilities to extreme
            environments
  JOURNAL   Nucleic Acids Res. 30 (18), 3927-3935 (2002)
   PUBMED   12235376
REFERENCE   2  (bases 1 to 3630528)
  AUTHORS   Takami,H., Takaki,Y. and Chee,G.
  TITLE     Direct Submission
  JOURNAL   Submitted (26-DEC-2001) Hideto Takami, Japan Marine Science and
            Technology Center, Deep-sea Microorganisms Research Group; 2-15
            Natsushima-cho, Yokosuka, Kanagawa 237-0061, Japan
FEATURES             Location/Qualifiers
     source          1..3630528
                     /organism="Oceanobacillus iheyensis HTE831"
                     /strain="HTE831"
                     /db_xref="taxon:221109"
     <span class="gene">gene            1830..2966
                     /gene="dnaN"
                     /locus_tag="OBB_0002"</span>
     <span class="annot">CDS             1830..2966
                     /gene="dnaN"
                     /locus_tag="OBB_0002"
                     /EC_number="2.7.7.7"
                     /codon_start=1
                     /transl_table=11
                     /product="DNA-directed DNA polymerase III beta chain"
                     /translation="MRFTIQRDKLINGVSNVMKAISARTVIPILTGMKIEVKNHGVTL
                     TGSDSDISIEYYIPIEEDGIVHVENIEEGTIILQAKYFPDIVRKLPESTVDIVVDDQL
                     NVRITSGKAEFNLNGQSAEEYPQLPKVQTENSFELPIDLLKSMIKQTVFAVSTMETRP
                     ILTGVNLKLVDNSLSFTATDSHRLARREIPVSNAPIEISQIVVPGKSLNELNKILGDS
                     EETVEISVTNNQILFRTKHLNFLSRLLDGNYPETSRLIPEQSKTKIQLKTKELLGTID
                     RASLLAKEERNNVVKFNAPGNSMIEISSNSPEVGNVVEEITADQMEGEDVKISFSSKY
                     MIDALKAIEYDEVQIEFTGAMRPFIIRPVGDDSILQLILPVRTY"</span>
     <span class="gene">gene            3219..3440
                     /locus_tag="OBB_0003"</span>
     <span class="annot">CDS             3219..3440
                     /locus_tag="OBB_0003"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /translation="MHEQIQIDTEYITLGQLIKLLNFLESGGMVKTFLQEEGALVNGH
                     LEQRRGRKLYPKDVVEIQGIGSYIVIKED"</span>
     <span class="gene">gene            3443..4552
                     /gene="recF"
                     /locus_tag="OBB_0004"</span>
     <span class="annot">CDS             3443..4552
                     /gene="recF"
                     /locus_tag="OBB_0004"
                     /function="DNA repair and genetic recombination"
                     /codon_start=1
                     /transl_table=11
                     /product="RecF"
                     /translation="MHIEKLELTNYRNYDQLEIAFDDQINVIIGENAQGKTNLMEAIY
                     VLSFARSHRTPREKELIQWDKDYAKIEGRITKRNQSIPLQISITSKGKKAKVNHLEQH
                     RLSDYIGSVNVVMFAPEDLTIVKGAPQIRRRFMDMELGQIQPTYIYHLAQYQKVLKQR
                     NHLLKQLQRKPNSDTTMLEVLTDQLIEHASILLERRFIYLELLRKWAQPIHRGISREL
                     EQLEIQYSPSIEVSEDANKEKIGNIYQMKFAEVKQKEIERGTTLAGPHRDDLIFFVNG
                     KDVQTYGSQGQQRTTALSIKLAEIELIYQEVGEYPILLLDDVLSELDDYRQSHLLNTI
                     QGKVQTFVSTTSVEGIHHETLQQAELFRVTDGVVN"</span>
     <span class="gene">gene            5109..7034
                     /gene="gyrB"
                     /locus_tag="OBB_0006"</span>
     <span class="annot">CDS             5109..7034
                     /gene="gyrB"
                     /locus_tag="OBB_0006"
                     /EC_number="5.99.1.3"
                     /codon_start=1
                     /transl_table=11
                     /product="DNA gyrase subunit B"
                     /translation="MSMEDKITENQEYGADQIQVLEGLEAVRKRPGMYIGSTSEKGLH
                     HLVWEIVDNSIDEALAGYCDHIQVVVEEDNSITVKDNGRGIPVDIQQKTGRPALEVIM
                     TVLHAGGKFGGGGYKVSGGLHGVGASVVNALSSELEVYVHRDGKVHFLSFKKGVPDGE
                     IKVIGDTDITGTVTHFRPDTEIFTETTEYNFDTLEQRLRELAFLNKGLKISIEDKRTD
                     REQVTYHYEGGISSYVEFINKNKEVLHEPFFAEGEDQGISVEVAIQYNDGFASNLYSF
                     ANNIHTYEGGSHEVGFRSGLTRIINDYAKKNGLIKDGDSNLSGDDVREGMTTIVSIKH
                     PDPQFEGQTKTKLGNSEVRAITDGVFSEAFSKFLYENPSTAKIIVEKGLMASRARLAA
                     KKARELTRRKSNLEISNLPGKLADCSSRDAAISELYIVEGDSAGGSAKSGRDRHFQAI
                     LPLRGKILNVEKARLDRILSNNEVRAMITALGSGVGEEFDISKARYHKIVIMTDADVD
                     GAHIRTLLLTFFYRYMRPLIEQGYIYIAQPPLYQVKQGKTVNYAYNDKELDRILNEIP
                     KAPKPNIQRYKGLGEMNADQLWDTTMDPDTRTLLQVELSDAIDADQVFDMLMGDKVEP
                     RRIFIEENAQYVKNLDI"</span>
     <span class="gene">gene            complement(44806..45081)
                     /gene="abrB"
                     /locus_tag="OBB_0045"</span>
     <span class="annot">CDS             complement(44806..45081)
                     /gene="abrB"
                     /locus_tag="OBB_0045"
                     /function="transcriptional pleiotropic regulator"
                     /codon_start=1
                     /transl_table=11
                     /product="AbrB"
                     /translation="MKSTGIVRKVDELGRVVIPIELRRTLDIHEKDTMEIYVDNDKIV
                     LKKYKPNMTCQVTGEVSDENLSIANGNLVLSPAGAQILLEEIQSRFK"</span>
     <span class="gene">gene            64225..64758
                     /locus_tag="OBB_0064"</span>
     <span class="annot">CDS             64225..64758
                     /locus_tag="OBB_0064"
                     /function="transcriptional regulator"
                     /codon_start=1
                     /transl_table=11
                     /product="stage V sporulation protein T"
                     /translation="MKATGIVRRIDDLGRVVVPKEIRRTLRIREGDPLEIFVDREGEV
                     ILKKYSPINELGHFAKEYAEALFQSLQTPVMITDRDDVIAVAGESKKEYLNKPISNAI
                     ADTIEGRSQVFEVDTKSMEIIDGQEQQLQSYCIHPVIANGDPIGCVLIFSKEEKLSKI
                     EQKAAETASTFLAKQME"</span>
     <span class="gene">gene            84524..85393
                     /locus_tag="OBB_0082"</span>
     <span class="annot">CDS             84524..85393
                     /locus_tag="OBB_0082"
                     /note="heat shock protein 33"
                     /codon_start=1
                     /transl_table=11
                     /product="chaperonin"
                     /translation="MKDYLIKATANNGKIRAYAVQSTNTIEEARRRQDTFATASAALG
                     RTITITAMMGAMLKGDDSITTKVMGNGPLGAIVADADADGHVRGYVTNPHVDFDLNDK
                     GKLDVARAVGTEGNISVIKDLGLKDFFTGETPIVSGEISEDFTYYYATSEQLPSAVGA
                     GVLVNPDHTILAAGGFIVQVMPGAEEEVINELEDQIQAIPAISSLIREGKSPEEILTQ
                     LFGEECLTIHEKMPIEFRCKCSKDRLAQAIIGLGNDEIQAMIEEDQGAEATCHFCNEK
                     YHFTEEELEDLKQ"</span>
     <span class="gene">gene            89569..91050
                     /locus_tag="OBB_0088"</span>
     <span class="annot">CDS             89569..91050
                     /locus_tag="OBB_0088"
                     /EC_number="6.1.1.6"
                     /codon_start=1
                     /transl_table=11
                     /product="lysine-tRNA ligase"
                     /translation="MSEELNEHMQVRRDKLAEHMEKGLDPFGGKFERSHQATDLIEKY
                     DSYSKEELEETTDEVTIAGRLMTKRGKGKAGFAHIQDLSGQIQLYVRKDMIGDDAYEV
                     FKSADLGDIVGVTGVMFKTNVGEISVKAKQFQLLTKSLRPLPEKYHGLKDIEQRYRQR
                     YLDLITNPDSRGTFVSRSKIIQSMREYLNGQGFLEVETPMMHSIPGGASARPFITHHN
                     ALDIELYMRIAIELHLKRLMVGGLEKVYEIGRVFRNEGVSTRHNPEFTMIELYEAYAD
                     YHDIMELTENLVAHIAKQVHGSTTITYGEHEINLEPKWTRLHIVDAVKDATGVDFWKE
                     VSDEEARALAKEHGVQVTESMSYGHVVNEFFEQKVEETLIQPTFIHGHPVEISPLAKK
                     NKEDERFTDRFELFIVGREHANAFSELNDPIDQRARFEAQVKERAEGNDEAHYMDEDF
                     LEALEYGMPPTGGLGIGVDRLVMLLTNSPSIRDVLLFPQMRTK"</span>
     <span class="operon">operon          91493..96462
                     /operon="rrnA"</span>
     <span class="gene">gene            91493..93058
                     /gene="rrsA"
                     /locus_tag="OBB_0089"
                     /operon="rrnA"</span>
     <span class="rrna">rRNA            91493..93058
                     /gene="rrsA"
                     /locus_tag="OBB_0089"
                     /operon="rrnA"
                     /product="16S ribosomal RNA"</span>
     <span class="gene">gene            93292..96213
                     /gene="rrlA"
                     /locus_tag="OBB_0090"
                     /operon="rrnA"
     <span class="rrna">rRNA            93292..96213
                     /gene="rrlA"
                     /locus_tag="OBB_0090"
                     /operon="rrn"
                     /product="23S ribosomal RNA"</span>
     <span class="gene">gene            96347..96462
                     /gene="rrfA"
                     /locus_tag="OBB_0091"
                     /operon="rrnA"
     <span class="rrna">>rRNA            96347..96462
                     /gene="rrfA"
                     /locus_tag="OBB_0091"
                     /operon="rrnA"
                     /product="5S ribosomal RNA"</span>
     <span class="operon">operon          96468..96744
                     /operon="trnC"</span>
     <span class="gene">gene            96468..96543
                     /gene="trnV"
                     /locus_tag="OBB_0092"
                     /operon="trnC"</span>
     <span class="trna">tRNA            96468..96543
                     /gene="trnV"
                     /locus_tag="OBB_0092"
                     /operon="trnC"
                     /product="tRNA-Val"</span>
     <span class="gene">gene            96545..96620
                     /gene="trnT"
                     /locus_tag="OBB_0093"
                     /operon="trnC"</span>
     <span class="trna">tRNA            96545..96620
                     /gene="trnT"
                     /locus_tag="OBB_0093"
                     /operon="trnC"
                     /product="tRNA-Thr"</span>
     <span class="gene">gene            96669..96744
                     /gene="trnK"
                     /locus_tag="OBB_0094"
                     /operon="trnC"</span>
     <span class="trna">tRNA            96669..96744
                     /gene="trnK"
                     /locus_tag="OBB_0094"
                     /operon="trnC"
                     /product="tRNA-Lys"</span>
     <span class="gene">gene            complement(1914066..1914923)
                     /gene="folD"
                     /locus_tag="OBB_1880"</span>
     <span class="annot">CDS             complement(1914066..1914923)
                     /gene="folD"
                     /EC_number="1.5.1.5"
                     /EC_number="3.5.4.9"
                     /locus_tag="OBB_1880"
                     /codon_start=1
                     /transl_table=11
                     /product="bifunctional methylenetetrahydrofolate dehydrogenase (NADP+)/
                     methenyltetrahydrofolate cyclohydrolase"
                     /translation="MATLLNGKELSEELKQKMKIEVDELKEKGLTPHLTVILVGDNPA
                     SKSYVKGKEKACAVTGISSNLIELPENISQDELLQIIDEQNNDDSVHGILVQLPLPDQ
                     MDEQKIIHAISPAKDVDGFHPINVGKMMTGEDTFIPCTPYGILTMLRSKDISLEGKHA
                     VIIGRSNIVGKPIGLLLLQENATVTYTHSRTKNLQEITKQADILIVAIGRAHAINADY
                     IKEDAVVIDVGINRKDDGKLTGDVDFESAEQKASYITPVPRGVGPMTITMLLKNTIKA
                     AKGLNDVER"</span> <span class="operon">BASE COUNT  1165552 a 648314 c 647106 g1169556 t
ORIGIN
        1 actttcaaaa aaatcagcgt aaaaaacata ctaatttggg caaattccca cctgttttta
       61 gggacatttt tctttgaatt agagcctcag cagctcgtca ttgctgaatt ttcttgaagt</span> </span></span>
</pre>

For an additional examples see GenBank Accession Number [CP000141](//www.ncbi.nlm.nih.gov/nuccore/CP000141?) .



