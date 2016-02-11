
# Validation Error Explanations for Genomes

This page has explanations for individual errors that are commonly found during processing of prokaryotic and eukaryotic genomes, along with suggestions to fix them. Write to [genomes@ncbi.nlm.nih.gov](mailto:genomes@ncbi.nlm.nih.gov) if you do not know how to correct the error in your submission.

Explanations of disrepancy report problems that are reported in the "discrep" file can be found at [http://www.ncbi.nlm.nih.gov/genbank/asndisc#fatal](/~/asndisc#fatal) and [http://www.ncbi.nlm.nih.gov/genbank/asndisc.examples](/~/asndisc.examples)

Remember that annotation is not required for genome submissions, and that you can request NCBI's [Prokaryotic Genome Annotation Pipeline](http://www.ncbi.nlm.nih.gov/genome/annotation_prok/) for your prokaryotic genome submissions. For more information about annotation, see the [Prokaryotic Genome Annotation Guidelines](/~/genomesubmit_annotation) or [Eukaryotic Genome Annotation Guidelines.](/~/eukaryotic_genome_submission_annotation)

### Error List

*   [SEQ_FEAT_BadCharInAuthorLastName](#BadCharInAuthorLastName)
*   [SEQ_FEAT_BadCharInAuthorName](#BadCharInAuthorName)
*   [SEQ_DESCR_BadCollectionCode](#BadCollectionCode)
*   [SEQ_DESCR_BadCollectionDate](#BadCollectionDate)
*   [SEQ_DESCR.BadCountryCode](#BadCountryCode)
*   [SEQ_INST.BadProteinStart](#StartCodonandBadProteinStart)
*   [SEQ_DESCR.BadVoucherID](#BadVoucherID)
*   [SEQ_DESCR.BioSourceMissing](#BioSourceMissing)
*   [SEQ_FEAT.EcNumberProblem](#EcNumberProblem)
*   [SEQ_FEAT.FeatureBeginsOrEndsInGap](#FeatureBeginsOrEndsInGap)
*   [SEQ_INST.InternalNsInSeqRaw](#InternalNsInSeqRaw)
*   [SEQ_FEAT.InternalStop](#InternalStopandStopInProtein)
*   [SEQ_FEAT.InvalidQualifierValue: rRNA has no name](#InvalidQualifierValuerRNAhasnoname)
*   [SEQ_DESCR.LatLonCountry](#LatLonCountry)
*   [SEQ_DESCR.LatLonFormat](#LatLonFormat)
*   [SEQ_DESCR.LatLonProblem](#LatLonProblem)
*   [SEQ_DESCR.LatLonRange](#LatLonRange)
*   [SEQ_DESCR.LatLonValue](#LatLonValue)
*   [SEQ_FEAT.MisMatchAA](#MisMatchAA)
*   [GENERIC.MissingPubInfo: No submission citation anywhere on this entire record](#MissingPubInfoNosubmissioncitation)
*   [GENERIC.MissingPubInfo: Submission citation affiliation has no state](#MissingPubInfoSubmissioncitationaffiliationhasnostate)
*   [GENERIC.MissingPubInfo](#MissingPubInfo)
*   [SEQ_FEAT.MissingTrnaAA](#MissingTrnaAA)
*   [SEQ_DESCR.NoOrgFound](#NoOrgFound)
*   [SEQ_DESCR.NoPubFound](#NoPubFound)
*   [SEQ_FEAT.NoStop](#NoStop)
*   [SEQ_FEAT.OnlyGeneXrefs](#OnlyGeneXrefs)
*   [SEQ_FEAT.PartialProblem PartialLocation: Start does not include first/last residue of sequence](#PartialProblemPartialLocationStartdoesnotincludefirstlastresidue)
*   [SEQ_FEAT.StartCodon](#StartCodonandBadProteinStart)
*   [SEQ_INST.StopInProtein](#InternalStopandStopInProtein)
*   [SEQ_INST.TerminalNs](#TerminalNs)
*   [SEQ_FEAT.TransLen](#TransLen)
*   [SEQ_DESCR.UnstructuredVoucher](#UnstructuredVoucher)
*   [SEQ_DESCR.WrongVoucherType](#WrongVoucherType)

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

### SEQ_DESCR.BadCollectionCode

_Explanation:_  The culture collection is not in the list of registered institutes, or is in the wrong format, or there are multiple culture-collections in a single qualifier.

_Suggestion_: See the description for the proper format and list of allowed institutes, [http://www.insdc.org/controlled-vocabulary-culturecollection-qualifier](http://www.insdc.org/controlled-vocabulary-culturecollection-qualifier). Include only the culture-collection from which the sample was obtained. If the sample was deposited into multiple culture-collections, then present each culture-collection in a separate qualifier. If the culture collection is not in the list of allowed institutes, write to us with details of the culture collection. If the error is from a genome that was created from a fasta submission, then the information comes from the BioSample, which will need to be updated. Send the correct source information to us at genomes@ncbi.nlm.nih.gov, and we will update the genome and BioSample. Be sure to include the SUBid of the genome submission and the accession of the BioSample (SAMNxxxxxxxx), if one has been assigned.

Note that culture-collection should be used for microbial sequences, while specimen-voucher should be used for plants and animals only. However, do not use specimen-voucher to describe host information for a microbial sequence submission.

### SEQ_DESCR_BadCollectionDate

_Explanation_: The collection date is not in the required format.

_Suggestion_: Correct the collection-date source modifier so the date is in the correct format. For example, a collection-date should be formatted like this: DD-MMM-YYYY, where the month is the three letter code in English. Alternatively, the ISO 8601 standard may be used; see descriptions and examples [<u>here</u>](http://www.insdc.org/files/feature_table.html). If the error is from a genome that was created from a fasta submission, then the information comes from the BioSample, which will need to be updated. Send the correct source information to us at genomes@ncbi.nlm.nih.gov, and we will update the genome and BioSample. Be sure to include the SUBid of the genome submission and the accession of the BioSample (SAMNxxxxxxxx), if one has been assigned.

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

If the error is from a genome that was created from a fasta submission, then the information comes from the BioSample, which will need to be updated. Send the correct source information to us at genomes@ncbi.nlm.nih.gov, and we will update the genome and BioSample. Be sure to include the SUBid of the genome submission and the accession of the BioSample (SAMNxxxxxxxx), if one has been assigned.

### SEQ_DESCR.BadVoucherID

_Explanation_: The voucher is missing a specific identifier.

_Suggestion_: Correct the format of the culture-collection or specimen-voucher source modifiers. The culture-collection or specimen-voucher is missing the identifier. If the error is from a genome that was created from a fasta submission, then the information comes from the BioSample, which will need to be updated. Send the correct source information to us at genomes@ncbi.nlm.nih.gov, and we will update the genome and BioSample. Be sure to include the SUBid of the genome submission and the accession of the BioSample (SAMNxxxxxxxx), if one has been assigned.

The culture-collection must be formatted like this: "<institution-code>:[<collection-code>:]<culture id>". The institution code and culture ID are required, the collection-code is optional. The institution code must be valid. See the [<u>description</u>](http://www.insdc.org/controlled-vocabulary-culturecollection-qualifier) for the proper format and [<u>list</u>](ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/coll_dump.txt) of allowed institutes.

An example culture-collection is: CBS:1234

Culture-collection should be used for microbial sequences, while specimen-voucher should be used for plants and animals only. Do not use specimen-voucher to describe host information for a microbial sequence submission. The specimen-voucher is not required to be structured.

### SEQ_DESCR_BioSourceMissing

_Explanation_: The biological source of this sequence has not been described correctly.  A submission must have a source descriptor that covers the entire molecule. Please add the source information.

_Suggestion_: Provide an organism name for each sequence in your submission.

### SEQ_FEAT.EcNumberProblem

_Explanation:_ Apparent EC number in protein title. A product name includes a value that looks like an EC number, eg : “L-pipecolate oxidase (1.5.3.7)”

_Suggestion:_ Remove the EC number from the product name and field it in the EC_number qualifier. If it is something else, eg a TC number, then move it to a note.

### SEQ_FEAT.FeatureBeginsOrEndsInGap

_Explanation_: A feature begins or ends in a gap.

_Suggestion_: Remove the feature or adjust its location to be  partial and abut the gap, whichever is appropriate.

### SEQ_INST.InternalNsInSeqRaw

_Explanation:_ A sequence has a run of 100 or more Ns, which is most likely a gap, not a run of ambiguous bases.

_Suggestion:_ Label the run's of N's as assembly_gaps.  Choose a smaller length (eg 1 or 10) to convert runs of Ns to an assembly_gap with the appropriate linkage evidence.  Do not simply remove internal N's.

### SEQ_FEAT.InternalStop and SEQ_INST.StopInProtein

_Explanation_: The InternalStop and StopInProtein errors are produced when there is an internal stop codon within the CDS.

_Suggestion_: The problem could be the genetic code, the location of the CDS, the reading frame of the CDS, or that the CDS cannot produce an error-free translation. Use the correct [genetic code](http://%28http://www.ncbi.nlm.nih.gov/Taxonomy/taxonomyhome.html/index.cgi?chapter=cgencodes) to get the correct translations. For example, include [gcode=11] for prokaryotic genome submissions. If the genetic code is correct, then adjust the CDS location, if possible. If the CDS is partial at its 5' end, then you might need to add a codon_start qualifier with a value of 2 or 3 to shift the reading frame one or two bases, respectively.  If the CDS does not have an error-free translation, then add the /pseudo qualifier to the gene to indicate that the CDS cannot be translated.

### SEQ_FEAT.InvalidQualifierValue: rRNA has no name

_Explanation_: rRNA features must have a product name.

_Suggestion_: Use the appropriate full product name for each rRNA feature, eg “16S ribosomal RNA”

### SEQ_DESCR_LatLonCountry

_Explanation_: lat_lon and country disagree

_Suggestion_: The latitude-longitude (lat-lon) value provided does not map to the source country provided, so correct or remove the lat-lon values and/or country source modifiers. Provide lat-lon in decimal degrees with the compass direction (for example: 39.7 N 42.1 W) and check that the lat-lon coordinates map to the country you have provided. If the error is from a genome that was created from a fasta submission, then the information comes from the BioSample, which will need to be updated. Send the correct source information to us at genomes@ncbi.nlm.nih.gov, and we will update the genome and BioSample. Be sure to include the SUBid of the genome submission and the accession of the BioSample (SAMNxxxxxxxx), if one has been assigned.

### SEQ_DESCR_LatLonFormat

_Explanation_: The format of lat-lon should be dd.dd N|S ddd.dd E|W.

_Suggestion_: Correct the latitude-longitude (lat-lon) source modifier with lat-lon coordinates in decimal degree format with the compass directions. For example: 39.7 N 42.1 W If the error is from a genome that was created from a fasta submission, then the information comes from the BioSample, which will need to be updated. Send the correct source information to us at genomes@ncbi.nlm.nih.gov, and we will update the genome and BioSample. Be sure to include the SUBid of the genome submission and the accession of the BioSample (SAMNxxxxxxxx), if one has been assigned.

### SEQ_DESCR_LatLonProblem

_Explanation_: There is a problem with the lat-lon modifier provided.

_Suggestion_: Correct or remove the latitude-longitude (lat-lon) values in the source modifiers. Provide lat-lon in decimal degrees and include the compass direction (for example, 39.7 N 42.1 W). Longitude values range from 0 to 180E or 0 to 180W. Latitude values range from 0 to 90 N or 0 to 90 S. If the error is from a genome that was created from a fasta submission, then the information comes from the BioSample, which will need to be updated. Send the correct source information to us at genomes@ncbi.nlm.nih.gov, and we will update the genome and BioSample. Be sure to include the SUBid of the genome submission and the accession of the BioSample (SAMNxxxxxxxx), if one has been assigned.

### SEQ_DESCR_LatLonRange

_Explanation_: Latitude or longitude is out of range.

_Suggestion_: Correct or remove the latitude-longitude (lat-lon) values in the source modifiers. Provide lat-lon in decimal degrees and include the compass direction (for example, 39.7 N 42.1 W). Longitude values range from 0 to 180E or 0 to 180W. Latitude values range from 0 to 90 N or 0 to 90 S. Numbers outside of these ranges will cause errors. If the error is from a genome that was created from a fasta submission, then the information comes from the BioSample, which will need to be updated. Send the correct source information to us at genomes@ncbi.nlm.nih.gov, and we will update the genome and BioSample. Be sure to include the SUBid of the genome submission and the accession of the BioSample (SAMNxxxxxxxx), if one has been assigned.

### SEQ_DESCR_LatLonValue

_Explanation_: Latitude or longitude values appear to be in the wrong hemisphere or swapped.

_Suggestion_: Correct or remove the latitude- longitude (lat-lon) values in the source modifiers. The lat-lon value for the record does not agree with the source country provided. Based on the source country, the lat-lon value appears to have the incorrect hemisphere or is swapped. Check the coordinates and compass direction and provide the correct values. If the error is from a genome that was created from a fasta submission, then the information comes from the BioSample, which will need to be updated. Send the correct source information to us at genomes@ncbi.nlm.nih.gov, and we will update the genome and BioSample. Be sure to include the SUBid of the genome submission and the accession of the BioSample (SAMNxxxxxxxx), if one has been assigned.

### SEQ_FEAT.MisMatchAA

_Explanation_: The conceptual translation does not match the provided translation.

_Suggestion_: Make the CDS partial if it does not begin at the start codon (and extend to end of the sequence for incomplete prokaryotic sequence). Set the genetic code of prokaryotes ( [gcode=11] ) to get the correct translations.

### GENERIC.MissingPubInfo: No submission citation anywhere on this entire record

_Explanation_: There is no submitter block.

_Suggestion_: Include the template when you create the .sqn submission file. You can create a template here: [http://www.ncbi.nlm.nih.gov/WebSub/template.cgi](http://www.ncbi.nlm.nih.gov/WebSub/template.cgi).

### GENERIC.MissingPubInfo: Submission citation affiliation has no state

_Explanation_: The country is USA, but the state is not included in the affiliation in the submitter block.

_Suggestion_: Include the state in the template file (for .sqn submissions) or your submission portal profile (for fasta submissions).

### GENERIC_MissingPubInfo

_Explanation_: The publication is missing essential information, such as title or authors.

_Suggestion_: Check the references. Provide author names, a title, and select the publication status (unpublished, in press, or published). If the title is published or is in press, provide additional information including publication year, journal, volume, and pages, where applicable.

### SEQ_FEAT.MissingTrnaAA

_Explanation_: The amino acid that the tRNA carries is not included.

_Suggestion_: Include the amino acid as the product of the tRNA. If the amino acid of a tRNA is unknown, use tRNA-Xxx as the product. See [prokaryotic examples](/~/genomesubmit_annotation#RNA) and [eukaryotic examples](/~/eukaryotic_genome_submission_annotation#rRNA).

### SEQ_DESCR.NoOrgFound

_Explanation_: No organism name is included.

_Suggestion_: Include the organism information when creating the .sqn file. When running tbl2asn, the organism information can be included in the definition lines of the fasta files or in the command line with –j.

### SEQ_DESCR.NoPubFound

_Explanation_: There is no submitter block or other reference.

_Suggestion_: Include the template when you create the .sqn submission file. You can create a template here: [http://www.ncbi.nlm.nih.gov/WebSub/template.cgi](http://www.ncbi.nlm.nih.gov/WebSub/template.cgi).

### SEQ_FEAT.NoStop

_Explanation_: The CDS is not marked as partial at its 3’ end and does not end with a stop codon.

_Suggestion_: Extend the CDS to the stop codon, or mark the 3’ end as partial (and extend the CDS to the end of the sequence for prokaryotic sequences), or add the /pseudo qualifier to the gene to indicate that the CDS cannot be translated.

### SEQ_FEAT.OnlyGeneXrefs

_Explanation_: Features, such as CDS, refer to genes but there are no corresponding gene features.

_Suggestion_: Include gene features with a unique locus_tag on each gene.

### SEQ_FEAT.PartialProblem PartialLocation: Start does not include first/last residue of sequence

_Explanation_: Since prokaryotes have very little splicing, their features need to be complete or to extend to the end of the sequence and be partial. In eukaryotes this error can be ignored if the partial is at an intron/exon boundary.

_Suggestion_: Extend the feature one or a few bases to the end of the sequence. If the feature is complete, remove the partial symbols. If this is only a fragment or a nonfunctional gene,  change the feature’s location to be complete and add the /pseudo qualifier to the gene.      

### SEQ_FEAT.StartCodon and SEQ_INST.BadProteinStart

_Explanation_: The StartCodon and BadProteinStart errors are produced when the CDS is not marked as partial at its 5’ end and does not begin with a start codon.

_Suggestion_: Use the correct [genetic code](http://%28http://www.ncbi.nlm.nih.gov/Taxonomy/taxonomyhome.html/index.cgi?chapter=cgencodes) to get the correct translations. For example, include [gcode=11] for prokaryotic genome submissions. Other possible fixes include: extend the CDS to the start codon, or mark the 5’ end as partial (and extend the CDS to the end of the sequence for prokaryotic sequences), or add the /pseudo qualifier to the gene to indicate that the CDS cannot be translated.

### SEQ_INST.TerminalNs

_Explanation_: There are Ns at the beginning or end to the sequence.

_Suggestion_: Remove Ns from the beginning and end of the sequence or indicate that the sequence circular, if that is applicable.

### SEQ_FEAT.TransLen

_Explanation_: The length of the protein does not match the provided protein length

_Suggestion_: Recreate the .sqn file and if the error persists, send your file to us with a description of how you created it and a request to help fix the error.

### SEQ_DESCR.UnstructuredVoucher

_Explanation_: The voucher needs to be structured as "<institution-code>:[<collection-code>:]<culture id>".

_Suggestion_: Correct the format of the culture-collection source modifier. The institution code and culture ID are required, the collection-code is optional. Follow the formatting instruction in the explanation. The culture collection must have a valid institution code followed by a colon and the culture ID. See the [<u>list</u>](ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/coll_dump.txt) of allowed institutes. If the error is from a genome that was created from a fasta submission, then the information comes from the BioSample, which will need to be updated. Send the correct source information to us at genomes@ncbi.nlm.nih.gov, and we will update the genome and BioSample. Be sure to include the SUBid of the genome submission and the accession of the BioSample (SAMNxxxxxxxx), if one has been assigned.

For example CBS:1234

In this example, CBS is the insitution code and 1234 is the culture ID. There must be a colon between the institution code and the culture ID.

### SEQ_FEAT.WrongQualOnImpFeat

_Explanation_: The feature has an illegal qualifier

_Suggestion_: Find the legal qualifiers for each feature in the [Feature Table](https://www.insdc.org/documents/feature-table#7.2).

### SEQ_DESCR_WrongVoucherType

_Explanation_: The institution (or institution: collection) code normally uses a different bio material/culturecollection/specimen voucher type.

_Suggestion_: In the source modifiers, use the source modifier “culture-collection” instead of “specimen-voucher” or vice versa.  For example, if you provided the source modifiers in a tab-delimited table, edit the table so the column header “culture-collection” is used in place of “specimen-voucher” and upload the revised table. If the error is from a genome that was created from a fasta submission, then the information comes from the BioSample, which will need to be updated. Send the correct source information to us at genomes@ncbi.nlm.nih.gov, and we will update the genome and BioSample. Be sure to include the SUBid of the genome submission and the accession of the BioSample (SAMNxxxxxxxx), if one has been assigned.

Note that culture-collection should be used for microbial sequences, while specimen-voucher should be used for plants and animals only. Do not use specimen-voucher to describe host information for a microbial sequence submission.

</div>

</div>

<div id="shared-content-1" nid="1465">

<div class="rightnav">

## WGS Resources

*   [About WGS](/~/wgs)
*   [WGS Project List](http://www.ncbi.nlm.nih.gov/Traces/wgs)
*   [WGS Submission Guide](/~/wgs.submit)
*   [Update Genome Records](/~/wgs_update)
*   [FAQ](/~/wgsfaq)
*   [tbl2asn](/~/tbl2asn2)
*   [Create Submission Template](http://www.ncbi.nlm.nih.gov/WebSub/template.cgi)
*   [BioProject](http://www.ncbi.nlm.nih.gov/bioproject)
*   [Eukaryotic Annotation Guide](/~/eukaryotic_genome_submission)
*   [Prokaryotic Annotation Guide](/~/genomesubmit)
*   [Discrepancy Report](/~/asndisc)
*   [WGS Example Files](/~/examples.wgs)
*   [Assembly Submission Guide](http://www.ncbi.nlm.nih.gov/assembly/docs/submission/)
*   [AGP Format](http://www.ncbi.nlm.nih.gov/assembly/agp/AGP_Specification/)
*   [WGS Submission Portal](https://submit.ncbi.nlm.nih.gov/subs/wgs/)
*   [NCBI Prokaryotic Genome Annotation Pipeline](http://www.ncbi.nlm.nih.gov/genome/annotation_prok/)
*   [Metagenome Submission Guide](/~/metagenome)
*   [Structured Comment](/~/structuredcomment)

</div>

</div>