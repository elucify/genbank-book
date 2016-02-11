
## Sequence Revision History

GenBank can show the revision history of a sequence. The revision history shows the various GI numbers, version numbers, and update dates for sequences that appeared in a specific GenBank record.

To see the revision history of a sequence, append `report=girevhist`to the record's URL. For example, [accession U46667](http://www.ncbi.nlm.nih.gov/nuccore/U46667)'s revision history's URL is [http://www.ncbi.nlm.nih.gov/nuccore/U46667**?report=girevhist**](/nuccore/U46667?report=girevhist).

Looking at that record, note that the original gi number for the nucleotide sequence, [2734632](/nuccore/2734632), does not have a corresponding version number. The version number is missing because it was removed from the database (and replaced by [3172140](/nuccore/3172140)) before the new accession.version system was implemented in Feb. 1999\. At that time, each sequence in the GenBank/EMBL/DDBJ database received a version number of 1, even if they had been updated in the past.

In addition, when a GenBank record contains an updated sequence, the `COMMENT` field will contain a cross-reference to the gi number of the earlier sequence; e.g., see this excerpt from [U46667](/nucleotide/U46667?format=grevhist):

<pre>COMMENT     [WARNING] On Jun 2, 1998 this sequence was replaced by gi:[3172140](/nuccore/3172140).
</pre>

If you follow the link for that earlier gi number, Entrez will display that version of the GenBank record. Similarly, the `COMMENT` field of the older version will have a warning that the sequence has been updated, and will contain a cross-reference to the newer version.

Read more about [Sequence and Version Numbers](/~/sequenceids/).

</div>

</div>