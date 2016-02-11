<meta http-equiv="Content-Type" content="text/html; charset=utf-8">  <meta name="node-id" content="4778"> <meta name="revision-id" content="29021"> <meta name="cms-base-url" content="http://cms.ncbi.nlm.nih.gov"> <meta name="cms-view-url" content="http://cms.ncbi.nlm.nih.gov/genbank/sequencecheck"> <meta name="cms-edit-url" content="http://cms.ncbi.nlm.nih.gov/node/4778/edit"> <meta name="created" content="2015-08-25T09:54:07-04:00"> <meta name="modified" content="2015-08-25T10:12:43-04:00"> <meta name="publication-date" content="2015-08-25T09:53:00-04:00"> <meta name="author" content="yankie"> <meta name="subsite" content="genbank"> <meta name="path" content="genbank/sequencecheck"> <meta name="node-type" content="page"> <meta name="jira-ticket" content=""> <meta name="cms-tags" content="">  <meta name="" content=""> <link type="text/css" rel="stylesheet" href="/core/assets/genbank/css/genbank.css"> <title>sequencecheck</title>

<div class="node clear-block">

<div class="content">

# Prokaryotic 16S Ribosomal RNA Sequence Processing at NCBI

Prokaryotic 16S ribosomal RNA sequences are checked for a number of issues before they are accepted for GenBank. You will be notified during submission processing if your sequences have any of the issues listed below. If you have questions, please write to: [gb-admin@ncbi.nlm.nih.gov](mailto:gb-admin@ncbi.nlm.nih.gov) and include your submission number.

### Error List

*   [Trimmed Vector](#TrimmedVector)
*   [Removed Vector](#RemovedVector)
*   [Trimmed Ends and Ambiguous Sequences](#TrimmedEndsandAmbiguousSequences)
*   [Removed Short Sequences](#RemovedShortSequences)
*   [Removed Long Sequences](#RemovedLongSequences)
*   [Sequences with Low or No Similarity to 16S rRNA](#SequenceswithLoworNoSimilarityto16SrRNA)
*   [Misassembled Sequences](#MisassembledSequences)
*   [Chimeric Sequences](#ChimericSequences)

### Trimmed Vector

Sequences with terminal vector (or adaptor, linker, etc.) contamination are trimmed to remove the contaminating sequence. Sequences are checked for vector via BLAST search of your sequences against our vector and UniVec databases. While these similarities may be due to a variety of reasons, there is the possibility that contamination is the cause. To perform a BLAST search against the vector database, go to [VecScreen](//www.ncbi.nlm.nih.gov/tools/vecscreen).

### Removed Vector

Sequences with internal vector matches or sequences that match vector across the length of the sequence are removed. Sequences are checked for vector via BLAST search of your sequences against our vector and UniVec databases. To perform a BLAST search against the vector database, go to [VecScreen](//www.ncbi.nlm.nih.gov/tools/vecscreen).

### Trimmed Ends and Ambiguous Sequences

Terminal NNNs and sequences with a high percentage of ambiguities near the ends of the sequences are trimmed. Sequences with more 50% ambiguities are removed. Please be sure to trim or remove low quality sequence before submitting sequences to GenBank.

### Removed Short Sequences

Short sequences (<200 bp) are automatically removed from your submission.  Unassembled sequences from next-generation sequencing platforms should be submitted to the NCBI Sequence Read Archive [SRA](//www.ncbi.nlm.nih.gov/sra).

### Removed Long Sequences

Sequences longer than the expected 16S rRNA (>1,600 bp) are automatically removed.  If you are submitting sequences that contain 16S rRNA and other features, please use a different [submission tool](/~/submit) for submitting to GenBank and annotate the appropriate features when you submit.

### Sequences with Low or No Similarity to 16S rRNA

Submitters will be contacted regarding sequences with BLAST query coverage less than 90% or sequences that do not have a BLAST match to other prokaryotic 16S rRNA sequences.Prokaryotic 16S Ribosomal RNAs are generally highly conserved and thus, we would expect to see similarity to other rRNA sequences over the entire length.  A lack of similarity over the entire length of the sequence may be due to one of the following:

*   contaminant sequence
*   low quality sequencing
*   chimera formation
*   misassembly of the sequence reads
*   vector contamination
*   PCR artifact

_**Only prokaryotic 16S ribosomal RNA sequences should be submitted using the 16S rRNA Submission Tool**_. If you are submitting other types of sequences, you need to use a different [submission tool](/~/submit) for submitting to GenBank and annotate the appropriate features when you submit.

### Misassembled Sequences

Submitters will be contacted regarding sequences identified as misassembled by BLAST.  Misassembled sequences are often due to incorrectly ordering the sequence fragments, mixing plus and minus strand fragments and/or incorrectly joining non-overlapping sequence reads.

### Chimeric Sequences

Submitters will be contacted regarding sequences identified as chimeric. Chimeras are artifact sequences formed by two or more biological sequences incorrectly joined together. This often occurs during PCR reactions using mixed templates (i.e., uncultured environmental samples). Incomplete extensions during PCR allow subsequent PCR cycles to use a partially extended strand to bind to the template of a different, but similar, sequence.  This partially extended strand then acts as a primer to extend and form a chimeric sequence. Once created, the chimeric sequence is then further amplified in subsequent cycles. The end result is a PCR artifact that does not represent a sequence that exists in nature.

Studies have estimated that as many as 30% of the sequences from mixed template environmental samples may be chimeric. While chimera formation is most common in mixed template amplifications, in practice it is also seen at lower frequency in supposedly pure cultures.

A number of tools are available to detect chimeric sequences. NCBI uses [Uchime](http://www.drive5.com/usearch/manual/uchime_algo.html) in reference database mode to scan for chimeras. NCBI has optimized the Uchime parameters to find chimeras that are >3% diverged from the closest parent and therefore tend to produce spurious OTUs (Operational Taxonomic Units) and degrade diversity estimates and taxonomic predictions.

Accurate representations of biological diversity are not possible with data containing chimeras and other artifacts. The entire community must work together to prevent these artifact sequences from polluting the public databases.

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