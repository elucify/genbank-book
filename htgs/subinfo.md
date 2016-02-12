
## Submitting HTG Sequences

The submission [process](/~/htgs/processing) for HTGs is quite different from that for other direct [submissions](/~/). The goal of the process is to make new and updated sequences available to the public in a timely fashion. Thus, NCBI will perform only very basic validation checks of HTGs, and submitters must check their records carefully before submission. Furthermore, because sequences will be released to the public as soon as processing is finished, it is presently not the standard procedure to indicate a "hold until published" (HUP) date on which they should be released. If a HUP date is necessary, the submitter should please [contact](mailto:htgs-admin@ncbi.nlm.nih.gov) the database staff about submitting through an alternate route.

Sequencing centers that will be submitting HTGs to NCBI should email [htgs-admin@ncbi.nlm.nih.gov](mailto:htgs-admin@ncbi.nlm.nih.gov) to establish an [FTP account](/~/htgs/ftp). Prepared records should be transferred to this site, where they will be retrieved daily by the NCBI staff. These records should not be emailed to the NCBI. Submitted HTG sequences must be written in ASN.1 format.

## Submission Tools

There are currently two ways to create HTG records:

1.  [The Sequin program](/~/htgs/sequininfo)  
    Sequin contains a setting that allows genome centers to prepare HTG submissions. Sequin reads in a FASTA sequence file (or an Ace Contig file with Phrap sequence quality values) and a Sequin submission template file (to get contact and citation information). Users then enter additional information into a Sequin form, the same information that they would enter at the command line in fa2htgs (see below). Sequin generates the ASN.1 file for submission.
2.  [The tbl2asn tool](/~/htgs/tbl2asninfo)  
    tbl2asn is a command-line program that has replaced the deprecated program fa2htgs. tbl2asn reads in a FASTA sequence file (or an Ace Contig file with Phrap sequence quality values), a Sequin submission template file (to get contact and citation information), and a series of command-line arguments (to get additional information). tbl2asn then generates the ASN.1 file for submission. tbl2asn can be incorporated into scripts to facilitate expedient processing of records.





<div id="shared-content-1" nid="1331">

<div class="rightnav">
