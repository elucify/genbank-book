
## Sequence Identifiers

Many sequences have two<span> types of identification numbers,</span> _GI_ <span>and</span> _VERSION_<span>. The two identifier types differ in format , and were implemented at different times.</span>

### GI numbers

A _GI_ number (for GenInfo Identifier, sometimes written in lower case, "_gi_") is a simple series of digits that are assigned consecutively to each sequence record processed by NCBI. The GI number bears no resemblance to the Version number of the sequence record. Each time a sequence record is changed, it is assigned a new GI number.

A _nucleotide sequence GI number_ is shown in the VERSION field of the database record. A _protein sequence GI number_ is shown in the VERSION field of a protein database record, and is cross-referenced in the CDS/db_xref field of a nucleotide database record.

### Sequence Versions

A sequence _Version_ groups all of the gi numbers for a specific sequence into an ordered series. A sequence version number consists of a base Accession number, a dot, and a version suffix that starts with 1`1`. (This identifier is often referred to as an "_accession dot version_".) The base Accession number identifies the sequence record, and the version suffixes form the series of versions, starting with 1`1`. A sequence Accession number without a version suffix always refers to the latest version of the sequence.

The two systems of identifiers run in parallel to each other. That is, when any change is made to a sequence, it both receives a new GI number, and the version part of its accession number is incremented by 1.

For example, here is the [sequence revision history of Reference Sequence Human Chromosome 1](/nuccore/NC_000001?report=girevhist), as of October 2014:

<style type="text/css">.col table { width: 90%; margin: auto; margin-bottom: 1em; }</style>

<div class="col six_col">

<table>

<thead>

<tr>

<th>Accession.Version</th>

<th>gi</th>

<th>Date</th>

</tr>

</thead>

<tbody>

<tr>

<td>NC_000001.11</td>

<td>568815597</td>

<td>Feb 3, 2014 11:01 PM</td>

</tr>

<tr>

<td>NC_000001.10</td>

<td>224589800</td>

<td>Aug 13, 2013 12:15 PM</td>

</tr>

<tr>

<td>NC_000001.10</td>

<td>224589800</td>

<td>Mar 5, 2013 02:59 PM</td>

</tr>

<tr>

<td>NC_000001.10</td>

<td>224589800</td>

<td>Mar 5, 2013 02:13 PM</td>

</tr>

<tr>

<td>NC_000001.10</td>

<td>224589800</td>

<td>Mar 3, 2013 10:59 PM</td>

</tr>

<tr>

<td>NC_000001.10</td>

<td>224589800</td>

<td>Oct 30, 2012 08:39 PM</td>

</tr>

<tr>

<td>NC_000001.10</td>

<td>224589800</td>

<td>Jul 24, 2012 03:18 PM</td>

</tr>

<tr>

<td>NC_000001.10</td>

<td>224589800</td>

<td>Jul 29, 2011 05:58 AM</td>

</tr>

<tr>

<td>NC_000001.10</td>

<td>224589800</td>

<td>Oct 25, 2010 05:33 PM</td>

</tr>

<tr>

<td>NC_000001.10</td>

<td>224589800</td>

<td>Jun 10, 2009 04:09 PM</td>

</tr>

<tr>

<td>NC_000001.9</td>

<td>89161185</td>

<td>Mar 3, 2008 05:58 PM</td>

</tr>

<tr>

<td>NC_000001.9</td>

<td>89161185</td>

<td>Aug 30, 2006 12:10 PM</td>

</tr>

<tr>

<td>NC_000001.9</td>

<td>89161185</td>

<td>Mar 3, 2006 05:23 PM</td>

</tr>

<tr>

<td>NC_000001.8</td>

<td>51511461</td>

<td>Oct 25, 2004 02:33 PM</td>

</tr>

<tr>

<td>NC_000001.8</td>

<td>51511461</td>

<td>Aug 24, 2004 04:34 PM</td>

</tr>

</tbody>

</table>



<div class="col six_col last">

<table>

<thead>

<tr>

<th>Accession.Version</th>

<th>gi</th>

<th>Date</th>

</tr>

</thead>

<tbody>

<tr>

<td>NC_000001.8</td>

<td>51511461</td>

<td>Aug 24, 2004 11:05 AM</td>

</tr>

<tr>

<td>NC_000001.7</td>

<td>42406218</td>

<td>Feb 20, 2004 09:34 AM</td>

</tr>

<tr>

<td>NC_000001.7</td>

<td>42406218</td>

<td>Feb 4, 2004 03:56 PM</td>

</tr>

<tr>

<td>NC_000001.6</td>

<td>42405892</td>

<td>Feb 4, 2004 12:17 PM</td>

</tr>

<tr>

<td>NC_000001.5</td>

<td>37623929</td>

<td>Jan 28, 2004 04:08 PM</td>

</tr>

<tr>

<td>NC_000001.5</td>

<td>37623929</td>

<td>Oct 23, 2003 11:08 AM</td>

</tr>

<tr>

<td>NC_000001.5</td>

<td>37623929</td>

<td>Oct 17, 2003 10:45 AM</td>

</tr>

<tr>

<td>NC_000001.5</td>

<td>37623929</td>

<td>Oct 16, 2003 03:44 PM</td>

</tr>

<tr>

<td>NC_000001.5</td>

<td>37623929</td>

<td>Oct 10, 2003 01:19 PM</td>

</tr>

<tr>

<td>NC_000001.4</td>

<td>29824572</td>

<td>May 6, 2003 10:42 AM</td>

</tr>

<tr>

<td>NC_000001.4</td>

<td>29824572</td>

<td>Apr 12, 2003 11:33 AM</td>

</tr>

<tr>

<td>NC_000001.3</td>

<td>29824110</td>

<td>Apr 11, 2003 11:54 PM</td>

</tr>

<tr>

<td>NC_000001.2</td>

<td>27777714</td>

<td>Feb 14, 2003 04:18 PM</td>

</tr>

<tr>

<td>NC_000001.2</td>

<td>27777714</td>

<td>Jan 17, 2003 12:40 PM</td>

</tr>

<tr>

<td>NC_000001.1</td>

<td>22539468</td>

<td>Aug 29, 2002 04:14 PM</td>

</tr>

</tbody>

</table>



Note that the gi number doesn't change every time the record is modified. Only changes to the sequence data trigger assignment of a new gi; minor updates are tracked, but don't change the gi or version number. But note that every time the gi changes, the version number is incremented.

See [Sequence Revision History](/~/sequencerevisionhistory/) for more details.

* * *

## Historical Note

The GI number has been used for many years by NCBI to track sequence histories in GenBank and the other NCBI sequence databases. The Accession.Version system of identifiers was adopted in February 1999 by the International Nucleotide Sequence Database Collaboration (GenBank, EMBL, and DDBJ).

The first type of sequence identification number was GI, which stands for "GenInfo Identifier." GenInfo was an early system used to access GenBank and related databases. A GI number was assigned to each nucleotide and protein sequence accessible through the NCBI search systems, and was a means of tracking changes to the sequence. However, GI numbers were not used uniformly across the collaborating databases (GenBank, EMBL, DDBJ). They instead served as an internal tracking system for the databases that chose to implement them. In addition, the gi number for a nucleotide sequence originally appeared in the `COMMENT`field of a record. There was no separate field for sequence identification numbers.

When the collaborating databases began to formalize use of sequence identifiers, they created a new, separate field called [NID](/~/samplerecord/#NIDA) (nucleotide identifier) in the database record, which contained the GI number of the nucleotide sequence. Similarly, the GI number for each protein sequence was named [PID](/~/samplerecord/#PIDA), and placed above each amino acid translation in the field: FEATURES/CDS/db_xref="PID:gNNNNNN". Hence, there became two types of gi numbers: NID and PID. In December 1999, the use of the abbreviations "NID" and "PID" was discontinued. Both are now just shown as "GI".

In February 1999, GenBank/EMBL/DDBJ implemented a new "[accession.version](/~/samplerecord/#VersionA)" system of sequence identifiers that runs parallel to the gi number system.

Unlike the gi number system, in which sequence identification numbers were not necessarily consistent across the databases (e.g., GenBank and EMBL could each assign their own gi number to a sequence), the new system is designed to ensure consistency. It is also designed to show a relationship between a sequence identification number and the accession number of the record in which it is found. In contrast, GI numbers are assigned consecutively and bear no resemblance to the accession number. Finally, the new system allows the assignment of alphanumeric protein IDs to proteins translations within nucleotide sequence records. The protein IDs contain three letters followed by five digits, a period, and a version number.

Since December 1999 (GenBank release 115.0):

*   the NID field and `/db_xref="PID:xxxxxxx"`qualifier were removed, and both are now simply shown as "GI" numbers
*   the VERSION field of nucleotide records contain both an accession.version and a GI number for the nucleotide sequence
*   each amino acid translation is labeled with an accession.version sequence identifier (in the `/protein_id`field) and a GI number (in the `/db_xref=GI:xxxxxxx`qualifier), under the `CDS`feature of a GenBank record
*   the accession.version and GI systems of sequence identifiers run in parellel to each other. Therefore, when any change is made to a sequence, it receives a new GI number, and its version suffix is incremented by 1

For more information, see section 3.4.7 ("VERSION") of the [current GenBank release notes](ftp://ftp.ncbi.nih.gov/genbank/gbrel.txt).



