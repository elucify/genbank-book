<meta http-equiv="Content-Type" content="text/html; charset=utf-8">  <meta name="node-id" content="4563"> <meta name="revision-id" content="31786"> <meta name="cms-base-url" content="http://cms.ncbi.nlm.nih.gov"> <meta name="cms-view-url" content="http://cms.ncbi.nlm.nih.gov/genbank/validation"> <meta name="cms-edit-url" content="http://cms.ncbi.nlm.nih.gov/node/4563/edit"> <meta name="created" content="2015-04-23T10:20:37-04:00"> <meta name="modified" content="2016-01-12T07:55:13-05:00"> <meta name="publication-date" content="2015-04-23T10:12:00-04:00"> <meta name="author" content="yankie"> <meta name="subsite" content="genbank"> <meta name="path" content="genbank/validation"> <meta name="node-type" content="page"> <meta name="jira-ticket" content=""> <meta name="cms-tags" content="">  <meta name="" content=""> <link type="text/css" rel="stylesheet" href="/core/assets/genbank/css/genbank.css"> <title>validation</title>

<div class="node clear-block">

<div class="content">

# Validation and Discrepancy Report Error Explanations

Explanations for individual errors found during processing are listed below. Suggestions for fixing the errors are included to fix the most common issues. For genomes-related questions, write to: [genomes@ncbi.nlm.nih.gov](mailto:genomes@ncbi.nlm.nih.gov). For GenBank-related questions, write to: [gb-admin@ncbi.nlm.nih.gov](mailto:gb-admin@ncbi.nlm.nih.gov)

### Error List

*   [SEQ_FEAT_BadCharInAuthorLastName](#BadCharInAuthorLastName)
*   [SEQ_FEAT_BadCharInAuthorName](#BadCharInAuthorName)
*   [SEQ_DESCR_BadCollectionDate](#BadCollectionDate)
*   [SEQ_DESCR_BadCountryCode](#BadCountryCode)
*   [SEQ_DESCR_BadPCRPrimerName](#BadPCRPrimerName)
*   [SEQ_DESCR_BadPCRPrimerSequence](#BadPCRPrimerSequence)
*   [SEQ_DESCR_BadVoucherID](#BadVoucherID)
*   [SEQ_DESCR_BioSourceMissing](#BioSourceMissing)
*   [SEQ_DESCR_DuplicatePCRPrimerSequence](#DuplicatePCRPrimerSequence)
*   [SEQ_DESCR_LatLonCountry](#LatLonCountry)
*   [SEQ_DESCR_LatLonFormat](#LatLonFormat)
*   [SEQ_DESCR_LatLonProblem](#LatLonProblem)
*   [SEQ_DESCR_LatLonRange](#LatLonRange)
*   [SEQ_DESCR_LatLonValue](#LatLonValue)
*   [GENERIC_MissingPubInfo](#MissingPubInfo)
*   [SEQ_DESCR_UnstructuredVoucher](#UnstructuredVoucher)
*   [SEQ_DESCR_WrongOrganismFor16SrRNA](#WrongOrganismFor16SrRNA)
*   [SEQ_DESCR_WrongVoucherType](#WrongVoucherType)
*   [DISC_DUP_DEFLINE](#DUPDEFLINE)
*   [DISC_FEATURE_MOLTYPE_MISMATCH](#FEATUREMOLTYPEMISMATCH)
*   [DISC_MISSING_AFFIL](#MISSINGAFFIL)
*   [DISC_REQUIRED_CLONE](#REQUIREDCLONE)

### SEQ_FEAT_BadCharInAuthorLastName

_Explanation_: An author name has illegal characters.

_Suggestion_: Check the last names (family names) in the sequence and publication references. Use only plain ASCII text for the names. The last name should NOT contain symbols, numbers, accents, umlauts, characters with diacritical marks, and should NOT end in punctuation. Note that names with internal punctuation such as “St. John” or “D'Abaco” will validate.

examples:

incorrect: Henry Jones., Carlos Méndez, Xu 1Weng

corrected: Henry Jones, Carlos Mendez, Xu Weng

The use of a terminal period and number in these family names causes an error. The error can be corrected by removing the symbols, characters with diacritical marks, numbers, or punctuation.

### SEQ_FEAT_BadCharInAuthorName

_Explanation_: An author name has illegal characters.

_Suggestion_: Check the first names (given names) in the sequence and publication references. Use only plain ASCII text for the names. The names should NOT contain symbols, numbers, accents, umlauts, characters with diacritical marks, and should NOT end in punctuation. Note that names with internal punctuation such as “St. John” or “D'Abaco” or "Doe-Smith" are okay.

examples:

incorrect: J#ane Doe, José Perez, 1Xu Weng

corrected: Jane Doe, Jose Perez, Xu Wang

The use of symbols and numbers causes an error. The error can be corrected by removing the symbols, characters with diacritical marks, numbers, or punctuation.

### SEQ_DESCR_BadCollectionDate

_Explanation_: The collection date is not in the required format.

_Suggestion_: Correct the collection-date source modifier so the date is in the correct format. For example, a collection-date should be formatted like this: DD-MMM-YYYY, where the month is the three letter code in English. For genomes and biosample submissions, the ISO 8601 standard may be used, see descriptions and examples [<u>here</u>](http://www.insdc.org/files/feature_table.html).

examples of correctly formatted collection-dates:

01-Jul-1999

Nov-2010

2008

### SEQ_DESCR_BadCountryCode

_Explanation_: The country code (up to the first colon) is not on the approved list of countries.

_Suggestion_: Correct the country source modifier with a country name on the approved [<u>country list</u>](/~/collab/country/) and verify the country value is correctly formatted. If you want to include more specific location information, you must place the approved country name first, followed by a colon and then the additional information. The country has a specific format and must be formatted as follows:

<approved country name>: <region or specific area>

Examples:

Iceland

Canada: Vancouver

Atlantic Ocean: Charlie Gibbs Fracture Zone

### SEQ_DESCR_BadPCRPrimerName

_Explanation_: The PCR primer name appears to be a sequence instead of an identifying label.

_Suggestion_: The fwd-primer-name and rev-primer-name values should not be primer sequences. Correct this information in the source modifiers. If you intended to provide primer sequences, use the fwd-primer-sequence and rev-primer-sequence source modifiers.

### SEQ_DESCR_BadPCRPrimerSequence

_Explanation_: The PCR primer sequence has illegal characters or non-IUPAC nucleotides.

_Suggestion_: PCR primer sequences must only contain the nucleotide sequence. Do not include any extra information such as primer names, 5’-, or 3’. Remove the extra information so the fwd-primer-sequence and rev-primer-sequence modifiers contain nucleotides given in the IUPAC degenerate-base alphabet. If the there is an inosine in the primer sequence, format with brackets, like this “atg<i>gggaccc”

For example:

incorrect: 5’-atggggaccc-3’, 5'-ttkktcaiccgc-3'

corrected: atggggaccc, ttkktca<i>ccgc

### SEQ_DESCR_BadVoucherID

_Explanation_: The voucher is missing a specific identifier.

_Suggestion_: Correct the format of the culture-collection or specimen-voucher source modifiers. The culture-collection or specimen-voucher is missing the identifier.

The culture-collection must be formatted like this: "<institution-code>:[<collection-code>:]<culture id>". The institution code and culture ID are required, the collection-code is optional. The institution code must be valid. See the [<u>description</u>](http://www.insdc.org/controlled-vocabulary-culturecollection-qualifier) for the proper format and [<u>list</u>](ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/coll_dump.txt) of allowed institutes.

An example culture-collection is: CBS:1234

Culture-collection should be used for microbial sequences, while specimen-voucher should be used for plants and animals only. Do not use specimen-voucher to describe host information for a microbial sequence submission. The specimen-voucher is not required to be structured.

### SEQ_DESCR_BioSourceMissing

_Explanation_: The biological source of this sequence has not been described correctly.  A submission must have a source descriptor that covers the entire molecule. Please add the source information.

_Suggestion_: Provide an organism name for each sequence in your submission.

### SEQ_DESCR_DuplicatePCRPrimerSequence

_Explanation_: The PCR primer sequence has duplicate subsequences.

_Suggestion_: There are multiple identical primer sequences in the source modifiers. Remove the duplicate sequences so there are only unique primer sequences.                                                                         

### SEQ_DESCR_LatLonCountry

_Explanation_: lat_lon and country disagree

_Suggestion_: The latitude-longitude (lat-lon) value provided does not map to the source country provided, so correct or remove the lat-lon values and/or country source modifiers. Provide lat-lon in decimal degrees with the compass direction (for example: 39.7 N 42.1 W) and check that the lat-lon coordinates map to the country you have provided.

### SEQ_DESCR_LatLonFormat

_Explanation_: The format of lat-lon should be dd.dd N|S ddd.dd E|W.

_Suggestion_: Correct the latitude-longitude (lat-lon) source modifier with lat-lon coordinates in decimal degree format with the compass directions. For example: 39.7 N 42.1 W

### SEQ_DESCR_LatLonProblem

_Explanation_: There is a problem with the lat-lon modifier provided.

_Suggestion_: Correct or remove the latitude-longitude (lat-lon) values in the source modifiers. Provide lat-lon in decimal degrees and include the compass direction (for example, 39.7 N 42.1 W). Longitude values range from 0 to 180E or 0 to 180W. Latitude values range from 0 to 90 N or 0 to 90 S.

### SEQ_DESCR_LatLonRange

_Explanation_: Latitude or longitude is out of range.

_Suggestion_: Correct or remove the latitude-longitude (lat-lon) values in the source modifiers. Provide lat-lon in decimal degrees and include the compass direction (for example, 39.7 N 42.1 W). Longitude values range from 0 to 180E or 0 to 180W. Latitude values range from 0 to 90 N or 0 to 90 S. Numbers outside of these ranges will cause errors.

### SEQ_DESCR_LatLonValue

_Explanation_: Latitude or longitude values appear to be in the wrong hemisphere or swapped.

_Suggestion_: Correct or remove the latitude- longitude (lat-lon) values in the source modifiers. The lat-lon value for the record does not agree with the source country provided. Based on the source country, the lat-lon value appears to have the incorrect hemisphere or is swapped. Check the coordinates and compass direction and provide the correct values.

### GENERIC_MissingPubInfo

_Explanation_: The publication is missing essential information, such as title or authors.

_Suggestion_: Check the references. Provide author names, a title, and select the publication status (unpublished, in press, or published). If the title is published or is in press, provide additional information including publication year, journal, volume, and pages, where applicable.  

### SEQ_DESCR_UnstructuredVoucher

_Explanation_: The voucher needs to be structured as "<institution-code>:[<collection-code>:]<culture id>".

_Suggestion_: Correct the format of the culture-collection source modifier. The institution code and culture ID are required, the collection-code is optional. Follow the formatting instruction in the explanation. The culture collection must have a valid institution code followed by a colon and the culture ID. See the [<u>list</u>](ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/coll_dump.txt) of allowed institutes.

For example CBS:1234

In this example, CBS is the insitution code and 1234 is the culture ID. There must be a colon between the institution code and the culture ID.

### SEQ_DESCR_WrongOrganismFor16SrRNA

_Explanation:_ 16S ribosomal RNA is not present in eukaryotic ribosomes.

_Suggestions:_ Check the organism names for the sequences you are submitting. If you are submitting prokaryotic 16S ribosomal RNA, the organism names should have a prokaryotic name. Do not use the host as the organism name. For example if bacterial 16S rRNA was sequenced from human samples, use uncultured bacterium as the organism name, do NOT use Homo sapiens as the organism name.

Check the tool you are using to submit. If you are using the prokaryotic 16S rRNA sequence submission wizard for sequences that are not prokaryotic 16S rRNA, you should use a different [submission tool](/~/submit) to submit the sequences.

### SEQ_DESCR_WrongVoucherType

_Explanation_: The institution (or institution: collection) code normally uses a different bio material/culturecollection/specimen voucher type.

_Suggestion_: In the source modifiers, use the source modifier “culture-collection” instead of “specimen-voucher” or vice versa.  For example, if you provided the source modifiers in a tab-delimited table, edit the table so the column header “culture-collection” is used in place of “specimen-voucher” and upload the revised table.

Note that culture-collection should be used for microbial sequences, while specimen-voucher should be used for plants and animals only. Do not use specimen-voucher to describe host information for a microbial sequence submission.

### DISC_DUP_DEFLINE

_Explanation_: Definition lines should be unique

_Suggestion_: Some of your records do not have unique information. Provide a combination of unique source information. For example, provide unique clone names. For example, two unique clone names are xyz1-123 and xyz2-567.

### DISC_FEATURE_MOLTYPE_MISMATCH

_Explanation_: Sequences with rRNA or misc_RNA features should be genomic DNA

_Suggestion_: The molecule type should represent what type of molecule was actually sequenced. In general, submissions that are sequencing rRNA genes or rRNA/ITS regions are actually sequencing genomic DNA. Correct this information where you indicated the type of molecule that was sequenced. For example if you indicated rRNA in your FASTA definition lines, remove this information or change it to genomic DNA. If you actually sequenced RNA, please write to [gb-admin@ncbi.nlm.nih.gov](mailto:gb-admin@ncbi.nlm.nih.gov) with your submission number.

### DISC_MISSING_AFFIL

_Explanation_: Missing affiliation

_Suggestion_: The name of the institution where the sequencing/analysis work was performed is missing from your submission. Provide this information where you provided your contact information.

### DISC_REQUIRED_CLONE

_Explanation_: Uncultured or environmental sources should have clone

_Suggestion_: Provide unique (non-identical) clone names for your sequences. A clone name is typically an alpha-numeric identifier used to track the sample in your laboratory. The clone name is not the organism name and it is not the name of the gene you are working on. An example of two unique clone names are xyz1-123 and xyz2-567.

</div>

</div>

<div id="shared-content-1" nid="1092">

<div class="rightnav">

## GenBank Resources

*   [GenBank Home](/~/)
*   [Submission Types](/~/submit_types)
*   [Submission Tools](/~/submit)
*   [Search GenBank](http://www.ncbi.nlm.nih.gov/nuccore/)
*   [Update GenBank Records](/~/update)

</div>

</div>