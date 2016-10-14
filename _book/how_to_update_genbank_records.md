
# How To Update Information On GenBank Records

The following information provides the different methods to submit updates to GenBank in order to ensure that your update is processed quickly and correctly. Updates provided in an incorrect format will delay processing. All update files should be saved as plain text. If you are updating many records, please send a list of all accessions to be updated at the top of your request.

Do not submit a new Sequin file to update an existing record.

Update files in the formats below should be emailed directly to [gb-admin@ncbi.nlm.nih.gov](mailto:gb-admin@ncbi.nlm.nih.gov) or uploaded using [UpdateMacroSend](/projects/GenBankUpdate/genbank_update.cgi).

### Update Formats:

*   [Source Information](#source)
*   [Publication Information](#pub)
*   [Nucleotide Sequence](#sequence)
*   [Adding Features](#new_feats)
*   [Updating Features](#upd_feats)

### Editing Source Information

Send updates to the [source information](//www.ncbi.nlm.nih.gov/Sequin/modifiers.html) (i.e. strain, cultivar, country, specimen_voucher) in a multi-column tab-delimited table, for example:

<pre>acc. num.       strain  country	organism
AYxxxx02        82      USA	Escherichia coli
AYxxxx03        ABC     Canada	Bacillus subtilis

</pre>

### Updating Publication Information

Replace any non-ASCII characters (for example, characters with accents and umlauts) with the appropriate English letters. Send updates to the publication information in a multicolumn, tab-delimited table; for example:

<pre>acc. num.	authors	title
FJxxxx01	John A. Smith	Identification of gene A	
FJxxxx02	Xu P. Weng, Jane Doe	Identification of gene B
</pre>

The complete list of revised author names should be provided in the following format:

given_name middle_initial surname, etc.

These are the valid publication fields which should be used in the column headers:

*   authors
*   journal
*   volume
*   issue
*   pages
*   publication date
*   title
*   affiliation
*   department
*   city
*   state
*   publication country
*   street
*   postal code
*   PMID
*   class

All columns may not be appropriate for each reference. Use only the relevant columns. If the reference has been published, include the complete journal title, not an abbreviation.

* If the publication has a PubMed identifier (PMID), it is not necessary to supply any of the remaining publication fields. It is sufficient to send a table with only an accession number and PMID.

* The class descriptor should only be used when the publication status has been changed. This descriptor has a controlled vocabulary and may only include one of the following three class values:

  * unpublished
  * in-press journal
  * journal

### Nucleotide Sequence Update

If you are updating the current nucleotide sequence send the complete new sequence(s) in fasta format:

<pre>>AYxxxx02
cggtaataatggaccttggaccccggcaaagcggagagac
>AYxxxx03
ggaccttggaccccggcaaagcggagagaccggtaataat 
</pre>

Please do not send a list of nucleotide changes. Do not include non-IUPAC characters within the sequence. Use n's for unknown nucleotides within the sequence.

### Update features on record without annotation

If you are adding annotation to a record that has none, then send us the features as a tab-delimited 5-column [Feature table.](http://www.ncbi.nlm.nih.gov/Sequin/table.html) For example:

<pre>>Feature gb|EFxxxxxx|EFxxxxxx
<1      400     gene
                        gene            ENO1
<1      30      CDS
70      300
                        product         enolase
                        note            homodimer
<1      30      mRNA
70      400
                        product         enolase
<1      30      exon
                        number          1
70      400     exon
                        number          2

</pre>

### Update features on record with annotation

If you are updating many features of a record, let us know, and we can send you a tab-delimited 5-column [Feature table](http://www.ncbi.nlm.nih.gov/Sequin/table.html) with the current annotation for you to edit and return to us.

