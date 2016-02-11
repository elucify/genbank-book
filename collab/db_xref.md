
# db_xrefs

The /db_xref qualifier serves as a vehicle for linking DNA sequence records to other external databases.

The text below outlines the format and the present list of allowed database cross references. Inquiries about the addition of other database types should be made to one of the collaborating databases.

<pre>**Qualifier:**       /db_xref="_database_:_identifier_"
**Definition:**      database cross-reference: pointer to related information 
                 in another database                         
**Scope:**           all feature keys
**Value format:**    "_database_:_identifier_" where _database_ is the name of the
                 database containing related information, and 
                 _identifier_ is the internal identifier of the related 
                 information according to the naming conventions of the
                 cross-referenced database.

**Examples:**        

cross reference to GDB identifier:            /db_xref="GDB:39999"   
cross reference to Swiss-Prot entry:          /db_xref="Swiss-Prot:P12345" 

</pre>

For all _databases_ types 'Case' is important. All member databases of the International Collaboration (DDBJ, EMBL/EBI and GenBank/NCBI) may make recommendations for additions or removal of databases to this list at their convenience, and need not rely on the release cycle of the Feature Table documentation.

* * *

**Database:** Description of database, and type with example(s).

* * *

**Presently the list includes:**

<table cellpadding="0" cellspacing="0"><caption>db_xref List</caption>

<tbody>

<tr>

<td valign="top" width="199">

[AceView/WormGenes](/IEB/Research/Acembly/)

</td>

<td valign="top" width="240">

AceView Worm Genome

</td>

<td valign="top" width="367">

/db_xref="AceView/WormGenes:vha-6"

</td>

</tr>

<tr>

<td valign="top">[AFTOL](http://aftol.org)</td>

<td valign="top">Assembling the Fungal Tree of Life</td>

<td valign="top">/db_xref="AFTOL:959"</td>

</tr>

<tr>

<td valign="top">[AntWeb](http://www.antweb.org)</td>

<td valign="top">Ant Database</td>

<td valign="top">/db_xref="AntWeb:CASENT0058943-D01"</td>

</tr>

<tr>

<td valign="top">[APHIDBASE](http://www.aphidbase.com/aphidbase/)</td>

<td valign="top">Aphid Genome Database</td>

<td valign="top">/db_xref="APHIDBASE:ACYPI007424"</td>

</tr>

<tr>

<td valign="top">[ApiDB](http://eupathdb.org/eupathdb/)</td>

<td valign="top">Apicomplexan Database Resources</td>

<td valign="top">/db_xref="ApiDB:cgd1_1090"</td>

</tr>

<tr>

<td valign="top">[ApiDB_CryptoDB](http://cryptodb.org/cryptodb/)</td>

<td valign="top">Cryptosporidium Genome Resources</td>

<td valign="top">/db_xref="ApiDB_CryptoDB:cgd7_20"</td>

</tr>

<tr>

<td valign="top">[ApiDB_PlasmoDB](http://www.plasmodb.org/plasmo/home.jsp)</td>

<td valign="top">Plasmodium Genome Resources</td>

<td valign="top">/db_xref="ApiDB_PlasmoDB: PF11_0344"</td>

</tr>

<tr>

<td valign="top">[ApiDB_ToxoDB](http://www.toxodb.org/toxo/home.jsp)</td>

<td valign="top">Toxoplasma Genome Resources</td>

<td valign="top">/db_xref="ApiDB_ToxoDB:49.m00014"</td>

</tr>

<tr>

<td valign="top" width="199">

[ASAP](https://asap.genetics.wisc.edu/asap/logon.php)

</td>

<td valign="top" width="240">

A Systematic Annotation Package for Community Analysis of Genomes

</td>

<td valign="top" width="367">

/db_xref="ASAP:ABE-0000006"

</td>

</tr>

<tr>

<td valign="top" width="199">

[ATCC](http://www.atcc.org/)

</td>

<td valign="top" width="240">

American Type Culture Collection database

</td>

<td valign="top" width="367">

/db_xref="ATCC:123456"

</td>

</tr>

<tr>

<td valign="top" width="199">

[ATCC(in host)](http://www.atcc.org/)

</td>

<td valign="top" width="240">

American Type Culture Collection database

</td>

<td valign="top" width="367">

/db_xref="ATCC(in host):123456"

</td>

</tr>

<tr>

<td valign="top" width="199">

[ATCC(dna)](http://www.atcc.org/)

</td>

<td valign="top" width="240">

American Type Culture Collection database

</td>

<td valign="top" width="367">

/db_xref="ATCC(dna):123456”

</td>

</tr>

<tr>

<td valign="top" width="199">[Axeldb](http://www.dkfz-heidelberg.de/molecular_embryology/axeldb.htm)</td>

<td valign="top" width="240">

A Xenopus laevis database

</td>

<td valign="top" width="367">

/db_xref="Axeldb:32B3.1"

</td>

</tr>

<tr>

<td valign="top" width="199">

[BDGP_EST](http://www.fruitfly.org/EST/index.shtml)

</td>

<td valign="top" width="240">

Berkeley Drosophila Genome Project EST database

</td>

<td valign="top" width="367">

/db_xref="BDGP_EST:123456"

</td>

</tr>

<tr>

<td valign="top" width="199">

[BDGP_INS](http://www.fruitfly.org/)

</td>

<td valign="top" width="240">

Berkeley Drosophila Genome Project -- Insertion

</td>

<td valign="top" width="367">

/db_xref="BDGP_INS:123456"

</td>

</tr>

<tr>

<td valign="top" width="199">

[BEEBASE](http://hymenopteragenome.org/beebase/?q=home)

</td>

<td valign="top" width="240">

BeeBase

</td>

<td valign="top" width="367">

/db_xref="BEEBASE:GB55480"

</td>

</tr>

<tr>

<td valign="top" width="199">

[BEETLEBASE](http://www.beetlebase.org/)

</td>

<td valign="top" width="240">

Tribolium Genome Database -- Insertion

</td>

<td valign="top" width="367">

/db_xref="BEETLEBASE:TC030551"

</td>

</tr>

<tr>

<td valign="top" width="199">

[BGD](http://bovinegenome.org/genepages/btau40/)

</td>

<td valign="top" width="240">

Bovine Genome Database

</td>

<td valign="top" width="367">

/db_xref="BGD:BT10004"

</td>

</tr>

<tr>

<td valign="top" width="199">

[BOLD](http://www.barcodinglife.com)

</td>

<td valign="top" width="240">

Barcode of Life database

</td>

<td valign="top" width="367">

/db_xref="Bold:EPAF263"

</td>

</tr>

<tr>

<td valign="top" width="199">

[CABRI](http://www.cabri.org/)

</td>

<td valign="top" width="240">

Common Access to Biological Resources and Information Project

</td>

<td valign="top" width="367">

/db_xref="CABRI:ACC 424"

</td>

</tr>

<tr>

<td valign="top" width="199">[CCAP](http://www.ccap.ac.uk/)</td>

<td valign="top" width="240">

Culture Collection of Algae and Protozoa

</td>

<td valign="top" width="367">

/db_xref="CCAP:1460/15"

</td>

</tr>

<tr>

<td valign="top" width="199">[CDD](http://www.ncbi.nlm.nih.gov/Structure/cdd/cdd.shtml)</td>

<td valign="top" width="240">

Conserved Domain Database

</td>

<td valign="top" width="367">

/db_xref="CDD:02194"

</td>

</tr>

<tr>

<td valign="top" width="199">[CGD](http://www.candidagenome.org/)</td>

<td valign="top" width="240">

Candida Genome Database

</td>

<td valign="top" width="367">

/db_xref="CGD:CAL0005934"

</td>

</tr>

<tr>

<td valign="top" width="199">

[dbEST](http://www.ncbi.nlm.nih.gov/dbEST/index.html)

</td>

<td valign="top" width="240">

EST database maintained at the NCBI.

</td>

<td valign="top" width="367">

/db_xref="dbEST:123456"

/db_xref="dbEST:BP535535"

</td>

</tr>

<tr>

<td valign="top" width="199">

[dbProbe](http://www.ncbi.nlm.nih.gov/sites/entrez?db=probe)

</td>

<td valign="top" width="240">

NCBI Probe database Public registry of nucleic acid reagents

</td>

<td valign="top" width="367">

/db_xref="dbProbe:38"

</td>

</tr>

<tr>

<td valign="top" width="199">

[dbSNP](http://www.ncbi.nlm.nih.gov/SNP/)

</td>

<td valign="top" width="240">

Variation database maintained at the NCBI.

</td>

<td valign="top" width="367">

/db_xref="dbSNP:4647"

/db_xref="dbSNP:rs133073"

</td>

</tr>

<tr>

<td valign="top" width="199">

[dbSTS](http://www.ncbi.nlm.nih.gov/dbSTS/index.html)

</td>

<td valign="top" width="240">

STS database maintained at the NCBI.

</td>

<td valign="top" width="367">

/db_xref="dbSTS:456789"

/db_xref="dbSTS:BV210161"

</td>

</tr>

<tr>

<td valign="top">[dictyBase](http://dictybase.org/)</td>

<td valign="top">Dictyostelium genome database</td>

<td valign="top">/db_xref="dictyBase:DDB0191090"</td>

</tr>

<tr>

<td valign="top">[EcoGene](http://ecogene.org)</td>

<td valign="top">Database of _Escherichia coli_ Sequence and Function</td>

<td valign="top">/db_xref="EcoGene:EG11277"</td>

</tr>

<tr>

<td valign="top" width="199">

[ENSEMBL](http://www.ensembl.org)

</td>

<td valign="top" width="240">

Database of automatically annotated genomic data

</td>

<td valign="top" width="367">

/db_xref="ENSEMBL:HUMAN-Clone-AC005612"

/db_xref="ENSEMBL:HUMAN-Gene-ENSG00000007102"

</td>

</tr>

<tr>

<td valign="top" width="199">

[EnsemblGenomes](http://ensemblgenomes.org)

</td>

<td valign="top" width="240">

Extending Ensembl across taxonomic space

</td>

<td valign="top" width="367">

/db_xref="EnsemblGenomes:AAC73116"

/db_xref="EnsemblGenomes:b0005"

</td>

</tr>

<tr>

<td valign="top" width="199">

[EnsemblGenomes-Gn](http://ensemblgenomes.org)

</td>

<td valign="top" width="240">

EnsemblGenomes Gene

</td>

<td valign="top" width="367">

/db_xref="EnsemblGenomes-Gn"

</td>

</tr>

<tr>

<td valign="top" width="199">

[EnsemblGenomes-Tr](http://ensemblgenomes.org)

</td>

<td valign="top" width="240">

EnsemblGenomes Transcript

</td>

<td valign="top" width="367">

/db_xref="EnsemblGenomes-Tr:MAPG_00606T0"

</td>

</tr>

<tr>

<td valign="top" width="199">

[EPD](http://epd.vital-it.ch/)

</td>

<td valign="top" width="240">

Eukaryotic Promoter Database

</td>

<td valign="top" width="367">

/db_xref="EPD:EP00576"

</td>

</tr>

<tr>

<td valign="top">ERIC</td>

<td valign="top">Enteropathogen Resource Integration Center</td>

<td valign="top">db_xref="ERIC:ABY-0246137"</td>

</tr>

<tr>

<td valign="top" width="199">

ESTLIB

</td>

<td valign="top" width="240">

EBI's EST library identifier

</td>

<td valign="top" width="367">

/db_xref="ESTLIB:1200"

</td>

</tr>

<tr>

<td valign="top" width="199">

[FANTOM_DB](http://fantom.gsc.riken.go.jp/)

</td>

<td valign="top" width="240">

Database of Functional Annotation of Mouse

</td>

<td valign="top" width="367">

/db_xref="FANTOM_DB:0610005A07"

</td>

</tr>

<tr>

<td valign="top" width="199">

[FBOL](http://www.fungalbarcoding.org/)

</td>

<td valign="top" width="240">

International Fungal Working Group Fungal Barcoding.

</td>

<td valign="top" width="367">

/db_xref="FBOL:2224"

</td>

</tr>

<tr>

<td valign="top" width="199">

[FLYBASE](http://www.flybase.org/)

</td>

<td valign="top" width="240">

Database of Genetic and molecular data of Drosophila.

</td>

<td valign="top" width="367">

/db_xref="FLYBASE:FBgn0000024"

</td>

</tr>

<tr>

<td valign="top" width="199">

[Fungorum](http://www.indexfungorum.org)

</td>

<td valign="top" width="240">

Index Fungorum

</td>

<td valign="top" width="367">

/db_xref="Fungorum:ID550186"

</td>

</tr>

<tr>

<td valign="top" width="199">

[GABI](http://www.gabipd.org/information/about.shtml)

</td>

<td valign="top" width="240">

Network of Different Plant Genomic Research Projects

</td>

<td valign="top" width="367">

/db_xref="GABI:HA05J18"

</td>

</tr>

<tr>

<td valign="top" width="199">

GDB

</td>

<td valign="top" width="240">

Human Genome Database accession numbers

</td>

<td valign="top" width="367">

/db_xref="GDB:G00-128-600"

</td>

</tr>

<tr>

<td valign="top" width="199">

[GeneDB](http://www.genedb.org/)

</td>

<td valign="top" width="240">

Curated gene database for Leishmania major and Trypanosoma brucei

</td>

<td valign="top" width="367">

/db_xref="GeneDB:SPCC285.16c"

</td>

</tr>

<tr>

<td valign="top" width="199">

[GeneID](http://www.ncbi.nlm.nih.gov/sites/entrez?db=gene)

</td>

<td valign="top" width="240">

Entrez Gene Database (replaces NCBI Locus Link)

</td>

<td valign="top" width="367">

/db_xref="GeneID:3054987"

</td>

</tr>

<tr>

<td valign="top" width="199">

GI

</td>

<td valign="top" width="240">

GenInfo identifier, used as a unique sequence identifier for nucleotide and proteins

</td>

<td valign="top" width="367">

/db_xref="GI:1234567890"

</td>

</tr>

<tr>

<td valign="top" width="199">

[GO](http://amigo.geneontology.org/)

</td>

<td valign="top" width="240">

Gene Ontology Database identifier

</td>

<td valign="top" width="367">

/db_xref="GO:123"

</td>

</tr>

<tr>

<td valign="top" width="199">

[GOA](http://www.ebi.ac.uk/GOA/)

</td>

<td valign="top" width="240">

Gene Ontology Annotation Database Identifier

</td>

<td valign="top" width="367">

/db_xref=" GOA :P01100"

</td>

</tr>

<tr>

<td valign="top">[Greengenes](http://greengenes.lbl.gov/)</td>

<td valign="top">16S rRNA gene database</td>

<td valign="top">/db_xref="Greengenes:269185"</td>

</tr>

<tr>

<td valign="top">[GRIN](http://www.ars-grin.gov/)</td>

<td valign="top">Germplasm Resources Information Network</td>

<td valign="top">/db_xref="GRIN:1005973"</td>

</tr>

<tr>

<td valign="top">

[HGNC](http://www.genenames.org/cgi-bin/search)

</td>

<td valign="top">

Human Gene Nomenclature Database

</td>

<td valign="top">

/db_xref="HGNC:2041"

</td>

</tr>

<tr>

<td valign="top" width="199">

[H-InvDB](http://www.h-invitational.jp)

</td>

<td valign="top" width="240">

H-Invitational Database

</td>

<td valign="top" width="367">

/db_xref="H-InvDB:HIT000000001"

/db_xref="H-InvDB:HIX0000001”

</td>

</tr>

<tr>

<td valign="top" width="199">

[HMP](http://www.hmpdacc.org/)

</td>

<td valign="top" width="240">

Human Microbiome Project

</td>

<td valign="top" width="367">

/db_xref="HMP:0536"

</td>

</tr>

<tr>

<td valign="top" width="199">

[HOMD](http://www.homd.org/)

</td>

<td valign="top" width="240">

Human Oral Microbiome Database

</td>

<td valign="top" width="367">

/db_xref="HOMD:tax_078"

/db_xref="HOMD:seq_1603”

</td>

</tr>

<tr>

<td valign="top" width="199">

[HPM](http://www.humanproteomemap.org/)

</td>

<td valign="top" width="240">

Human Proteome Map

</td>

<td valign="top" width="367">

/db_xref="HPM:8106"

</td>

</tr>

<tr>

<td valign="top" width="199">

HSSP

</td>

<td valign="top" width="240">

Database of homology-derived secondary structure of proteins

</td>

<td valign="top" width="367">

/db_xref="HSSP:12GS

</td>

</tr>

<tr>

<td valign="top" width="199">

[I5KNAL](https://i5k.nal.usda.gov/)

</td>

<td valign="top" width="240">

i5k Workspace

</td>

<td valign="top" width="367">

/db_xref="I5KNAL:OFAS008986"

</td>

</tr>

<tr>

<td valign="top" width="199">

[IKMC](http://www.knockoutmouse.org/)

</td>

<td valign="top" width="240">

International Knockout Mouse Consortium

</td>

<td valign="top" width="367">

/db_xref="IKMC:66303"

</td>

</tr>

<tr>

<td valign="top" width="199">

[IMGT/GENE-DB](http://www.imgt.org/IMGTindex/IMGTgene-db.html)

</td>

<td valign="top" width="240">

Immunogenetics database, immunoglobulin and T-cell receptor genes

</td>

<td valign="top" width="367">

/db_xref="IMGT/GENE-DB:IGKC"

</td>

</tr>

<tr>

<td valign="top" width="199">

[IMGT/LIGM](http://www.imgt.org/IMGTinformation/LIGM.html)

</td>

<td valign="top" width="240">

Immunogenetics database, immunoglobulins and T-cell receptors

</td>

<td valign="top" width="367">

/db_xref="IMGT/LIGM:U03895"

</td>

</tr>

<tr>

<td valign="top" width="199">

[IMGT/HLA](http://www.ebi.ac.uk/imgt/hla/)

</td>

<td valign="top" width="240">

Immunogenetics database, human MHC

</td>

<td valign="top" width="367">

/db_xref="IMGT/HLA:HLA00031"

</td>

</tr>

<tr>

<td valign="top" width="199">

[InterPro](http://www.ebi.ac.uk/interpro/)

</td>

<td valign="top" width="240">

InterPro protein sequence database

</td>

<td valign="top" width="367">

/db_xref="InterPro:IPR002928"

</td>

</tr>

<tr>

<td valign="top" width="199">

[IntrepidBio](http://server1.intrepidbio.com/)

</td>

<td valign="top" width="240">

Intrepid BioInformatics

</td>

<td valign="top" width="367">

/db_xref="IntrepidBio:5259707746"

</td>

</tr>

<tr>

<td valign="top" width="199">

[IRD](http://www.fludb.org/)

</td>

<td valign="top" width="240">

Influenza Research Database

</td>

<td valign="top" width="367">

/db_xref="IRD:CEIRS-CIP045-123456.2"

</td>

</tr>

<tr>

<td valign="top" width="199">

[ISFinder](http://www-is.biotoul.fr/)

</td>

<td valign="top" width="240">

Insertion sequence elements database

</td>

<td valign="top" width="367">

/db_xref="ISFinder:ISA1083-2"

</td>

</tr>

<tr>

<td valign="top" width="199">

[ISHAM-ITS](http://its.mycologylab.org/DefaultSlideUD.aspx?Page=Home)

</td>

<td valign="top" width="240">

ITS reference database for pathogenic fungi

</td>

<td valign="top" width="367">

/db_xref="ISHAM-ITS:MITS310"

</td>

</tr>

<tr>

<td valign="top" width="199">

[JCM](http://www.jcm.riken.go.jp/)

</td>

<td valign="top" width="240">

Japan Collection of Microorganisms

</td>

<td valign="top" width="367">

/db_xref="JCM:1339"

</td>

</tr>

<tr>

<td valign="top" width="199">

[JGIDB](http://genome.jgi-psf.org/)

</td>

<td valign="top" width="240">

JGI Genome Portal

</td>

<td valign="top" width="367">

/db_xref="JGIDB:Chluvu1_81011"

</td>

</tr>

<tr>

<td valign="top" width="199">

LocusID

</td>

<td valign="top" width="240">

NCBI LocusLink ID **Discontinued March 2005

</td>

<td valign="top" width="367">

/db_xref="LocusID:51199"

</td>

</tr>

<tr>

<td valign="top" width="199">

[MaizeGDB](http://www.maizegdb.org/)

</td>

<td valign="top" width="240">

Maize Genome Database unique identifiers

</td>

<td valign="top" width="367">

/db_xref="MaizeGDB:635633 "

</td>

</tr>

<tr>

<td valign="top" width="199">

[MedGen](http://www.ncbi.nlm.nih.gov/medgen)

</td>

<td valign="top" width="240">

Human Medical Genetics

</td>

<td valign="top" width="367">

/db_xref="MedGen:C0010674"

</td>

</tr>

<tr>

<td valign="top" width="199">

[MGI](http://www.informatics.jax.org/)

</td>

<td valign="top" width="240">

Mouse Genome Informatics

</td>

<td valign="top" width="367">

/db_xref="MGI:1894891"

</td>

</tr>

<tr>

<td valign="top" width="199">

[MIM](http://www.ncbi.nlm.nih.gov/sites/entrez?db=omim)

</td>

<td valign="top" width="240">

Mendelian Inheritance in Man numbers

</td>

<td valign="top" width="367">

/db_xref="MIM:123456"

</td>

</tr>

<tr>

<td valign="top" width="199">

[miRBase](http://www.mirbase.org/)

</td>

<td valign="top" width="240">

miRNA Database

</td>

<td valign="top" width="367">

/db_xref="miRBase:MI0000681"

</td>

</tr>

<tr>

<td valign="top" width="199">

[MycoBank](http://www.mycobank.org)

</td>

<td valign="top" width="240">

Fungal Nomenclature and Species Bank

</td>

<td valign="top" width="367">

/db_xref="MycoBank:8284"

</td>

</tr>

<tr>

<td valign="top" width="199">

[NBRC](http://www.nbrc.nite.go.jp/e/catalog-e.html)

</td>

<td valign="top" width="240">

NITE Biological Resource Center

</td>

<td valign="top" width="367">

/db_xref="NBRC:3189"

</td>

</tr>

<tr>

<td valign="top" width="199">

[NextDB](http://nematode.lab.nig.ac.jp/)

</td>

<td valign="top" width="240">

Nematode Expression Pattern DataBase

</td>

<td valign="top" width="367">

/db_xref="NextDB:CELK01662"

</td>

</tr>

<tr>

<td valign="top" width="199">

[niaEST](http://esbank.nia.nih.gov/)

</td>

<td valign="top" width="240">

NIA Mouse cDNA Project

</td>

<td valign="top" width="367">

/db_xref="niaEST:L0304H12-3"

</td>

</tr>

<tr>

<td valign="top">[NMPDR](http://www.nmpdr.org)</td>

<td valign="top">National Microbial Pathogen Data Resource</td>

<td valign="top">/db_xref="NMPDR:fig|306254.1.peg.183"</td>

</tr>

<tr>

<td valign="top">[NRESTdb](http://www.genomemalaysia.gov.my/nrestdb/)</td>

<td valign="top">Natural Rubber EST database</td>

<td valign="top">/db_xref="NRESTdb:Y01A01"</td>

</tr>

<tr>

<td valign="top">[OrthoMCL](http://orthomcl.org/orthomcl)</td>

<td valign="top">Ortholog Groups of Protein Sequences</td>

<td valign="top">/db_xref="OrthoMCL:OG5_130679"</td>

</tr>

<tr>

<td valign="top">[Osa1](http://rice.plantbiology.msu.edu/)</td>

<td valign="top">Rice Genome Annotation Project</td>

<td valign="top">/db_xref="Osa1:LOC_Os01g12345"</td>

</tr>

<tr>

<td valign="top">[Pathema](http://pathema.jcvi.org/)</td>

<td valign="top">Pathema Genome Resource</td>

<td valign="top">

/db_xref="Pathema:BA_4405"

/db_xref="Pathema:191218"

</td>

</tr>

<tr>

<td valign="top">[PBmice](http://www.idmshanghai.cn/PBmice/)</td>

<td valign="top">PiggyBac Mutagenesis Information Center</td>

<td valign="top">

/db_xref="PBmice:38"

</td>

</tr>

<tr>

<td valign="top" width="199">

[PDB](http://www.rcsb.org/pdb/)

</td>

<td valign="top" width="240">

Biological macromolecule three dimensional structure database

</td>

<td valign="top" width="367">

/dbxref="PDB:12GS"

</td>

</tr>

<tr>

<td valign="top">[PFAM](http://pfam.sanger.ac.uk/)</td>

<td valign="top">Collection of protein families</td>

<td valign="top">/db_xref="PFAM:PF00003</td>

</tr>

<tr>

<td valign="top" width="199">

PGN

</td>

<td valign="top" width="240">

Plant Genome Network

</td>

<td valign="top" width="367">

/db_xref="PGN:aam01-1ms3-a05"

</td>

</tr>

<tr>

<td valign="top" width="199">

[JGI Phytozome](http://phytozome.jgi.doe.gov/pz/portal.html)

</td>

<td valign="top" width="240">

Plant Genome Network

</td>

<td valign="top" width="367">

/db_xref="Phytozome:Glyma0021s00410"

/db_xref="Phytozome:ppb016588m_2_1.p"

</td>

</tr>

<tr>

<td valign="top" width="199">

[PIR](http://pir.georgetown.edu/)

</td>

<td valign="top" width="240">

Protein Information Resource accession numbers

</td>

<td valign="top" width="367">

/db_xref="PIR:S12345"

</td>

</tr>

<tr>

<td valign="top" width="199">

[PomBase](http://www.pombase.org/)

</td>

<td valign="top" width="240">

Database of Structural and Functional Data for Schizosaccaromyces pombe

</td>

<td valign="top" width="367">

/db_xref="PomBase:SPBC11B10.09"

</td>

</tr>

<tr>

<td valign="top" width="199">

PSEUDO

</td>

<td valign="top" width="240">

EMBL pseudo protein identifier

</td>

<td valign="top" width="367">

/db_xref="PSEUDO:CAC44644.1"

</td>

</tr>

<tr>

<td valign="top" width="199">

[PseudoCap](http://www.pseudomonas.com/)

</td>

<td valign="top" width="240">

Pseudomonas Genome Database

</td>

<td valign="top" width="367">

/db_xref="PseudoCap:PA0001"

</td>

</tr>

<tr>

<td valign="top" width="199">

[RAP-DB](http://rapdb.dna.affrc.go.jp/)

</td>

<td valign="top" width="240">

Rice Annotation Project Database

</td>

<td valign="top" width="367">

/db_xref="RAP-DB:Os01g1234567"

</td>

</tr>

<tr>

<td valign="top" width="199">

RATMAP

</td>

<td valign="top" width="240">

Rat Genome Database

</td>

<td valign="top" width="367">

/db_xref="RATMAP:5"

</td>

</tr>

<tr>

<td valign="top" width="199">

[RBGE_garden](http://elmer.rbge.org.uk/bgbase/livcol/bgbaselivcol.php)

</td>

<td valign="top" width="240">

Royal Botanic Garden Edinburgh Living Collections

</td>

<td valign="top" width="367">

/db_xref="RBGE_garden:20021433"

</td>

</tr>

<tr>

<td valign="top" width="199">

[RBGE_herbarium](http://elmer.rbge.org.uk/bgbase/vherb/bgbasevherb.php)

</td>

<td valign="top" width="240">

Royal Botanic Garden Edinburgh Herbarium

</td>

<td valign="top" width="367">

/db_xref="RBGE_herbarium:E00217291"

</td>

</tr>

<tr>

<td valign="top">[RFAM](http://www.sanger.ac.uk/Software/Rfam/)</td>

<td valign="top">RNA families database of alignments and CMs</td>

<td valign="top">/db_xref="RFAM:RF00230"</td>

</tr>

<tr>

<td valign="top" width="199">

[RGD](http://rgd.mcw.edu/rgdweb/search/search.html)

</td>

<td valign="top" width="240">

Rat Genome Database

</td>

<td valign="top" width="367">

/db_xref="RGD:620528"

</td>

</tr>

<tr>

<td valign="top" width="199">

[RiceGenes](http://www.gramene.org/)

</td>

<td valign="top" width="240">

Rice database accession numbers

</td>

<td valign="top" width="367">

/db_xref="RiceGenes:AA231856"

</td>

</tr>

<tr>

<td valign="top" width="199">

[RZPD](http://www.gate2biotech.com/rzpd-german-science-centre-for-genome/)

</td>

<td valign="top" width="240">

Resource Centre Primary Database Clone Identifiers

</td>

<td valign="top" width="367">

/db_xref="RZPD:IMAGp998I142450Q6"

</td>

</tr>

<tr>

<td valign="top">[SEED](http://www.theseed.org)</td>

<td valign="top">The SEED Database</td>

<td valign="top">/db_xref="SEED:fig|83331.1.peg.1"</td>

</tr>

<tr>

<td valign="top" width="199">

[SGD](http://www.yeastgenome.org/)

</td>

<td valign="top" width="240">

Saccharomyces Genome Database

</td>

<td valign="top" width="367">

/db_xref="SGD:L0000470"

</td>

</tr>

<tr>

<td valign="top" width="199">

[SGN](http://www.sgn.cornell.edu)

</td>

<td valign="top" width="240">

SOL Genomics Network

</td>

<td valign="top" width="367">

/db_xref="SGN:E553090"

</td>

</tr>

<tr>

<td valign="top">[SK-FST](http://aafc-aac.usask.ca/fst/)</td>

<td valign="top">Saskatoon Arabidopsis T-DNA mutant population - SK Collection</td>

<td valign="top">/db_xref="SK-FST: FST:SK32219"</td>

</tr>

<tr>

<td valign="top" width="199">

[SoyBase](http://soybase.agron.iastate.edu/)

</td>

<td valign="top" width="240">

Glycine max Genome Database

</td>

<td valign="top" width="367">

/db_xref="SoyBase:Satt005"

</td>

</tr>

<tr>

<td valign="top" width="199">

[SRPDB]( http://bio.lundberg.gu.se/dbs/SRPDB/SRPDB.html)

</td>

<td valign="top" width="240">

Signal Recognition Particle Database

</td>

<td valign="top" width="367">

/db_xref="SRPDB:Arth.aure._CP000474"

</td>

</tr>

<tr>

<td valign="top" width="199">

[SubtiList](http://genolist.pasteur.fr/SubtiList/)

</td>

<td valign="top" width="240">

Bacillus subtilis genome sequencing project

</td>

<td valign="top" width="367">

/db_xref="SubtiList:BG10001"

</td>

</tr>

<tr>

<td valign="top" width="199">

[TAIR](http://www.arabidopsis.org/servlets/Search?type=gene&action=new_search)

</td>

<td valign="top" width="240">

Arabidopsis IR

</td>

<td valign="top" width="367">

/db_xref="TAIR:AT1F51370"

</td>

</tr>

<tr>

<td valign="top" width="199">

[taxon](http://www.ncbi.nlm.nih.gov/Taxonomy/taxonomyhome.html/)

</td>

<td valign="top" width="240">

NCBI's taxonomic identifier

</td>

<td valign="top" width="367">

/db_xref="taxon:4932"

</td>

</tr>

<tr>

<td valign="top" width="199">

[TIGRFAM](http://www.tigr.org/TIGRFAMs/index.shtml)

</td>

<td valign="top" width="240">

TIGR protein families

</td>

<td valign="top" width="367">

/db_xref="TIGRFAM:TIGR00094"

</td>

</tr>

<tr>

<td valign="top" width="199">

[TubercuList](http://tuberculist.epfl.ch/)

</td>

<td valign="top" width="240">

TubercuList knowledge base

</td>

<td valign="top" width="367">

/db_xref="TubercuList:Rv3322c"

</td>

</tr>

<tr>

<td valign="top" width="199">

UNILIB

</td>

<td valign="top" width="240">

Unified Library Database, a library-level view of the EST and SAGE libraries present in dbEST, UniGene and SAGEmap

</td>

<td valign="top" width="367">

/db_xref="UNILIB:1002"

</td>

</tr>

<tr>

<td valign="top" width="199">

[UniProtKB/Swiss-Prot](http://www.uniprot.org)

</td>

<td valign="top" width="240">

section of the UniProt Knowledgebase, containing annotated records, which include curator-evaluated computational analysis, as well as, information extracted from the literature

</td>

<td valign="top" width="367">

/db_xref="UniProtKB/Swiss-Prot:P12345"

</td>

</tr>

<tr>

<td valign="top" width="199">

[UniProtKB/TrEMBL](http://www.uniprot.org)

</td>

<td valign="top" width="240">

section of the UniProt Knowledgebase, containing computationally analysed records waiting for full manual annotation

</td>

<td valign="top" width="367">

/db_xref=" UniProtKB/TrEMBL:Q00177"

</td>

</tr>

<tr>

<td valign="top" width="199">

UniSTS

</td>

<td valign="top" width="240">

Database of Sequence Tagged Sites

</td>

<td valign="top" width="367">

/db_xref=" UniSTS:486599"

</td>

</tr>

<tr>

<td valign="top" width="199">

[UNITE](http://unite.ut.ee/index.php)

</td>

<td valign="top" width="240">

Molecular database for the identification of fungi

</td>

<td valign="top" width="367">

/db_xref=" UNITE:UDB000157"

</td>

</tr>

<tr>

<td valign="top" width="199">

[VBASE2](http://www.vbase2.org/)

</td>

<td valign="top" width="240">

Integrative database of germ-line V genes from the immunoglobulin loci of human and mouse

</td>

<td valign="top" width="367">

/db_xref="VBASE2:humIGKV165"

</td>

</tr>

<tr>

<td valign="top" width="199">

[ViPR](http://www.viprbrc.org/brc/home.do?decorator=vipr)

</td>

<td valign="top" width="240">

Virus Pathogen Resource

</td>

<td valign="top" width="367">

/db_xref="ViPR:HRV-A34_p1058_sR263_2008"

</td>

</tr>

<tr>

<td valign="top" width="199">

[VISTA](http://enhancer.lbl.gov/)

</td>

<td valign="top" width="240">

Vista Enhancer Browser

</td>

<td valign="top" width="367">

db_xref="VISTA:hs123"

</td>

</tr>

<tr>

<td valign="top" width="199">

[VectorBase](http://www.vectorbase.org/index.php)

</td>

<td valign="top" width="240">

Bioinformatics Resource Center for Invertebrate Vectors of Human Pathogens

</td>

<td valign="top" width="367">

db_xref="VectorBase:ENSANGG00000007825"

</td>

</tr>

<tr>

<td valign="top" width="199">

[WorfDB](http://worfdb.dfci.harvard.edu/)

</td>

<td valign="top" width="240">

C. elegans ORFeome cloning project

</td>

<td valign="top" width="367">

/db_xref="WorfDB:pos-1"

</td>

</tr>

<tr>

<td valign="top" width="199">

[WormBase](http://www.wormbase.org/)

</td>

<td valign="top" width="240">

Caenorhabditis elegans Genome Database

</td>

<td valign="top" width="367">

/db_xref="WormBase:R13H7"

</td>

</tr>

<tr>

<td valign="top" width="199">

[Xenbase](http://www.xenbase.org/common/)

</td>

<td valign="top" width="240">

Xenopus laevis and tropicalis biology and genomics resource

</td>

<td valign="top" width="367">

/db_xref=Xenbase:XB-GENE-1019547

</td>

</tr>

<tr>

<td valign="top" width="199">

[ZFIN](http://zfin.org)

</td>

<td valign="top" width="240">

Zebrafish Information Network

</td>

<td valign="top" width="367">

/db_xref="ZFIN:ZDB-GENE-011205-17"

</td>

</tr>

</tbody>

</table>





<div id="shared-content-1" nid="1163">

## INSDC Members

### [DDBJ](http://www.ddbj.nig.ac.jp/)

*   [Submission](http://www.ddbj.nig.ac.jp/submission_general-e.html)*   [Sequence Retrieval](http://getentry.ddbj.nig.ac.jp/)

### [ENA](http://www.ebi.ac.uk/)

*   [Submission](http://www.ebi.ac.uk/embl/Submission/index.html)*   [Sequence Retrieval](http://www.ebi.ac.uk/embl/index.html)

### [GenBank](/~/)

*   [Submission](/~/submit)*   [Sequence Retrival](http://www.ncbi.nlm.nih.gov/sites/entrez?db=nucleotide)