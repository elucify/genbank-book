<meta http-equiv="Content-Type" content="text/html; charset=utf-8">  <meta name="node-id" content="2686"> <meta name="revision-id" content="31932"> <meta name="cms-base-url" content="http://cms.ncbi.nlm.nih.gov"> <meta name="cms-view-url" content="http://cms.ncbi.nlm.nih.gov/genbank/tsaguide"> <meta name="cms-edit-url" content="http://cms.ncbi.nlm.nih.gov/node/2686/edit"> <meta name="created" content="2013-02-14T11:20:30-05:00"> <meta name="modified" content="2016-01-19T14:10:05-05:00"> <meta name="publication-date" content="2013-02-14T11:17:00-05:00"> <meta name="author" content="schafer"> <meta name="subsite" content="genbank"> <meta name="path" content="genbank/tsaguide"> <meta name="node-type" content="page"> <meta name="jira-ticket" content=""> <meta name="cms-tags" content="">  <meta name="" content=""> <title>TSA submission guide</title>

<div class="node clear-block">

<div class="content">

# TSA Submission Guide

### Requirements:

*   Register your project in the [BioProject](https://submit.ncbi.nlm.nih.gov/subs/bioproject/) database as a Transcriptome Shotgun Assembly project.
*   Register your library information in the [BioSample](https://submit.ncbi.nlm.nih.gov/subs/biosample) database.
*   Raw reads should be submitted to [SRA](https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi) and the SRA run accession(s) (SRR) provided.  Do not provide SRX accession numbers.
*   EST sequences should be submitted to [dbEST](//www.ncbi.nlm.nih.gov/dbEST/index.html) and the accession range provided in the COMMENT section of the submission.
*   Assembly Data structured comment. This information can be input through the Submission Portal dialogs or can be created using the [Structured Comment Template](https://submit.ncbi.nlm.nih.gov/structcomment/nongenomes/).
*   Description of the assembly process if a multi-step assembly was performed should be provided in the COMMENT section.
*   If annotation is provided the product names should follow the [UniProt-Protein Naming Guidelines](//www.uniprot.org/docs/nameprot).
*   Annotation must be biologically valid.
*   The keyword 'Targeted' and feature annotation should be included for all targeted subsets of transcriptome data.  See [Targeted vs. Non-targeted TSA Studies](#target) for more information.

### Creating the TSA submission file:

[1] The BioProject accession, BioSample accession(s), SRA run accession(s) and Assembly Structured Comment data are entered using the Submission Portal dialogs.  See [Requirements](#RQ) for the links to these databases.

[2] If submitting a Targeted subset of your data see the additional requirements under [Targeted vs. Non-targeted TSA](#target).

[3] All TSA submissions are submitted through the TSA [Submission Portal](#SP) .

[4] The submission file should be generated using [tbl2asn](/~/tbl2asn2).

*   [tbl2asn](/~/tbl2asn2) reads a [template.sbt](//www.ncbi.nlm.nih.gov/WebSub/template.cgi) along with the sequence and table files, and outputs ASN.1 for submission to TSA through the portal.
*   Annotation may be included using a Feature table. See [tbl2asn](/~/tbl2asn2).

fasta defline components:

*   [moltype=transcribed_RNA]
*   [tech=TSA]
*   To add Source information see [tbl2asn](/~/tbl2asn2) Source table format 

Sample command line:

tbl2asn -t template.sbt -p.  -Y comment -M t

The validator output (*.val) should be reviewed before submitting.  Any validator errors not resolved prior to submission may be stopped in the Submission Portal.  See [Submitting the file to TSA-Submission Portal](#SP) for more information.

<table border="1" cellpadding="0" cellspacing="0"><caption>tbl2asn command line arguments</caption>

<tbody>

<tr>

<td>-Y</td>

<td>To import Assembly Description Comment</td>

</tr>

<tr>

<td>-M t</td>

<td>To run standard validator and additional TSA checks</td>

</tr>

<tr>

<td>-j</td>

<td>Allows the addition of [source qualifiers](//www.ncbi.nlm.nih.gov/Sequin/modifiers.html) that will be the same for each submission.

Example: -j "[organism=Homo sapiens] [tissue-type=liver]"

</td>

</tr>

<tr>

<td>-w assembly.cmt</td>

<td>To import Structured Comment Table*</td>

</tr>

</tbody>

</table>

*This is optional, but can be helpful when there are multiple transcriptomes, because there will be less information to supply on the web form during submission.  See [Creating the Structured Comment Table](#strcomm) for more information.

### Submitting the file to TSA-Submission Portal

All files must be submitted via the [<u>Submission Portal</u> ](https://submit.ncbi.nlm.nih.gov/subs/tsa/).

When the file is uploaded it will undergo a series of validation checks. The following will stop your submission in portal:

*   Sequences less than 200 bp
*   Sequences with univec hits that are for Next-Gen sequencing primers
*   Sequences that are more than 10% n's or have more than 14n's in a row
*   Files that are incorrectly formatted or have biologically invalid annotation

Submission statuses in the Submission Portal:

*   Queued: The submission is successful and waiting for review by TSA staff.  If there are any issues the submitter will be contacted with a list of revisions and/or inquiries.
*   Error: The TSA staff has reported any error(s) to the submitter.  The corrections need to be made and a new file uploaded using the Fix button.
*   Processing: The submission has been successfully completed and an accession number for the project has been assigned.
*   Processed:  The project has been released to the database.

### Targeted vs. Non-targeted TSA Studies

It is expected that submissions to TSA would comprise a large-scale comprehensive study of the complete transcriptome of an organism.  However, some scientists do targeted studies of their transcriptome data and only want to submit this small subset.  For targeted studies the regular submission process should be followed with the following requirements:

*   The keyword 'Targeted' should be added to the submission file.  Using tbl2asn this can be done by including [keyword=Targeted] in the fasta definition line. 
*   Annotation must be included showing the focus of the targeted study. This can be done with a gene, misc_feature, or RNA feature.
*   If coding regions are provided the product names should follow the [UniProt-Protein Naming Guidelines](//www.uniprot.org/docs/nameprot). If misc_features are provided then the  /note should be in the following format “similar to product_name”.
*   Set the molecule type (moltype) to the appropriate RNA type -mRNA, rRNA, ncRNA, or transcribed RNA.

*SRA cannot release a subportion of your data to match your subset. The entire SRA dataset will be released upon release of your subset.­­­­­­­­­­

### Assembly Gaps

Sequences with known gaps can be submitted to TSA providing the gap is annotated with an assembly_gap feature.

The required qualifiers for the assembly_gap feature are:

*   estimated_length
*   linkage_evidence
    *   paired-ends: paired sequences from the two ends of a DNA fragment.
    *   align_genus: alignment to a reference genome within the same genus.
    *   align_xgenus: alignment to a reference genome within another genus.
    *   align_trnscpt: alignment to a transcript from the same species.

### Updating TSA submissions

*   If you are updating a publication send the TSA accession prefix and complete publication information in the text portion of an email to gb-admin@ncbi.nlm.nih.gov.
*   If you are updating any other information or adding an additional sequence(s) to your assembly do not create a new submission. Please contact gb-admin@ncbi.nlm.nih.gov for directions and include the following information with your request:
    *   Description of your update.
    *   TSA accession prefix or submission portal ID for your submission.TSA will send instructions on how to proceed with the requested update.

    ### Creating the Assembly Structured Comment Table

    The Assembly Structured Comment table is a single tab-delimited table that includes the tag-value pairs that are to be applied to all of the sequences in your submission. For TSA records the Assembly Method (with version and/or year if available) and Sequencing technology must be included. Coverage and Assembly name are optional.

    The table to import is created using the [Structured Comment](https://submit.ncbi.nlm.nih.gov/structcomment/nongenomes/) page.

    An example table:

    <table border="1" cellpadding="0" cellspacing="0">

    <tbody>

    <tr>

    <td>StructuredCommentPrefix</td>

    <td>Assembly</td>

    </tr>

    <tr>

    <td>Assembly Method</td>

    <td>Newbler 2.0</td>

    </tr>

    <tr>

    <td>Coverage</td>

    <td>220x</td>

    </tr>

    <tr>

    <td>Sequencing Technology</td>

    <td>454; Solexa</td>

    </tr>

    </tbody>

    </table>

</div>

</div>

<div id="shared-content-1" nid="1470">

<div class="rightnav">

## TSA Resources

*   [About TSA](/~/TSA)
*   [TSA Submission Guide](/~/TSAguide)
*   [FAQ](/~/TSAfaq)
*   [tbl2asn](/~/tbl2asn2)
*   [Sequin](//www.ncbi.nlm.nih.gov/Sequin/)
*   [Submission Portal](https://submit.ncbi.nlm.nih.gov/subs/)
*   [BioProject](https://submit.ncbi.nlm.nih.gov/subs/bioproject/)
*   [BioSample](https://submit.ncbi.nlm.nih.gov/subs/biosample/)
*   [WGS/TSA Browser](http://www.ncbi.nlm.nih.gov/Traces/wgs/?term=tsa)
*   [SRA](https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi)

</div>

</div>