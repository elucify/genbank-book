
<div>

# Chimera Detection in 16S rRNA Sequences at NCBI

Chimeras are artifact sequences formed by two or more biological sequences incorrectly joined together. This often occurs during PCR reactions using mixed templates (i.e., uncultured environmental samples). Incomplete extensions during PCR allow subsequent PCR cycles to use a partially extended strand to bind to the template of a different, but similar, sequence.  This partially extended strand then acts as a primer to extend and form a chimeric sequence. Once created, the chimeric sequence is then further amplified in subsequent cycles. The end result is a PCR artifact that does not represent a sequence that exists in nature.

Studies have estimated that as many as 30% of the sequences from mixed template environmental samples may be chimeric. While chimera formation is most common in mixed template amplifications, in practice it is also seen at lower frequency in supposedly pure cultures.

A number of tools are available to detect chimeric sequences. NCBI uses [Uchime](http://drive5.com/usearch/manual/uchime_algo.html) in reference database mode to scan for chimeras. NCBI has optimized the Uchime parameters to find chimeras that are >3% diverged from the closest parent and therefore tend to produce spurious OTUs (Operational Taxonomic Units) and degrade diversity estimates and taxonomic predictions.

Accurate representations of biological diversity are not possible with data containing chimeras and other artifacts. The entire community must work together to prevent these artifact sequences from polluting the public databases.

</div>

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