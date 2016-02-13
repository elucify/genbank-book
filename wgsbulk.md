# WGS Bulk Submission by FTP

1\. Register BioProject and BioSample with the supplied spreadsheet for bacterial pathogen. Send the spreadsheet to genomeprj@ncbi.nlm.nih.gov

2\. Create files for wgs submission  
 a. Template, [http://www.ncbi.nlm.nih.gov/WebSub/template.cgi](http://www.ncbi.nlm.nih.gov/WebSub/template.cgi) = template.sbtx  
 b. Fasta file of all contigs >200bp, with no Ns at ends or internal Ns that represent gaps =file1.fsa  
        Put source info into the fasta header of each contig:  
  >contig0001 [organism=Genus species] [strain=strain] [bioproject=PRJNAxxxxx] [biosample=SAMNxxxxxxx] [host=Genus species] [isolation-source=text] [country=country: more details] [collection-date=dd-Mmm-yyyy or Mmm-yyyy]

  c. Genome-Assembly-Data structured comment = file1.cmt  
    [https://submit.ncbi.nlm.nih.gov/structcomment/genomes/](https://submit.ncbi.nlm.nih.gov/structcomment/genomes/)  
    or create the 2-column tab-delimited table yourself:  
```
StructuredCommentPrefix    GenomeAssembly-Data  
Assembly Method    algorithm v. version/date  
Genome Coverage    12x  
Sequencing Technology    Illumina HiSeq2000  
StructuredCommentSuffix    GenomeAssembly-Data
```

NOTE: the value of Assembly Method must include ‘v. ‘ between the name of the algorithm and the version used, or date that it was used.

Assembly Name (a brief abbreviation to name this version) is optional tag:  
StructuredCommentPrefix    GenomeAssembly-Data  
Assembly Method    Newbler v. 2.3  
Assembly Name    EcoliABCD_v1.0  
Genome Coverage    12x  
Sequencing Technology    Illumina HiSeq2000  
StructuredCommentSuffix    GenomeAssembly-Data  

Use semi-colon to separate multiple values, like this:  
StructuredCommentPrefix    GenomeAssembly-Data  
Assembly Method    Newbler v. 2.3; Celera Assembly v. May 2010  
Genome Coverage    12x Illumina; 6x 454  
Sequencing Technology    Illumina HiSeq2000; 454  
StructuredCommentSuffix    GenomeAssembly-Data  

d. Optional 5-column feature table (.tbl) file. Format and requirements are [http://www.ncbi.nlm.nih.gov/genbank/genomesubmit#prepare_table](http://www.ncbi.nlm.nih.gov/genbank/genomesubmit#prepare_table) and [http://www.ncbi.nlm.nih.gov/genbank/genomesubmit_annotation](http://www.ncbi.nlm.nih.gov/genbank/genomesubmit_annotation). Use the locus_tag prefix registered in step 1.  

4\. Run tbl2asn, [http://www.ncbi.nlm.nih.gov/genbank/tbl2asn2](http://www.ncbi.nlm.nih.gov/genbank/tbl2asn2/ )/ (available by FTP, [ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/converters/by_program/tbl2asn](ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/converters/by_program/tbl2asn/)/):  

If all the genomes use the same template, then you can put all the .fsa and .cmt and optional .tbl files into a single directory and run:  

    tbl2asn -t template.sbt -p path_to_files -M n -j "[gcode=11]" -X C -c bx  

Any ERROR, REJECT and FATAL problems in the the *.val and *.dr files need to be fixed  

5\. Deposit .sqn files on ftp account, and send an email to genomes@ncbi.nlm.nih.gov with a table with this info:  

BioProjectID (PRJNAxxxxx)    Organism name  Strain Name    File name    Release date (Immediate OR Mmm-Dd-Yyyy)  

---------------------  

There are some options, which can be chosen according to which works best for the submitter's system:  

1\. The source information can be included in the fasta deflines, as described, OR in the -j argument of the tbl2asn commandline  

2\. The biosampleID and bioprojectID can be included in the template, OR with the source information in either the fasta defline, as described, or with the source information with the -j argument of the tbl2asn commandline  

3.The structured comment file can have the same basename as the .fsa file and be put into the same directory and then called with -X C, as described.  OR it can have any name and be in any directory and then called specifically by name with -w, eg -w ../structuredcmt_file.  NOTE: if both options are used, then the file called with -w will be used to create the .sqn file.

4\. tbl2asn can be run individually on a .fsa file by using -i file1.fsa (instead of -p path_to_files, which will read all the .fsa files in that directory)  




