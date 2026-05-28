"""
RNA to Protein Translator
This script translates RNA codons to their corresponding amino acids.
"""

# Dictionary: finding the amino acid for a given RNA codon
codon_table = {
    "AUG" : "Methionine",
    "UUU" : "Phenylalanine",
    "GGC" : "Glycine"
}

# RNA codon to be translated
rna_codon = "UUU"

# Look up the amino acid corresponding to the RNA codon in the codon table
amino_acid = codon_table[rna_codon]

# Print the resulting amino acid
print(amino_acid)