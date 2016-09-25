
# Published in Genome Research 7(10), 1997

## Database Divisions and Homology Search Files: A Guide for the Perplexed

B.F. Francis Ouellette and Mark S. Boguski

National Center for Biotechnology Information, National Library of Medicine, National Institutes of Health, Building 38A, Room 8N805, 8600 Rockville Pike, Bethesda, MD 20894\. Tel: (301) 496-2475, FAX: (301) 480-9241

Introduction

The exponential growth of DNA sequence data has become a challenge for both end-users and database curators alike. When one of the authors (M.S.B) was finishing graduate school, GenBank (release 42) contained a mere 6.7 megabases in 9,700 sequences. However, as we write this, GenBank (Benson et al. 1997) has topped 1,000 megabases in more than 1.6 million sequences (release 102). The National Center for Biotechnology Information (NCBI), and its partners in the international database collaboration — the DNA Database of Japan (DDBJ) and the European Molecular Biology Laboratory (EMBL) — all strive to collect, manage and distribute this data in the most useable forms and in the most efficient manner possible. These organizations also provide homology search and database query and information retrieval services that serve the general molecular biology community as well as more specialized users. Unfortunately it is easy to become confused about the many ways in which the data is made available for downloading, for homology searching, and for more general information retrieval purposes. We hope to clarify some of these issues here, with an emphasis on the manner in which high-throughput genomic sequence is processed, distributed and made available for BLAST searching. We will emphasize services provided through NCBI, but also note comparable services at EBI and the slight differences between GenBank, DDBJ and the EMBL Data Library.

Divisions of the Nucleotide Sequence Databases

The nucleotide sequence databases were originally organized around loosely defined taxonomic groupings that reflected research trends and sequencing activity of a former era. These divisions are not as biologically relevant today, but so many public and private software systems have been developed to process these divisions that the databases must be conservative when contemplating changes in the structure of data distributions. The current divisional structures of GenBank, EMBL and DDBJ are shown in [Table 1](/~/htgs/table1). The reader will note that not all of these divisions are taxonomically based and that certain "functional" divisions have been added over time. Notably, in recent years, new divisions were added for EST and STS data because these sequences differed from traditional GenBank entries in many ways, including the way in which people computed on the data (Boguski et al. 1993). The newest functional division, "HTG", is described below.

The High Throughput Genomic (HTG) Sequence Division. Although the issue is still a matter of some controversy (Adams and Venter 1996; Bentley 1996), a consortium of large scale sequencing centers and their funding agencies have reached a consensus agreement (the "Bermuda Principles") regarding data produced in publicly funded projects. This agreement states that "unfinished" sequence data be released as soon as it is "useable" for homology searching and other types of sequence analysis. Useable data is currently defined as all sequences existing in contigs of >2 kilobases. Preliminary data such as this can be generated quite rapidly as it usually represents automated assemblies of single-pass, "shotgun" sequences. However, conversion to the "finished" state (complete contiguity with an error rate of 10<sup>-4</sup> or less) may take considerably longer, hence the motivation to release unfinished but useable sequence earlier. This process of data generation and public release is entirely different from traditional GenBank data submission and the international collaborators devised and implemented a system to accommodate this new paradigm. Unfinished sequences are submitted to and stored in the "HTG" Division and each record is plainly labeled to indicate the preliminary nature of the data.

HTG records contain sequences derived from a single genomic clone and the entire set receives a single GenBank accession number that remains with the sequence as it progresses to the finished state. When declared finished by the submitting laboratory, these records move into the traditional repositories of finished data, the organismal divisions of GenBank, and are placed according to the biological source of the sequence. Thus finished human sequences are distributed in the primate (PRI) division of GenBank (or the "HUM" division for EMBL and DDBJ) whereas finished nematode and Arabidopsis sequences are found in the invertebrate (INV) and plant (PLN) divisions, respectively ([Table 2](/~/htgs/table2)). It may seem rather coarse to "lump" H. sapiens with other primates and C. elegans with other invertebrates. But this legacy of the earlier history of GenBank is irrelevant in the face of meta-information retrieval systems such as NCBI’s Entrez that, in conjunction with NCBI’s Taxonomy Database, permits one to explore and retrieve sequence records for any of the approximately 25,000 biological species in GenBank. Furthermore, new versions of the BLAST software permit homology searches based on inclusive or exclusive taxonomy parameters (Zhang and Madden 1997).

Homology Search Files at NCBI and EBI

The divisional structures of GenBank, DDBJ and EMBL Data Library were primarily designed for the purposes of efficient data distribution and file storage. For homology search purposes, there are other, more practical and desirable ways to organize the sequence data. For example, "unfinished" data such as EST and HTG sequences always need to be analyzed with error-tolerant software (such as BLASTX or TBLASTN) (Altschul et al. 1994). On the other hand, "finished" (accurate and annotated) data may have coding features that can be automatically converted to conceptual translations in a protein database where BLASTP provides a more sensitive and specific search tool. Thus it is inefficient to combine finished and unfinished data in a single file for homology search purposes. It is also undesirable to combine qualitatively different types of data in a single search file. STSs, for example, have their own Division of GenBank and homology searching is not the most appropriate method for querying this data (Schuler 1997).

Another important consideration in the construction of homology search files is the issue of sequence redundancy (Altschul et al. 1994). GenBank, DDBJ and EMBL Data Library are historical archives and may contain many, nearly identical versions of the same sequence. The "nr" (for non-redundant) data set (Altschul et al. 1994) is NCBI’s attempt to provide a more streamlined, yet comprehensive collection of sequences for homology search purposes. NR includes finished (but not unfinished) HTG records ([Table 2](/~/htgs/table2)). Another important example is the "month" data set that provides a rolling month view of new GenBank entries. "Month" is provided so that one does not have to repeatedly search previously examined portions of nr to identify matches to new sequences that have appeared since the last search was performed. "Month" includes newly finished HTG records. Unfinished (phase 1 and phase 2) HTG data is accessible for BLAST searching at NCBI by specifying the "htgs" database (Table 2).

As previously described, there are slight variations in the divisional structures of the three collaborating databases ([Table 1](/~/htgs/table1)). There are also differences in the ways in which the sequence data is made available for homology searching. One important example of this is the EMBL "ALL" database (emall) that combines both finished and unfinished HTG sequences for FASTA searching ([Table 2](/~/htgs/table2)).

DDBJ, EMBL and GenBank must be conservative in contemplating changes to the divisional structures of the databases. However, these organizations can be and have been more flexible in producing specialized collections for homology searching. Thus, the user community should view the databases listed in [Table 2](/~/htgs/table2) as subject to changes and improvements, driven by the ever-increasing quantity and variety of new sequence data.

Other Ways to Access the Data

Entrez is a meta-information system that has been described in detail elsewhere (Schuler et al. 1996; Benson et al. 1997). Entrez allows the user to query an extensive information space characterized by five main divisions: DNA sequences, protein sequences, maps and genomes, macromolecular structures and the biomedical literature. Regarding DNA sequences in Entrez, all data in GenBank, regardless of Division, is available, including unfinished HTG records. This data may be queried using accession numbers, NIDs, authors names and a variety of other keywords as well as by accessing pre-computed homology search results – a concept referred to as "neighboring." In the near future, NCBI hopes to make available BLASTX neighbors through its Entrez service. This would allow users to access sequence similarities between even unfinished HTG records and the proteins they may encode.

Summary

All of the data in GenBank (and EMBL and DDBJ) is made available in a variety of ways, tailored to particular uses such as efficient data submission, distribution and sequence homology searching. Unfortunately this can be somewhat confusing for contributors, data managers and end users all of whom have somewhat different perspectives and needs. The international database collaborators have striven to meet the various requirements of a diverse community but new suggestions are always welcomed and may be directed to NCBI’s service desk at info@ncbi.nlm.nih.gov. Information resource providers will continue to experiment with new ways in which to make sequence data more accessible and useful to the community, particularly for homology search purposes.

References

Adams, M. D. and J. C. Venter (1996). "Should non-peer-reviewed raw DNA sequence data release be forced on the scientific community?" <u>Science</u> 274(5287): 534-6.

Altschul, S. F., M. S. Boguski, W. Gish and J. C. Wootton (1994). "Issues in searching molecular sequence databases." <u>Nat Genet</u> 6(2): 119-29\.

Benson, D. A., M. S. Boguski, D. J. Lipman and J. Ostell (1997). "GenBank." <u>Nucleic Acids Res</u> 25(1): 1-6.

Bentley, D. R. (1996). "Genomic sequence information should be released immediately and freely in the public domain." <u>Science</u> 274(5287): 533-4.

Boguski, M. S., T. M. Lowe and C. M. Tolstoshev (1993). "dbEST--database for "expressed sequence tags" [letter]." <u>Nat Genet</u> 4(4): 332-3.

Schuler, G. D. (1997). "Sequence mapping by electronic PCR." <u>Genome Res</u> 7(5): 541-50.

Schuler, G. D., J. A. Epstein, H. Ohkawa and J. A. Kans (1996). "Entrez: molecular biology database and retrieval system." <u>Methods Enzymol.</u> 266: 141-162.

Zhang, J. and T. L. Madden (1997). "PowerBLAST: a new network BLAST application for interactive or automated sequence analysis and annotation." <u>Genome Res</u> 7: 649-656\.





