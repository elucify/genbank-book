
# HTGS: Processing

## Getting Started

NCBI has implemented the HTG procedure with the following assumptions. These assumptions are the result of a variety of communications with submitters, as well as our own experience in processing records.

**<u>Assumptions:</u>**

1\. Centers have communicated with NCBI about the HTG process before submitting data.  
If this is not the case, please contact us and describe the amount of genomic sequence (base pairs/month) you plan on submitting to us. If the HTG submission route is not warranted, we will suggest an [alternative submission path](/~/). You must [contact NCBI](mailto:info@ncbi.nlm.nih.gov) to establish an FTP account, which is required for HTG submissions.

2\. Data submitted through the HTGS route will be released as soon as processing is completed.  
HTG sequences are not held until publication (HUP). If you require a HUP status on your sequence, please [contact](mailto:info@ncbi.nlm.nih.gov) the database staff about submitting through an alternate route.

3\. All new submissions will include:

*   genome center name
*   sequence name

NCBI will issue the accession number.

4\. All updates to that record will include:

*   the same genome center name
*   the same sequence name
*   the same accession number that we assigned to this clone

Any deviation from this will cause a "fatal" error, which will prevent further processing and release of this submission.  

## How Are HTG Submissions Processed?

NCBI staff have established a standard operating procedure for processing HTG submissions. Some of this information is of general use to submitting centers and is outlined here. HTG sequences submitted to the FTP site are processed on a daily basis. Files are transferred from the FTP site SEQSUBMIT directory at 4 a.m. Eastern Standard Time (EST) and examined and processed the same day. Successful submissions are immediately released to the database. Any identified errors are communicated to the submitting center by email. At 6 p.m. EST each day, a .ac4htgs and a .GBFF file are put into the FTP site REPORT directory for each submitting center, listing the sequences that were fully processed and deposited into GenBank. These sequences are then available from the Entrez system and BLASTable databases within, on average, 48 hours, but they can be retrieved by the accession number immediately.

## How Are Errors Handled?

All files placed on the FTP site are checked for a variety of possible errors. Some errors result in the submission not being released. For example, if an update does not include the accession number, then the update cannot be processed. All errors preventing release are reported to the FTP site with the file name appended by ".ERR". This file is generated when an email, describing the error, is sent to the submitting center. Less serious errors, which do not prevent release, are reported by email to the submitting center, which can then correct this error in the next update.  

## The HTG Processing Procedure

![htgsop](/core/assets/genbank/images/htgsop.gif)





<div id="shared-content-1" nid="1331">

<div class="rightnav">

## HTGs Resources

*   [About HTGs](/~/htgs)
*   [Submitting HTGs](/~/htgs/subinfo)
*   [Processing HTGs](/~/htgs/processing)
*   [](/~/htgs/processing)[HTGs FAQ](/~/htgs/faq)



